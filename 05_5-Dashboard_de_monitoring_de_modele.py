#Dashboard de monitoring de modèle
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import time

# Configuration de la page
st.set_page_config(
    page_title="Monitoring ML",
    page_icon="📊",
    layout="wide"
)

# Titre avec style
st.markdown("""

📊 Dashboard de Monitoring ML

""", unsafe_allow_html=True)

# Simuler des données de production en temps réel
@st.cache_data(ttl=60)  # Cache pendant 1 minute
def generate_production_data():
    """
    Générer des données simulées de production
    """
    np.random.seed(int(time.time()) % 1000)  # Seed basé sur le temps pour variation
    
    # Générer 30 jours de données
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    
    data = []
    for date in dates:
        # Simuler des métriques de modèle avec dérive
        day_num = (date - dates[0]).days
        
        # Accuracy qui diminue légèrement avec le temps (data drift)
        base_accuracy = 0.95 - (day_num * 0.001) + np.random.normal(0, 0.01)
        
        # Latence qui augmente parfois (problèmes système)
        base_latency = 50 + (day_num * 0.5) + np.random.exponential(10)
        
        # Volume de prédictions variable
        predictions_count = np.random.poisson(1000) + 500
        
        # Erreurs qui augmentent parfois
        error_rate = max(0, 0.05 + np.random.normal(0, 0.02) + (day_num * 0.0005))
        
        data.append({
            'date': date,
            'accuracy': base_accuracy,
            'latency_ms': base_latency,
            'predictions_count': predictions_count,
            'error_rate': error_rate,
            'memory_usage_gb': 2.5 + np.random.normal(0, 0.3),
            'cpu_usage_pct': 45 + np.random.normal(0, 10)
        })
    
    return pd.DataFrame(data)

# Générer les données
production_data = generate_production_data()

# Métriques en temps réel
st.markdown("### 📈 Métriques en Temps Réel")

col1, col2, col3, col4 = st.columns(4)

# Métriques actuelles (dernier jour)
current_metrics = production_data.iloc[-1]

with col1:
    accuracy_delta = current_metrics['accuracy'] - production_data.iloc[-2]['accuracy']
    st.metric(
        label="Accuracy",
        value=f"{current_metrics['accuracy']:.3f}",
        delta=f"{accuracy_delta:.3f}"
    )

with col2:
    latency_delta = current_metrics['latency_ms'] - production_data.iloc[-2]['latency_ms']
    st.metric(
        label="Latence (ms)",
        value=f"{current_metrics['latency_ms']:.0f}",
        delta=f"{latency_delta:.0f}"
    )

with col3:
    pred_delta = current_metrics['predictions_count'] - production_data.iloc[-2]['predictions_count']
    st.metric(
        label="Prédictions/jour",
        value=f"{current_metrics['predictions_count']:,}",
        delta=f"{pred_delta:+.0f}"
    )

with col4:
    error_delta = current_metrics['error_rate'] - production_data.iloc[-2]['error_rate']
    st.metric(
        label="Taux d'Erreur",
        value=f"{current_metrics['error_rate']:.1%}",
        delta=f"{error_delta:.1%}"
    )

st.markdown("---")

# Graphiques de tendances
st.markdown("### 📊 Tendances de Performance")

col1, col2 = st.columns(2)

with col1:
    # Évolution de l'accuracy
    fig_accuracy = px.line(production_data, x='date', y='accuracy',
                          title='Évolution de la Précision du Modèle')
    
    # Ajouter une ligne de seuil d'alerte
    fig_accuracy.add_hline(y=0.90, line_dash="dash", line_color="red",
                          annotation_text="Seuil d'Alerte (90%)")
    
    fig_accuracy.update_layout(height=400)
    st.plotly_chart(fig_accuracy, use_container_width=True)

with col2:
    # Évolution de la latence
    fig_latency = px.line(production_data, x='date', y='latency_ms',
                         title='Évolution de la Latence')
    
    # Ajouter une ligne de seuil SLA
    fig_latency.add_hline(y=100, line_dash="dash", line_color="orange",
                         annotation_text="SLA: 100ms")
    
    fig_latency.update_layout(height=400)
    st.plotly_chart(fig_latency, use_container_width=True)

# Volume et erreurs
col1, col2 = st.columns(2)

with col1:
    # Volume de prédictions
    fig_volume = px.bar(production_data, x='date', y='predictions_count',
                       title='Volume de Prédictions par Jour')
    fig_volume.update_layout(height=400)
    st.plotly_chart(fig_volume, use_container_width=True)

