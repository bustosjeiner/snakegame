from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time

#Draw board
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor('blue')
screen.title('Snake game')
screen.tracer(0)

#Snake object
snake = Snake()
#Food object
food = Food()
#Score board
score_board = ScoreBoard()

#Listen keys to move the snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

#Game running condition
while score_board.game_is_on:
  screen.update()
  time.sleep(0.2)
  snake.movement()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score_board.increase_score() 
  
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    score_board.game_over()
  
  for segment in snake.snake_body:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      score_board.game_over()
#Close game
screen.exitonclick()