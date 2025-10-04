import requests
from bs4 import BeautifulSoup
import csv

def rating_to_stars(rating):
    mapping = {
        "One": "⭐",
        "Two": "⭐⭐",
        "Three": "⭐⭐⭐",
        "Four": "⭐⭐⭐⭐",
        "Five": "⭐⭐⭐⭐⭐"
    }
    return mapping.get(rating, rating)

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
products = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"   

    if response.status_code != 200:
        print(f"⚠️ Page {page} not found, stopping...")
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.find_all('article', class_='product_pod'):
        name = item.h3.a['title']

       
        price_text = item.find('p', class_='price_color').text.strip()

        rating_tag = item.find('p', class_='star-rating')
        rating = rating_tag['class'][1] if rating_tag else "No Rating"
        rating_stars = rating_to_stars(rating)

        products.append({'Name': name, 'Price (£)': price_text, 'Rating': rating_stars})
    print(f"✅ Scraped page {page}")

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Price (£)', 'Rating'])
    writer.writeheader()
    writer.writerows(products)

print(f"🎉 Scraped {len(products)} books into books.csv")
