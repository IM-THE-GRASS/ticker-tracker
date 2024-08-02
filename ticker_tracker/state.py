from random import randrange
import reflex as rx
import requests
from bs4 import BeautifulSoup



class State(rx.State):
    goal_random_rot = randrange(-3, 0)
    tickets_random_rot = randrange(0, 3)
    
    
        
    
    def strip_url(self, input_url:str):
        input_url = input_url.replace(" ", '')
        input_url = input_url.replace("https:", '')
        input_url = input_url.replace("http:", '')
        input_url = input_url.replace("shop", '')
        input_url = input_url.replace("hackclub.com/arcade", '')
        input_url = input_url.replace("/", '')
        return input_url
        
    def get_balance(self, id:str):
        try:
            response = requests.get(f"https://hackclub.com/arcade/" + id + "/shop/")
            print("huh")
            print(response.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            balance_span = soup.find('span', class_='gaegu css-3ha5y3')
            balance_text = balance_span.text
            balance_text = balance_text.replace("Your current balance is ", "")
            balance_text = balance_text.replace(" 🎟️", "")
            balance_text = f"You currently have {balance_text} tickets!"
            print(balance_text)
            return balance_text
        except:
            return "Please set your shop URL in the settings!"    
    
    
    
    
    
    shop_url_cookie:str = rx.Cookie(name="shopurl")
    shop_url:str
    shop_id:str
    
    
    tickets:str = "9999"    
    goal_percent:str = "7.5"
    
    ticket_text:str = get_balance(None, shop_url_cookie)
    
    
    
    
    
    
    
    
    def set_shop_url(self, new_text:str):
        self.shop_url = new_text
    def update_ticket_text(self):
        self.ticket_text = self.get_balance(self.shop_url_cookie)
    def update(self):
        self.shop_url_cookie = self.strip_url(self.shop_url)
        self.update_ticket_text()
    
    
    
        
        
    
    
    