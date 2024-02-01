import pandas as pd
import matplotlib.pyplot as plt

# Import the Economy csv file
dfSectors = pd.read_csv('SP100/Tables/Economy.csv')

# List of columns to convert back to numeric
cols_to_convert = ['Total Revenue (USD millions)', 'Total Employees',
                   'Mean revenue per Company in Industry', 'Mean jobs created per Company by Industry']

for col in cols_to_convert:
    dfSectors[col] = dfSectors[col].str.replace(',', '').astype(float)

# Group the companies in sectors and sum their total number per sector
companies = dfSectors.groupby('Sector')['Company Count'].sum()

# Define size
plt.figure(figsize=(10, 6))

# Create a pie chart with companies data substracted from df
patches, texts, autotexts = plt.pie(
    companies, labels=companies.index, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add the title in the center of the chart
plt.text(0, 0, 'Number of Companies in Each Sector', horizontalalignment='center',
         verticalalignment='center', fontsize=9, color='black')

# Increase the font size of the labels
for text in texts:
    text.set_fontsize(14)
for autotext in autotexts:
    autotext.set_fontsize(14)

legend_labels = [f'{sector}: {companies:.0f} companies' for sector,
                 companies in companies.items()]

plt.legend(legend_labels, title="Sectors",
           loc="upper right", bbox_to_anchor=(0.24, 1.16))

# Save the figure to a file
plt.savefig('SP100 - Companies by Sector.png')
