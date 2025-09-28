# 📦 Module 3 • Chapitre 1  
## Installation et configuration de l'environnement Python

**Niveau** : Débutant  
**Durée** : ~30-35 min  

---

## 🎯 Objectifs
- Découvrir 3 méthodes pour installer Python : **Cloud**, **Local (Anaconda)**, **Portable**  
- Installer Anaconda (recommandé)  
- Ajouter les bibliothèques ML essentielles  
- Vérifier le bon fonctionnement  
- Résoudre les problèmes courants  

---

## 🔑 Choisir votre méthode d'installation

### ☁️ Option 1 — **Google Colab** (recommandée pour débuter)
✅ Aucune installation  
✅ GPU gratuits (12h/jour)  
✅ Sauvegarde auto sur Google Drive  
❌ Internet requis  

Idéal pour : **débutants, apprentissage, prototypage rapide**  

**Étapes** :
1. Aller sur [Google Colab](https://colab.research.google.com)  
2. Se connecter avec un compte Google  
3. Créer un nouveau notebook  
4. Tester avec :  

```python
import sys
print(f"🐍 Version Python : {sys.version}")
```

---

### 💻 Option 2 — **Installation locale avec Anaconda**  
Recommandée pour un **usage régulier ou professionnel**.

#### 🔹 Windows
1. Télécharger → [anaconda.com/download](https://www.anaconda.com/download)  
2. Double-clic sur `.exe`  
3. Suivre l’assistant (options par défaut OK)  
4. Vérifier avec :  
   ```bash
   conda --version
   ```

#### 🔹 macOS
1. Télécharger la version macOS  
2. Installer via `.pkg`  
3. Vérifier dans **Terminal.app** :  
   ```bash
   conda --version
   ```

#### 🔹 Linux (Ubuntu/Debian)
```bash
cd ~
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
chmod +x Anaconda3-2024.02-1-Linux-x86_64.sh
./Anaconda3-2024.02-1-Linux-x86_64.sh
source ~/.bashrc
conda --version
```

⚠️ Si `conda` n’est pas trouvé, utilisez :  
```bash
$HOME/anaconda3/bin/conda init bash
source ~/.bashrc
```

---

### 🎒 Option 3 — **Python.org + pip** (portable)  
✅ Installation légère et rapide  
❌ Gestion manuelle des dépendances  
❌ Conflits possibles  

Réservé aux **utilisateurs avancés**.

---

## ⚙️ Configuration de l’environnement ML

### 1. Créer un environnement dédié
```bash
conda create -n ml-course python=3.10 -y
conda activate ml-course
python --version
```

### 2. Installer les bibliothèques essentielles
```bash
conda install -c conda-forge   numpy   pandas   scikit-learn   matplotlib   seaborn   jupyter   notebook -y
```

### 3. Ajouter des bibliothèques utiles
```bash
pip install   plotly   ydata-profiling   streamlit
```

---

## ✅ Vérification post-installation
```bash
conda --version
python --version
conda info --envs
```

---

## 🛠️ Dépannage rapide

- **Conda non trouvé après installation**  
  ```bash
  $HOME/anaconda3/bin/conda init bash
  source ~/.bashrc
  ```

- **Recharger la config shell**  
  ```bash
  exec bash -l
  ```

- **Forcer l’ajout au PATH**  
  ```bash
  echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  ```

---

## 📌 Points clés à retenir
- **Colab** → meilleur choix pour **débuter** (simple, gratuit).  
- **Anaconda** → idéal pour un **usage régulier et pro** (gestion d’environnements).  
- **Python.org + pip** → réservé aux **avancés**.  
- Après installation, toujours **tester Python + bibliothèques ML**.  
