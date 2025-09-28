# Données pour le Machine Learning — Résumé simplifié (Module 2)
*Public : débutant — Format : aide-mémoire Markdown en français*

---

## 2.1 Types de données : structurées vs non-structurées

### Objectifs
- Différencier **données structurées** et **non-structurées**  
- Voir **comment tout devient des nombres** pour un ordinateur  
- Parcourir **formats et exemples** (+ snippets Python)  
- Comprendre **avantages / défis** et **choix par projet**

### La grande division
- **📊 Structurées** (tableaux, SQL) — lignes/colonnes, format stable, faciles à trier/analyser, prêtes pour le ML.  
- **📄 Non-structurées** (texte, image, audio, vidéo) — format libre, riches mais nécessitent preprocessing.  
> *Analogie* : les structurées = livre de recettes ; les non-structurées = histoires de grand‑mère, passionnantes mais difficiles à ranger.

### Données structurées — exemple
**Base clients** : `ID, Nom, Âge, Ville, Salaire, Abonné`

```python
# Lire/inspecter des données structurées
import pandas as pd

data = {
    'nom': ['Marie', 'Jean', 'Sophie', 'Pierre'],
    'age': [28, 34, 25, 42],
    'ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
    'salaire': [45000, 52000, 38000, 48000],
    'abonne': [True, False, True, True]
}
df = pd.DataFrame(data)
print(df)
print(df.describe())
print(df.dtypes)
```

**Types courants**  
- **Numériques** : entiers, décimaux, % → calculs directs.  
- **Catégorielles** : nominales/ordinales/binaires → *encodage requis*.  
- **Temporelles** : dates/heures/timestamps → séries temporelles.

### Données non-structurées — exemples
- **Texte** (emails, articles, réseaux sociaux, avis, PDF)  
- **Multimédia** (images, vidéos, audio, documents scannés)

```python
# Transformer des avis texte en tableau structuré simple
import pandas as pd

avis_clients = [
    "Ce produit est fantastique ! Je le recommande vivement. Excellent service client.",
    "Très déçu de mon achat. La qualité n'est pas au rendez-vous. Service client lent.",
    "Produit correct, rien d'exceptionnel. Livraison rapide. Prix un peu élevé.",
    "Absolument parfait ! Dépasse mes attentes. Bravo à l'équipe !",
    "Mauvaise expérience. Produit défectueux. Remboursement difficile."
]

pos = ['fantastique','excellent','parfait','bravo','recommande','rapide']
neg = ['déçu','lent','mauvaise','défectueux','difficile']

def sentiment(t):
    t=t.lower()
    sp=sum(w in t for w in pos); sn=sum(w in t for w in neg)
    return "Positif" if sp>sn else ("Négatif" if sn>sp else "Neutre")

df_avis = pd.DataFrame([{
    'id': i+1,
    'sentiment': sentiment(a),
    'longueur_mots': len(a.split()),
    'contient_service': 'service' in a.lower(),
    'contient_produit': 'produit' in a.lower(),
} for i,a in enumerate(avis_clients)])

print(df_avis)
```

### Comment l’ordinateur « voit » les données (tout en nombres)
- **Texte → vecteurs** : encodage (ASCII/Unicode), *tokens* → indices, embeddings denses.  
- **Image → tenseurs** : pixels **RGB** ∈ [0,255] → tableau `H×W×3`.  

```python
# Image 3x3 en nombres
import numpy as np
image = np.array([
    [[255,0,0],[0,255,0],[0,0,255]],
    [[255,255,0],[255,0,255],[0,255,255]],
    [[0,0,0],[128,128,128],[255,255,255]]
], dtype=np.uint8)
print(image.shape, image.size, image.flatten()[:10])
```

### Avantages & défis
| Aspect | Structurées | Non-structurées |
|---|---|---|
| Traitement | ✅ Simple | ❌ Complexe |
| Richesse | ⚠️ Limitée | ✅ Très riche |
| Préparation | ✅ Faible coût | ❌ Préprocessing lourd |
| Algorithmes | ✅ Nombreux | ⚠️ Spécialisés |
| Interprétabilité | ✅ Claire | ❌ Plus difficile |

