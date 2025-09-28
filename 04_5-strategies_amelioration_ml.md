# Stratégies d’amélioration par contexte

Ce mémo te donne **quoi faire selon le symptôme** observé lors de l’entraînement d’un modèle. Inclut un tableau récapitulatif, des *recipes* concrètes et des snippets scikit‑learn pour diagnostiquer rapidement.

## Tableau récapitulatif

| Situation                 | Symptôme                               | Solutions recommandées |
|--------------------------|----------------------------------------|------------------------|
| **Overfitting**          | Écart train/test > 10%                 | Régularisation (L1/L2), limiter la complexité (max_depth, n_estimators, C), **plus de données**, **feature selection**, **early stopping**, **subsample** (pour GBM) |
| **Underfitting**         | Scores faibles partout                 | Modèle **plus complexe** (RF/GBM/SVM), **feature engineering**, augmenter la capacité (plus d’estimateurs, profondeur), enlever/relaxer la régularisation |
| **Données insuffisantes**| Variance élevée                        | **Data augmentation**, **collecte de données**, modèles simples, régularisation, validation robuste (KFold stratifié) |
| **Features peu informatives** | Tous modèles médiocres            | **Feature engineering**, **feature selection** (mutual_info, RFECV), expertise métier, nouvelles sources de données |
| **Classes déséquilibrées**| Accuracy élevée, **Recall** faible    | **Rééchantillonnage** (SMOTE/undersampling), **class_weight='balanced'**, métriques **AUC‑PR/Recall**, **seuil optimal** (tuning du threshold) |
| **Plateau de performance**| Pas d’amélioration                    | **Ensemble methods** (stacking/boosting), feature engineering, **plus de données**, *random search* / recherche bayésienne, calibration, tuning fin (learning_rate, max_depth) |

> 💡 **Rappels rapides** : privilégie **AUC‑PR** et **Recall** sur classes rares; ne touche **jamais** au *test set* avant la fin; conserve une **baseline** de référence.

---

## Points clés à retenir

- **Approche systématique** : *Baseline → Tuning → Feature Engineering → Ensemble*  
- **Random Search** souvent meilleur (plus efficace que Grid Search sur espace large)  
- **Feature Engineering** : souvent plus d’impact que le tuning pur  
- **Ensemble methods** : gain final, mais complexité/coût accrus  
- **Validation rigoureuse** : *test final* intouché jusqu’au dernier moment  
- **Équilibre performance/complexité** : « plus » n’est pas toujours « mieux »  

---

## Diagnostics rapides (scikit‑learn)

### 1) Détecter overfitting/underfitting
```python
from sklearn.model_selection import cross_val_score
import numpy as np

def gap_train_cv(model, X_train, y_train, scoring="accuracy", cv=5):
    model.fit(X_train, y_train)
    train_score = getattr(model, "score")(X_train, y_train)  # ou métrique custom
    cv_scores = cross_val_score(model, X_train, y_train, scoring=scoring, cv=cv)
    gap = train_score - cv_scores.mean()
    return {"train": train_score, "cv_mean": cv_scores.mean(), "cv_std": cv_scores.std(), "gap": gap}

# usage :
# from sklearn.ensemble import RandomForestClassifier
# res = gap_train_cv(RandomForestClassifier(random_state=42), X_train, y_train)
# print(res)  # gap>0.1 ≈ overfitting, scores bas ≈ underfitting
```

### 2) Déséquilibre de classes
```python
import numpy as np
def ratio_classes(y):
    uniq, counts = np.unique(y, return_counts=True)
    ratios = counts / counts.sum()
    return dict(zip(uniq, ratios))
# if max(ratios.values()) > 0.8 → fort déséquilibre
```

### 3) Seuil optimal pour maximiser le Recall sous contrainte de précision
```python
from sklearn.metrics import precision_recall_curve

def seuil_pour_recall(y_true, y_prob, precision_min=0.5):
    prec, rec, thr = precision_recall_curve(y_true, y_prob)
    mask = prec >= precision_min
    if mask.any():
        i = rec[mask].argmax()
        return float(thr[mask][i]), float(prec[mask][i]), float(rec[mask][i])
    return 0.5, float(prec.max()), float(rec.max())
```

### 4) Sélection de features (RFECV)
```python
from sklearn.feature_selection import RFECV

def rfecv_features(estimator, X, y, scoring="accuracy", cv=5):
    selector = RFECV(estimator, step=1, cv=cv, scoring=scoring, n_jobs=-1)
    selector.fit(X, y)
    support = selector.support_  # bool par colonne
    return support, selector.ranking_, selector.n_features_
```

### 5) Random Search (tuning efficace)
```python
from sklearn.model_selection import RandomizedSearchCV

def random_search(model, param_distributions, X, y, scoring="accuracy", cv=5, n_iter=30):
    rs = RandomizedSearchCV(model, param_distributions=param_distributions, n_iter=n_iter, scoring=scoring, cv=cv, n_jobs=-1, random_state=42)
    rs.fit(X, y)
    return rs.best_estimator_, rs.best_params_, rs.best_score_
```

---

## Recettes rapides par cas

**Overfitting**  
- Limiter capacité: `max_depth`, `min_samples_leaf`, `max_features` (arbres/RF).  
- Régulariser: `C` (LogReg/SVM), `alpha` (Ridge/Lasso), `l2_regularization`.  
- Early stopping: `n_iter_no_change`/`early_stopping=True` (GBM/LogReg SAG/SAGA).  
- Sous‑échantillonnage aléatoire (`subsample<1.0`) en gradient boosting.

**Underfitting**  
- Plus de capacité: plus d’arbres/feuilles, `max_depth`↑, `n_estimators`↑.  
- Modèles non linéaires: RandomForest, GradientBoosting, XGBoost, SVM (RBF).

**Classes déséquilibrées**  
- `class_weight='balanced'` (LogReg/SVM/Tree).  
- SMOTE/ADASYN (imblearn), undersampling.  
- Reporter **AUC‑PR**, **Recall**, **PR‑curve**; régler le seuil.

**Features peu informatives**  
- `mutual_info_classif/regression`, permutation importance, SHAP.  
- RFECV + création de variables (ratios, interactions, encodages ciblés).

**Plateau de performance**  
- Stacking/Blending, GBM (learning_rate bas, +estimators), recherche bayésienne.  
- Plus de données et **meilleure** qualité d’étiquettes.

---

### Garde‑fou final
- Gèle le **test set**.  
- Conserve un **notebook de traçabilité** (versions, seeds, splits).  
- Sauvegarde **modèle + métadonnées** (cf. fonction `save_model_and_metadata`).

