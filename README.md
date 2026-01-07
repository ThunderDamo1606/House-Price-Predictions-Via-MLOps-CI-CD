# 🏠 House Price Predictions — MLOps + CI/CD  

An end-to-end machine learning project that predicts house prices and demonstrates how to automate the ML workflow using **GitHub Actions CI/CD**.

This project focuses on:

- reproducible ML pipelines  
- automated testing  
- training + evaluation  
- model + metrics artifacts  
- clean, production-style code  

---

## ✨ Features

✅ Auto dataset generation  
✅ Model training & evaluation  
✅ Unit tests  
✅ CI/CD pipeline  
✅ Artifacts saved per run  
✅ Easy to extend & deploy  

---

## 🛠 Tech Stack

| Area | Tools |
|------|------|
Programming | Python
ML | Pandas, NumPy, Scikit-learn
Automation | GitHub Actions (CI/CD)
Serialization | joblib
Optional | Docker, MLflow

---

## 📂 Project Structure

```
project/
│── data/                 # datasets
│── models/               # saved models + metrics
│── src/
│   ├── generate_data.py  # dataset generator
│   ├── train.py          # model training
│   ├── evaluate.py       # evaluation
│   ├── validate_data.py  # sanity checks
│── tests/
│   └── test_training.py  # unit tests
│── .github/workflows/
│   └── ml_pipeline.yml   # CI/CD pipeline
│── requirements.txt
│── README.md
```

---

## ▶️ Setup & Installation

### 1️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset (auto-generated)

Generate sample dataset:

```bash
python src/generate_data.py
```

Creates:

```
data/housing.csv
```

---

## 🤖 Train Model

```bash
python src/train.py
```

Saves model:

```
models/model.pkl
```

---

## 📈 Evaluate Model

```bash
python src/evaluate.py
```

Metrics saved:

```
models/metrics.txt
```

---

## 🔄 CI/CD — GitHub Actions

On every push:

1️⃣ Lint  
2️⃣ Validate data  
3️⃣ Run tests  
4️⃣ Train model  
5️⃣ Evaluate  
6️⃣ Upload artifacts  

Workflow:

```
.github/workflows/ml_pipeline.yml
```

---

## 🧪 Tests

```bash
pytest
```

---

## 🤝 Contributing

1. Fork  
2. Create branch  
3. Commit  
4. Open PR  

---

## 📜 License

This project is for **learning and educational purposes** only.

---

### 🙌 Credits

Built while learning **MLOps + CI/CD best practices**.
