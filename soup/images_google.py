import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


search = input("Search : ")
params={"q":search}
r=requests.get("https://www.google.com/images",params=params)

soup=BeautifulSoup(r.text,"html.parser")
links=soup.findAll("a",{"class":"rg_l"})

for item in links:

    img_obj=requests.get(item.attrs["href"])
    title=item.find["href"].split("/")[-1]
    img=Image.open(BytesIO(img_obj.content))
    img.save("./google_images"+title,img.format)