with col2:
    # Taux d'erreur
    fig_errors = px.line(production_data, x='date', y='error_rate',
                        title='Évolution du Taux d\'Erreur')
    
    # Zone d'alerte
    fig_errors.add_hline(y=0.10, line_dash="dash", line_color="red",
                        annotation_text="Seuil Critique (10%)")
    
    fig_errors.update_layout(height=400)
    st.plotly_chart(fig_errors, use_container_width=True)

st.markdown("---")

# Analyse des ressources système
st.markdown("### 💻 Ressources Système")

col1, col2 = st.columns(2)

with col1:
    # Utilisation mémoire
    fig_memory = px.line(production_data, x='date', y='memory_usage_gb',
                        title='Utilisation Mémoire (GB)')
    fig_memory.add_hline(y=4.0, line_dash="dash", line_color="red",
                        annotation_text="Limite: 4GB")
    st.plotly_chart(fig_memory, use_container_width=True)

with col2:
    # Utilisation CPU
    fig_cpu = px.line(production_data, x='date', y='cpu_usage_pct',
                     title='Utilisation CPU (%)')
    fig_cpu.add_hline(y=80, line_dash="dash", line_color="orange",
                     annotation_text="Seuil d'Alerte: 80%")
    st.plotly_chart(fig_cpu, use_container_width=True)

# Alertes automatiques
st.markdown("### 🚨 Alertes Automatiques")

alerts = []

# Vérifier les seuils
if current_metrics['accuracy'] < 0.90:
    alerts.append(("CRITIQUE", "Accuracy en dessous de 90%", "danger"))

if current_metrics['latency_ms'] > 100:
    alerts.append(("ATTENTION", "Latence au-dessus du SLA (100ms)", "warning"))

if current_metrics['error_rate'] > 0.10:
    alerts.append(("CRITIQUE", "Taux d'erreur au-dessus de 10%", "danger"))

if current_metrics['memory_usage_gb'] > 4.0:
    alerts.append(("ATTENTION", "Utilisation mémoire élevée", "warning"))

if current_metrics['cpu_usage_pct'] > 80:
    alerts.append(("ATTENTION", "Utilisation CPU élevée", "warning"))

# Détecter les tendances négatives
accuracy_trend = np.polyfit(range(len(production_data)), production_data['accuracy'], 1)[0]
if accuracy_trend < -0.001:
    alerts.append(("INFO", "Tendance décroissante de l'accuracy détectée", "info"))

latency_trend = np.polyfit(range(len(production_data)), production_data['latency_ms'], 1)[0]
if latency_trend > 1:
    alerts.append(("INFO", "Tendance croissante de la latence détectée", "info"))

if alerts:
    for level, message, alert_type in alerts:
        if alert_type == "danger":
            st.error(f"🔴 {level}: {message}")
        elif alert_type == "warning":
            st.warning(f"🟡 {level}: {message}")
        else:
            st.info(f"🔵 {level}: {message}")
else:
    st.success("✅ Tous les indicateurs sont dans les normes")

# Bouton de rafraîchissement
if st.button("🔄 Rafraîchir les Données", type="primary"):
    st.cache_data.clear()
    st.experimental_rerun()

# Analyse de dérive des données (Data Drift)
st.markdown("---")
st.markdown("### 🔄 Analyse de Dérive des Données")

# Simuler des statistiques de features au fil du temps
feature_stats = []
for i, date in enumerate(production_data['date']):
    # Simuler une dérive graduelle des features
    drift_factor = i * 0.02
    
    stats = {
        'date': date,
        'feature_1_mean': 0.5 + drift_factor + np.random.normal(0, 0.1),
        'feature_1_std': 1.0 + drift_factor * 0.5 + np.random.normal(0, 0.05),
        'feature_2_mean': -0.2 + drift_factor * 0.3 + np.random.normal(0, 0.08),
        'feature_2_std': 0.8 + np.random.normal(0, 0.03)
    }
    feature_stats.append(stats)

feature_drift_data = pd.DataFrame(feature_stats)

# Graphique de dérive
fig_drift = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Feature 1 - Moyenne', 'Feature 1 - Écart-type',
                   'Feature 2 - Moyenne', 'Feature 2 - Écart-type'),
    vertical_spacing=0.1
)

