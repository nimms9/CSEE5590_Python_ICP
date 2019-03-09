from bs4 import BeautifulSoup
import requests

page_link = 'https://en.wikipedia.org/wiki/Google'
page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")
text = page_content.get_text()
f = open('input.txt', 'w',encoding='utf-8')
f.write(text)