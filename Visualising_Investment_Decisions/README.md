# Visualizing Investment Decisions

This project is a tool designed to assist with investment decisions. It's currently under development and offers the following features:

## Features

### Investment Parameters

Users is be able to input the following parameters to tailor the tool to their specific investment scenario:

1. **Investment Amount**: The desired sum to invest.
2. **Investment Start**: The start date of the investment.
3. **Investment End**: The end date of the investment.
4. **Annual Income**: If provided it will be used to calculate taxes, eelse taxes will be calculated assuming the investment value is the income.

### Inflation Calculation

The tool calculates inflation based on a set growth rate of +2% per year. However, there is a ceiling set at 90% of historical inflation rates ( 4.1% inflation ). If the calculated inflation for the current year hits this ceiling, it will be treated as a trigger for government intervention. This means that we assume the government would take measures to control inflation, and therefore, the inflation rate would be halved for the next year to simulate a bounce back to normal inflation rates.

## Current Limitations

The tool currently has the following limitations:

- Intermediary fees are not considered.
- The company-related growth per year approximation is currently set at 20%, which is the average for S&P 100 companies. For more information check [SP100](https://github.com/AmadeusMoon/DataAnalysis/tree/master/SP100), in there you can check the `plots` inside `visualisation` directory and see the mean as shown here:
  <img src="https://github.com/AmadeusMoon/DataAnalysis/blob/master/SP100/Visualisation/Plots/SP100%20-%20Mean%20Revenue%20Growth%20by%20Sector.png" width="66%" height="66%">
- The tax brackets are currently only for the USA.
- The inflation rate is currently only for the USA economy.

## Technologies Used

This project is built using the following technologies:

- BeautifullSoup
- Matplotlib
- Requests
- Python
- Pandas
- Numpy
