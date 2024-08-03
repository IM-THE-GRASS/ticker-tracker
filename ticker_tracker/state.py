from random import randrange
import random
import reflex as rx
import requests
from bs4 import BeautifulSoup
import json


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
        
    def get_balance(self, id:str, ints = False):
        try:
            response = requests.get(f"https://hackclub.com/arcade/" + id + "/shop/")
            soup = BeautifulSoup(response.text, 'html.parser')
            balance_span = soup.find('span', class_='gaegu css-3ha5y3')
            balance_text = balance_span.text
            balance_text = balance_text.replace("Your current balance is ", "")
            balance_text = balance_text.replace(" 🎟️", "")
            if not ints:
                balance_text = f"You currently have {balance_text} tickets!"
            else:
                balance_text = int(balance_text)
            return balance_text
        except:
            if not ints:
                return "Please set your shop URL in the settings!"  
            else:
                return 0  
    
    
    def get_shop_info():
        response = requests.get("https://hackclub.com/api/arcade/shop/")
        data = json.loads(response.text)
        newdata={}
        for item in data:
            try:
                item.pop("smallName")
            except:
                pass
            item.pop("stock")
            tickets = item["hours"]
            item.pop("hours")
            item["tickets"] = str(tickets)
            newdata[item["name"]] = item
        return newdata
    
    shop_data:dict[str, dict[str,str]] = get_shop_info()
    shop_url_cookie:str = rx.Cookie(name="shopurl", secure= True, same_site="strict")
    shop_url:str
    shop_id:str
    
    
    
    goal_img:str
    goal_name:str
    goal_price:str   
    current_goal_choice:dict
    goal_cookie:str = rx.Cookie(name="goal")    
    has_goal:bool = True
    goal_percent:str = "7.5"
    def get_goal_info(self, full = False):
        tickets = self.get_balance(self.shop_url_cookie, ints=True)
        goal = int(self.goal_price)
        if not full:
            return str(round(100 * float(tickets)/float(goal)))
    def get_goal_name(self):
        datar =  self.goal_cookie
        return datar
    def get_goal_img(self):
        try:
            info = self.shop_data[self.goal_cookie]
            
            return info['imageURL']
        except:
            return "https://cloud-4x9tycf9y-hack-club-bot.vercel.app/0transpent.png"
    def get_goal_price(self):
        
        print("shop data", self.shop_data)
        print("goal cook", self.goal_cookie)
        try:
            info = self.shop_data[self.goal_cookie]
            
            return info['tickets']
        except:
            return "1"
        
        
    def check_has_goal(self):
        if self.goal_cookie in self.shop_data:
            return True
        else:
            return False
    
    
    
    
    ticket_text:str = get_balance(None, shop_url_cookie)
    
    
    
        
    
    
    
    
    
    def set_shop_url(self, new_text:str):
        self.shop_url = new_text
    def update_ticket_text(self):
        self.goal_price = self.get_goal_price()
        self.ticket_text = self.get_balance(self.shop_url_cookie)
        self.goal_name = self.get_goal_name()
        self.goal_img = self.get_goal_img()
        self.has_goal = self.check_has_goal()
        self.goal_percent = self.get_goal_info()
        
        print("goal+price", self.goal_price)
    def update(self):
        self.shop_url_cookie = self.strip_url(self.shop_url)
        self.update_ticket_text()
    
    def get_random_img(self):
        data = self.shop_data
        return random.choice(list(data.values()))['imageURL']
    random_img_1:str
    random_img_2:str
    def on_load(self):
        self.random_img_1 = self.get_random_img()
        self.random_img_2 = self.get_random_img()
        self.update_ticket_text()
    
    def set_goal(self, info):
        self.goal_cookie = info[0]
        self.update_ticket_text()
        #self.goal_cookie = self.current_goal_choice
    def choose_goal(self, *args):
        pass
        #self.current_goal_choice = info
    
    
        
    
    
    