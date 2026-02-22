# goal_engine.py

def calculate_monthly_investment(goal_amount, annual_return, years):
    """
    Calculate required monthly investment using the Future Value of an ordinary annuity formula.
    
    FV = P * [((1 + r)^n - 1) / r]

    Args:
        goal_amount (float): Target amount to achieve (inflation-adjusted).
        annual_return (float): Expected annual return in percentage (e.g., 10 for 10%).
        years (float): Number of years to achieve the goal.

    Returns:
        tuple: (monthly_required, total_invested)
            monthly_required: Required monthly investment to reach goal.
            total_invested: Total amount invested over the period.
    """
    # Ensure numeric types
    goal_amount = float(goal_amount)
    annual_return = float(annual_return)
    years = float(years)

    r = annual_return / 100 / 12  # Monthly return as decimal
    n = years * 12  # Total number of months

    if r == 0:
        # If return is 0%, simply divide goal by number of months
        monthly_required = goal_amount / n
    else:
        monthly_required = goal_amount * r / ((1 + r) ** n - 1)

    total_invested = monthly_required * n

    return monthly_required, total_invested


def generate_goal_projection(goal_amount, annual_return, years):
    """
    Generate a goal projection dictionary for Streamlit display.

    Args:
        goal_amount (float): Target goal amount (already inflation-adjusted).
        annual_return (float): Expected annual return in percentage.
        years (float): Years to achieve the goal.

    Returns:
        dict: {
            "monthly_required": float,  # Rounded monthly investment
            "total_invested": float     # Rounded total invested
        }
    """
    monthly_required, total_invested = calculate_monthly_investment(
        goal_amount, annual_return, years
    )

    return {
        "monthly_required": round(monthly_required, 2),
        "total_invested": round(total_invested, 2)
    }
