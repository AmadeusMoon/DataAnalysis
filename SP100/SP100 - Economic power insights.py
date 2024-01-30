import pandas as pd

# Use the previously created file from scrapped data
df = pd.read_csv('./Tables/SP100.csv')

# Create new dataframe
newDf = df.groupby('Industry').agg(
    {'Revenue (USD millions)': 'sum', 'Employees': 'sum', 'Revenue growth': 'mean', 'Name': 'count'}).reset_index()

# Rename output columns
newDf.columns = ['Industry', 'Total Revenue (USD millions)',
                 'Total Employees', 'Mean Revenue Growth', 'Company Count']

# Add a salary per employee yearly
newDf['Annual Employee Salary'] = (newDf['Total Revenue (USD millions)'] * 1000000) / \
    newDf['Total Employees']

# Mean revenue per company in each industry
newDf['Mean revenue in industry'] = newDf[
    'Total Revenue (USD millions)'] / newDf['Company Count']

# Mean ammount of jobs created
newDf['Mean jobs created by industry'] = newDf[
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
                'Company Count', 'Annual Employee Salary', 'Mean revenue in industry', 'Mean jobs created by industry']

# Reindex the DataFrame
newDf = newDf.reindex(columns=column_order)

# Export data as file
newDf.to_csv('Economy.csv', float_format='%.2f', index=False)
