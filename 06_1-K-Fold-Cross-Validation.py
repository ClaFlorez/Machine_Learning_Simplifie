from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
# --- HOTFIX Matplotlib (Windows + Streamlit) ---
import os, tempfile
os.environ.setdefault(
    "MPLCONFIGDIR",
    os.path.join(tempfile.gettempdir(), "mplconfig_mlcourse")  # carpeta segura en escritura
)

import matplotlib as mpl
mpl.use("Agg")  # backend sin UI (robusto en Streamlit)
from matplotlib import font_manager as fm
mpl.rcParams["font.family"] = "DejaVu Sans"
try:
    fm._load_fontmanager(try_read_cache=False)  # reconstruye cache de fuentes si está corrupto
except Exception:
    pass
# ------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# Charger un dataset d'exemple
print("🌸 Chargement du dataset Iris (classification de fleurs)")
iris = load_iris()
X, y = iris.data, iris.target

print(f"📊 Dataset: {len(X)} échantillons, {len(iris.feature_names)} features")
print(f"🏷️  Classes: {len(iris.target_names)} ({', '.join(iris.target_names)})")

# Render robusto de figuras Matplotlib en Streamlit
#st.set_option('deprecation.showPyplotGlobalUse', False)
def safe_mpl_render(fig=None, close=True, caption=None):
    """Renderiza una figura Matplotlib en Streamlit sin romper la app.
    Si st.pyplot falla, hace fallback a PNG.
    """
    import os, tempfile
    try:
        import matplotlib.pyplot as plt
        if fig is None:
            if plt.get_fignums():
                fig = plt.gcf()
            else:
                fig = plt.figure(figsize=(6, 4))
        st.pyplot(fig, clear_figure=False)
    except Exception as e:
        tmpdir = os.path.join(tempfile.gettempdir(), "mpl_streamlit_safe")
        os.makedirs(tmpdir, exist_ok=True)
        png_path = os.path.join(tmpdir, "plot.png")
        try:
            fig.savefig(png_path, bbox_inches="tight", dpi=150)
            st.image(png_path, caption=caption, use_column_width=True)
        except Exception as ee:
            st.error(f"Impossible d'afficher la figure: {ee}")
    finally:
        if close:
            plt.close(fig)

# Créer notre modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)


print(f"\n🤖 Modèle choisi: Random Forest avec 100 arbres")
print("🔄 Lancement de la validation croisée...")

# Validation croisée à 5 plis
cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

print(f"\n📈 Résultats de la validation croisée (5 plis):")
print("=" * 50)

for i, score in enumerate(cv_scores, 1):
    print(f"Pli {i}: {score:.4f} ({score*100:.2f}%)")

# Statistiques
mean_score = cv_scores.mean()
std_score = cv_scores.std()

print(f"\n📊 Statistiques globales:")
print(f"• Moyenne: {mean_score:.4f} ({mean_score*100:.2f}%)")
print(f"• Écart-type: {std_score:.4f} ({std_score*100:.2f}%)")
print(f"• Minimum: {cv_scores.min():.4f} ({cv_scores.min()*100:.2f}%)")
print(f"• Maximum: {cv_scores.max():.4f} ({cv_scores.max()*100:.2f}%)")

# Intervalle de confiance à 95%
confidence_interval = 1.96 * std_score  # 1.96 pour 95% de confiance
lower_bound = mean_score - confidence_interval
upper_bound = mean_score + confidence_interval

print(f"\n🎯 Intervalle de confiance à 95%:")
print(f"• [{lower_bound:.4f}, {upper_bound:.4f}]")
print(f"• En pourcentage: [{lower_bound*100:.2f}%, {upper_bound*100:.2f}%]")

# Visualisation des résultats
plt.figure(figsize=(12, 8))

# Graphique en barres des scores
plt.subplot(2, 2, 1)
plt.bar(range(1, 6), cv_scores, color='skyblue', alpha=0.7, edgecolor='black')
plt.axhline(y=mean_score, color='red', linestyle='--', linewidth=2, label=f'Moyenne: {mean_score:.3f}')
plt.title('Scores de Validation Croisée par Pli', fontweight='bold')
plt.xlabel('Numéro du Pli')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)

# Ajouter les valeurs sur les barres
for i, score in enumerate(cv_scores):
    plt.text(i+1, score + 0.005, f'{score:.3f}', ha='center', va='bottom', fontweight='bold')

# Boxplot des scores
plt.subplot(2, 2, 2)
plt.boxplot(cv_scores, patch_artist=True, 
           boxprops=dict(facecolor='lightgreen', alpha=0.7))
