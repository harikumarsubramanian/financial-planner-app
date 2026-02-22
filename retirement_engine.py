def calculate_retirement_corpus(
    current_annual_expense,
    years_to_retirement,
    inflation_rate,
    withdrawal_rate=0.04
):
    # Adjust expenses for inflation
    future_expense = current_annual_expense * ((1 + inflation_rate) ** years_to_retirement)

    # Required retirement corpus using 4% rule
    required_corpus = future_expense / withdrawal_rate

    return round(future_expense, 2), round(required_corpus, 2)
