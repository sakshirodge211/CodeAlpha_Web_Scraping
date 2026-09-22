# CodeAlpha Task 1 - Web Scraping

## Project Overview

This project is completed as part of the CodeAlpha Data Analytics Internship.

The objective of this task is to collect book-related data from a public website using Python web scraping techniques.

## Website Used

Books to Scrape  
https://books.toscrape.com/

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected

The scraper collects the following information:

- Title
- Price
- Rating
- Availability
- Product URL

## Methodology

1. Send HTTP requests to the website using Requests.
2. Parse HTML content using BeautifulSoup.
3. Extract book details from each product page.
4. Navigate through multiple pages automatically.
5. Store the collected data in a Pandas DataFrame.
6. Export the final dataset to `books_data.csv`.

## Dataset

A total of **1,000 books** were collected from the Books to Scrape website.

The final dataset is stored in:

`books_data.csv`

## Project Files

- `scraper.py` - Python web scraping script
- `books_data.csv` - Scraped dataset
- `README.md` - Project documentation

## Result

The web scraping process successfully collected 1,000 book records with details such as title, price, rating, availability, and product URL.

## Internship

**Program:** CodeAlpha Data Analytics Internship  
**Task:** Task 1 - Web Scraping  
**Intern:** Sakshi Rodge