plt.title('Distribution des Scores CV', fontweight='bold')
plt.ylabel('Accuracy')
plt.grid(True, alpha=0.3)

# Comparaison avec un simple train/test split
from sklearn.model_selection import train_test_split

# Faire 20 train/test splits différents pour montrer la variabilité
simple_scores = []
for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    simple_scores.append(score)

plt.subplot(2, 2, 3)
plt.hist(simple_scores, bins=10, alpha=0.7, color='orange', edgecolor='black', 
         label=f'Train/Test Split\n(moy: {np.mean(simple_scores):.3f})')
plt.axvline(mean_score, color='blue', linestyle='--', linewidth=2, 
           label=f'Cross-Validation\n(moy: {mean_score:.3f})')
plt.title('Comparaison des Méthodes de Validation', fontweight='bold')
plt.xlabel('Accuracy')
plt.ylabel('Fréquence')
plt.legend()

# Stabilité des résultats
plt.subplot(2, 2, 4)
x_pos = [1, 2]
means = [np.mean(simple_scores), mean_score]
stds = [np.std(simple_scores), std_score]
labels = ['Train/Test\nSplit', 'Cross\nValidation']

plt.bar(x_pos, means, yerr=stds, capsize=10, 
        color=['orange', 'blue'], alpha=0.7, edgecolor='black')
plt.title('Stabilité des Méthodes', fontweight='bold')
plt.ylabel('Accuracy')
plt.xticks(x_pos, labels)
plt.grid(True, alpha=0.3)

# Ajouter les valeurs
for i, (mean_val, std_val) in enumerate(zip(means, stds)):
    plt.text(x_pos[i], mean_val + std_val + 0.01, 
             f'{mean_val:.3f}±{std_val:.3f}', 
             ha='center', va='bottom', fontweight='bold')
# No usar tight_layout ni plt.show en Streamlit
fig = plt.gcf() 
#plt.tight_layout()
#safe_mpl_render(fig)   # <- reemplaza la llamada a st.pyplot(...)
safe_mpl_render(fig)   # sin tight_layout ni plt.show
#plt.show()

# Analyse comparative
print(f"\n🔍 Analyse comparative:")
print("=" * 50)
print(f"Train/Test Split (20 essais):")
print(f"  • Moyenne: {np.mean(simple_scores):.4f}")
print(f"  • Écart-type: {np.std(simple_scores):.4f}")
print(f"  • Variabilité: {np.std(simple_scores)/np.mean(simple_scores)*100:.1f}%")

print(f"\nValidation Croisée (5 plis):")
print(f"  • Moyenne: {mean_score:.4f}")
print(f"  • Écart-type: {std_score:.4f}")
print(f"  • Variabilité: {std_score/mean_score*100:.1f}%")

# Recommandation
variability_ratio = (np.std(simple_scores)/np.mean(simple_scores)) / (std_score/mean_score)
print(f"\n💡 La validation croisée est {variability_ratio:.1f}x plus stable!")

# Test avec différentes valeurs de K
print(f"\n🧪 Test avec différents nombres de plis:")
k_values = [3, 5, 7, 10]
k_results = {}

for k in k_values:
    cv_k = KFold(n_splits=k, shuffle=True, random_state=42)
    scores_k = cross_val_score(model, X, y, cv=cv_k, scoring='accuracy')
    k_results[k] = {
        'mean': scores_k.mean(),
        'std': scores_k.std(),
        'scores': scores_k
    }
    
    print(f"  K={k}: {scores_k.mean():.4f} ± {scores_k.std():.4f}")

# Recommandations
print(f"\n🎯 Recommandations:")
if std_score < 0.05:
    print("• ✅ Modèle très stable - performance fiable")
elif std_score < 0.10:
    print("• ✅ Modèle assez stable - performance correcte")
else:
    print("• ⚠️ Modèle instable - investiguer les causes")

if mean_score > 0.90:
    print("• ✅ Excellente performance moyenne")
elif mean_score > 0.80:
    print("• ✅ Bonne performance moyenne")
elif mean_score > 0.70:
    print("• ⚠️ Performance correcte mais améliorable")
else:
    print("• ❌ Performance faible - revoir le modèle ou les données")

# Analyse de la distribution des scores
score_range = cv_scores.max() - cv_scores.min()
print(f"\n📏 Analyse de la variabilité:")
print(f"• Étendue des scores: {score_range:.4f}")
print(f"• Coefficient de variation: {std_score/mean_score:.4f}")

if score_range < 0.05:
    print("• ✅ Très faible variabilité - modèle très robuste")
elif score_range < 0.10:
    print("• ✅ Faible variabilité - modèle robuste")
else:
    print("• ⚠️ Forte variabilité - modèle sensible aux données")
