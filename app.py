import streamlit as st

#(BLACK & ORANGE)
st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111111;
}

/* Buttons */
.stButton>button {
    background-color: #ff7a00;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ff9500;
}

/* Input boxes */
.stTextInput>div>div>input,
.stNumberInput input,
.stDateInput input {
    background-color: #1c1c1c;
    color: white;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: #1c1c1c;
}

/* Metric cards */
[data-testid="stMetricValue"] {
    color: #ff7a00;
}

/* Titles */
h1, h2, h3 {
    color: #ff7a00;
}

</style>
""", unsafe_allow_html=True)

from database import *
from analytics import *

# Page config
st.set_page_config(page_title="Expense Tracker Ano Tara", page_icon="💰", layout="wide")

create_table()

# Sidebar
st.sidebar.title("💰 Expense Tracker")
st.sidebar.write("A Smart Student Finance App")
menu = ["➕ Add Expense","📄 View Expenses","📊 Dashboard"]
choice = st.sidebar.radio("Navigate", menu)

# Title
st.title("💰 iSmart Expense Tracker Ano Tara?")
st.write("Track your daily spending and understand your money better! at wag maging gastador")

# ---------------- ADD EXPENSE ----------------
if choice == "➕ Add Expense":
    st.subheader("Add New Expense")

    col1, col2 = st.columns(2)

    with col1:
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0)

    with col2:
        category = st.selectbox("Category",["Food","Transport","School","Bills","Other"])
        desc = st.text_input("Description")

    if st.button("Add Expense"):
        add_expense(str(date), amount, category, desc)
        st.success("✅ Expense Added Successfully!")

# ---------------- VIEW EXPENSES ----------------
elif choice == "📄 View Expenses":
    st.subheader("All Expenses")

    if len(st.session_state.expenses) == 0:
        st.info("No expenses yet")
    else:
        st.info("No expenses yet.")

# ---------------- DASHBOARD ----------------
elif choice == "📊 Dashboard":
    st.subheader("Spending Dashboard")

    data = view_expenses()

    if data:
        df = load_data(data)

        # Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Expenses", len(df))
        col2.metric("Total Spending", f"₱ {df['Amount'].sum():.2f}")
        col3.metric("Highest Expense", f"₱ {df['Amount'].max():.2f}")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.write("### Spending by Category")
            st.bar_chart(category_chart(df))

        with col2:
            st.write("### Monthly Spending")
            st.line_chart(monthly_chart(df))
    else:
        st.info("Add some expenses to see dashboard.")