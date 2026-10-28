import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("Starting the scraping...")

titles = []
prices = []
ratings = []
availability = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Scrape first 5 pages
for page in range(1, 6):
    print(f"Scraping page {page}...")
    
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        # Title
        title = book.h3.a["title"]
        titles.append(title)
        
        # Price (remove £ and any strange characters)
        price = book.find("p", class_="price_color").text
        price = price.replace("£", "").replace("Â", "").strip()
        prices.append(float(price))
        
        # Rating
        rating = book.p["class"][1]
        ratings.append(rating)
        
        # Availability
        stock = book.find("p", class_="instock availability").text.strip()
        availability.append(stock)
    
    time.sleep(1)  # Be polite to the website

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})

# Convert Rating from words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

# Save the cleaned data
df.to_csv("books_data_cleaned.csv", index=False, encoding="utf-8")

print("\nScraping finished successfully!")
print(f"Total books saved: {len(df)}")
print("\nHere are the first 5 books:")
print(df.head())
print("\nData types:")
print(df.dtypes)
