import requests
from bs4 import BeautifulSoup
import re

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# data = soup.findAll(['a','div'])
# data = soup.findAll('div',class_='quote')
# regex
# data = soup.findAll(re.compile('(^a|div)'))
data = soup.findAll('div', re.compile('(^quote)'))

for d in data:
    print(d.text)