
from bs4 import BeautifulSoup
import requests

search=input("enter the serach : ")
params={"q":search}

r=requests.get("https://www.google.com/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")
#result=soup.find("div",{"id":"rso"})
links=soup.findAll("h3",{"class":"r"})


for item in links:

    item_text=item.find("a").text
    item_link=item.find("a").attrs["href"]

    if item_text and item_link:
        print(item_text)
        print(item_link)