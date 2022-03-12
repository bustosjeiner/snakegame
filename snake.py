from turtle import Turtle

#Create initial position
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
#Movements in degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Define snake class
class Snake:
  #Constructor method
  def __init__(self):
    self.snake_body = []
    self.create_snake()
    #Snake's head
    self.head = self.snake_body[0]

  #Create snake method
  def create_snake(self):
    for position in STARTING_POSITION:
      self.add_segment(position)
  
  def add_segment(self, position):
    snake_segment = Turtle('square')
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(position)
    self.snake_body.append(snake_segment)
  
  def extend(self):
    self.add_segment(self.snake_body[-1].position())

  #Snake movement
  def movement(self):
    for segment in range(len(self.snake_body)-1, 0, -1):
      x = self.snake_body[segment-1].xcor()
      y = self.snake_body[segment-1].ycor()
      self.snake_body[segment].goto(x, y)
    self.head.forward(20)
    
  #Snake movement to up
  def up(self):
    if self.head.heading() != DOWN: 
      self.head.setheading(UP)
  #Snake movement to down
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  #Snake movement to left
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
  #Snake movement to right
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
