from turtle import Turtle
import random

#Define food class
class Food(Turtle):
  #Constructor method
  def __init__(self):
    #Heredar from turtle class
    super().__init__()
    #Drow food
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len = 0.5, stretch_wid= 0.5)
    self.color('red')
    self.speed('fast')
    self.refresh()
  
  #Aleatory food
  def refresh(self):
    random_x = random.randint(-300, 300)
    random_y = random.randint(-300, 300)
    self.goto(random_x, random_y)
