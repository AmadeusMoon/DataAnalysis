import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.ticker as mtick

dfEconomic = pd.read_csv('SP100/Tables/Economy.csv')

# List of columns to convert back to numeric
cols_to_convert = ['Total Revenue (USD millions)', 'Total Employees',
                   'Annual Employee Salary in Industry', 'Mean revenue per Company in Industry', 'Mean jobs created per Company by Industry']

for col in cols_to_convert:
    # Remove commas and convert to float
    dfEconomic[col] = dfEconomic[col].str.replace(',', '').astype(float)

# Retrieve data
employeesBySector = dfEconomic.groupby('Sector')['Total Employees'].sum()
meanSalaryBySector = dfEconomic.groupby('Sector')['Annual Employee Salary in Industry'].sum(
) / dfEconomic.groupby('Sector')['Industry'].count()
companiesBySector = dfEconomic['Sector'].value_counts()
meanSalary = meanSalaryBySector.mean()
# Sort by sector names
meanSalaryBySector = meanSalaryBySector.sort_index()
companiesBySector = companiesBySector.sort_index()
employeesBySector = employeesBySector.sort_index()

plt.figure(figsize=(11, 7))

ax = meanSalaryBySector.plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.axhline(y=meanSalary, color='black', linestyle='--')

plt.title('Mean Employee Annual Salary by Sector')

xlabels = [f'{numCompanies}' for numCompanies in companiesBySector]
ax.set_xticklabels(xlabels)
plt.xlabel('Number of Companies by Sector')

plt.ylabel('Mean Annual Employee Salary')

plt.xticks(rotation=45)

# Format y-axis labels to plain numbers
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sector_labels = [f'{sector}: {salary:,.0f} mean salary' for sector,
                 salary in meanSalaryBySector.items()]
legend_labels = sector_labels + \
    [f'Mean salary SP100 Companies: {meanSalary:,.0f}']

# Create legend
handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=8) for c in [
    'skyblue', 'orange', 'green']] + [Line2D([0], [0], color='black', linestyle='--')]

# Add number of employees inside bars
for i, sector in enumerate(meanSalaryBySector.index):
    numEmployees = employeesBySector[sector]
    # Adjust the vertical position of the text based on the mean salary
    va = 'top' if meanSalaryBySector[sector] > meanSalary else 'top'
    plt.text(i, meanSalaryBySector[sector], f'Employees: {numEmployees:,.0f}',
             ha='center', va=va, color='black')

plt.legend(handles, legend_labels, title="Mean Salary by Sector",
           loc="upper right", bbox_to_anchor=(0.24, 1.3))

plt.savefig('SP100 - Mean Salary by Sector.png', bbox_inches='tight')
