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
def calculate_future_values_after_tax_and_fee(investment: int, investment_start: str, investment_end: str = None):

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
    values_adjusted = calculate_adjusted_values(
        investment_start, investment_end)

    # Calculate the future value of the investment after accounting for inflation and average annual growth
    future_value = values_clean * (1 + average_anual_growth_SP100)**years
    inflated_values = values_adjusted * (1 + average_anual_growth_SP100)**years

    # Calculate the SEC fee $22.90 per $1 million
    sec_fee_value = future_value * (22.90 / 1e6)
    sec_fee_valued_inflated = values_adjusted * (22.90 / 1e6)

    # Calculate the tax
    tax_value = np.array([calculate_taxes(brackets, rates, fv)
                         for fv in future_value])
    tax_value_adjusted = np.array(
        [calculate_taxes(brackets, rates, fv) for fv in inflated_values])

    # Subtract the SEC fee and tax from the future value
    future_values_after_tax_and_fee = future_value - sec_fee_value - tax_value
    adjusted_values_after_tax_and_fee = inflated_values - \
        sec_fee_valued_inflated - tax_value_adjusted

    # Future value after inflation
    clean_future_values = np.round(future_values_after_tax_and_fee)

    # Future value accounting for inflation
    adjusted_future_values = np.round(adjusted_values_after_tax_and_fee)

    return {'clean': clean_future_values, 'inflation': adjusted_future_values}
