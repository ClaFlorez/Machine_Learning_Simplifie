# Machine Learning — Résumé simplifié (Module 1)
*Public : débutant — Format : aide-mémoire Markdown en français*

---

## 1.1 Qu’est-ce que l’Intelligence Artificielle ?

### Définition simple
> **IA = faire exécuter à une machine des tâches qui exigent habituellement l’intelligence humaine** (voir, comprendre, décider, parler, traduire).

### Vocabulaire minimal
- **Algorithme** : suite d’étapes pour résoudre un problème.  
- **Données** : exemples (textes, images, sons, tableaux) utilisés pour apprendre.  
- **Modèle** : paramétrage appris à partir des données ; il généralise à de nouveaux cas.  
- **Machine Learning (ML)** : l’ordinateur **apprend des règles à partir d’exemples**.  
- **Deep Learning (DL)** : famille de modèles (réseaux de neurones) très puissants.

### IA du quotidien (exemples)
- Maison : assistants vocaux, recommandations, recherche dans photos, traduction, domotique.  
- Déplacements / travail : cartes & trafic, antispam, anti-fraude, e-commerce, agents conversationnels.

### IA faible vs IA forte
| Aspect | **IA faible (Narrow AI)** | **IA forte (General AI)** |
|---|---|---|
| Définition | Spécialisée dans **une tâche** | Intelligence **générale**, polyvalente |
| Exemples | Reconnaissance vocale, recommandation | Robots fictifs « bons à tout » |
| État actuel | **Existe aujourd’hui** (2025) | **N’existe pas** |
| Capacité | Excellente **dans son domaine** | S’adapterait à tout contexte |

**Réalité 2025 :** toute l’IA utilisée en pratique est **faible** (spécialisée).

### 5 dates pour situer
- **1956** — Dartmouth : naissance officielle du terme « IA ».  
- **1997** — **Deep Blue** bat Kasparov (échecs).  
- **2012** — **AlexNet** (vision) : tournant Deep Learning.  
- **2016** — **AlphaGo** bat des champions de Go.  
- **2022** — Arrivée massive d’**agents conversationnels** (IA générative).

### Trois approches pour « faire de l’IA »
- **Programmation classique** (règles « si… alors… ») : prévisible mais couvre mal les cas non prévus.  
- **Machine Learning** : apprend **à partir de données** ; s’adapte mieux.  
- **Deep Learning** : réseaux de neurones **profonds** ; très performant mais coûteux et moins explicable.

### Mythes vs réalités
- **Mythes** : « l’IA remplace tous les humains », « est consciente », « sait ce qu’elle fait ».  
- **Réalités** : excellences **spécifiques**, besoin de **beaucoup de données**, **outil** qui **complète** l’humain.

### Chaîne type (ex. assistant vocal)
Audio → Nombres → **Reconnaissance vocale** → **Compréhension d’intention** → Action/Réponse.

### Pourquoi apprendre l’IA ?
- **Opportunités** : métiers en croissance, tous secteurs, télétravail, innovation.  
- **Compétences** : comprendre les outils, automatiser, résoudre par les données, rester à jour.

#### Mini-quiz (révision)
1) Citer 3 usages d’IA quotidiens.  
2) Résumer la différence **IA faible** vs **IA forte**.  
3) Pourquoi les **données** sont-elles indispensables ?  
4) Rôle de la **reconnaissance vocale** dans un assistant ?

**À retenir**
- L’IA exécute des tâches « intelligentes » mais **spécialisées**.  
- **ML** apprend depuis des exemples ; **DL** utilise des **réseaux de neurones**.  
- L’IA **augmente** les capacités humaines.

---

## 1.2 Machine Learning expliqué simplement

### Définition
> **ML = au lieu d’écrire toutes les règles, on fournit des exemples étiquetés et la machine apprend les règles.**

### Différence clé avec la programmation classique
- **Programmation** : des milliers de règles explicites (fragiles, incomplètes).  
- **ML** : on fournit **données + réponses** (pour le supervisé) → l’algorithme apprend les **patterns**.

### Comment un modèle « apprend »
Observation → Recherche de **motifs** → **Généralisation** → **Prédiction** → Amélioration (à partir des erreurs).

### Exemple éclair (prix d’une maison)
Le modèle découvre : +surface, +chambres, centre-ville ⇒ **prix ↑**, puis **prévoit** le prix d’un nouveau bien.

