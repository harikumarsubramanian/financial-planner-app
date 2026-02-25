# app.py
import streamlit as st
import matplotlib.pyplot as plt
from openai import OpenAI
from country_config import country_config
from financial_engine import analyze_finances
from goal_engine import generate_goal_projection
from retirement_engine import calculate_retirement_corpus

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#client = OpenAI()

st.set_page_config(page_title="Advanced AI Financial Planner", layout="centered")
st.title("🌍 Advanced AI Financial Planner")

# -----------------------
# Default allocation models
# -----------------------
default_models = {
    "Conservative": {"Stocks": 20, "Bonds": 80},
    "Balanced": {"Stocks": 50, "Bonds": 50},
    "Aggressive": {"Stocks": 80, "Bonds": 20}
}

# -----------------------
# Country Selection
# -----------------------
country = st.selectbox("Select Your Country", list(country_config.keys()))
config = country_config[country]
currency_symbol = config["currency_symbol"]

# Merge allocation_models from country_config with default_models
allocation_models = {**default_models, **config.get("allocation_models", {})}
config["allocation_models"] = allocation_models  # Update config

# -----------------------
# Income & Expenses
# -----------------------
st.header("💰 Monthly Financial Details")

income = st.number_input(f"Monthly Income ({currency_symbol})", min_value=0.0)

rent = st.number_input(f"Rent ({currency_symbol})", min_value=0.0)
groceries = st.number_input(f"Groceries ({currency_symbol})", min_value=0.0)
utilities = st.number_input(f"Utilities ({currency_symbol})", min_value=0.0)
emi = st.number_input(f"Loan EMI ({currency_symbol})", min_value=0.0)

expenses = {
    "Rent": rent,
    "Groceries": groceries,
    "Utilities": utilities,
    "EMI": emi
}

# -----------------------
# Goal Section
# -----------------------
st.header("🎯 Financial Goal")

goal_name = st.text_input("Goal Name")
goal_amount = st.number_input(f"Target Amount Today ({currency_symbol})", min_value=0.0)
goal_years = st.number_input("Years to Achieve Goal", min_value=1)
expected_annual_return = st.number_input("Expected Annual Return (%)", min_value=0.0, value=10.0)
inflation_rate = st.slider("Expected Inflation Rate (%)", 0.0, 15.0, 5.0) / 100

# -----------------------
# Retirement Section
# -----------------------
st.header("🏖 Retirement Planning")

current_annual_expense = st.number_input(
    f"Current Annual Living Expense ({currency_symbol})", min_value=0.0
)
years_to_retirement = st.number_input("Years to Retirement", min_value=1)

# -----------------------
# Generate Financial Plan
# -----------------------
plan_generated = False
if st.button("Generate Full Financial Plan"):
    plan_generated = True

    # --- Basic Analysis ---
    results = analyze_finances(income, expenses)

    st.subheader("📊 Current Financial Summary")
    st.write(f"Monthly Savings: {currency_symbol}{results['savings']}")
    st.write(f"Savings Rate: {results['savings_rate']}%")

    # --- Inflation Adjusted Goal ---
    inflated_goal = goal_amount * ((1 + inflation_rate) ** goal_years)
    st.subheader("📈 Inflation Adjusted Goal")
    st.write(f"Future Goal Value: {currency_symbol}{round(inflated_goal,2)}")

    # --- Goal Projection ---
    projections = generate_goal_projection(
        goal_amount=inflated_goal,
        annual_return=expected_annual_return,
        years=goal_years
    )

    st.subheader("💡 Goal Investment Projection")
    st.write(f"Monthly Investment Required: {currency_symbol}{projections['monthly_required']}")
    st.write(f"Total Investment Over {int(goal_years)} Years: {currency_symbol}{projections['total_invested']}")

    # --- Retirement Corpus ---
    future_expense, required_corpus = calculate_retirement_corpus(
        current_annual_expense,
        years_to_retirement,
        inflation_rate
    )

    st.subheader("🏖 Retirement Projection")
    st.write(f"Future Annual Expense at Retirement: {currency_symbol}{future_expense}")
    st.write(f"Required Retirement Corpus (4% Rule): {currency_symbol}{required_corpus}")

# -----------------------
# Investment Allocation Selection (outside button)
# -----------------------
strategy = st.selectbox(
    "Select Investment Strategy",
    ["None"] + list(config["allocation_models"].keys())
)

if plan_generated and strategy != "None":
    allocation = config["allocation_models"][strategy]

    st.subheader(f"📊 Suggested Allocation ({strategy})")
    for asset, percent in allocation.items():
        st.write(f"{asset}: {percent}%")

    # Pie Chart
    fig, ax = plt.subplots()
    ax.pie(allocation.values(), labels=allocation.keys(), autopct='%1.1f%%')
    ax.set_title(f"{strategy} Allocation")
    st.pyplot(fig)

# -----------------------
# AI Strategic Advice
# -----------------------
if plan_generated:
    prompt = f"""
You are a professional financial advisor in {country}.

User financial summary:
Monthly Income: {income}
Savings Rate: {results['savings_rate']}%

Goal: {goal_name}
Inflation Adjusted Goal: {inflated_goal}

Retirement Corpus Required: {required_corpus}

Selected Strategy: {strategy if strategy != 'None' else 'No Strategy'}
Allocation: {allocation if strategy != 'None' else 'N/A'}

Provide:
1. Whether savings are sufficient
2. Goal achievement feasibility
3. Retirement readiness evaluation
4. Risk explanation
5. Clear action plan
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("🤖 AI Strategic Advice")
    st.write(response.choices[0].message.content)
