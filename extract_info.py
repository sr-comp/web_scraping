import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.digikala.com/search/category-mobile-phone/?pageno='
titles = []
stars = []
prices = []
for page in range(1,3):
    page = requests.get(url+str(page))
    # print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.select('div.c-product-box__content--row')
    for t in title:
        name = t.text
        titles.append(name)

    star = soup.select('span.c-product-box__engagement-rating-num')
    for s in star:
        rate = s.text.strip()
        stars.append(rate)

    price = soup.select('div.c-price__value-wrapper')
    for p in price:
        pr = p.text.strip()
        prices.append(pr)
product = {'Title': titles, 'Star': stars, 'Price': prices}
data = pandas.DataFrame.from_dict(product, orient='index')
data = data.transpose()
writer = pandas.ExcelWriter('product.xlsx')
data.to_excel(writer)
writer.save()


