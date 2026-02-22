def analyze_finances(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    savings_rate = (savings / income * 100) if income > 0 else 0

    return {
        "total_expenses": total_expenses,
        "savings": savings,
        "savings_rate": round(savings_rate, 2)
    }