### Les 3 grandes familles
| Type | Entrée | Objectif | Exemples |
|---|---|---|---|
| **Supervisé** | Données **+ étiquettes** | Prédire sur des **nouveaux cas** | **Classification** (spam/normal), **régression** (prix) |
| **Non-supervisé** | Données **sans étiquette** | Découvrir des **structures** | **Clustering** (segmentation), **anomalies** |
| **Renforcement** | Actions + récompenses | **Optimiser** une stratégie | Jeux, robotique, conduite autonome |

### Quand (ne pas) utiliser le ML
**À utiliser si** : beaucoup de données, règles difficiles, patterns variables, automatisation utile.  
**À éviter si** : peu de données, problème simple, **explicabilité obligatoire**, **zéro erreur** exigée.

### Workflow typique d’un projet ML
1. **Collecter** → 2. **Nettoyer** → 3. **Explorer** → 4. **Préparer** →  
5. **Choisir** l’algorithme → 6. **Entraîner** → 7. **Évaluer** → 8. **Déployer**.

### Algorithmes populaires (aperçu)
- **Arbre de décision** (simple, interprétable).  
- **Régression linéaire** (nombres).  
- **K-Means** (clustering, segmentation).

### Limites à garder en tête
Données de qualité, **biais**, **surapprentissage** (overfitting), **boîte noire** possible, pas de « bon sens ».

#### Questions de réflexion
- Supervisé vs non-supervisé ?  
- Un cas **inadapté** au ML ?  
- Pourquoi **Netflix** recommande-t-il des contenus via ML ?  
- Pourquoi **beaucoup de données** ?

**À retenir**
- **ML = apprendre des règles à partir d’exemples**.  
- Trois familles : **supervisé**, **non-supervisé**, **renforcement**.  
- Utile quand les règles sont **complexes/inconnues**, avec **données suffisantes**.

---

## 1.3 Deep Learning et réseaux de neurones

### Définition
> **Deep Learning = ML avec des réseaux de neurones « profonds »** (plusieurs couches), inspirés du cerveau.

### Parallèle (cerveau ↔ réseau)
- Neurones ↔ neurones artificiels ; connexions ↔ **poids** ; apprentissage ↔ **ajustement des poids**.

### Neurone artificiel (idée)
Entrées × Poids → Somme → **Fonction d’activation** → Sortie (s’active ou non).

### Réseau de neurones (architecture)
**Entrée** (ex. pixels) → **Couches cachées** (apprennent des caractéristiques) → **Sortie** (classe/valeur).

### DL vs ML « traditionnel »
| Aspect | **ML traditionnel** | **Deep Learning** |
|---|---|---|
| Préparation | **Beaucoup** de features manuelles | **Apprentissage** automatique des features |
| Données | Peu à moyennes | **Beaucoup** (≥ dizaines de milliers) |
| Calcul | CPU | **GPU** requis |
| Interprétation | Plus simple | **Boîte noire** |
| Performance | Bonne (problèmes simples) | **Excellente** (images, texte, audio) |

### Applications marquantes
Vision (reconnaissance, médecine, AR), Langage (chatbots, traduction), Génératif (images, musique, vidéo, code), Jeux & optimisation.

### Types de réseaux
- **Denses (MLP)** : données tabulaires.  
- **CNN** : **images** (convolutions).  
- **RNN** : **séquences** (texte, temps).  
- (+ **Transformers** pour texte, image, audio).

### Avantages / Inconvénients
- ✅ **Performance**, **polyvalence**, apprend les caractéristiques.  
- ❌ **Données massives**, **GPU**, temps d’entraînement, moins explicable.

### Quand utiliser le DL ?
- **Oui** : beaucoup de données, problème complexe (image/texte/audio), besoin de performance maximale.  
- **Non** : peu de données, besoin d’explication, ressources limitées, délai court.

### Repères historiques
1943 (neurone artificiel) → 1986 (rétropropagation) → **2012 AlexNet** → **2017 Transformers** → **2022 IA générative**.

#### Questions de réflexion
- Similarités **neurone bio** vs **neurone artificiel** ?  
- Pourquoi **tant de données** ?  
- Quand préférer **ML classique** ?  
- Risques **sociaux** (biais, vie privée, désinformation) ?

**À retenir**
- DL excelle sur données **complexes** ; exige **données + calcul**.  
- Pas toujours nécessaire : souvent, un **ML classique** suffit.

