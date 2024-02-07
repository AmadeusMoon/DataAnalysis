from Investment_Value_Accounting_Inflation import calculate_true_value
from Investment_Value_Inflation import calculate_adjusted_values
from Calculate_Tax import calculate_taxes
from dateutil import parser
import numpy as np

# 20% anual growth as per SP100 average growth
average_anual_growth_SP100 = 0.20

# Short-Term Capital Gains Tax
short_term_brackets = np.array([11600, 47150, 100525, 191950, 243725, 609350])
short_term_rates = np.array([0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])

# Long-Term Capital Gains Tax
long_term_brackets = np.array([44625, 492300, 50000])
long_term_rates = np.array([0.00, 0.15, 0.20])

# Calculate value of investments after taxes
def calculate_future_values_after_tax_and_fee(investment: int, investment_start: str, investment_end: str, income: int=None):

    # Parse dates
    try:
        investment_start_date = parser.parse(investment_start)
        investment_end_date = parser.parse(investment_end)
    except ValueError:
        print("Invalid date format. 'Month-Day-Year'.")

    investment_start_year = investment_start_date.year
    investment_end_year = investment_end_date.year

    # Error checks
    if investment_start_year > investment_end_year:
        raise ValueError(
            'Investment end year cannot be earlier than start year.')
    if investment_start_year < 2000:
        raise ValueError('Investment start year should be from 2000.')
    if investment_end_year < 2000:
        raise ValueError('Investment end year should be above 2000')
    # Calculate investment duration
    years = investment_end_year - investment_start_year

    # Initialise variable for investment type
    investment_type = ''

    # Define investment type
    if years > 5:
        investment_type = 'long_term'
    else:
        investment_type = 'short_term'

    # Choose the correct tax brackets and rates based on the investment type
    if investment_type == 'short_term':
        brackets = short_term_brackets
        rates = short_term_rates
    elif investment_type == 'long_term':
        brackets = long_term_brackets
        rates = long_term_rates

    # Call the functions to get the values
    values_clean = calculate_true_value(
        investment, investment_start, investment_end)
    values_adjusted = calculate_adjusted_values(investment,
                                                investment_start, investment_end)

    # Copy arrays
    future_values = values_clean.copy()
    inflated_values = values_adjusted.copy()

    # Loop through array and apply 20% growth only every 12 months
    for i in range(len(values_clean)):

        if i % 12 == 0:  # Apply the growth every 12 values
            future_values[i:] *= 1 + average_anual_growth_SP100
            inflated_values[i:] *= 1 + average_anual_growth_SP100

        # Calculate the SEC fee $22.90 per $1 million
        sec_fee_value = future_values[i] * (22.90 / 1e6)
        sec_fee_valued_inflated = inflated_values[i] * (22.90 / 1e6)

        if income is None:
            tax_value = calculate_taxes(brackets, rates, future_values[i])
            tax_value_adjusted = calculate_taxes(
                brackets, rates, inflated_values[i])
        else:
            # Calculate the tax based on income
            tax_value = calculate_taxes(brackets, rates, income)
            tax_value_adjusted = calculate_taxes(
                brackets, rates, income)

        # Subtract the SEC fee and tax from the future value
        future_values[i] -= sec_fee_value + tax_value
        inflated_values[i] -= sec_fee_valued_inflated + tax_value_adjusted

    # Future value after inflation
    clean_future_values = np.round(future_values)

    # Future value accounting for inflation
    adjusted_future_values = np.round(inflated_values)

    return {'clean': clean_future_values, 'inflation': adjusted_future_values}
