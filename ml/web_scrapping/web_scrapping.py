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


# Target website URL
url = 'https://books.toscrape.com/'


# Send GET request to website
response = req.get(url, headers=headers)

# Print response status
# Example: <Response [200]> means success
print(response)


# Parse HTML response content
soup = bs(response.content, 'html.parser')


# Print full formatted HTML (for debugging / inspection)
print(soup.prettify())


# Find all anchor tags <a>
a = soup.find_all('a')


# Loop through all anchor tags
# Print only those tags having title attribute
for tag in a:
    if tag.get("title") is not None:
        print("Title:", tag.get("title"))


# Find all price elements
# Example: <p class="price_color">£51.77</p>
products_price = soup.find_all('p', class_='price_color')


# Print all product prices
for product_price in products_price:
    print(product_price.text.strip())


# Find all product containers
# Each book card is inside article.product_pod
products_pod = soup.find_all("article", class_="product_pod")


# Print total products on page
len(products_pod)


# Function to convert stock text into boolean
def checkStock(text):
    if text == 'In stock':
        return True
    else:
        return False


# Dictionary to store scraped data column-wise
data = {}


# Function to insert values into dictionary lists
def makeData(key, val):

    # If key already exists, append new value
    if key in data:
        data[key].append(val)

    # If key does not exist, create empty list first
    else:
        data[key] = [val]


# Loop through every product card
for prod in products_pod:

    # Extract title from title attribute
    makeData('title', prod.h3.a.get('title'))

    # Extract rating
    # Example classes = ['star-rating', 'Three']
    makeData('rating', prod.find('p').get('class')[1])

    # Extract price
    makeData('price', prod.find('p', class_='price_color').text)

    # Extract stock availability
    stock_text = prod.find('p', class_='instock availability').text.strip()
    makeData('in stock', checkStock(stock_text))


# Convert dictionary into DataFrame
df = pd.DataFrame(data)


# Save DataFrame into CSV file
df.to_csv('output.csv', index=False)