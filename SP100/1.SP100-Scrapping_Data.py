from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

# Import data from page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')

# Retrieve table
table = soup.find_all('table')[1]

# Retrieve table headers
headers = table.find_all('th')

# Clean retrieved headers
cleanHeaders = [data.text.strip() for data in headers]

# Define headers as columns
df = pd.DataFrame(columns=cleanHeaders)

# Get the rest of the data
columnData = table.find_all('tr')[1:]
for row in columnData:
    rowData = row.find_all('td')
    # Separate it in individual rows
    individualCleanRows = [data.text.strip() for data in rowData]
    # Increase length of rows in df with each loop iteration
    length = len(df)
    # Populate rows with individual rows
    df.loc[length] = individualCleanRows

# Convert the string data from Revenue to int
df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace(
    ',', '').astype(int)

# Do the same for Employees
df['Employees'] = df['Employees'].str.replace(
    ',', '').astype(int)

# Convert the data from growth to actual percentages
df['Revenue growth'] = df['Revenue growth'].str.replace(
    '%', '').astype(float) / 100

# Clean up the data and match the 2 similar entities
df['Industry'] = df['Industry'].replace('Financials', 'Financial')

# Same for Health and Healthcare
df['Industry'] = df['Industry'].replace('Health', 'Healthcare')

# Archer Daniel Midlands is food processing
df.loc[df['Name'] == 'Archer Daniels Midland', 'Industry'] = 'Food processing'

# Convert all columns to the a nicer more readable format
def custom_format(x):
    if x % 1 == 0:
        return '{:,.0f}'.format(x)
    else:
        return '{:,.2f}'.format(x)


# Convert all columns to the a nicer more readable format
for col in df.select_dtypes(include=[np.number]).columns:
    if col != 'Revenue growth':
        df[col] = df[col].apply(custom_format)

# Export data frame
df.to_csv('SP100.csv', index=False)
