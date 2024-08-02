from random import randrange
import reflex as rx
import requests
from bs4 import BeautifulSoup



class State(rx.State):
    user_shop_url:str = rx.Cookie(name="shopurl",secure=True,same_site="strict")
    tickets:str = "9999"    
    goal_percent:str = "7.5"
    goal_random_rot = randrange(-3, 0)
    tickets_random_rot = randrange(0, 3)
    
    
    def set_shop_url(self, new_text):
        self.user_shop_url = new_text
        
    
    def get_balance(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            balance_span = soup.find('span', class_='gaegu css-3ha5y3')
            balance_text = balance_span.text
            return balance_text
        except:
            return "Please set your shop URL in the settings!"
    tickert_text = get_balance(user_shop_url)
    