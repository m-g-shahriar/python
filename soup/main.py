''''
from bs4 import BeautifulSoup
import requests

search=input("Enter the srarch item : ")
param={"q":search}
r=requests.get("https://www.google.com/search",params=search)

soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
'''

from bs4 import BeautifulSoup
import requests


search=input("Enter teh key : ")
params={"q":search}
r=requests.get("https://www.bing.com/search",params=params)

soup=BeautifulSoup(r.text,"html.parser")
result=soup.find("ol",{"id":"b_results"})
links=result.findAll("li",{"class":"b_algo"})

for item in links:

    item_text=item.find("a").text
    item_link=item.find("a").attrs["href"]
    item_details=item.find("p")
    item_h=item.find("h2")

    if item_text and item_link:
        print(item_text)
        print(item_link)
        print(item_h)
        print(item_details)