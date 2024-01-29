from bs4 import BeautifulSoup
import pandas as pd
import requests

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
# Export data frame
df.to_csv('SP100.csv', index=False)
