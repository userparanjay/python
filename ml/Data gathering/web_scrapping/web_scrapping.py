# Import pandas for DataFrame creation and CSV export
import pandas as pd

# Import requests for sending HTTP requests
import requests as req

# Import BeautifulSoup for parsing HTML content
from bs4 import BeautifulSoup as bs


# Headers used to mimic a real browser request
# Some websites block bot requests, so headers help avoid that
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://example.com/",
    "Origin": "https://example.com",
    "Connection": "keep-alive"
}


# Main website home page URL
url = 'https://books.toscrape.com/'


# Send GET request to website
response = req.get(url, headers=headers)

# Print response object
# Example: <Response [200]> means request successful
print(response)


# Parse HTML response content into BeautifulSoup object
soup = bs(response.content, 'html.parser')


# Print full formatted HTML (used for learning / debugging)
print(soup.prettify())


# Find all anchor tags <a> from page
a = soup.find_all('a')


# Loop through all anchor tags
# Print only those tags having title attribute
# These title attributes usually contain full book names
for tag in a:
    if tag.get("title") is not None:
        print("Title:", tag.get("title"))


# Find all price elements on first page
# Example: <p class="price_color">£51.77</p>
products_price = soup.find_all('p', class_='price_color')


# Print all prices from first page
for product_price in products_price:
    print(product_price.text.strip())


# Empty list to store products from all 50 pages
total_products = []


# Loop through all catalogue pages
# BooksToScrape contains 50 pages total
for i in range(1, 51):

    # Create dynamic page URL using f-string
    # Example page-2.html, page-3.html
    page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    # Send request to current page
    response = req.get(page_url, headers=headers)

    # Parse current page HTML
    soup = bs(response.content, 'html.parser')

    # Find all product cards on current page
    # Each book is inside article.product_pod
    products_pod = soup.find_all("article", class_="product_pod")

    # Add all current page products into master list
    total_products.extend(products_pod)


# Print total number of products scraped
# Expected result = 1000 books
print(len(total_products))


# Function to convert stock text into boolean
# 'In stock' -> True
# anything else -> False
def checkStock(text):
    if text == 'In stock':
        return True
    else:
        return False


# Dictionary to store scraped data column-wise
# Example:
# {
#   "title": [],
#   "price": [],
#   "rating": []
# }
data = {}


# Function to insert values into dictionary lists
def makeData(key, val):

    # If key already exists, append new value
    if key in data:
        data[key].append(val)

    # If key does not exist, create new list with first value
    else:
        data[key] = [val]


# Loop through every product card collected from all pages
for prod in total_products:

    # Extract title from title attribute
    makeData('title', prod.h3.a.get('title'))

    # Extract rating
    # Example classes = ['star-rating', 'Three']
    # Index 1 gives actual rating
    makeData('rating', prod.find('p').get('class')[1])

    # Extract price text
    makeData('price', prod.find('p', class_='price_color').text.strip())

    # Extract stock availability text
    stock_text = prod.find('p', class_='instock availability').text.strip()

    # Convert stock text into True / False
    makeData('in stock', checkStock(stock_text))


# Convert dictionary into pandas DataFrame
df = pd.DataFrame(data)


# Save DataFrame into CSV file
# index=False prevents extra serial number column
df.to_csv('output.csv', index=False)


# Print first 5 rows
print(df.head())