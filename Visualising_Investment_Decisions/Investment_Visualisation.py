# %%
from Deductions import calculate_future_values_after_tax_and_fee as calculate_values
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


def Visualise_Investment(investment: int, investment_start: str, investment_end: str, income: int = None):

    # Parse date
    start = datetime.strptime(investment_start, "%m-%d-%Y")
    end = datetime.strptime(investment_end, "%m-%d-%Y")

    # Calculate the number of years between the start and end dates
    months = pd.date_range(start=start, end=end, freq='MS')

    # Null check
    if income == None:
        income = 0
    else:
        income = income

    # Get values
    true_returns = calculate_values(
        investment, investment_start, investment_end, income)
    adjusted_returns = calculate_values(
        investment, investment_start, investment_end, income)

    # Access the returns
    clean_returns = true_returns['clean']
    inflated_returns = adjusted_returns['inflation']

    # Create a figure and a set of subplots
    fig, ax = plt.subplots()

    # Plot the investment and benefits over time
    ax.plot(months, clean_returns - investment,
            label='Benefits Accounting for Inflation')
    ax.plot(months, inflated_returns - investment, label='Adjusted Benefits')
    ax.plot(months, [0] * len(months), 'k--', label='Break-even Point')

    # Add labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Benefit')
    ax.set_title('SP100 Investment Benefits over Time')
    ax.set_ylim([0, max(clean_returns)])
    # Adjust x limits to include all dates
    ax.set_xlim([start, end])
    # Add a legend
    ax.legend()

    # Create plot
    plt.savefig('SP100_Investment_Visualisation.png')

    return


# Call function
Visualise_Investment(1000, '1-1-2012', '1-1-2023')
# %%