### Semi‑structurées (entre‑deux)
- **JSON / XML / CSV + métadonnées** : structure souple mais parsable.

### Choisir pour votre projet
- **Structurées si** tabulaires, débuts rapides, besoin d’explicabilité.  
- **Non‑structurées si** beaucoup de texte/images, ressources de preprocessing, priorité performance.  

**Exercices** : classer des types, créer un DataFrame à partir d’un texte, compter mots +/- dans un avis, aplatir une image 2×2.

**À retenir** : tout devient **nombres** ; 80% des données mondiales sont **non‑structurées**.

---

## 2.2 Qualité des données & principe GIGO

### GIGO (Garbage In, Garbage Out)
> **La qualité des prédictions ≤ qualité des données d’entraînement.**  
Mauvais ingrédients ⇒ mauvais plat, même avec un grand chef.

### 6 dimensions clés
**Exactitude · Complétude · Cohérence · Fraîcheur · Pertinence · Validité**

### Problèmes typiques → impacts
- **Manquants / aberrants / doublons / formats incohérents / obsolètes / typos** → baisse de précision, surcoûts, erreurs en prod.

```python
# Diagnostic rapide de qualité
import pandas as pd, numpy as np
df = pd.DataFrame({
    'nom':['Jean Dupont','marie martin','PIERRE DURAND',None,'Jean Dupont'],
    'age':[25,999,30,28,25],
    'email':['jean@gmail.com','marie@yahoo','pierre@outlook.com','invalide','jean@gmail.com'],
    'salaire':[45000,52000,None,48000,45000],
    'ville':['Paris','LYON','marseille','Paris','Paris'],
    'date_embauche':['2024-01-15','2023-13-45','2022-06-10','2024-02-30','2024-01-15']
})
print("NaN par colonne:
", df.isnull().sum())
print("Doublons:", df.duplicated().sum())
print("Emails invalides:", df[~df['email'].str.contains('@.*\.', na=False)]['email'].tolist())
```

```python
# Nettoyage minimal
df2 = df.drop_duplicates().copy()
df2['nom'] = df2['nom'].str.title()
df2['ville'] = df2['ville'].str.title()
median_age = df2['age'].median()
df2.loc[df2['age']>120,'age']=median_age
df2['salaire'] = df2['salaire'].fillna(df2['salaire'].mean())
print(df2)
```

**Stratégies manquants** : suppression (si <5%), imputation simple (moyenne/médiane/mode), ou **avancée** (KNN/ML).

**Cas d’étude e‑commerce** : dédoublonnage, normalisation, correction d’âges, imputation (KNN) → *dataset prêt ML*, KPI qualité ↑.

**Impact qualité** : mauvaise qualité ⇒ précision ~65%, erreurs fréquentes, coûts élevés ; bonne qualité ⇒ précision ~90%+, confiance & ROI ↑.

**Checklist qualité** : complétude, exactitude, cohérence formats, unicité, validité métier, fraîcheur, documentation.

---

## 2.3 Split Train / Validation / Test (règle d’or)

### Pourquoi splitter ?
Éviter **l’overfitting** : ne jamais évaluer sur les données qui ont servi à apprendre.

### Les 3 ensembles
- **Train (~70%)** : apprend les paramètres.  
- **Validation (~15%)** : règle les hyperparamètres, surveille overfitting.  
- **Test (~15%)** : *une seule fois à la fin*, performance réelle.

```python
# Split 70/15/15 avec stratification
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)
n=1000
df = pd.DataFrame({
    'age': np.random.randint(18,70,n),
    'salaire': np.random.randint(25_000,80_000,n),
    'experience': np.random.randint(0,30,n),
    'formation': np.random.choice(['BAC','BAC+3','BAC+5'], n)
})
df['satisfaction'] = (df['salaire']>50_000).astype(int) + (df['experience']>5).astype(int)

X = df.drop('satisfaction', axis=1); y = df['satisfaction']

X_tmp, X_test, y_tmp, y_test = train_test_split(X,y,test_size=0.15,random_state=42,stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_tmp,y_tmp,test_size=0.176,random_state=42,stratify=y_tmp)
print(len(X_train), len(X_val), len(X_test))
```

