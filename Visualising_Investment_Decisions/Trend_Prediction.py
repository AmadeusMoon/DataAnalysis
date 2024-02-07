from Inflation_Calculator import get_inflation

# Return the trend for the data input by user
def get_trend(investment_start: str, investment_end: str = None):

    # Create trend variable
    trend = ''

    # Get the data values in the period specified by user
    monthly_inflation = get_inflation(investment_start, investment_end)

    # Retrieve the last 3 months of the data set for inflations
    trend_check = monthly_inflation[-3:]

    # Check for trends
    if trend_check[0] < trend_check[1] < trend_check[2]:
        trend = 'inflation'
    elif trend_check[0] > trend_check[1] > trend_check[2]:
        trend = 'deflation'
    else:
        trend = ''

    return trend
