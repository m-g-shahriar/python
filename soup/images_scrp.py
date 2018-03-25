import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

def search_again() :
    seach = input("Enter for search : ")
    params={"q":seach}
    r=requests.get("https://www.bing.com/images/search",params=params)
    dir_name = seach.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    soup= BeautifulSoup(r.text,"html.parser")
    links=soup.findAll("a",{"class":"thumb"})

    for item in links:

        image_obj=requests.get(item.attrs["href"])
        title=item.attrs["href"].split("/")[-1]
        print("Getting",item.attrs["href"])
        try:
            img=Image.open(BytesIO(image_obj.content))
            img.save("./"+dir_name+"/"+title,img.format)

        except:
            print("nothing happen")

    search_again()

search_again()


