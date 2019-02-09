import requests
import re
#Getting request of the webpage wikipedia
website_url=requests.get('https://en.wikipedia.org/wiki/Deep_learning').text
from bs4 import BeautifulSoup
#BeautifulSoup pulls the data out of html and xml files
soup=BeautifulSoup(website_url,'lxml')
print(soup.prettify())
#Getting title of the webpage
print("Title of web page:",soup.title.string)
#Opening the file in write mode
file=open("href.txt","w")
#Getting the http links from the href attribute of all the anchor tags
for link in soup.find_all('a',attrs={'href': re.compile("^http://")}):
    file.write(link.get('href')+'\n')
file.close()

