# Module 12 – IA & ML : Tendances, Éthique, Carrières & Ressources
**Niveau : Réflexion / Orientation • Durée totale : ~2h40**  

---

## 12.1 – Tendances émergentes en Machine Learning
### Ce que vous allez découvrir
- Révolutions technologiques en cours (IA générative, quantique, AutoML)
- IA explicable & éthique (XAI)
- Nouvelles architectures (ViT, NAS, Foundation Models)

### IA générative : l’accélération
> *« L’IA générative n’augmente pas seulement la productivité : elle élargit l’espace des possibles créatifs. »*  
**Domaines & impact actuel :**
- **Texte** (rédaction, code, traduction, synthèse) — **~85%**
- **Images** (art, design, photo, concept art) — **~75%**
- **Multimodal** (vidéo, audio, avatars, mondes virtuels) — **~45%**

**Évolution des architectures**
- **2017–2019 :** GANs (StyleGAN) → images réalistes
- **2020–2021 :** Transformers (GPT‑3) → texte de haute qualité
- **2022–2023 :** Explosion multimodale (DALL·E 2, Midjourney, SD) + ChatGPT
- **2024+ :** IA générative omniprésente, assistants personnalisés, vidéo haute qualité

**Défis clés** : authenticité, droits d’auteur, désinformation, sécurité.

### ML quantique (QML) : prochaine frontière
- **Promesses :** parallélisme massif, optimisation combinatoire, simulation complexe, chiffrement quantique.
- **Calendrier indicatif :**
  - **2019–2021 :** suprématie quantique (prototypes), premiers algos QML
  - **2022–2024 :** cas d’usage ciblés, cloud quantique
  - **2025–2030 :** correction d’erreurs, gains pratiques, adoption sectorielle
- **Réalité actuelle :** ère **NISQ** (machines bruyantes, taille limitée).

### AutoML : démocratisation du ML
- **Niveau 1 :** sélection d’algorithmes, HPO, CV, métriques
- **Niveau 2 :** feature engineering auto, NAS, ensembles intelligents, détection d’anomalies
- **Niveau 3 :** pipeline autonome (compréhension métier → déploiement → monitoring)
- **Impact :** abaisse les barrières (PME, santé, agriculture, éducation).

### IA explicable (XAI)
- **Pourquoi :** régulations (RGPD), confiance, débogage, équité.
- **Approches :** modèles intrinsèquement explicables ; post‑hoc global (SHAP/LIME) ; post‑hoc local ; *explainability‑by‑design* (attention interprétable).

### Architectures émergentes
- **Vision Transformers (ViT) :** relations longue portée, meilleure généralisation, unification vision‑langage, interprétabilité via attention.
- **NAS :** recherche auto d’architectures (RL, évolution, gradients) → EfficientNet, MobileNet, DARTS, ProxylessNAS…
- **Foundation Models :** (GPT‑4, BERT, T5, CLIP…) — pré‑entraînement massif, auto‑supervisé, capacités émergentes, *fine‑tuning* rapide.

### 2025–2030 : projections (indicatives)
- **2025 :** assistants multimodaux, intégrés aux OS, XAI standardisé (**~85%**)
- **2027 :** premiers avantages quantiques pratiques (**~60%**)
- **2030 :** signaux d’AGI limitée (**~30%**)
- **Défis transverses :** énergie, biais, sécurité, emploi, régulation, éthique.

---

## 12.2 – Impact sociétal & éthique
### Travail : menace ou opportunité ?
- **À risque (40–60% tâches) :** saisie, caisse, conduite, L1 support, junior compta/finance, traduction basique…
- **En évolution (20–40%) :** médecins, avocats, enseignants, journalistes, designers, devs, marketeurs…
- **Émergents (+300% d’ici 2030) :** IA éthique, *prompt* engineers, explicateurs d’IA, auditeurs, coordinateurs humain‑IA…
- **Transition juste :** re/up‑skilling, politiques publiques (RU ?), mobilité interne, innovation sociale.

### Biais algorithmiques
- **Sources :** données (historiques, représentation, mesure), algorithmes (agrégation, optimisation, interprétation).
- **Cas emblématiques :** justice pénale (COMPAS), recrutement (outil abandonné), reconnaissance faciale.
- **Parades :** audits de *fairness*, jeux de données équilibrés, métriques d’équité (EO/DP), adversarial debiasing, XAI, gouvernance & équipes diverses.

### Vie privée & surveillance
- **Triptyque :** commerciale (profilage), étatique (RF, prédictif), auto‑surveillance (IoT, wearables).
- **Modèles & techniques :** RGPD (consentement, DPO, droit à l’oubli), *differential privacy*, *federated learning*, chiffrement homomorphe, ZK‑proofs, identité décentralisée.

### Impact environnemental
- **Contrainte :** coûts énergétiques entraînement/inférence/refroidissement.
- **Voies “IA verte” :** architectures efficaces (distillation, pruning, quantization), *transfer learning*, edge, énergies renouvelables, métriques carbone, mutualisation & régulation.

### Désinformation & post‑vérité
- **Vecteurs :** deepfakes, textes générés, images synthétiques.
- **Contre‑mesures :** détection IA, provenance/traçabilité, watermarking, fact‑checking, signatures cryptographiques, éducation aux médias, transparence des plateformes, cadre légal.

### Vers une IA responsable
- **Principes :** bienfaisance, non‑malfaisance, autonomie, justice, explicabilité.
- **Mise en œuvre :** privacy‑by‑design, *human‑in‑the‑loop*, audits, transparence, responsabilité.
- **Initiatives :** EU AI Act (cadre par risques), Executive Order (US), Partnership on AI, recherche en AI Safety.

