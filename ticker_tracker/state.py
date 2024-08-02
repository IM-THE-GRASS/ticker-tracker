from random import randrange
import reflex as rx
import requests
from bs4 import BeautifulSoup



class State(rx.State):
    shop_url_cookie:str = rx.Cookie(name="shopurl")
    shop_url:str
    tickets:str = "9999"    
    goal_percent:str = "7.5"
    goal_random_rot = randrange(-3, 0)
    tickets_random_rot = randrange(0, 3)
    
    
    def set_shop_url(self, new_text):
        self.shop_url_cookie = self.shop_url
        print(self.shop_url_cookie)
        
    def update(self):
        self.shop_url_cookie = rx.Cookie(name="shopurl")
        self.shop_url_cookie = self.shop_url
        
        
    
    def get_balance(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            balance_span = soup.find('span', class_='gaegu css-3ha5y3')
            balance_text = balance_span.text
            return balance_text
        except:
            return "Please set your shop URL in the settings!"
    tickert_text = get_balance(shop_url_cookie)
    