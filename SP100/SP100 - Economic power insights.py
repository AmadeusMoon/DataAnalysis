import pandas as pd
import numpy as np

# Use the previously created file from scrapped data
df = pd.read_csv('SP100/Tables/SP100.csv')

# Convert columns back to numeric
cols_to_convert = ['Revenue (USD millions)', 'Employees']

for col in cols_to_convert:
    df[col] = df[col].str.replace(',', '').astype(float)

# Ammount of revenue that goes to salaries
percentages = {
    'Retail and cloud computing': 0.42,
    'Healthcare': 0.06,
    'Technology and cloud computing': 0.180,
    'Retail': 0.09,
    'Financial services': 0.18,
    'Health insurance': 0.033,
    'Telecommunications': 0.12,
    'Financial': 0.08,
    'Media': 0.11,
    'Logistics': 0.9,
    'Technology': 0.083,
    'Food service': 0.036,
    'Infotech': 0.05,
    'Insurance': 0.076,
    'Conglomerate': 0.23,
    'Automotive and energy': 0.1,
    'Transportation': 0.30,
    'Airline': 0.29,
    'Food industry': 0.02,
    'Conglomerate and telecomunications': 0.14,
    'Aerospace and defense': 0.20,
    'Agriculture cooperative': 0.015,
    'Agriculture manufacturing': 0.10,
    "Apparel": 0.12,
    'Automotive industry': 0.07,
    'Beverage': 0.30,
    'Chemical industry': 0.092,
    'Consumer products manufacturing': 0.08,
    'Electronics industry': 0.10,
    'Food processing': 0.05,
    'Laboratory instruments': 0.20,
    'Machinery': 0.20,
    'Petroleum industry': 0.015,
    'Petroleum industry and logistics': 0.01,
    'Pharmaceutical industry': 0.08,
    'Telecom hardware manufacturing': 0.20,
}

# Create new dataframe
newDf = df.groupby('Industry').agg(
    {'Revenue (USD millions)': 'sum', 'Employees': 'sum', 'Revenue growth': 'mean', 'Name': 'count'}).reset_index()

# Rename output columns
newDf.columns = ['Industry', 'Total Revenue (USD millions)',
                 'Total Employees', 'Mean Revenue Growth', 'Company Count']

# Mean revenue per company in each industry
newDf['Mean revenue per Company in industry'] = newDf[
    'Total Revenue (USD millions)'] / newDf['Company Count']

# Mean ammount of jobs created per company in industry
newDf['Mean jobs created per Company by industry'] = newDf[
    'Total Employees'] / newDf['Company Count']

# Service sector
servicesSector = ['Retail and cloud computing', 'Healthcare', 'Technology and cloud computing', 'Retail', 'Financial services', 'Health insurance', 'Telecommunications',
                  'Financial', 'Media', 'Logistics', 'Technology', 'Food service', 'Infotech', 'Insurance', 'Conglomerate', 'Automotive and energy', 'Transportation', 'Airline', 'Food industry', 'Conglomerate and telecomunications']
# Prime mater
primarySector = ['Petroleum industry', 'Beverage',
                 'Petroleum industry and logistics', 'Automotive and energy', 'Conglomerate']
# Industrial sector
manufacturingSector = ['Electronics industry', 'Automotive industry', 'Conglomerate', 'Pharmaceutical industry', 'Consumer products manufacturing', 'Aerospace and defense', 'Machinery',
                       'Chemical industry', 'Agriculture manufacturing', 'Telecom hardware manufacturing', 'Food processing', 'Agriculture cooperative', 'Apparel', 'Laboratory instruments', 'Automotive and energy']

# Create function to check industry
def assignCategory(industry):
    if industry in servicesSector:
        return 'Services Sector'
    elif industry in primarySector:
        return 'Primary Sector'
    elif industry in manufacturingSector:
        return 'Manufacturing Sector'
    else:
        return industry


# Substitute Industry with Sector
newDf['Sector'] = newDf['Industry'].apply(assignCategory)

# Define the column order
column_order = ['Sector', 'Industry', 'Total Revenue (USD millions)', 'Total Employees', 'Mean Revenue Growth',
                'Company Count', 'Annual Employee Salary', 'Mean revenue per Company in industry', 'Mean jobs created per Company by industry']

# Add a salary per employee yearly depending on industry
newDf['Annual Employee Salary'] = newDf.apply(lambda row: (
    row['Total Revenue (USD millions)'] * 1000000 * percentages[row['Industry']]) / row['Total Employees'], axis=1)

# Reindex the DataFrame
newDf = newDf.reindex(columns=column_order)

# Convert all columns to the a nicer more readeable format
for col in newDf.select_dtypes(include=[np.number]).columns:
    if col != 'Revenue growth':
        newDf[col] = newDf[col].map('{:,.2f}'.format)

# Export data as file
newDf.to_csv('Economy.csv', index=False)
