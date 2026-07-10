# 📊 Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project predicts whether a customer is likely to leave the company using Machine Learning. It also provides business recommendations and an interactive Streamlit dashboard for decision making.

--- 

# 🚀 Features 

- Data Cleaning & Preprocessing 
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Logistic Regression Model
- Feature Importance Analysis 
- Customer Risk Segmentation
- Interactive Streamlit Prediction App
- Business Analytics Dashboard
- SQL Business Analysis 
- Downloadable Prediction Report

---

# 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

Target Variable:

- Churn
  - 1 → Customer Leaves
  - 0 → Customer Stays

---

# 🛠 Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

### Database

- SQLite

### SQL

- Business Analysis Queries

---

# 📁 Project Structure

```
WHY-ARE-WE-LOSING-CUSTOMERS
│
├── dashboard/
│   ├── app.py
│   └── analytics.py
│
├── data/
│   ├── customer_churn.csv
│   └── feature_importance.csv
│
├── images/
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── reports/
│
├── sql/
│   └── analysis.sql
│
├── customer_churn.db
├── churn_analysis.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
EDA
   │
   ▼
Feature Engineering
   │
   ▼
Train/Test Split
   │
   ▼
StandardScaler
   │
   ▼
Logistic Regression
   │
   ▼
Evaluation
   │
   ▼
Risk Prediction
   │
   ▼
Streamlit Dashboard
```

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 80.38% |
| ROC-AUC | 83.57% |
| Precision | 64.76% |
| Recall | 57.49% |

---

# 📉 Top Features Affecting Churn

| Feature | Importance |
|----------|-----------:|
| tenure | 1.3476 |
| MonthlyCharges | 0.8516 |
| InternetService_Fiber optic | 0.7277 |
| TotalCharges | 0.6390 |
| Contract_Two year | 0.6026 |
| Contract_One year | 0.3109 |
| StreamingTV_Yes | 0.2497 |
| StreamingMovies_Yes | 0.2364 |
| MultipleLines_Yes | 0.2144 |
| PaymentMethod_Electronic check | 0.1815 |

---

# 📊 Dashboard Features

### Customer Prediction

- Predict customer churn
- Churn probability
- Risk level
- Business recommendation

### Analytics Dashboard

- Customer Overview
- Churn Rate
- Contract Distribution
- Internet Service Analysis
- Payment Method Analysis
- Senior Citizen Analysis

---

# 🗄 SQL Analysis

Business SQL queries include:

- Overall Churn Rate
- Contract-wise Churn
- Payment Method Analysis
- Internet Service Analysis
- Customer Segmentation
- High Risk Customers
- Revenue Analysis
- Monthly Charges Statistics

---

# 💡 Business Insights

- Customers with **Month-to-month contracts** have higher churn.
- **Fiber optic** users show a higher churn tendency.
- **Electronic check** users churn more frequently.
- Longer customer **tenure** reduces churn risk.
- Higher monthly charges increase churn probability.

---

# ▶️ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Prediction App

```bash
streamlit run dashboard/app.py
```

### Run Analytics Dashboard

```bash
streamlit run dashboard/analytics.py
```

---

# 📷 Screenshots

Add screenshots here:

- Prediction Dashboard
- Analytics Dashboard
- Risk Distribution
- Feature Importance
- Confusion Matrix
- ROC Curve

---

# 🔮 Future Improvements

- XGBoost & LightGBM
- Hyperparameter Tuning
- SHAP Explainability
- Docker Deployment
- Cloud Deployment
- Real-time Prediction API

---

# 👨‍💻 Author

**Dipak Chaudhari**

- AI / ML Enthusiast
- Data Science Student
- Machine Learning Projects
