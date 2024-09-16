# Requests is http libiery that enables to developers to send http requests . make it possiable 
# to intecract with api and web serivices 
import requests
r=requests.get("https://www.google.com")
# print(r.text)
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
# for head in soup.find_all("h3"):
#     print(head.text) 