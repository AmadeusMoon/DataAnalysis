from dateutil import parser
import pandas as pd
import numpy as np

# Import tables
inflation_rates_file = '/home/amadeusmoon/Projects/DataAnalysis/Visualising_Investment_Decisions/Tables/US_Inflation_Rates.csv'
inflation_rates = pd.read_csv(inflation_rates_file)

# Return inflation rate for user specified data until most recent
def get_inflation(investment_start: str, investment_end: str):
    # Test the input
    try:
        # Parse the user input and retrieve it
        start_date = parser.parse(investment_start)
        start_month = start_date.month
        start_year = start_date.year
        # Parse the investment end time if provided
        if investment_end:
            end_date = parser.parse(investment_end)
            end_month = end_date.month
            end_year = end_date.year
            if end_month < 1 or end_month > 12:
                raise ValueError("Please choose a proper end_month.")
            if end_year < 2000:
                raise ValueError("Year_end must be after 2000.")
            if end_year < start_year:
                raise ValueError(
                    "Investment end year cannot be before investment start year.")
            if end_year == start_year & end_month <= start_month:
                raise ValueError(
                    'Investment end month cannot happen before investment start month.')
            # Set investment end to 2023 if it surpasses
            if end_year > 2023:
                investment_end = 2023
        # If investment end is not given then set values to be last in table
        else:
            end_month = 12
            end_year = inflation_rates['Year'].max()
        # Define stricter start_date input and raise error if input is invalid
        if start_month < 1 or start_month > 12:
            raise ValueError("Please choose a proper start_month.")
        if start_year < 2000 or start_year > 2023:
            raise ValueError("Year must be between 2000 and 2023.")
    # Catch any other input errors
    except ValueError:
        print("Invalid start_date format. Please try again.")

    # Create array to hold values
    monthly_inflation = np.array([])

    # Access inflation based on user data and retrieve from input till the end of data frame
    for year in range(start_year, end_year + 1):
        # Set the index of the year we are looping through to the respective column value
        data_year = inflation_rates[inflation_rates['Year'] == year]
        if year == start_year:
            loop_start_month = start_month
        else:
            loop_start_month = 1
        # If we reach the end year set the last month to be the one from input else last
        if year == end_year:
            loop_end_month = end_month
        else:
            loop_end_month = 12
        # Retrieve the months in range
        for month in range(loop_start_month, loop_end_month + 1):
            month_data = data_year.iloc[0, month]
            monthly_inflation = np.append(monthly_inflation, month_data)

    # Return array
    return monthly_inflation
