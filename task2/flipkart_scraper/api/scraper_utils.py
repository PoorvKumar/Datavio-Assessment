import requests
from bs4 import BeautifulSoup

def scrape_flipkart_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the required data fields from the HTML soup
        title = soup.find('span', {'class': 'B_NuCI'}).text
        price = float(soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.replace('₹', '').replace(',', ''))
        description = soup.find('div', {'class': '_1mXcCf RmoJUa'}).text.strip()
        num_reviews = int(soup.find('span', {'class': '_2_R_DZ'}).text.split()[0])
        ratings = float(soup.find('div', {'class': '_3LWZlK'}).text)
        num_media = len(soup.find_all('div', {'class': '_3DFQ-7'}))
        
        return {
            'url': url,
            'title': title,
            'price': price,
            'description': description,
            'num_reviews': num_reviews,
            'ratings': ratings,
            'num_media': num_media,
        }
    except Exception as e:
        print(f"Error while scraping: {e}")
        return None
