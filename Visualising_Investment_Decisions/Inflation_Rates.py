from bs4 import BeautifulSoup
import pandas as pd
import requests

# Retrieve data for inflation rates
url = 'https://www.usinflationcalculator.com/inflation/current-inflation-rates/'
page = requests.get(url)
data = BeautifulSoup(page.text, features='html.parser')

# Retrieve all tables
tables = data.find_all('table')

# Single out the table we need
table = tables[0]

# Retrieve table headers
headers = table.find_all('tr')[0]

# Clean retrieved headers
cleanHeaders = headers.text.strip()

# Create a list
cleanHeaders = cleanHeaders.split()

# Retrieve the rows
rows = table.find_all('tr')[2:]
data = []

# Populate the array with the td data
for row in rows:
    tds = row.find_all('td')
    row_data = [td.text.strip() for td in tds]
    data.append(row_data)

# Create a DataFrame with the data
df = pd.DataFrame(data, columns=cleanHeaders)

# Rename the last column to be more descriptive
df.rename(columns={'Ave': 'Mean Inflation'}, inplace=True)

# Ensure that your 'Year' column is of type int or float
df['Year'] = df['Year'].astype(int)

# Sort the DataFrame by 'Year' in ascending order
df = df.sort_values('Year')

# Export file to csv table
df.to_csv('US_Inflation_Rates.csv', index=False)
