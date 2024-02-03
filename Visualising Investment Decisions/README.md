# Visualizing Investment Decisions

This project is a tool designed to assist with investment decisions. It's currently under development and will offer the following features:

## Features

### Investment Parameters

Users will be able to input the following parameters to tailor the tool to their specific investment scenario:

1. **Investment Duration**: The exact duration of the investment.
2. **Investment Amount**: The desired sum to invest.
3. **Annual Income**: Required for calculating the benefits of short-term investments, which are based on the user's income tax bracket.

### Inflation Calculation

The tool calculates inflation based on a set growth rate of +2% per year. However, there is a ceiling set at 83% of historical inflation rates. If the calculated inflation for the current year hits this ceiling, it will be treated as a trigger for government intervention. This means that we assume the government would take measures to control inflation, and therefore, the inflation rate would be halved for the next year to simulate a bounce back to normal inflation rates.

## Current Limitations

The tool currently has the following limitations:

- Intermediary fees are not considered.
- The company-related growth per year approximation is currently set at 20%, which is the average for S&P 100 companies. For more information check [SP100]("https://github.com/AmadeusMoon/DataAnalysis/tree/master/SP100") .
- The tax brackets are currently only for the USA.
- The inflation rate is currently only for the USA economy.

## Technologies Used

This project is built using the following technologies:

- Matplotlib
- Python
- Pandas
- Numpy

## Future Work

I am actively working on addressing the current limitations to make this tool more versatile and accurate. Feel free to drop by any feedback or suggestions. # %%
