# Jupyter_Widgets_interactives.py
# -------------------------------------------------------------
# Interactifs de ML avec ipywidgets (Notebook) + Mode CLI (Terminal)
# - En Notebook: muestra sliders y explorador de datasets.
# - En Terminal: permite pasar parámetros y generar gráficos una vez.
# -------------------------------------------------------------

import sys
import os
import argparse

# --- IMPORTS ---
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import make_classification, load_iris, load_wine, load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import seaborn as sns
import plotly.express as px

# --- PARCHE FUENTES MATPLOTLIB (evita RuntimeError de font cache) ---
try:
    mpl.rcParams['font.family'] = 'DejaVu Sans'
    if hasattr(mpl.font_manager, "_rebuild"):
        mpl.font_manager._rebuild()
except Exception:
    pass

# --- DATOS DE EJEMPLO ---
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=10,
    n_redundant=5, n_clusters_per_class=1, random_state=42
)

# División base (se redivide dinámicamente en la función)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- FUNCIÓN DE ACTUALIZACIÓN ---
def update_model_analysis(n_estimators, max_depth, min_samples_split, test_size_pct):
    """
    Redivide el set, entrena RandomForest y muestra métricas + visualizaciones.
    Funciona en Notebook y también desde CLI (generará la misma figura).
    """
    try:
        clear_output(wait=True)
    except Exception:
        # fuera de IPython/Notebook no pasa nada
        pass

    # Redividir según tamaño de test seleccionado
    X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(
        X, y, test_size=test_size_pct/100, random_state=42
    )

    # Entrenar modelo
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    model.fit(X_train_new, y_train_new)
    y_pred = model.predict(X_test_new)

    # Métricas
    acc = accuracy_score(y_test_new, y_pred)

    # Figuras
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # 1) Importancia de características (Top 10)
    importance = model.feature_importances_
    top_features_idx = np.argsort(importance)[-10:]
    axes[0, 0].barh(range(len(top_features_idx)), importance[top_features_idx])
    axes[0, 0].set_yticks(range(len(top_features_idx)))
    axes[0, 0].set_yticklabels([f'Feature {i}' for i in top_features_idx])
    axes[0, 0].set_title(f'Top 10 Features Importantes\nAccuracy: {acc:.3f}')
    axes[0, 0].set_xlabel('Importance')

    # 2) Matriz de confusión
    cm = confusion_matrix(y_test_new, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0, 1])
    axes[0, 1].set_title('Matrice de Confusion')
    axes[0, 1].set_ylabel('Vraie classe')
    axes[0, 1].set_xlabel('Classe prédite')

    # 3) Distribución de profundidades de los árboles
    tree_depths = [est.tree_.max_depth for est in model.estimators_]
    axes[1, 0].hist(tree_depths, bins=20, alpha=0.7)
    axes[1, 0].set_title('Distribution des Profondeurs des Arbres')
    axes[1, 0].set_xlabel('Profondeur')
    axes[1, 0].set_ylabel("Nombre d'arbres")
    axes[1, 0].axvline(np.mean(tree_depths), linestyle='--',
                       label=f'Moyenne: {np.mean(tree_depths):.1f}')
    axes[1, 0].legend()

    # 4) Accuracy vs # árboles
    complexities, accuracies = [], []
    for n_est in range(10, n_estimators + 1, 10):
        tmp = RandomForestClassifier(
            n_estimators=n_est,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42
        )
        tmp.fit(X_train_new, y_train_new)
        temp_pred = tmp.predict(X_test_new)
        complexities.append(n_est)
        accuracies.append(accuracy_score(y_test_new, temp_pred))

    axes[1, 1].plot(complexities, accuracies, 'o-', linewidth=2, markersize=6)
    axes[1, 1].set_title("Accuracy vs Nombre d'Arbres")
    axes[1, 1].set_xlabel("Nombre d'Arbres")
    axes[1, 1].set_ylabel('Accuracy')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axvline(n_estimators, linestyle='--',
                       label=f'Paramètre actuel: {n_estimators}')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.show()

    # Informe de clasificación
    print("\nRapport de Classification:")
    print("=" * 50)
    print(classification_report(y_test_new, y_pred, target_names=['Classe 0', 'Classe 1']))

    # Análisis de parámetros
    print(f"\nAnalyse des Paramètres:")
    print(f"• Nombre d'arbres: {n_estimators}")
    print(f"• Profondeur max: {max_depth}")
    print(f"• Min samples split: {min_samples_split}")
    print(f"• Taille test: {test_size_pct}%")
    print(f"• Profondeur moyenne réelle: {np.mean(tree_depths):.1f}")
    if max_depth is not None and np.mean(tree_depths) < max_depth * 0.7:
        print("  → Les arbres n'utilisent pas la profondeur max (bon signe)")
    elif max_depth is not None:
        print("  → Les arbres atteignent la profondeur max (possible overfitting)")
    else:
        print("  → Profondeur max = None (les arbres déterminent leur propre profondeur)")

