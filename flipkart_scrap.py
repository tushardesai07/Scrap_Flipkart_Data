import requests
from bs4 import BeautifulSoup
import pandas as pd
names=[]
ratings=[]
prices=[]
descriptions=[]
for i in range(1,10):
    url="https://www.flipkart.com/search?q=mobile+phones+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_desc&page="+str(i)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,"lxml")
# names of device
    name=soup.find_all("div",class_="KzDlHZ")
    for j in name:
        names.append(j.text)

    
# price of the data
    price=soup.find_all("div",class_="Nx9bqj _4b5DiR")
    for k in price:
        prices.append(k.text)
        
    
# description data
    des=soup.find_all("ul",class_="G4BRas")
    for l in  des:
        descriptions.append(l.text)

    

# names of rating
    rating=soup.find_all("div",class_="XQDdHH")
    for m in rating:
        ratings.append(m.text)


    if not names and not prices:
        print(f"No more data found on page {i}. Stopping...")
        break

print(" succesfully stored names ")
print(names)
print(" succesfully stored prices ")
print(prices)
print(" succesfully stored description ")
print(descriptions)
print(" succesfully stored ratings ")
print(ratings)

min_length = min(len(names), len(prices), len(ratings), len(descriptions))
names = names[:min_length]
prices = prices[:min_length]
ratings = ratings[:min_length]
descriptions = descriptions[:min_length]
data=pd.DataFrame({
    "names":names,
    "prices":prices,
    "ratings":ratings,
    "descriptions":descriptions

})

data.to_csv(r"E:\flipkart scrap\mobile_phones_under_20000.csv")
