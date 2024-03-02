from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.core.cache import cache

@shared_task
def scrape_nifty50():
    url = 'https://www.nseindia.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = extract_nifty50_data(soup)
        cache.set('nifty50_data', data)

def extract_nifty50_data(soup):
    data = {}
    table = soup.find('table', class_='table-bordered')
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) >= 2:
                company = cols[0].text.strip()
                value = cols[1].text.strip()
                data[company] = value
    return data