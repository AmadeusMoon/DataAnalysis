from Deductions import calculate_future_values_after_tax_and_fee as calculate_values
import matplotlib.ticker as ticker
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from dateutil import parser
import pandas as pd
import numpy as np

def Visualise_Investment(investment: int, investment_start: str, investment_end: str = None):

    # Parse the investment dates
    try:
        investment_start_date = parser.parse(investment_start)
        investment_end_date = parser.parse(investment_end)
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
    except ValueError:
        print("Invalid date format. 'Month-Day-Year'.")

    # Create an array of years
    years = np.arange(investment_start_year, investment_end_year + 1)

    # Calculate future values after tax and fee for a given income and investment type for each year
    future_values = calculate_values(
        investment, investment_start, investment_end)

    # Extract future values
    future_values_clean = future_values['clean']
    future_values_inflated = future_values['inflation']

    # Convert future values to represent benefit for each year
    clean_benefit = future_values_clean - investment
    inflated_benefit = future_values_inflated - investment
    print(clean_benefit)
    print(inflated_benefit)
    # Calculate the number of months
    num_months = len(clean_benefit)

    # Create an array of months
    months = np.arange(num_months)

    # Create a DataFrame with 'Years', 'Clean Benefit' and 'Inflated Benefit' columns
    df = pd.DataFrame({
        'Years': investment_start_year + months / 12,
        'Clean Benefit': clean_benefit,
        'Inflated Benefit': inflated_benefit
    })

    plt.figure(figsize=(15, 6))
    plt.plot(df['Years'], df['Clean Benefit'],
             color='lightgreen', label='Clean Benefit')
    plt.plot(df['Years'], df['Inflated Benefit'],
             color='lightblue', label='Inflated Benefit')

    # Add breaking points every five years for short term
    plt.vlines(years[::5], 0, 1, transform=plt.gca(
    ).get_xaxis_transform(), colors='green', linestyles='--')

    # Add a line starting at 5 years for long term
    plt.axvline(x=2029, color='blue', linestyle=':')

    # Create a legend for the dots and lines
    lightgreen_line = mlines.Line2D([], [], color='lightgreen',
                                    linestyle='-', label='Clean Benefit')
    lightblue_line = mlines.Line2D([], [], color='lightblue',
                                   linestyle='-', label='Inflated Benefit')
    break_even_line = mlines.Line2D(
        [], [], color='black', linestyle='--', label='Break-Even Point')

    # Add the legends for the lines, dots, and break-even point to the plot
    plt.legend(handles=[lightgreen_line, lightblue_line, break_even_line])

    plt.xlim(min(years), max(years))  # Set the x-axis range
    plt.ylim(-investment, max(max(clean_benefit),
                              max(inflated_benefit)))  # Set the y-axis range

    # Add a horizontal line representing the break-even point
    plt.axhline(y=0, color='black', linestyle='--')

    # Set the y-ticks to include only the negative investment
    plt.yticks([-investment] + [tick for tick in plt.yticks()[0] if tick >= 0])
    # Format y-axis to display full numbers
    formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x))
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.title('Clean and Inflated Benefit')
    plt.ylabel('Benefit ($)')
    plt.xlabel('Years')
    plt.grid(True)
    plt.savefig('Investment_Visualisation.png', bbox_inches='tight')

    return


# Call function
Visualise_Investment(1000, '1-1-2012', '1-1-2023')
