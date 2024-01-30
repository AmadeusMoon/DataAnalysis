import pandas as pd

# Import the Economic table
dfEconomic = pd.read_csv('../Tables/Economy.csv')


# Create dataframe to store results
dfEconomic

# Create a new DataFrame with the sectors
dfSectors = dfEconomic.groupby('Sector').agg(
    {'Industry': 'count', }).reset_index()

# Rename columns
dfSectors.columns = ['Sectors', 'Number of Companies']

# Save the DataFrame to a CSV file
dfSectors.to_csv('Sectors.csv', index=False)
