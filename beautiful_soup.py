import requests
from bs4 import BeautifulSoup

# url = "https://www.python.org/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# show = soup.find('a')
# print(show)
# show = soup.findAll('a')
# show = soup.find_all('a')
# for s in show:
#     print(s['href'])

# show = soup.select_one('a')
# print(show)
# show = soup.select('a')
# for s in show:
#     print(s['href'])
# show = soup.select_one('button.search-button')
# show = soup.find('button', {'id': 'submit'})
# print(show.text)
# print(show.text.strip())

#################################################################
url = "https://www.skysports.com/premier-league-table"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    data = []
    for head in row.find_all('th'):
        heads = head.text
        data.append(heads)
    for body in row.find_all('td'):
        bodies = body.text.replace('\n', '')
        data.append(bodies)
    print(data)