---

## 12.3 – Opportunités de carrière en ML
### Marché & secteurs
- **Croissance offres :** +35%/an ; **pénurie** chronique ; recrutements en ~3 mois.
- **Secteurs :** Tech, finance, santé, retail, industrie ; **remote ~60%** ; hubs : SV, Paris, Londres, Berlin, Asie.

### Métiers techniques (fourchettes indicatives, FR)
- **Data Scientist :** 45–120k€ — EDA, modèles, A/B, storytelling.
- **ML Engineer :** 55–140k€ — archi prod, MLOps, perf, cloud/edge.
- **Research Scientist :** 60–200k€ (+equity) — SOTA, publis, transfert.
- **Data Engineer :** 45–110k€ — pipelines, lakes/warehouses, qualité.

### Rôles business & produit
- **AI PM :** stratégie, priorisation, métriques d’adoption.
- **AI Business Analyst :** ROI/faisabilité, change, formation.

### Spécialisations demandées
- **Générative :** Prompt Engineer, Content Strategist, RLHF Trainer.
- **Éthique :** AI Ethics Officer, AI Auditor (conformité & biais).
- **Tech :** CV, NLP, Robotics AI, Reco, Time Series, LLM Ops.

### Parcours & accélération
- **Junior (0–2a) :** bases solides, 5+ projets GitHub, 1ère expérience.
- **Confirmé (2–5a) :** spécialisation, lead technique, mentoring, talks.
- **Senior (5–10a) :** vision produit, end‑to‑end, business impact.
- **Lead/Expert (10+a) :** thought leadership, recherche/stratégie.
- **Boosters :** niche d’expertise, open‑source, SOTA appliquée, certifs, réseau, communication.

### Salaires (repères)
- **FR/Paris :** Junior 40–60k€ • Confirmé 60–90k€ • Senior 85–130k€ • Expert 120–200k€ • Dir/VP 150–300k€+
- **International :** Junior 50–80k$ • Confirmé 80–120k$ • Senior 110–180k$ • Expert 160–350k$ • Top‑tier 200–500k$+
- **Primes :** LLM/GenAI (+20–40%), CV (+15–25%), MLOps (+10–20%), PhD/Research (+25–50%).

### Plan d’action carrière (30 jours)
- **Portfolio GitHub** (5 projets “cours + perso”)
- **LinkedIn** (skills, projets, résumé orienté impact)
- **Candidatures** (stage/Junior) + **communautés** (3 groupes)
- **Veille** (newsletters) + **certif** (GCP/AWS/Azure, Databricks, HF)

---

## 12.4 – Ressources pour continuer
### Formations de référence
- **Stanford CS229/CS231n**, **MIT 6.034**, **fast.ai**, **DeepLearning.ai**
- **Plateformes :** Coursera, Udacity, Pluralsight, **Kaggle Learn**

### Livres “bibliothèque ML”
- **Fondations :** *Hands‑On ML* (Géron), *ESL* (Hastie), *PRML* (Bishop)
- **Deep/RL :** *Deep Learning* (Goodfellow), *RL* (Sutton & Barto)
- **MLOps/Prod :** *Designing ML Systems* (Chip Huyen), *ML Engineering*

### Recherche & veille
- **Conf :** NeurIPS, ICML, ICLR, CVPR, ACL
- **Journaux :** JMLR (OA), PAMI, ML (Springer)
- **Sites :** Papers with Code, arXiv + Sanity, Semantic Scholar
- **Newsletters/Podcasts :** The Batch, Import AI, TWIML, MLST
- **YouTube :** Two Minute Papers, 3Blue1Brown, Yannic Kilcher

### Outils & frameworks
- **PyData :** NumPy, Pandas, Matplotlib/Seaborn, SciPy, Jupyter
- **ML :** scikit‑learn, XGBoost/LightGBM, Statsmodels, Imbalanced‑learn
- **DL :** PyTorch, TensorFlow/Keras, JAX, fastai, HF Transformers
- **MLOps :** Docker, K8s, FastAPI, Streamlit, MLflow, Kubeflow
- **Monitoring/Qualité :** W&B, Neptune, Evidently, Great Expectations

### Veille outillée
- **Alerts :** Google Scholar Alerts, Connected Papers, Twitter Lists
- **Routine 12 mois :**
  - M1–2 : bases (maths, NumPy/Pandas/Matplotlib, sklearn)
  - M3–4 : algos avancés, feature eng, CV/metrics, 1ère Kaggle
  - M5–6 : DL (from scratch + PyTorch/TensorFlow), projet GPU
  - M7–8 : spécialisation (CV/NLP/RL), fine‑tuning, open‑source
  - M9–10 : MLOps (Docker/API/CI/CD, monitoring), projet E2E
  - M11–12 : papers, blog/talks, réseau, préparation entretiens

---

## Checklists express
- **Éthique/XAI :** ✅ Fairness tests • ✅ Privacy‑by‑design • ✅ Human‑in‑the‑loop • ✅ Audit & logs
- **Prod ML :** ✅ Versionner data/modèles • ✅ Observabilité • ✅ Tests (unitaires/data) • ✅ Guardrails
- **Carrière :** ✅ Portfolio • ✅ Réseau • ✅ Certifs ciblées • ✅ Veille hebdo • ✅ Communication

> **Rappel :** l’excellence vient de la constance, pas de la perfection. Construisez des boucles courtes *apprendre → faire → partager → itérer*.
