# 🏠 House Price Predictions — MLOps + CI/CD

This project demonstrates how to build a Machine Learning workflow for predicting house prices along with CI/CD automation.

---

## 🚀 Objectives

✔ Build an ML model to predict house prices  
✔ Automate training and testing  
✔ Integrate CI/CD (GitHub Actions)  
✔ Maintain clean, production-ready code  

---

## 🛠 Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- GitHub Actions (CI/CD)
- Docker (optional)
- MLflow (optional)

---

## 📂 Project Structure

```
project/
│── data/
│── src/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│── models/
│── notebooks/
│── requirements.txt
│── README.md
```

---

## ▶️ How to Set Up

### 1️⃣ Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Training

```bash
python src/train.py
```

---

## 🧪 Testing (if tests added)

```bash
pytest
```

---

## 🔄 CI/CD (GitHub Actions)

Whenever code is pushed:

✔ Lint  
✔ Install dependencies  
✔ Run training/tests  

You can customize workflows inside:

```
.github/workflows/
```

---

## 🤝 Contributing

1. Fork repository  
2. Create branch  
3. Commit changes  
4. Open Pull Request  

---

## 📜 License

This project is for educational and learning purposes.

---

### 💡 Credits

Developed as part of learning MLOps + CI/CD workflow.
