import pandas as pd
import requests
from bs4 import BeautifulSoup
class Main():

    def __init__(self,url):
        url = url
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, 'html.parser')
        self.titleName = []
        self.titlePrice = []
        self.discountPrice = []
        self.total = []

    def game(self,etiqueta, clase):
        game = self.soup.find_all(etiqueta, class_=clase)
        count = 0
        self.total = len(game)
        for i in game:
            if count < self.total:
                self.titleName.append(i.text)
            else :
                break 
            count += 1

    def price(self,etiqueta, clase):
        price = self.soup.find_all(etiqueta, class_=clase)
        count = 0
        for i in price:
            if count < self.total:
                number = i.text.replace('ARS$ ', '')
                numberdot = number.replace('.', '')
                newNumber = numberdot.replace(',', '.')
                value = float(newNumber)
                impuesto = 65 * value / 100
                value += impuesto
                newValue ="{:.2f}".format(value)
                self.titlePrice.append(newValue)
            else:
                break 
            count += 1

    def discount(self, etiqueta, clase):
        discount = self.soup.find_all(etiqueta, class_=clase)
        count = 0
        for i in discount:
            if count < self.total:
                self.discountPrice.append(i.text)
            else:
                break
            count += 1

    def printeo(self, name):
        print('                                             ', name)
        print(' ')
        df = pd.DataFrame({'Nombre': self.titleName,'Descuento': self.discountPrice ,'Precio': self.titlePrice})
        print(df)
        

m = Main('https://store.steampowered.com/specials#tab=TopSellers')
m.game('div', 'tab_item_name')
m.price('div', 'discount_final_price')
m.discount('div', 'discount_pct')
m.printeo('Top Sellers')
print('-----------------------------------------------------------------------------------------------------------')
input('Press enter to close')

