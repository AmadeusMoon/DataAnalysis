import pandas as pd
import matplotlib.pyplot as plt

# Import the Economy csv file
dfSectors = pd.read_csv('./Tables/Economy.csv')
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

# Save the figure to a file
plt.savefig('SP100 - Companies by Sector.png')
