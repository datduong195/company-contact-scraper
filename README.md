# Description:
Scraper script in Python 3 that read input from an excel file "input.xlsx" and do a Wiki search for each item. Then with the summary section of each item, do a quick regular expression string matching with a list of keyword and write all of those queries back to excel file "output.xlsx"

# Requirement:
1. Pandas:
> pip3 install pandas
2. Wikipedia API:
> pip3 install wikipedia