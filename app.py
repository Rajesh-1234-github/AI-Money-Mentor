import streamlit as st
import matplotlib.pyplot as plt

from finance_logic import calculate_savings, calculate_health_score, calculate_sip
from tax_logic import tax_suggestion
from ai_engine import get_ai_advice

# Title
st.title(" AI Money Mentor")

st.write("Enter your financial details:")

# User Input
salary = st.number_input("Monthly Salary (₹)", min_value=0)
expenses = st.number_input("Monthly Expenses (₹)", min_value=0)

# Goal Planning
st.subheader("Goal Planning")
goal_amount = st.number_input("Enter your Goal Amount (₹)", min_value=0)
goal_years = st.number_input("Years to achieve goal", min_value=1)

# Analyze Button
if st.button("Analyze"):

    #  Calculations
    savings = calculate_savings(salary, expenses)
    score = calculate_health_score(salary, expenses)
    tax = tax_suggestion(salary)
    sip = calculate_sip(goal_amount, goal_years)

    #  Results
    st.subheader(" Results")
    st.write(f" Monthly Savings: ₹{savings}")
    st.write(f" Money Health Score: {score}/100")
    st.write(f" Tax Suggestion: {tax}")
    st.write(f" Required Monthly Investment (SIP): ₹{int(sip)}")

    #  Basic AI Advice
    st.subheader(" AI Advice")
    if score > 80:
        st.success("Excellent financial health! Keep investing regularly.")
    elif score > 60:
        st.info("Good, but you can improve your savings and investments.")
    else:
        st.warning("Your savings are low. Try to reduce expenses and invest more.")

    #  Advanced AI (IMPORTANT FIX)
    st.subheader(" AI Financial Advisor")
    ai_advice = get_ai_advice(salary, expenses, savings, score)
    st.write(ai_advice)

    #  BAR GRAPH
    st.subheader(" Financial Overview")

    labels = ['Expenses', 'Savings']
    values = [expenses, savings]

    fig, ax = plt.subplots()
    ax.bar(labels, values, width=0.4)

    ax.set_ylim(0, max(values) * 1.25)
    ax.set_title("Monthly Financial Comparison")
    ax.set_ylabel("Amount (₹)")

    for i, v in enumerate(values):
        ax.text(i, v + (max(values) * 0.05), f"₹{v}", ha='center')

    st.pyplot(fig)

    #  PIE CHART
    st.subheader(" Expense vs Savings Distribution")

    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax2.set_title("Expense vs Savings Split")

    st.pyplot(fig2)
