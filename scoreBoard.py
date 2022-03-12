from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.x = -300
    self.y = 270
    self.size = 20
    self.font = ('Roboto', self.size, 'bold')
    self.penup()
    self.goto(self.x, self.y)
    self.color('yellow')
    self.update_score()  
    self.hideturtle()
  
  def update_score(self):
    self.write(f"Score: {self.score}", font = self.font)
  
  def increase_score(self):
    self.clear()
    self.score += 1
    self.update_score()
  
  def game_over(self):
    self.clear()
    self.x = -250
    self.y = -20
    self.size = 70
    self.font = ('Arial', self.size, 'bold')
    self.goto(self.x, self.y)
    self.color('red')
    self.write("Game over", font = self.font)
