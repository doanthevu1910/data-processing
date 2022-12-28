# Name:
# Student number:
"""
Scrape top movies from www.imdb.com between start_year and end_year (e.g., 1930 and 2020)
Continues scraping until at least a top 5 for each year can be created.
Saves results to a CSV file
"""

from helpers import simple_get
from bs4 import BeautifulSoup
import re
import pandas as pd
from math import ceil
import argparse

IMDB_URL = 'https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced'

def main(output_file_name, start_year, end_year):
    # Load website with BeautifulSoup
    html = simple_get(IMDB_URL)
    dom = BeautifulSoup(html, 'html.parser')

    # Extract movies from website
    movies_df = extract_movies(dom)

    # Save results to output file
    movies_df.to_csv(output_file_name, index=False)

def extract_movies(dom):
    # Print title dom.
    # (This is just an example for using BeautifulSoup. SHOULD BE REMOVED.)
    main_html = dom.find("div", {"id": "main"})
    header = dom.find("h1", {"class": "header"})
    print(header.get_text())

    # Return some nonsense dataframe
    # (This is just an example. SHOULD BE REPLACED.)
    df = pd.DataFrame([["nonsense-value1", "nonsense-value2"]], columns = ["nonsense-column-name1", "nonsense-column-name2"])
    return df

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "extract top N movies from IMDB")

    # Adding arguments
    parser.add_argument("output", help = "output file (csv)")
    parser.add_argument("-s", "--start_year", type=int, default = 1930, help="starting year (default: 1930)")
    parser.add_argument("-e", "--end_year",   type=int, default = 2020, help="ending year (default: 2020)")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.output, args.start_year, args.end_year)
