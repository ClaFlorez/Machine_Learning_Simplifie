# Module 10 – Introduction au Machine Learning
**Niveau : Débutant • Durée totale estimée : ~4h**

---

## Table des matières
- [10.1 – Introduction aux réseaux de neurones](#101--introduction-aux-réseaux-de-neurones)
- [10.2 – Architecture des réseaux profonds](#102--architecture-des-réseaux-profonds)
- [10.3 – Entraînement et backpropagation](#103--entraînement-et-backpropagation)
- [10.4 – CNN pour la vision](#104--cnn-pour-la-vision)
- [10.5 – Premiers pas avec TensorFlow](#105--premiers-pas-avec-tensorflow)
- [Résumé et points clés du Module 10](#résumé-et-points-clés-du-module-10)

---

## 10.1 – Introduction aux réseaux de neurones
**Durée : ~50–60 min**  

L'intelligence artificielle qui s'inspire du cerveau — découvrez comment les réseaux de neurones imitent le fonctionnement du cerveau humain pour résoudre des problèmes complexes.

### Ce que vous allez apprendre
- Qu'est-ce qu'un neurone artificiel et comment il fonctionne  
- De la biologie à l'informatique : l'inspiration du cerveau  
- Architecture d'un réseau de neurones simple  
- Différence entre ML classique et Deep Learning  
- Construire votre premier réseau de neurones  
- Applications révolutionnaires du Deep Learning  

### Du cerveau biologique au cerveau artificiel
Votre cerveau contient environ **86 milliards de neurones**. Chacun reçoit des signaux de milliers d'autres neurones, les traite, et décide s'il doit transmettre son propre signal.  
Les réseaux de neurones artificiels s'inspirent directement de ce fonctionnement.

> *« Si le Machine Learning classique imite l'intelligence, le Deep Learning imite l'apprentissage. »*

### Anatomie d'un neurone artificiel
- **Biologique** : dendrites, corps cellulaire, axone, synapses, seuil d’activation.  
- **Artificiel** : inputs, weights, bias, fonction d'activation, output.  

Analogie : un **comité de décision**. Chaque membre (input) a une influence (weight). Le président (neurone) prend une décision finale (output).

### Réseaux multicouches
Un neurone seul est limité. Les **réseaux multicouches (MLP)** organisent les neurones en **couches** (entrée → cachées → sortie).  
Plus il y a de couches, plus le réseau peut apprendre des patterns complexes.

### Deep Learning vs Machine Learning classique

| ML Classique | Deep Learning |
|--------------|---------------|
| Features manuelles | Feature learning automatique |
| Algorithmes simples (SVM, RF, Régression) | Réseaux complexes, millions de paramètres |
| Interprétabilité élevée | Boîte noire |
| Données structurées (CSV, tableaux) | Données non structurées (images, texte, audio) |
| Performance limitée par les features | Performance croît avec données et GPU |

### Applications du Deep Learning

| Domaine | Application | Réseau | Impact |
|---------|-------------|--------|--------|
| Vision | Reconnaissance d’images | CNN | Surpasse l’humain sur ImageNet |
| Langage | Traduction automatique | Transformer | Qualité proche traducteur humain |
| Jeux | Stratégie | RL | AlphaGo bat les champions |
| Créativité | Génération d’art | GAN | Œuvres indiscernables |
| Science | Médicaments | GNN | Accélération ×100 de la recherche |

---

## 10.2 – Architecture des réseaux profonds
**Durée : ~45–50 min**  

Construire l'intelligence couche par couche — apprenez à concevoir des architectures adaptées à vos problèmes.

### Ce que vous allez apprendre
- Types de couches et rôles spécifiques  
- Fonctions d'activation et impact  
- Architectures spécialisées par domaine  
- Régularisation et anti-overfitting  
- Optimisation et hyperparamètres  
- Design patterns efficaces  

> *« L'architecture détermine ce que votre réseau peut apprendre, les données déterminent ce qu'il apprend effectivement. »*

Révolution architecturale : ResNet (connexions résiduelles), Transformer (attention), GAN (adversarial).

---

## 10.3 – Entraînement et backpropagation
**Durée : ~40–45 min**  

Comment les réseaux apprennent de leurs erreurs — découvrez la **rétropropagation**.

### La backpropagation
Comme un chef d’orchestre qui ajuste chaque musicien, la backprop identifie quel poids « joue faux » et ajuste chaque paramètre pour réduire l’erreur.  
Inventée dans les années 1980, elle a rendu possible le Deep Learning moderne.

> *« La backpropagation : l'art d'apprendre de ses erreurs, neurone par neurone. »*

---

## 10.4 – CNN pour la vision
**Durée : ~45–50 min**  

Les yeux électroniques de l’IA — découvrez comment les **CNN** révolutionnent la vision.

### Ce que vous allez apprendre
- Pourquoi les CNN révolutionnent la vision  
- Convolution et détection de motifs  
- Pooling et réduction dimensionnelle  
- Architecture classique d'un CNN  
- Applications concrètes  
- Construire un premier CNN  

### Impact historique
En 2012, AlexNet a pulvérisé les records ImageNet (erreur -10%).  
Depuis, les CNN ont transformé la vision : reconnaissance faciale, voitures autonomes, diagnostic médical, AR, modération de contenu.

> *« Les CNN ont donné des yeux à l’intelligence artificielle. »*

---

## 10.5 – Premiers pas avec TensorFlow
**Durée : ~50–60 min**  

Votre premier réseau professionnel — apprenez à utiliser **TensorFlow**, standard industriel du Deep Learning.

### Ce que vous allez apprendre
- Installation et configuration de TensorFlow  
- Concepts fondamentaux : tenseurs et graphes  
- Keras, l’API simple  
- Construire un modèle complet  
- Entraînement, validation et sauvegarde  
- Déploiement en production  

### Pourquoi TensorFlow domine
Écosystème complet, performance, déploiement multi-plateforme, support Google.  

Écosystème :
- **Développement** : Keras, TensorBoard, TF Data, TF Probability, TF Agents.  
- **Déploiement** : TF Serving, TF Lite, TF.js, TF Extended, Cloud AI Platform.  

> *« TensorFlow démocratise le Deep Learning : de la recherche académique à l'application industrielle. »*

---

## Résumé et points clés du Module 10

- Les réseaux de neurones imitent le cerveau (neurones, connexions, activation).  
- L'architecture détermine la capacité d’apprentissage.  
- La backpropagation permet l’entraînement automatique.  
- Les CNN révolutionnent la vision.  
- TensorFlow démocratise le Deep Learning industriel.  

### Checklist
- [x] Comprendre un neurone artificiel  
- [x] Différencier ML classique vs Deep Learning  
- [x] Connaître les architectures clés (MLP, CNN, Transformer)  
- [x] Expliquer la backpropagation  
- [x] Citer TensorFlow comme outil standard  

---
*Version : 2025-09-28 — © Votre cours ML*
