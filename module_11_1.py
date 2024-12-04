# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as BS

URL = 'https://books.toscrape.com'

# GET запрос
def get_html(url):
    html = requests.get(url)
    return html.text

# создаем объект soup
def pars_html(html):
    soup = BS(html,'html.parser')
    return soup

# находим нужные тэги HTML полученой страницы и выводим в консоль
if __name__ == '__main__':
    html = get_html(URL)
    soup = pars_html(html)
    #data = soup.select('ol.row li')
    data = soup.find('ol', class_ = 'row').find_all('li')
    for book in data:
        href = book.find('img').get('src')
        book_name = book.find('img').get('alt')
        price = book.select_one('p.price_color').text
        print(href)
        print(book_name)
        print(price[2:])