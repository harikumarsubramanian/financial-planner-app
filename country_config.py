# country_config.py

country_config = {
    "United States": {
        "currency_symbol": "$",
        "investment_options": {
            "Stocks": "S&P 500 ETFs, Individual Stocks",
            "Bonds": "US Treasury Bonds, Corporate Bonds",
            "Real Estate": "REITs, Rental Properties"
        },
        "allocation_models": {
            "Conservative": {"Stocks": 20, "Bonds": 70, "Real Estate": 10},
            "Balanced": {"Stocks": 50, "Bonds": 40, "Real Estate": 10},
            "Aggressive": {"Stocks": 80, "Bonds": 10, "Real Estate": 10},
            "Growth Focused": {"Stocks": 70, "Bonds": 20, "Real Estate": 10},
            "Income Focused": {"Stocks": 30, "Bonds": 60, "Real Estate": 10}
        }
    },

    "India": {
        "currency_symbol": "₹",
        "investment_options": {
            "Stocks": "Nifty ETFs, Individual Stocks",
            "Bonds": "Government Bonds, Corporate Bonds",
            "Real Estate": "REITs, Rental Properties"
        },
        "allocation_models": {
            "Conservative": {"Stocks": 20, "Bonds": 70, "Real Estate": 10},
            "Balanced": {"Stocks": 50, "Bonds": 40, "Real Estate": 10},
            "Aggressive": {"Stocks": 80, "Bonds": 10, "Real Estate": 10},
            "Growth Focused": {"Stocks": 70, "Bonds": 20, "Real Estate": 10},
            "Income Focused": {"Stocks": 30, "Bonds": 60, "Real Estate": 10}
        }
    },

    "United Kingdom": {
        "currency_symbol": "£",
        "investment_options": {
            "Stocks": "FTSE 100 ETFs, Individual Stocks",
            "Bonds": "UK Gilts, Corporate Bonds",
            "Real Estate": "REITs, Rental Properties"
        },
        "allocation_models": {
            "Conservative": {"Stocks": 20, "Bonds": 70, "Real Estate": 10},
            "Balanced": {"Stocks": 50, "Bonds": 40, "Real Estate": 10},
            "Aggressive": {"Stocks": 80, "Bonds": 10, "Real Estate": 10},
            "Growth Focused": {"Stocks": 70, "Bonds": 20, "Real Estate": 10},
            "Income Focused": {"Stocks": 30, "Bonds": 60, "Real Estate": 10}
        }
    }

    # You can add more countries here
}
