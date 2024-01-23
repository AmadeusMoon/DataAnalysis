# %%
from Deductions import calculate_future_values_after_tax_and_fee
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

# Your investment amount
investment = 1000

# Define the interval for the profit checkpoints
interval = 500  # Add a dot every $500 of profit

# Number of years for the investment
years = np.arange(2024, 2051)

# Calculate future values after tax and fee for a given income and investment type for each year
future_values_short_term = calculate_future_values_after_tax_and_fee(
    120000, 'short_term', years - 2024, investment)
future_values_long_term = calculate_future_values_after_tax_and_fee(
    120000, 'long_term', years - 2024, investment)

# Convert future values to represent benefit for each year
benefit_short_term = (future_values_short_term['fvataf'] - investment)
benefit_long_term = (future_values_long_term['fvataf'] - investment)

# Calculate future values after tax and fee with depreciation for short term and long term investments
benefit_short_term_depreciation = (
    future_values_short_term['fvad'] - investment)
benefit_long_term_depreciation = (future_values_long_term['fvad'] - investment)

# Create a DataFrame with 'Years', 'Benefit Short Term', 'Benefit Long Term', 'Benefit Short Term Depreciation' and 'Benefit Long Term Depreciation' columns
df = pd.DataFrame({
    'Years': years,
    'Benefit Short Term': benefit_short_term,
    'Benefit Long Term': benefit_long_term,
    'Benefit Short Term Depreciation': benefit_short_term_depreciation,
    'Benefit Long Term Depreciation': benefit_long_term_depreciation
})

plt.figure(figsize=(15, 6))
plt.plot(df['Years'], df['Benefit Short Term'],
         color='lightgreen', label='Short Term Benefit')
plt.plot(df['Years'], df['Benefit Long Term'],
         color='lightblue', label='Long Term Benefit')
plt.plot(df['Years'], df['Benefit Short Term Depreciation'],
         color='green', linestyle='-', label='Short Term Benefit Depreciation')
plt.plot(df['Years'], df['Benefit Long Term Depreciation'],
         color='blue', linestyle='-', label='Long Term Benefit Depreciation')

# Add breaking points every five years for short term
plt.vlines(years[::5], 0, 1, transform=plt.gca(
).get_xaxis_transform(), colors='green', linestyles='--')

# Add a line starting at 5 years for long term
plt.axvline(x=2029, color='blue', linestyle=':')

# Create a legend for the dots and lines
lightgreen_line = mlines.Line2D([], [], color='lightgreen',
                                linestyle='-', label='Short Term Benefit')
lightblue_line = mlines.Line2D([], [], color='lightblue',
                               linestyle='-', label='Long Term Benefit')
green_line = mlines.Line2D(
    [], [], color='green', linestyle='-', label='Short Term Benefit After Depreciation')
blue_line = mlines.Line2D(
    [], [], color='blue', linestyle='-', label='Long Term Benefit After Depreciation')
green_dash = mlines.Line2D([], [], color='green', marker='_',
                           linestyle=':', label='Maximum Time Until Withdrawal (Short Term)')
blue_dash = mlines.Line2D([], [], color='blue', marker='_',
                          linestyle=':', label='Minimum Time Until Withdrawal (Long Term)')
break_even_line = mlines.Line2D(
    [], [], color='black', linestyle='--', label='Break-Even Point')

# Add the legends for the lines, dots, and break-even point to the plot
plt.legend(handles=[lightgreen_line, lightblue_line, green_line, blue_line,
           green_dash, blue_dash, break_even_line])

plt.xlim(min(years), max(years))  # Set the x-axis range
plt.ylim(-investment, max(max(benefit_short_term),
         max(benefit_long_term)))  # Set the y-axis range

# Add a horizontal line representing the break-even point
plt.axhline(y=0, color='black', linestyle='--')

# Set the y-ticks to include only the negative investment
plt.yticks([-investment] + [tick for tick in plt.yticks()[0] if tick >= 0])

plt.title('Years vs Benefit')
plt.xlabel('Years')
plt.ylabel('Benefit ($)')
plt.grid(True)
plt.show()
# %%
