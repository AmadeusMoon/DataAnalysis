# SP100 Data Analysis Project

This project uses Python libraries, specifically `BeautifulSoup` and `requests`, to extract and `pandas` and `numpy` to analyze data about SP100 companies from the Wikipedia page for the year 2023, the data is then visualised into plots using `mattplotlib`.

## Project Structure

The project is structured as follows:

- `SP100`: This is the main directory containing all the files.
- `Tables`: This directory contains the csv files obtained from data scrapping and processing.
- `Visualisation`: This directory contains the scripts ran to create the plots.
- `Plots`: This directory contains the generated plots.

## How it Works

1. **Data Extraction**: The script starts by extracting data about SP100 companies from the Wikipedia page for 2023. This data is saved as a CSV file in the `Tables` directory.

2. **Data Processing**: The script then reads the extracted data and performs various calculations. The results of these calculations are saved as a secondary CSV file in the `Tables` directory.

3. **Data Visualization**: Finally, the script uses `matplotlib` to generate plots from the calculated data. These plots are saved in the `Plots` directory.

## Requirements

- Python
- Pandas
- Mattplotlib
