import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
page=requests.get(url)#Making a request for the url given and creating a response object called 'page'
soup=BeautifulSoup(page.content,'html.parser')#The soup takes arguments page.content(the content of the server's response and then parse it using python builtin html parser
tb=soup.find('table',class_='wikitable')#Finding the table tag in the sourcecode with class 'wikitable'
tb_rows=tb.find_all('tr')#Finding the tags with table rows i.e 'tr'
file=open("href.txt",'w')#opening the file in the write mode to write the data into the file
for  tr in tb_rows:
    th=tr.find_all('th')#Finding the table head tags
    sdf=[j.text for j in th]#finding the table headings to display the states names
    print('\n'.join(sdf[:1]))
    file.write(':'.join(sdf[:1]))#and writing the states to the file
    td=tr.find_all('td')
    row=[i.text for i in td]#Finding the capital names using td tag and writing to the file
    print(' '.join(row[0:2]))
    file.write(':'.join(row[0:2]))
    file.write('---------\n')
file.close()#closing the file in the end