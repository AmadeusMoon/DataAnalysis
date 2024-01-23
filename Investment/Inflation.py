import numpy as np


def calculate_inflation_adjusted_value(present_value):
    # Define the years and inflation rates
    years = np.array([1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940,
                      1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952,
                      1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964,
                      1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976,
                      1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988,
                      1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
                      2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                      2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
    inflation_rates = np.array([0.006, -0.064, -0.093, -0.103, 0.008, 0.015,
                                0.03, 0.014, 0.029, -0.028, 0.00, 0.007, 0.099,
                                0.09, 0.03, 0.023, 0.022, 0.181, 0.088, 0.03, -0.021, 0.059, 0.06,
                                0.008, 0.007, -0.007, 0.004, 0.03, 0.029, 0.018, 0.017, 0.014, 0.007,
                                0.013, 0.016, 0.01, 0.019, 0.035, 0.03, 0.047, 0.062, 0.056, 0.033,
                                0.034, 0.087, 0.123, 0.069, 0.049, 0.067, 0.09, 0.133, 0.125, 0.089,
                                0.038, 0.038, 0.039, 0.038, 0.011, 0.044, 0.044, 0.046, 0.061, 0.031,
                                0.029, 0.027, 0.027, 0.025, 0.033, 0.017, 0.016, 0.027, 0.034, 0.016,
                                0.024, 0.019, 0.033, 0.034, 0.025, 0.041, 0.001, 0.027, 0.015, 0.03,
                                0.017, 0.015, 0.008, 0.007, 0.021, 0.021, 0.019, 0.023, 0.014, 0.07,
                                0.065, 0.034
                                ])

    # Define the ceiling for the inflation rate
    ceiling = np.percentile(inflation_rates, 83)

    # Add 2% inflation for each year after 2024
    additional_years = np.arange(2025, 2050)
    additional_inflation_rates = np.full(len(additional_years), 0.02)

    # Halve the inflation rate if it reaches the ceiling
    for i in range(len(additional_inflation_rates)):
        if additional_inflation_rates[i] > ceiling:
            additional_inflation_rates[i] /= 2

    years = np.concatenate((years, additional_years))
    inflation_rates = np.concatenate(
        (inflation_rates, additional_inflation_rates))

    # Calculate the adjusted dollar values
    adjusted_values = np.cumprod(1 + inflation_rates)

    # Calculate the depreciation due to inflation
    depreciation = present_value * np.mean(inflation_rates)

    # Calculate the future value of the investment after accounting for the average annual growth of the S&P 500
    future_value = (present_value - depreciation)

    return future_value
