
# 📊 5.1 – Exploration des données visuelles

> **Module 5 • Chapitre 1 • Niveau : Débutant • Durée : ~25-30 min**  
> *Premier pas vers la visualisation — Avant de créer des modèles ML, il faut comprendre nos données. La visualisation est notre meilleur outil pour cela.*

---

## 🎯 Objectifs pédagogiques

- Comprendre pourquoi visualiser les données est crucial.
- Connaître les types de graphiques essentiels (histogramme, scatter plot, boxplot, bar chart, heatmap).
- Apprendre à détecter les problèmes (valeurs aberrantes, distributions anormales).
- Savoir utiliser **Matplotlib** et **Seaborn** pour créer des visualisations claires.
- Adopter une bonne démarche EDA (Exploratory Data Analysis).

---

## 🧠 Pourquoi visualiser les données ?

> La visualisation agit comme des **lunettes pour vos données**. Elle permet de voir les **patterns**, les **problèmes** et les **relations** sans lire 10 000 lignes de tableau.

**Exemple** : repérer les jours de ventes très basses dans un tableau Excel ? Impossible. Mais un graphique avec des creux rend cela évident.

### Avantages :
- Compréhension rapide
- Détection de valeurs aberrantes
- Validation d’hypothèses
- Communication claire
- Décision facilitée

---

## 🕵️‍♂️ L'approche EDA : Analyse exploratoire des données

L'EDA, c'est votre **enquête préliminaire** avant tout modèle ML.

### Étapes :
1. Vue d'ensemble (taille, colonnes, types)
2. Qualité (valeurs manquantes, doublons)
3. Distributions (via histogrammes, boxplots...)
4. Corrélations (via scatter plots, heatmaps...)
5. Anomalies (valeurs extrêmes)

---

## 📈 1. Histogramme – Distribution d’une variable

- Range les données par intervalles (bins)
- Permet d’identifier les formes de distribution : normale, asymétrique, bimodale…

📌 **Utilité** : comprendre la **répartition** d’une variable numérique (âge, revenu...)

![Histogramme des âges](images_visualisation/histogramme_age.png)

---

## 🔵 2. Scatter Plot – Relation entre deux variables

- Affiche les **liens entre variables numériques**
- Permet d’observer la **corrélation** : positive, négative, inexistante, non linéaire

📌 **Attention** : corrélation ≠ causalité.

![Scatter plot: Taille vs Poids](images_visualisation/scatter_taille_poids.png)

---

## 📦 3. Boxplot – Résumé statistique visuel

- Médiane, quartiles, moustaches
- Détecte les **valeurs aberrantes** rapidement
- Idéal pour **comparer plusieurs groupes** (ex : salaires par département)

![Boxplot salaires](images_visualisation/boxplot_salaires.png)

---

## 🟪 4. Bar Chart – Comparer des catégories

- Montre les **effectifs** ou **moyennes** par catégorie
- Graphique incontournable pour les variables qualitatives

📌 Astuce : ajouter les valeurs au-dessus des barres pour plus de lisibilité.

![Répartition clients par ville](images_visualisation/bar_chart_villes.png)

---

## 🌡️ 5. Heatmap – Carte de chaleur des corrélations

- Visualise **toutes les corrélations** d’un coup
- Rouge = corrélation forte positive, Bleu = négative

📌 Outil essentiel pour les datasets avec >10 variables.

![Corrélations RH - Heatmap](images_visualisation/heatmap_correlation.png)

---

## 🧪 Étape pratique : inspection initiale du dataset

- Dimensions, types de colonnes, valeurs manquantes
- Aperçu des lignes et statistiques descriptives

```python
data.info()
data.describe()
```

---

## ✅ Bonnes pratiques de visualisation

| Critère     | Bonnes pratiques |
|-------------|------------------|
| Clarté      | Titres lisibles, légendes compréhensibles |
| Simplicité  | Un message par graphique, pas de surcharge |
| Exactitude  | Échelles correctes, contexte suffisant     |

---

## 🎓 Résumé du chapitre

- Toujours **explorer avant de modéliser**
- Histogrammes, scatter plots, boxplots, bar charts sont les bases
- Seaborn améliore la qualité visuelle et la simplicité
- Une **visualisation claire vaut mille statistiques**

---

## 💼 Exercice recommandé

1. Charger un dataset simple (Titanic, Boston Housing…)
2. Générer 3 graphiques variés
3. Identifier au moins 1 problème
4. Formuler 2 hypothèses visuelles
5. Rédiger un mini-rapport EDA

---

© Claud-IA | Module 5.1 - Visualisation des Données