# --- EXPLORADOR DE DATASETS ---
def create_dataset_explorer():
    datasets = {
        'Iris': load_iris(),
        'Wine': load_wine(),
        'Breast Cancer': load_breast_cancer()
    }

    def explore_dataset(dataset_name, feature_x, feature_y):
        data = datasets[dataset_name]
        X, y = data.data, data.target
        feature_names = list(data.feature_names)
        target_names = list(data.target_names)

        df = pd.DataFrame(X, columns=feature_names)
        df['target'] = [target_names[i] for i in y]

        fig = px.scatter(
            df, x=feature_x, y=feature_y, color='target',
            title=f'{dataset_name}: {feature_x} vs {feature_y}'
        )
        fig.show()

        # Statistiques
        print(f"\nStatistiques pour {dataset_name}:")
        print(f"• Nombre d'échantillons: {len(X):,}")
        print(f"• Nombre de features: {len(feature_names)}")
        print(f"• Nombre de classes: {len(target_names)}")
        print(f"• Classes: {', '.join(target_names)}")

        correlation = np.corrcoef(df[feature_x], df[feature_y])[0, 1]
        print(f"• Corrélation {feature_x} vs {feature_y}: {correlation:.3f}")

    dataset_widget = widgets.Dropdown(
        options=['Iris', 'Wine', 'Breast Cancer'],
        value='Iris',
        description='Dataset:'
    )

    feature_x_widget = widgets.Dropdown(
        options=list(datasets['Iris'].feature_names),
        value=list(datasets['Iris'].feature_names)[0],
        description='Feature X:'
    )
    feature_y_widget = widgets.Dropdown(
        options=list(datasets['Iris'].feature_names),
        value=list(datasets['Iris'].feature_names)[1],
        description='Feature Y:'
    )

    def update_feature_options(change):
        dataset_name = change['new']
        new_features = list(datasets[dataset_name].feature_names)
        feature_x_widget.options = new_features
        feature_y_widget.options = new_features
        feature_x_widget.value = new_features[0]
        feature_y_widget.value = new_features[1]

    dataset_widget.observe(update_feature_options, names='value')

    explorer_widget = widgets.interactive(
        explore_dataset,
        dataset_name=dataset_widget,
        feature_x=feature_x_widget,
        feature_y=feature_y_widget
    )
    return explorer_widget

def show_notebook_widgets():
    print("Widget interactif (RandomForest) :")
    n_estimators_widget = widgets.IntSlider(
        value=100, min=10, max=200, step=10, description='N Estimators:',
        style={'description_width': 'initial'}
    )
    max_depth_widget = widgets.IntSlider(
        value=10, min=1, max=20, step=1, description='Max Depth:',
        style={'description_width': 'initial'}
    )
    min_samples_split_widget = widgets.IntSlider(
        value=2, min=2, max=20, step=1, description='Min Samples Split:',
        style={'description_width': 'initial'}
    )
    test_size_widget = widgets.IntSlider(
        value=20, min=10, max=50, step=5, description='Test Size (%):',
        style={'description_width': 'initial'}
    )

    interactive_widget = widgets.interactive(
        update_model_analysis,
        n_estimators=n_estimators_widget,
        max_depth=max_depth_widget,
        min_samples_split=min_samples_split_widget,
        test_size_pct=test_size_widget
    )
    display(interactive_widget)

    print("\nExplorateur de dataset :")
    explorer = create_dataset_explorer()
    display(explorer)

def is_running_in_notebook():
    try:
        from IPython import get_ipython
        shell = get_ipython()
        if shell is None:
            return False
        # ZMQInteractiveShell -> Notebook/QtConsole
        return shell.__class__.__name__ == 'ZMQInteractiveShell'
    except Exception:
        return False

def main_cli():
    parser = argparse.ArgumentParser(description="RandomForest + Widgets (CLI mode)")
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--max_depth", type=int, default=10)
    parser.add_argument("--min_samples_split", type=int, default=2)
    parser.add_argument("--test_size_pct", type=int, default=20)
    args = parser.parse_args()

    print("Modo CLI (sin widgets). Usa Jupyter para interactividad.")
    update_model_analysis(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_samples_split=args.min_samples_split,
        test_size_pct=args.test_size_pct,
    )

if __name__ == "__main__":
    if is_running_in_notebook():
        # Si se ejecuta dentro de un Notebook, mostramos los widgets
        show_notebook_widgets()
    else:
        # Si se ejecuta desde Terminal/CLI
        main_cli()
