from Inflation import calculate_inflation_adjusted_value
import numpy as np

# 10% anual growth
average_anual_growth_SP500 = 0.10

# Short-Term Capital Gains Tax
short_term_brackets = np.array([11600, 47150, 100525, 191950, 243725, 609350])
short_term_rates = np.array([0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])

# Long-Term Capital Gains Tax
long_term_brackets = np.array([44625, 492300, 50000])
long_term_rates = np.array([0.00, 0.15, 0.20])

# Calculate tax based on income


def calculate_tax(income, brackets, rates):
    tax = 0
    remaining_income = income

    for i in range(len(brackets)):
        if remaining_income <= brackets[i]:
            tax += remaining_income * rates[i]
            break
        else:
            tax += brackets[i] * rates[i]
            remaining_income -= brackets[i]

    return tax

# Calculate value of investments after taxes


def calculate_future_values_after_tax_and_fee(income, investment_type, years, investment):
    # Choose the correct tax brackets and rates based on the investment type
    if investment_type == 'short_term':
        brackets = short_term_brackets
        rates = short_term_rates
    elif investment_type == 'long_term':
        brackets = long_term_brackets
        rates = long_term_rates
    else:
        print("Invalid investment type. Please choose 'short_term' or 'long_term'.")
        return

    # Calculate the future value of the investment after accounting for inflation and average annual growth
    future_value = investment * (1 + average_anual_growth_SP500)**years

    # Calculate the SEC fee
    sec_fee_value = future_value * (22.90 / 1e6)  # $22.90 per $1 million

    # Calculate the tax
    tax_value = np.array([calculate_tax(fv, brackets, rates)
                         for fv in future_value])

    # Subtract the SEC fee and tax from the future value
    future_value_after_tax_and_fee = future_value - sec_fee_value - tax_value

    # Future value after depreciation
    future_value_after_depreciation = calculate_inflation_adjusted_value(
        future_value_after_tax_and_fee)

    return {'fvataf': future_value_after_tax_and_fee, 'fvad': future_value_after_depreciation}
