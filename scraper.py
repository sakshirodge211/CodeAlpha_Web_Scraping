import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"
url = base_url

data = []

while url:
    print("Scraping:", url)

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text.strip()

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        product_link = book.h3.a["href"]
        product_url = urljoin(url, product_link)

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })

    # Find next page
    next_button = soup.find("li", class_="next")

    if next_button:
        next_link = next_button.a["href"]
        url = urljoin(url, next_link)
    else:
        url = None

# Create DataFrame
df = pd.DataFrame(data)

# Fix price encoding issue
df["Price"] = df["Price"].str.replace("Â£", "£", regex=False)

# Save CSV
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print("\nScraping completed successfully!")
print("Total books collected:", len(df))
print("CSV file created: books_data.csv")

print("\nFirst 5 records:")
print(df.head())