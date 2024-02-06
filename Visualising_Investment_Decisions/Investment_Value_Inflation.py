from Inflation_Calculator import get_inflation
from dateutil import parser
import numpy as np

def calculate_adjusted_values(investment: int, investment_start: str, investment_end: str = None):

    # Get the data values in the period specified by user
    monthly_inflation = get_inflation(investment_start, investment_end)

    # Create inflation ceiling
    ceiling = np.percentile(monthly_inflation, 83)

    # Check if investment_end and parse it
    try:
        if investment_end:
            end_date = parser.parse(investment_end)
            end_year = end_date.year
            if end_year < 2000:
                raise ValueError("Year_end must be after 2000.")
    except ValueError:
        print("Invalid start_date format. 'Month-Day-Year'.")

    # Add aditional years if investment_end is over last year in table
    if end_year > 2023:
        additional_years = np.arange(2023, end_year)
        # Inflate every year by 2% the target of The Federal Reserve annualy on aditional years
        additional_inflation_rates = np.full(len(additional_years), 0.02)
        # Halve inflation rate if it surpasses ceiling inflations
        for i in range(len(additional_inflation_rates)):
            if additional_inflation_rates > ceiling:
                additional_inflation_rates[i] /= 2
                # Join inflation rates for all years
                inflation_rates = np.concatenate(
                    monthly_inflation, additional_inflation_rates)
    else:
        # If there are no additional years then the inflation rates will be the monthly inflation
        inflation_rates = monthly_inflation

    # Calculate values adjusting for inflation
    adjusted_values = investment * (1 + inflation_rates)

    return adjusted_values
