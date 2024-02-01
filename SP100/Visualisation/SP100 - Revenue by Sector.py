import pandas as pd
import matplotlib.pyplot as plt

dfEconomic = pd.read_csv('SP100/Tables/Economy.csv')

# List of columns to convert back to numeric
cols_to_convert = ['Total Revenue (USD millions)', 'Total Employees',
                   'Mean revenue per Company in industry', 'Mean jobs created per Company by industry']

for col in cols_to_convert:
    dfEconomic[col] = dfEconomic[col].str.replace(',', '').astype(float)

# Group the revenue in each sector
totalRevenue = dfEconomic['Total Revenue (USD millions)'].sum()
revenuePerSector = dfEconomic.groupby(
    'Sector')['Total Revenue (USD millions)'].sum()
percentages = revenuePerSector / totalRevenue * 100

plt.figure(figsize=(10, 6))
patches, texts, autotexts = plt.pie(
    percentages, labels=revenuePerSector.index, autopct='%1.1f%%', pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')

plt.text(0, 0, 'Revenue per Sector', horizontalalignment='center',
         verticalalignment='center', fontsize=9, color='black')

for text in texts:
    text.set_fontsize(14)
for autotext in autotexts:
    autotext.set_fontsize(14)

legend_labels = [f'{sector}: {revenue:,.0f} revenue' for sector,
                 revenue in revenuePerSector.items()]

plt.legend(legend_labels, title='Total revenue in USD millions',
           loc="upper right", bbox_to_anchor=(0.28, 1.16))

plt.savefig('SP100 - Revenue by Sector.png')