---

## 1.5 Votre premier code Python d’IA

### Pourquoi Python ?
- Simple à lire, **écosystème riche** (scikit-learn, TensorFlow, PyTorch), communauté, polyvalence, open-source.

### Démarrer vite (conseil)
- **Google Colab** (recommandé) : gratuit, sans installation, GPU disponibles.  
- Alternatives : Anaconda local, Kaggle Notebooks, Replit, Deepnote.

### Exemple A — Chatbot simple (sans ML)
```python
def chatbot_simple():
    print("Bonjour ! Je suis votre assistant IA.")
    print("Tapez 'quit' pour quitter\n")
    while True:
        q = input("Vous: ").lower().strip()
        if q == "quit": break
        if "bonjour" in q or "salut" in q:
            print("Bonjour ! Comment allez-vous ?")
        elif "météo" in q:
            print("Je n’ai pas accès à la météo.")
        else:
            print("Je ne comprends pas encore. Essayez: bonjour, météo, merci...")

chatbot_simple()
```
**Idée** : logique **if/else** programmée à la main (pas de ML).

### Exemple B — Premier modèle ML (classification binaire)
```python
from sklearn.tree import DecisionTreeClassifier

ages = [[10],[12],[15],[18],[25],[30],[40],[55],[60],[70]]
labels = [1,1,1,1,1,1,0,0,0,0]  # 1=aime, 0=n'aime pas

model = DecisionTreeClassifier(random_state=42)
model.fit(ages, labels)

for a in [16, 27, 45, 62]:
    pred = model.predict([[a]])[0]
    proba = model.predict_proba([[a]])[0].max()
    print(f"{a} ans → {'Aimera' if pred==1 else "N'aimera pas"} (confiance: {proba*100:.1f}%)")
```
**Comprendre** : `fit()` **apprend** les motifs ; `predict()` **prédit** ; `predict_proba()` donne la **confiance**.

### Exemple C — Plusieurs caractéristiques
```python
from sklearn.tree import DecisionTreeClassifier

X = [
    [25,100,120], [28,150,140], [22,80,100], [30,50,90],
    [45,20,100],  [50,30,110],  [35,200,150],[40,180,130]
]  # âge, budget, durée
y = [1,1,0,0,2,2,3,3]  # 0=Comédie,1=Action,2=Drame,3=Thriller

model = DecisionTreeClassifier(random_state=42).fit(X, y)
print(model.predict([[26,120,110]]))  # ex. prédiction
```

### Bibliothèques essentielles
| Lib | Usage |
|---|---|
| **scikit-learn** | ML « classique » (classification, régression, clustering) |
| **pandas** | Manipulation de données (CSV, nettoyage) |
| **numpy** | Calcul numérique (matrices) |
| **matplotlib** | Visualisation |
| **tensorflow / torch** | Deep Learning |

### Bonnes pratiques (début)
- **Séparer** apprentissage / évaluation (train/test).  
- **Standardiser/encoder** au besoin.  
- **Valider** (k-fold, métriques adaptées).  
- **Garder simple** avant d’ajouter de la complexité.

#### Questions de réflexion
- Différence **chatbot règles** vs **modèle ML** ?  
- Pourquoi le modèle **généralise** à de nouveaux âges ?  
- Comment **améliorer** la précision (plus de données, features, réglages) ?

**À retenir**
- Python + scikit-learn = **entrée rapide** dans le ML.  
- Commencer simple, itérer, mesurer.

---

## Annexes — Fils rouges, pièges & repères

- **Données d’abord** : quantité **et** qualité > choix d’algorithme.  
- **Éthique & biais** : vérifier sources, représentativité, usages.  
- **Explicabilité** : préférer des modèles **simples** quand la décision doit être justifiée.  
- **Surapprentissage** : surveiller la **généralisation** (validation croisée).  
- **Itération** : petit → testé → amélioré.

---

## Révisions éclair (flashcards)

- **IA faible** = spécialisée ; **IA forte** = générale (n’existe pas).  
- **ML** : apprend à partir d’exemples ; **DL** : réseaux profonds.  
- **3 types ML** : supervisé / non-supervisé / renforcement.  
- **Workflow ML** : données → features → modèle → évaluation → déploiement.  
- **À éviter ML** : peu de données, exigence d’explications strictes, tolérance zéro à l’erreur.

---

*Fin du résumé — prêt à coller dans votre dépôt.*
