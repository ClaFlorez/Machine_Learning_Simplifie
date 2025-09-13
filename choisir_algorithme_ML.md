# Module 4 • Chapitre 1  
## 4.1 – Choisir le bon algorithme  
**Niveau : Débutant • Durée : ~30-35 min**  

---

## 🎯 Objectifs d’apprentissage
- Comprendre les types de problèmes de Machine Learning et leurs algorithmes.  
- Identifier le type de problème (supervisé, non supervisé, renforcement).  
- Suivre un guide de sélection d’algorithmes.  
- Connaître les avantages et limites de chaque approche.  
- Réaliser vos premiers tests avec Scikit-learn.  
- Définir une stratégie pour bien débuter.  

---

## 🚀 Les 3 grandes familles de Machine Learning

### Supervisé  
- Données étiquetées (X, y).  
- Objectif : prédire une cible connue.  
- Cas : classification ou régression.  
- 90% des problèmes ML.  

### Non supervisé  
- Données non étiquetées (X seulement).  
- Objectif : découvrir des structures cachées.  
- Cas : clustering, réduction de dimension, détection d’anomalies.  

### Par renforcement  
- Agent qui apprend par essai-erreur.  
- Interaction avec un environnement, récompenses.  
- Cas : jeux, robotique, trading.  
- Plus avancé, très spécialisé.  

---

## 🔍 Identifier votre type de problème
1. **Avez-vous des données avec la “bonne réponse” ?**  
   - ✅ Oui → **Supervisé**  
   - ❌ Non → **Non supervisé**  

2. **Si supervisé :**  
   - Catégorie → Classification.  
   - Nombre → Régression.  

3. **Si non supervisé :**  
   - Groupes similaires → Clustering.  
   - Simplification → Réduction de dimension.  
   - Détection d’anormal → Anomalies.  

---

## 🌳 Algorithmes principaux

### Classification  
- **Decision Tree** : simple, intuitif mais risque d’overfitting.  
- **Logistic Regression** : rapide, robuste, baseline solide.  
- **Random Forest** : performant, robuste, recommandé.  
- **KNN** : très simple, utile sur petits datasets.  

### Régression  
- **Linear Regression** : rapide, interprétable, baseline idéale.  
- **Decision Tree Regressor** : gère non-linéarités mais risque d’overfitting.  
- **Random Forest Regressor** : robuste, performant, choix sûr.  
- **Support Vector Regression** : flexible mais complexe et lent.  

---

## 🧭 Guide pratique de sélection
1. **Commencez simple :**  
   - Classification → Logistic Regression, Random Forest.  
   - Régression → Linear Regression, Random Forest.  

2. **Testez rapidement plusieurs modèles.**  

3. **Optimisez ensuite :** tuning, features, modèles avancés.  

4. **Validez rigoureusement :** cross-validation, métriques multiples.  

---

## 📊 Arbre de décision pratique
- Peu de données (< 1000) → KNN, Logistic Regression, Linear Regression.  
- Beaucoup de données (> 10k) → Random Forest, SVM, Neural Networks.  
- Besoin de vitesse → Linear/Logistic Regression, Naive Bayes.  
- Besoin d’interprétation → Decision Tree, Linear/Logistic Regression.  
- Performance maximale → Random Forest, XGBoost, ensembles.  

---

## 🧪 Premier test pratique avec Scikit-learn

```python
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

print("🧪 TEST D'ALGORITHMES ML")
print("=" * 25)

# 1. Classification
X_class, y_class = make_classification(n_samples=1000, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

classifiers = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'KNN': KNeighborsClassifier()
}

for name, model in classifiers.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}: {accuracy:.3f}")

# 2. Régression
X_reg, y_reg = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

regressors = {
    'Random Forest': RandomForestRegressor(random_state=42),
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'KNN': KNeighborsRegressor()
}

for name, model in regressors.items():
    model.fit(X_train_reg, y_train_reg)
    y_pred_reg = model.predict(X_test_reg)
    mse = mean_squared_error(y_test_reg, y_pred_reg)
    print(f"{name}: MSE={mse:.2f}")
```

---

## 📌 Cas d’usage par secteur
| Secteur      | Problème typique            | Type ML         | Algo recommandé               |
|--------------|-----------------------------|----------------|-------------------------------|
| E-commerce   | Recommandations produits    | Supervisé       | Random Forest, Collaborative Filtering |
| Finance      | Détection fraude            | Classification | Random Forest, XGBoost        |
| Immobilier   | Estimation prix             | Régression     | Random Forest, Linear Regression |
| Marketing    | Segmentation clients        | Non supervisé  | K-Means, Clustering hiérarchique |
| Santé        | Diagnostic médical          | Classification | SVM, Random Forest            |
| Transport    | Optimisation routes         | Régression     | Linear Regression, Neural Nets |

---

## ⚠️ Erreurs fréquentes à éviter
- Commencer trop complexe (neural networks).  
- Ignorer les baselines simples.  
- Optimiser trop tôt.  
- Se limiter à une seule métrique.  
- Tester uniquement sur les données d’entraînement.  
- Ne pas préparer correctement les données.  

✅ **Bonnes pratiques :**  
Commencer simple, tester plusieurs modèles, valider avec cross-validation, utiliser plusieurs métriques, bien comprendre les données, itérer rapidement.  

---

## 🗺️ Stratégie recommandée
1. Définir le problème.  
2. Construire une baseline simple.  
3. Utiliser un Random Forest comme référence.  
4. Comparer plusieurs algorithmes.  
5. Optimiser le meilleur modèle.  

---

## ✨ Points clés à retenir
- Commencez simple : Linear/Logistic Regression → Random Forest.  
- Testez plusieurs algorithmes avant d’optimiser.  
- Pas de solution magique : tout dépend des données.  
- Validation croisée essentielle pour comparer.  
- Itérez rapidement : prototype → test → amélioration.  
- Random Forest : excellent compromis pour débuter.  
