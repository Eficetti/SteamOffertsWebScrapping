import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/specials#tab=TopSellers'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
titleName = []
titlePrice = []
discountPrice = []
priceTax = []
game = soup.find_all('div', class_='tab_item_name')
count = 0
for i in game:
    if count < 50:
        titleName.append(i.text)
    else :
        break 
    count += 1

price = soup.find_all('div', class_="discount_final_price")
count = 0
for i in price:
    if count < 50:
        number = i.text.replace('ARS$ ', '')
        numberdot = number.replace('.', '')
        newNumber = numberdot.replace(',', '.')
        value = float(newNumber)
        impuesto = 65 * value / 100
        value += impuesto
        newValue ="{:.2f}".format(value)
        titlePrice.append(newValue)
    else:
        break 
    count += 1

discount = soup.find_all('div', class_="discount_pct")
count = 0
for i in discount:
    if count < 50:
        discountPrice.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({'Nombre': titleName,'Descuento': discountPrice ,'Precio': titlePrice})
print(df)
input('Press enter to close')