# Feature 1 - Moyenne
fig_drift.add_trace(
    go.Scatter(x=feature_drift_data['date'], y=feature_drift_data['feature_1_mean'],
              mode='lines+markers', name='Feature 1 Mean'),
    row=1, col=1
)

# Feature 1 - Écart-type
fig_drift.add_trace(
    go.Scatter(x=feature_drift_data['date'], y=feature_drift_data['feature_1_std'],
              mode='lines+markers', name='Feature 1 Std'),
    row=1, col=2
)

# Feature 2 - Moyenne
fig_drift.add_trace(
    go.Scatter(x=feature_drift_data['date'], y=feature_drift_data['feature_2_mean'],
              mode='lines+markers', name='Feature 2 Mean'),
    row=2, col=1
)

# Feature 2 - Écart-type
fig_drift.add_trace(
    go.Scatter(x=feature_drift_data['date'], y=feature_drift_data['feature_2_std'],
              mode='lines+markers', name='Feature 2 Std'),
    row=2, col=2
)

fig_drift.update_layout(height=600, title_text="Évolution des Statistiques des Features")
st.plotly_chart(fig_drift, use_container_width=True)

# Détecter la dérive automatiquement
print("\nAnalyse de dérive des données:")
print("=" * 40)

# Calculer les tendances
features_to_check = ['feature_1_mean', 'feature_1_std', 'feature_2_mean', 'feature_2_std']
drift_detected = False

for feature in features_to_check:
    trend = np.polyfit(range(len(feature_drift_data)), feature_drift_data[feature], 1)[0]
    
    # Seuil de dérive significative
    if abs(trend) > 0.01:
        drift_detected = True
        direction = "croissante" if trend > 0 else "décroissante"
        print(f"• {feature}: Tendance {direction} détectée (pente: {trend:.4f})")

if not drift_detected:
    print("• Aucune dérive significative détectée")
else:
    print("\n⚠️ Dérive des données détectée!")
    print("Recommandations:")
    print("• Investiguer les changements dans les sources de données")
    print("• Considérer un réentraînement du modèle")
    print("• Ajuster les seuils d'alerte")

# Résumé du monitoring
st.markdown("### 📋 Résumé du Monitoring")

summary_data = {
    'Métrique': ['Accuracy', 'Latence', 'Volume', 'Erreurs', 'Mémoire', 'CPU'],
    'Valeur Actuelle': [
        f"{current_metrics['accuracy']:.3f}",
        f"{current_metrics['latency_ms']:.0f} ms",
        f"{current_metrics['predictions_count']:,}",
        f"{current_metrics['error_rate']:.1%}",
        f"{current_metrics['memory_usage_gb']:.1f} GB",
        f"{current_metrics['cpu_usage_pct']:.0f}%"
    ],
    'Seuil': ['0.900', '100 ms', 'N/A', '10.0%', '4.0 GB', '80%'],
    'Statut': []
}

# Déterminer le statut de chaque métrique
statuts = []
if current_metrics['accuracy'] >= 0.90:
    statuts.append("✅ OK")
else:
    statuts.append("🔴 ALERTE")

if current_metrics['latency_ms'] <= 100:
    statuts.append("✅ OK")
else:
    statuts.append("🟡 ATTENTION")

statuts.append("➖ N/A")  # Volume

if current_metrics['error_rate'] <= 0.10:
    statuts.append("✅ OK")
else:
    statuts.append("🔴 ALERTE")

if current_metrics['memory_usage_gb'] <= 4.0:
    statuts.append("✅ OK")
else:
    statuts.append("🟡 ATTENTION")

if current_metrics['cpu_usage_pct'] <= 80:
    statuts.append("✅ OK")
else:
    statuts.append("🟡 ATTENTION")

summary_data['Statut'] = statuts

summary_df = pd.DataFrame(summary_data)
st.table(summary_df)

print("\nDashboard de monitoring créé!")
print("=" * 40)
print("Le dashboard inclut:")
print("• Métriques en temps réel avec deltas")
print("• Graphiques de tendances interactifs")
print("• Alertes automatiques basées sur des seuils")
print("• Analyse de dérive des données")
print("• Monitoring des ressources système")
print("• Résumé tabulaire des statuts")
print()
print("Pour utiliser:")
print("1. Sauvegardez dans 'monitoring_dashboard.py'")
print("2. Lancez: streamlit run monitoring_dashboard.py")
print("3. Le dashboard se mettra à jour automatiquement")
