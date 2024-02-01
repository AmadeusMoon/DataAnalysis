import pandas as pd
import matplotlib.pyplot as plt

dfEconomic = pd.read_csv('SP100/Tables/Economy.csv')

# List of columns to convert back to numeric
cols_to_convert = ['Total Revenue (USD millions)', 'Total Employees',
                   'Mean revenue per Company in Industry', 'Mean jobs created per Company by Industry']

for col in cols_to_convert:
    dfEconomic[col] = dfEconomic[col].str.replace(',', '').astype(float)

# Group the number of employees in each sector
totalEmployees = dfEconomic['Total Employees'].sum()
employeesPerSector = dfEconomic.groupby(
    'Sector')['Total Employees'].sum()
percentages = employeesPerSector / totalEmployees * 100

plt.figure(figsize=(10, 6))
patches, texts, autotexts = plt.pie(
    percentages, labels=employeesPerSector.index, autopct='%1.1f%%', pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')

plt.text(0, 0, 'Number of Employees in Each Sector', horizontalalignment='center',
         verticalalignment='center', fontsize=9, color='black')

for text in texts:
    text.set_fontsize(14)
for autotext in autotexts:
    autotext.set_fontsize(14)

# Create legend labels with the sector name and the number of employees
legend_labels = [f'{sector}: {employees:,.0f} employees' for sector,
                 employees in employeesPerSector.items()]

# Add a legend to the left corner of the graph
plt.legend(legend_labels, title="Sectors",
           loc="upper right", bbox_to_anchor=(0.3, 1.16))

plt.savefig('SP100 - Employees by Sector.png')