**Proportions conseillées**  
<1k : 60/20/20 · 1k–10k : 70/15/15 · 10k–100k : 80/10/10 · >100k : 85/7.5/7.5

**Validation croisée (K‑Fold)** : pour *optimiser* et *stabiliser* l’estimation (surtout petits jeux).

**Bonnes pratiques** : split **avant** preprocessing, **stratifier** si classes déséquilibrées, *seed* fixe, pas de **data leakage**, test unique.

---

## 2.4 Biais & éthique des données

### Définition
Distorsion systématique (dans données/algorithmes) → décisions **injustes**.

### Types courants
- **Sélection**, **historique**, **confirmation**, **étiquetage**, **algorithmique**, **culturel**.

### Détection (idées)
- Comparer taux/précision par **sous‑groupes**, tests statistiques (χ²), importance de variables sensibles, audits.

```python
# Schéma minimal d’analyse par sous-groupes (ex. genre)
# (à adapter à vos données réelles)
# 1) Taux positifs par groupe, 2) tests χ², 3) écarts TPR/PPR.
```

### Réduction des biais
- **Préventif** : échantillons équilibrés, collecte diversifiée, labels objectifs, audit amont.  
- **Correctif** : rééchantillonnage, retrait de variables sensibles, contraintes d’équité, post‑processing.

**Métriques d’équité** : parité démographique, égalité des chances, parité calibrée (*souvent impossibles à satisfaire simultanément*).

**Principes d’IA responsable** : transparence, équité, vie privée, responsabilité, robustesse, bénéfice humain, auditabilité.  
**Gouvernance** : documentation, tests d’équité, monitoring continu, recours utilisateur, mise à jour régulière.  
**Réglementation (ex.)** : RGPD/AI Act (UE), règles sectorielles (US), cadres Canada, etc.

---

## 2.5 Sources & acquisition de données

### Où trouver des données ?
- **Gratuit** : **Kaggle**, **UCI**, **Google Dataset Search** (idéals pour apprendre).  
- **Spécialisé** : gouvernement (Data.gouv.fr, Data.gov), finance (Yahoo/Quandl/Alpha Vantage), santé (MIMIC/PhysioNet), géo (OSM/NASA), réseaux sociaux (APIs), images (ImageNet/COCO), texte (Common Crawl).

**Datasets « Hello World »** : Iris, Titanic, Boston Housing, Wine.  
**Intermédiaires** : MNIST, CIFAR‑10, MovieLens, IMDb Reviews.

```python
# Chargements rapides (extraits)
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names).assign(species=iris.target)
print(df_iris.head())

# Sauvegarde rapide
df_iris.to_csv('iris.csv', index=False)
```

### APIs temps réel & scraping éthique
- Préférer **APIs officielles** (quotas, ToS).  
- **Scraping responsable** : robots.txt, délais, User‑Agent, pas de données perso, droits d’auteur.

### Créer ses propres données
- Enquêtes (Forms/Typeform), logs produits, capteurs, **données synthétiques** pour prototypage.

```python
# Générer jeu de classification synthétique
from sklearn.datasets import make_classification
import pandas as pd
X,y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_classes=3, random_state=42)
pd.DataFrame(X).assign(target=y).to_csv('synthetic_classification.csv', index=False)
```

### Légal & RGPD (essentiel)
- **OK** : données publiques, anonymisées, consentement explicite, APIs conformes.  
- **À éviter** : données perso sans base légale, scraping interdit, données sensibles, contenus protégés.

**Checklist conformité** : légalité source, consentements, anonymisation, sécurité/accès, durée de conservation, droits des personnes, documentation.

---

## Points clés (Module 2)
- **Types** : structurées (faciles) vs non‑structurées (riches, à préparer).  
- **Qualité** : GIGO — investir massivement dans nettoyage/validation.  
- **Split** : Train/Val/Test & CV pour évaluer **généralisation**.  
- **Équité** : détecter/corriger les biais ; principes d’IA responsable.  
- **Sources** : plateformes ouvertes, APIs, données synthétiques ; **RGPD** à respecter.

*Fin du Module 2 — prêt pour la pratique Python dans le Module 3.*
