import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)


# Title
st.title("📈 Customer Churn Business Analytics Dashboard")
st.markdown(
    "Business insights generated from the Telecom Customer Churn dataset."
)
# Load Data
df = pd.read_csv("data/customer_churn.csv")

# KPI Cards

total_customers = len(df)
churn_rate = (df["Churn"] == 1).mean() * 100
avg_monthly = df["MonthlyCharges"].mean()
avg_tenure = df["tenure"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Customers", total_customers)
c2.metric("📉 Churn Rate", f"{churn_rate:.2f}%")
c3.metric("💰 Avg Monthly Charges", f"${avg_monthly:.2f}")
c4.metric("📅 Avg Tenure", f"{avg_tenure:.1f} Months")

# Contract Distribution
st.divider()
st.subheader("📄 Contract Distribution")
contract = df["Contract"].value_counts()
fig, ax = plt.subplots(figsize=(6,6))
ax.pie(
    contract,
    labels=contract.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Contract Types")
st.pyplot(fig)

# Churn by Contract
st.divider()
st.subheader("📉 Churn by Contract")
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)
st.bar_chart(contract_churn)

# Internet Service
st.divider()
st.subheader("🌐 Internet Service Distribution")
internet = df["InternetService"].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(
    internet.index,
    internet.values
)

ax.set_xlabel("Internet Service")
ax.set_ylabel("Customers")
st.pyplot(fig)

# Churn by Internet Service
st.divider()
st.subheader("🌐 Churn by Internet Service")

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

st.bar_chart(internet_churn)

# Payment Method
st.divider()
st.subheader("💳 Payment Method Distribution")
payment = df["PaymentMethod"].value_counts()
st.bar_chart(payment)


# Churn by Payment Method
st.divider()
st.subheader("💰 Churn by Payment Method")
payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

st.bar_chart(payment_churn)

# Business Insights
st.divider()
st.subheader("📌 Business Insights")
st.info("""
### Key Findings
• Month-to-Month customers have the highest churn.
• Fiber Optic users churn more than DSL users.
• Electronic Check customers have the highest churn rate.
• Customers with longer tenure are much less likely to churn.
• Long-term contracts significantly improve customer retention.
""")


# Footer

st.divider()
st.caption("Built by Dipak Chaudhari | Customer Churn Business Analytics Dashboard")