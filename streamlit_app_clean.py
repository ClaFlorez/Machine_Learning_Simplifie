#Application Streamlit ML
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Config
st.set_page_config(page_title="Explorateur de Modèles ML", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")
st.title("🤖 Explorateur de Modèles Machine Learning")
st.markdown("---")

# Sidebar
st.sidebar.header("⚙️ Paramètres")
dataset_choice = st.sidebar.selectbox("Choisir un dataset:", ["Iris (Fleurs)", "Wine (Vins)", "Breast Cancer (Cancer du Sein)"])

@st.cache_data
def load_dataset(choice):
    if choice == "Iris (Fleurs)":
        data = load_iris()
        return data.data, data.target, data.feature_names, data.target_names
    elif choice == "Wine (Vins)":
        data = load_wine()
        return data.data, data.target, data.feature_names, data.target_names
    else:
        data = load_breast_cancer()
        return data.data, data.target, data.feature_names, data.target_names

X, y, feature_names, target_names = load_dataset(dataset_choice)

model_choice = st.sidebar.selectbox("Choisir un modèle:", ["Random Forest", "Logistic Regression", "SVM"])

if model_choice == "Random Forest":
    n_estimators = st.sidebar.slider("Nombre d'arbres:", 10, 200, 100)
    max_depth = st.sidebar.slider("Profondeur max:", 1, 20, 10)
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
elif model_choice == "Logistic Regression":
    C = st.sidebar.slider("Paramètre C:", 0.01, 10.0, 1.0)
    model = LogisticRegression(C=C, random_state=42, max_iter=1000)
else:
    C = st.sidebar.slider("Paramètre C:", 0.01, 10.0, 1.0)
    kernel = st.sidebar.selectbox("Kernel:", ["rbf", "linear", "poly"])
    model = SVC(C=C, kernel=kernel, random_state=42, probability=True)

test_size = st.sidebar.slider("Taille du test (%):", 10, 50, 20) / 100
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

with st.spinner("Entraînement du modèle..."):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test) if hasattr(model, 'predict_proba') else None

# Métriques
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Précision", f"{accuracy_score(y_test, y_pred):.3f}")
with c2: st.metric("Échantillons Train", f"{len(X_train):,}")
with c3: st.metric("Échantillons Test", f"{len(X_test):,}")
with c4: st.metric("Features", f"{X.shape[1]}")

st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Exploration", "🎯 Performance", "🔍 Analyse", "📋 Rapport"])

with tab1:
    st.header("Exploration du Dataset")
    a1, a2 = st.columns(2)
    with a1:
        fig_classes = px.histogram(x=y, title="Distribution des Classes")
        fig_classes.update_layout(xaxis_title="Classes", yaxis_title="Nombre d'échantillons")
        st.plotly_chart(fig_classes, use_container_width=True)
    with a2:
        if len(feature_names) > 4:
            selected_features = st.multiselect(
                "Sélectionner les features à visualiser (max 4):",
                feature_names,
                default=feature_names[:4]
            )
        else:
            selected_features = feature_names
        if selected_features:
            idx = [list(feature_names).index(f) for f in selected_features]
            df_viz = pd.DataFrame(X[:, idx], columns=selected_features)
            df_viz['target'] = [target_names[i] for i in y]
            fig_scatter = px.scatter_matrix(df_viz, dimensions=selected_features, color='target', title="Relations entre Features")
            fig_scatter.update_layout(height=600)
            st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.header("Performance du Modèle")
    b1, b2 = st.columns(2)
    with b1:
        cm = confusion_matrix(y_test, y_pred)
        fig_cm = px.imshow(cm, text_auto=True, aspect="auto",
                           title="Matrice de Confusion",
                           labels=dict(x="Classe Prédite", y="Vraie Classe"))
        st.plotly_chart(fig_cm, use_container_width=True)
    with b2:
        if y_pred_proba is not None:
            prob_df = pd.DataFrame(y_pred_proba, columns=[f'Classe {i}' for i in range(len(target_names))])
            prob_df_melted = prob_df.melt(var_name='Classe', value_name='Probabilité')
            fig_prob = px.histogram(prob_df_melted, x='Probabilité', color='Classe',
                                    title="Distribution des Probabilités de Prédiction")
            st.plotly_chart(fig_prob, use_container_width=True)

with tab3:
    st.header("Analyse Avancée")
    if hasattr(model, 'feature_importances_'):
        importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': model.feature_importances_}).sort_values('Importance', ascending=True)
        fig_importance = px.bar(importance_df.tail(15), x='Importance', y='Feature', orientation='h', title="Importance des Features (Top 15)")
        st.plotly_chart(fig_importance, use_container_width=True)

    st.subheader("Analyse des Erreurs")
    if y_pred_proba is not None:
        analysis_df = pd.DataFrame({
            'True_Class': y_test,
            'Predicted_Class': y_pred,
            'Confidence': np.max(y_pred_proba, axis=1),
            'Correct': y_test == y_pred
        })
        c1, c2 = st.columns(2)
        with c1:
            fig_conf = px.box(analysis_df, x='Correct', y='Confidence',
                              title="Distribution de la Confiance",
                              labels={'Correct': 'Prédiction Correcte', 'Confidence': 'Confiance'})
            st.plotly_chart(fig_conf, use_container_width=True)
        with c2:
            error_by_class = analysis_df[~analysis_df['Correct']]['True_Class'].value_counts()
            if len(error_by_class) > 0:
                fig_errors = px.bar(x=error_by_class.index, y=error_by_class.values, title="Nombre d'Erreurs par Classe")
                fig_errors.update_layout(xaxis_title="Classe", yaxis_title="Nombre d'Erreurs")
                st.plotly_chart(fig_errors, use_container_width=True)
            else:
                st.info("Aucune erreur détectée pour les paramètres actuels ✅")

with tab4:
    st.header("Rapport Détaillé")
    st.subheader("Rapport de Classification")
    report_dict = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)
    report_df = pd.DataFrame(report_dict).transpose()
    st.dataframe(report_df.round(3))

    st.subheader("Informations du Dataset")
    d1, d2 = st.columns(2)
    with d1:
        st.write("**Statistiques générales:**")
        st.write(f"- Nombre total d'échantillons: {len(X):,}")
        st.write(f"- Nombre de features: {len(feature_names)}")
        st.write(f"- Nombre de classes: {len(target_names)}")
        st.write(f"- Échantillons d'entraînement: {len(X_train):,}")
        st.write(f"- Échantillons de test: {len(X_test):,}")
    with d2:
        st.write("**Distribution des classes:**")
        for i, target_name in enumerate(target_names):
            count = (y == i).sum()
            percentage = count / len(y) * 100
            st.write(f"- {target_name}: {count} ({percentage:.1f}%)")

    st.subheader("Paramètres du Modèle")
    st.write(f"**Modèle:** {model_choice}")
    st.write(f"**Paramètres:** {model.get_params()}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 Instructions")
st.sidebar.markdown("""
1. **Choisissez un dataset** dans la liste  
2. **Sélectionnez un modèle** et ajustez ses paramètres  
3. **Explorez les onglets** pour voir différentes analyses  
4. **Modifiez les paramètres** pour voir l'impact en temps réel
""")
st.sidebar.markdown("### 💡 Conseils")
st.sidebar.markdown("""
- Commencez avec Random Forest (plus stable)  
- Augmentez progressivement la complexité  
- Observez l'impact des paramètres sur les métriques  
- Utilisez l'onglet Analyse pour comprendre les erreurs
""")
