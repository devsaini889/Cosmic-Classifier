# 🌌 COSMIC CLASSIFIER 🚀  


> 🪐 *“Decode Dr. Klaus Reinhardt’s final transmission and classify the galaxies to save humanity.”*

---

## 🧭 Theme

The **Galactic Classification Challenge (GCC)** — also known as **Cosmic Classifier** — is an official ML competition under **Cognizance 2025, IIT Roorkee**.  
Participants must develop an intelligent classifier to predict the type of planets based on their environmental and physical characteristics.  
The fate of humankind lies in your hands ⚡  

---

## 🪐 Storyline

In **2547**, Dr. Klaus Reinhardt — a visionary space explorer — transmitted his final dataset moments before his ship was consumed by a black hole.  
The data, distorted by gravitational interference, holds the key to identifying habitable worlds.  
Your mission: **reconstruct, clean, and classify** planets using machine learning techniques to ensure humanity’s survival.

---

## 🧠 Problem Statement

You are provided with a dataset containing **10 attributes per planet**.  
Your goal is to classify each planet into one of **10 German-named categories**.

### 🧩 Input Features  

| Feature | Description |
|----------|-------------|
| Atmospheric Density | Thickness of the planet’s atmosphere (kg/m³) |
| Surface Temperature | Average temperature on the planet (Kelvin) |
| Gravity | Surface gravitational acceleration (m/s²) |
| Water Content | Percentage of surface covered by water (0–100 %) |
| Mineral Abundance | Index representing valuable mineral presence (0–1) |
| Orbital Period | Time the planet takes to orbit its star (days) |
| Proximity to Star | Distance from host star (AU) |
| Magnetic Field Strength | Magnetic field intensity (Tesla) |
| Radiation Levels | Average radiation (Sieverts/year) |
| Atmospheric Composition Index | Suitability of atmosphere (0–1 scale) |

### 🎯 Output Classes (Planet Types in German)

1. **Bewohnbar** – Habitable  
2. **Terraformierbar** – Terraformable  
3. **Rohstoffreich** – Resource-Rich  
4. **Wissenschaftlich** – Scientific  
5. **Gasriese** – Gas Giant  
6. **Wüstenplanet** – Desert World  
7. **Eiswelt** – Ice World  
8. **Toxischetmosäre** – Toxic Atmosphere  
9. **Hohestrahlung** – High Radiation  
10. **Toterahswelt** – Dead World  

---

## 🪙 Objective

Build a **multi-class classification model** that predicts the type of a planet using the provided 10 attributes.  
The dataset contains **noise** and **missing labels** (caused by black-hole interference).  
📈 **Evaluation Metric:** Accuracy  

---

## 🧰 Dataset Details  

| File | Description |
|------|--------------|
| `train.csv` | 60 000 samples with labels |
| `test.csv` | 10 000 samples (no labels) |
| `submission.csv` | Columns → `Planet_ID`, `Predicted_Class` |

> ⚠️ Missing values are represented by large negative numbers — filter them before training.

---

## ⚙️ Project Workflow  



### 🚀 Pipeline Steps

1. **Data Preprocessing**
   - Handle missing values  
   - Scale numerical features  
   - Encode labels  

2. **Model Training**
   - Algorithms: Decision Tree, Random Forest, XGBoost, Logistic Regression  
   - Hyperparameter tuning via RandomizedSearchCV  

3. **Evaluation**
   - Compare Accuracy, F1 Score, ROC-AUC  

4. **Deployment**
   - Space-themed Streamlit Dashboard (`app.py`)  
   - Real-time classification and visualization  

---

## 🧠 Machine Learning Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3.9 + |
| **Frontend** | Streamlit + Custom CSS |
| **ML Algorithms** | Decision Tree, Random Forest, XGBoost, Logistic Regression |
| **Libraries** | NumPy • Pandas • Scikit-learn • Plotly |
| **Visualization** | Plotly Express • Seaborn |
| **Notebook IDE** | Jupyter / Colab |

---

## 🌌 Streamlit Interface Preview  

A beautiful **dark space-themed dashboard** with real-time prediction and feature analysis.


**Features of the App 🌠**
- Adjust planetary parameters using sliders  
- Visualize feature importance  
- See confidence scores & classification results  
- Export analysis as CSV  

---

## 📂 Project Structure  
```
cosmic-classifier/
│
├── app.py # Streamlit Frontend
├── model.ipynb # Model Training Notebook
├── decision_tree_model.pkl # Trained Model
├── x.xlsx # Input Features
├── y.xlsx # Target Labels
├── architecture_diagram.png # Workflow Image
├── images/
│ └── space_background.jpg # Background Image
└── README.md
```

---

## 💻 Installation  

```bash
git clone https://github.com/yourusername/cosmic-classifier.git
cd cosmic-classifier
pip install -r requirements.txt
```
🚀 Run the App
```streamlit run app.py```


