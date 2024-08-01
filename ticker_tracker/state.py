from random import randrange
import reflex as rx

class State(rx.State):
    def random_rot():
        return randrange(-3, 3)
    tickets:str = "9999"    
    goal_percent:str = "7.5"
    goal_random_rot = random_rot()
    tickets_random_rot = random_rot()