
# 🕵️‍♀️ L'approche EDA (Exploratory Data Analysis)

> *“Regarder vos données avant de les modéliser, c’est comme observer une scène de crime avant d’accuser quelqu’un.”*

L’**Analyse Exploratoire des Données (EDA)** est l’étape **la plus importante** — et trop souvent négligée — avant d’entraîner un modèle de Machine Learning.

## 📌 C’est quoi exactement ?

Imaginez que vous êtes un détective. À votre arrivée sur une scène de crime :
- Vous **n’accusez pas tout de suite**
- Vous **observez**, **collectez les indices**, **analysez les faits**
- Ensuite seulement, vous **formulez des hypothèses**

L’EDA fonctionne **exactement pareil** avec les données.

---

## ⚠️ Erreur fréquente chez les débutants

Beaucoup de personnes foncent directement vers un **algorithme ML**, sans même comprendre leur dataset. C’est comme :

> *Essayer de cuisiner sans vérifier ce qu’il y a dans le frigo. Résultat : désastre assuré !* 🍳❌

---

## 🧪 L’EDA : votre check-up médical pour les données

Voici les **5 grands axes** de l’EDA :

| Étape               | Objectif                                                   |
|---------------------|------------------------------------------------------------|
| **Vue d'ensemble**  | Dimensions, noms de colonnes, types de données             |
| **Qualité**         | Détection de valeurs manquantes, doublons                  |
| **Distributions**   | Observer la répartition des variables                      |
| **Relations**       | Corrélations, dépendances entre variables                  |
| **Anomalies**       | Valeurs extrêmes, erreurs de saisie, outliers              |

---

# 📊 Histogramme : voir la "personnalité" d’une variable

## 🧺 Qu’est-ce qu’un histogramme ?

> C’est comme **ranger vos chaussettes** par couleur dans des tiroirs.

Un histogramme découpe une variable **numérique** en intervalles (appelés **bins**) et compte combien de valeurs tombent dans chaque tiroir.

---

## 📈 Pourquoi c’est utile ?

L’histogramme vous montre **la forme de la distribution** :

| Type de distribution       | Description                                           | Exemple                                |
|----------------------------|-------------------------------------------------------|----------------------------------------|
| 📘 Normale (gaussienne)     | Forme en cloche                                       | Notes d’un examen équilibré            |
| 🟠 Asymétrique              | Penche d’un côté                                      | Salaires (majorité faibles, rares gros)|
| 🟣 Bimodale                | Deux pics distincts                                   | Âges dans un magasin de jouets         |
| 🟩 Uniforme                | Même fréquence partout                                | Lancer de dé parfait                   |

---

## 📌 Exemple concret

Vous analysez l’âge de vos clients :

- L’histogramme montre un **pic entre 25-35 ans**
- ➤ Votre produit plaît surtout aux **jeunes adultes**
- ➤ Cette info influence votre **marketing**, **tarification**, et même vos **horaires d’ouverture**

---

## 🛠️ Quand l’utiliser ?

Dès que vous avez une **variable numérique** (âge, prix, température, etc.)  
➡️ **C’est toujours votre premier réflexe en EDA !**

---

## 📷 Illustration

```markdown
![Histogramme des âges](histogramme.JPG)
```
