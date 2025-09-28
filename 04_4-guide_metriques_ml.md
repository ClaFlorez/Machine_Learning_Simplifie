# Guide de sélection des métriques

Ce guide résume **quelle métrique prioriser selon le contexte** et propose des calculs/implémentations rapides avec *scikit-learn*.

## Tableau récapitulatif

| Contexte                | Problème        | **Métrique principale** | Métriques secondaires        |
|-------------------------|-----------------|--------------------------|------------------------------|
| Classes équilibrées     | Classification  | **Accuracy**             | F1‑Score, AUC‑ROC            |
| Classes déséquilibrées  | Classification  | **F1‑Score, AUC‑PR**     | Precision, Recall            |
| Détection fraude        | Classification  | **Recall**               | AUC‑PR, F1‑Score             |
| Diagnostic médical      | Classification  | **Recall (Sensibilité)** | Précision, Spécificité       |
| Prédiction prix         | Régression      | **MAE, MAPE**            | RMSE, R²                     |
| Optimisation continue   | Régression      | **R²**                   | RMSE, MAE                    |
| Prévisions financières  | Régression      | **MAPE**                 | MAE, R²                      |

> **Rappels rapides** :  
> • **Accuracy** ok si classes ~équilibrées.  
> • **AUC‑PR** préférable à **AUC‑ROC** quand la classe positive est rare.  
> • **Recall** prime quand *rater* un positif est critique (santé, fraude).  
> • **MAE** (erreur absolue) facile à interpréter en unités réelles.  
> • **MAPE** (% d’erreur relatif) prudent si y≈0 (peut exploser).  
> • **RMSE** pénalise davantage les grosses erreurs.  
> • **R²** proportion de variance expliquée (attention aux comparaisons de séries non stationnaires).

---

## Définitions (classification)

- **TP/FP/TN/FN** : vrais/faux positifs, vrais/faux négatifs.  
- **Accuracy** = (TP + TN) / (TP + FP + TN + FN)  
- **Precision** = TP / (TP + FP)  
- **Recall (Sensibilité)** = TP / (TP + FN)  
- **Spécificité** = TN / (TN + FP)  
- **F1‑Score** = 2 · (Precision · Recall) / (Precision + Recall)  
- **AUC‑ROC** : aire sous la courbe TPR (=Recall) vs FPR (=1–Spécificité).  
- **AUC‑PR** : aire sous la courbe Précision–Recall (mieux si classes rares).

## Définitions (régression)

- **MAE** = moyenne(|y − ŷ|)  
- **MSE** = moyenne((y − ŷ)²) ; **RMSE** = √MSE  
- **MAPE** = moyenne(|(y − ŷ)/y|) × 100 (%), éviter si y≈0  
- **R²** = 1 − SSE/SST

---

## Implémentation rapide (scikit‑learn)

### Classification (binaire ou multi‑classe)

```python
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score,
    roc_auc_score, average_precision_score, confusion_matrix
)

y_true = ...  # 1D
y_prob = ...  # proba de la classe positive si binaire
y_pred = ...  # classes prédites

metrics = {}
metrics["accuracy"]  = accuracy_score(y_true, y_pred)
metrics["precision"] = precision_score(y_true, y_pred, average="binary")  # "macro" pour multi-classe
metrics["recall"]    = recall_score(y_true, y_pred, average="binary")
metrics["f1"]        = f1_score(y_true, y_pred, average="binary")

# Courbes/AUC (binaire)
metrics["auc_roc"] = roc_auc_score(y_true, y_prob)
metrics["auc_pr"]  = average_precision_score(y_true, y_prob)  # AUC‑PR

cm = confusion_matrix(y_true, y_pred)
```

> Multi‑classe : utiliser `average="macro"` (toutes classes pondérées pareil) ou `average="weighted"` (pondérées par fréquence).

### Régression

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

y_true = ...
y_pred = ...

mae  = mean_absolute_error(y_true, y_pred)
mse  = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_true, y_pred)

# MAPE (implémentation simple, éviter y≈0)
mape = (np.mean(np.abs((y_true - y_pred) / np.clip(np.abs(y_true), 1e-8, None))) * 100)
```

---

## Sélecteur de métriques (utilitaire)

```python
def choisir_metriques(contexte: str, probleme: str):
    contexte = contexte.lower()
    probleme = probleme.lower()
    if probleme.startswith("class"):
        if "déséquilibr" in contexte or "deséquilibr" in contexte:
            return ["f1", "auc_pr", "precision", "recall"]
        if "fraude" in contexte or "médical" in contexte or "medical" in contexte:
            return ["recall", "auc_pr", "f1", "specificite"]
        return ["accuracy", "f1", "auc_roc"]
    else:
        if "prix" in contexte or "financi" in contexte:
            return ["mape", "mae", "r2"]
        if "optimisation" in contexte:
            return ["r2", "rmse", "mae"]
        return ["mae", "rmse", "r2"]
``

---

## Conseils pratiques

- **Stratifier** les splits (`train_test_split(..., stratify=y)`) pour classification.  
- En classes rares, comparer surtout **AUC‑PR** et **Recall** à différents seuils.  
- Toujours **reporter plusieurs métriques** (principale + secondaires).  
- Valider par **cross‑validation** et fixer le **seuil de décision** avec une courbe PR/ROC selon le coût métier (FP vs FN).
