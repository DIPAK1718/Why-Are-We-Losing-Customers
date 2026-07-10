import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")

st.write(
    "Predict whether a customer is likely to churn."
)

st.sidebar.title("Customer Details")

gender = st.sidebar.selectbox(

    "Gender",

    ["Male","Female"]
)

senior = st.sidebar.selectbox(

    "Senior Citizen",

    [0,1]
)
partner = st.sidebar.selectbox(

    "Partner",

    ["Yes","No"]
)
dependents = st.sidebar.selectbox(

    "Dependents",

    ["Yes","No"]
)
tenure = st.sidebar.slider(

    "Tenure",

    0,

    72,

    24
)
monthly = st.sidebar.number_input(

    "Monthly Charges",

    18.25,

    120.0,

    70.0

)
contract = st.sidebar.selectbox(

    "Contract",

    [

        "Month-to-month",

        "One year",

        "Two year"

    ]

)
phone = st.sidebar.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

security = st.sidebar.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

backup = st.sidebar.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device = st.sidebar.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

support = st.sidebar.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

tv = st.sidebar.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

total = st.sidebar.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)
predict = st.sidebar.button(
    "Predict Churn"
)
import pandas as pd
from pathlib import Path
import joblib
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

model = joblib.load(MODEL_DIR / "churn_model.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
features = joblib.load(MODEL_DIR / "features.pkl")

if predict:

    sample = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[senior],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone],
        "MultipleLines":[multiple],
        "InternetService":[internet],
        "OnlineSecurity":[security],
        "OnlineBackup":[backup],
        "DeviceProtection":[device],
        "TechSupport":[support],
        "StreamingTV":[tv],
        "StreamingMovies":[movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless],
        "PaymentMethod":[payment],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]

    })

    sample = pd.get_dummies(sample)

    for col in features:
        if col not in sample.columns:
            sample[col] = 0

    sample = sample[features]

    sample = scaler.transform(sample)
    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    if probability < 0.30:
        risk = "🟢 Low"
    elif probability < 0.60:
        risk = "🟡 Medium"
    elif probability < 0.80:
        risk = "🟠 High"
    else:
        risk = "🔴 Very High"

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        if prediction == 1:
            st.error("❌ Customer Will Churn")
        else:
            st.success("✅ Customer Will Stay")

    with col2:
        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

    with col3:
        st.metric(
            "Risk Level",
            risk
        )
        st.progress(float(probability))

        st.caption(f"Model Confidence : {probability*100:.2f}%")

    st.subheader("💡 Business Recommendation")

    if probability >= 0.80:

        st.error("""
• Offer Discount

• Assign Premium Support

• Immediate Follow-up Call
""")

    elif probability >= 0.60:

        st.warning("""
• Send Retention Email

• Offer Upgrade

• Personalized Offer
""")

    else:

        st.success("""
• Customer is Stable

• Continue Normal Engagement
""")
    st.divider()


    st.subheader("📋 Customer Summary")

    summary = pd.DataFrame({

            "Feature":[
                "Gender",
                "Tenure",
                "Contract",
                "Internet",
                "Monthly Charges",
                "Payment"
            ],

            "Value":[
                gender,
                tenure,
                contract,
                internet,
                monthly,
                payment
            ]
        })

    st.dataframe(
            summary,
            use_container_width=True
        )
    st.divider()

    st.subheader("📈 Model Performance")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Accuracy","80.38%")
    c2.metric("ROC-AUC","83.57%")
    c3.metric("Precision","64.76%")
    c4.metric("Recall","57.49%")

    report = pd.DataFrame({

        "Prediction":[prediction],

        "Probability":[round(probability*100,2)],

        "Risk":[risk]

    })
    st.divider()

    st.subheader("📊 Top 10 Features Affecting Churn")

    importance = pd.read_csv(
        MODEL_DIR.parent / "data" / "feature_importance.csv"
    )

    top10 = importance.head(10)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        top10["Feature"],
        top10["Importance"]
    )

    ax.invert_yaxis()

    ax.set_xlabel("Importance")

    st.pyplot(fig)
    st.divider()

    st.subheader("🔍 Why did the model make this prediction?")

    reasons = []

    if tenure < 12:
        reasons.append("🟠 Customer tenure is less than 1 year.")

    if contract == "Month-to-month":
        reasons.append("🟠 Customer has a Month-to-Month contract.")

    if internet == "Fiber optic":
        reasons.append("🟠 Customer uses Fiber Optic Internet.")

    if payment == "Electronic check":
        reasons.append("🟠 Customer pays using Electronic Check.")

    if monthly > 80:
        reasons.append("🟠 Monthly Charges are high.")

    if support == "No":
        reasons.append("🟠 Customer has no Tech Support.")

    if security == "No":
        reasons.append("🟠 Customer has no Online Security.")

    if len(reasons) == 0:
        st.success("✅ No major churn indicators detected.")

    else:

        for r in reasons:
            st.write(r)
    st.divider()

    st.subheader("📌 Suggested Retention Actions")

    actions = []

    if contract == "Month-to-month":
        actions.append("✔ Offer 1-Year Contract Discount")

    if payment == "Electronic check":
        actions.append("✔ Encourage Auto-Payment")

    if support == "No":
        actions.append("✔ Offer Free Tech Support Trial")

    if security == "No":
        actions.append("✔ Bundle Online Security Service")

    if monthly > 80:
        actions.append("✔ Offer Loyalty Discount")

    if tenure < 12:
        actions.append("✔ Send Welcome Retention Offer")

    if len(actions) == 0:

        st.success("Customer appears stable. Continue regular engagement.")

    else:

        for a in actions:
            st.write(a)
    st.download_button(

        "📥 Download Report",

        report.to_csv(index=False),

        file_name="prediction_report.csv",

        mime="text/csv"
    )