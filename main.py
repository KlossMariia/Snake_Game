import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

# creating a screen
screen = Screen()
food = Food()
score = Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
game_is_on = True

# setting keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    # time,sleep is used for controlling snake's speed (less it is, faster the snake is)
    time.sleep(0.2)
    snake.move()
    snake.go_through_wall()

    #detect_food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.grow()

    #if head collides with any segment
    if snake.tail_hit() == True:
        snake.reset()
        score.reset()
    else:
        continue


    #detect collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on=False
    #     # score.game_over()


screen.exitonclick()
