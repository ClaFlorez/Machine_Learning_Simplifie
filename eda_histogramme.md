
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
![Histogramme des âges](histogramme.JPG)



# 🔵 Nuage de points – Relation entre deux variables

## 🌳 C’est quoi un nuage de points ?

Imaginez que vous êtes dans un parc 🌳 et que vous voulez savoir s'il y a un lien entre **la taille des arbres** et **leur âge**.  
Vous mesurez plein d'arbres et vous placez un point sur un graphique :
- **X** = taille
- **Y** = âge

🟢 Si les points forment une ligne qui monte : plus un arbre est vieux, plus il est grand !

---

## 🧠 Pourquoi c'est magique ?

Le **nuage de points révèle les relations cachées** entre vos variables.  
C'est comme mettre des **lunettes à rayons X** pour vos données.

### ⚠️ Attention au piège !

> **Corrélation ≠ causalité**

Exemple : Les ventes de glaces et les noyades augmentent en même temps ?  
➡️ Ce n’est pas parce que les glaces causent les noyades… c’est **l'été** la vraie cause commune ! ☀️🍦🏊

---

## 🔍 Ce que vous pouvez découvrir

| Type de relation        | Description                                        | Exemple                            |
|-------------------------|----------------------------------------------------|------------------------------------|
| 📈 Corrélation positive | Quand une variable augmente, l'autre aussi         | Taille et pointure de chaussures   |
| 📉 Corrélation négative | Quand une augmente, l'autre diminue                | Prix et demande                    |
| ❌ Pas de corrélation   | Aucun pattern visible                              | Couleur des yeux et QI             |
| 🔁 Non-linéaire         | Les points forment une courbe                      | Vitesse et consommation d’essence  |

---

## 🛍️ Exemple e-commerce

Vous analysez le **temps passé sur un site** vs le **montant des achats** :

- Moins de 2 minutes → Trop pressé
- 5 à 10 minutes → Achats maximisés 🛒✅
- Plus de 15 minutes → Indécision, moins d’achats

➡️ Le nuage de points peut révéler un **point optimal** de conversion !

---

## 📷 Illustration

![Scatter plot: Taille vs Poids](scatter_taille_poids.JPG)


# 📦 Boxplot – Résumé statistique visuel

## 📐 Qu’est-ce qu’un boxplot ?

Imaginez que vous voulez **résumer la taille de tous les élèves de votre école** en un seul dessin.  
➡️ Le boxplot le fait parfaitement : **un résumé compact de toute votre distribution**.

---

## 🧠 Pourquoi c’est génial ?

En **un coup d’œil**, le boxplot vous dit tout :

- 📍 Où se situe la **valeur typique** (la **médiane**)
- 📦 Où se trouvent **50% des gens** (la boîte entre Q1 et Q3)
- 📏 Où se trouvent **99% des cas** (les **moustaches**)
- ⚠️ Qui sont les **valeurs aberrantes** (les points isolés)

> 🩺 **Analogie pratique** : c’est comme un **thermomètre** de vos données !  
> - La température normale = dans la boîte  
> - La fièvre = les moustaches  
> - Les urgences = les outliers

---

## 🧪 Super pouvoir du boxplot

Vous pouvez **comparer plusieurs groupes d’un coup** 🔍 :

- Salaires par département  
- Notes par classe  
- Ventes par région  

➡️ On voit **immédiatement** qui performe le mieux… et où sont les anomalies.

---

## 🔎 Comment lire un boxplot ?

| Élément         | Interprétation                                      |
|------------------|-----------------------------------------------------|
| 📍 Ligne centrale | Médiane (50% des valeurs en dessous et au-dessus)  |
| 📦 La boîte       | Quartiles Q1 à Q3 (50% des données centrales)       |
| ── Moustaches    | Étendue normale (1.5 × IQR)                          |
| ⚠️ Points isolés | Valeurs aberrantes (outliers = "moutons noirs")     |

---

## 📷 Illustration

![Boxplot salaires par département](boxplot.JPG)



