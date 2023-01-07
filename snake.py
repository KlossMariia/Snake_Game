from turtle import Turtle

# class is responsible for creating and moving snake
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # snake is a list containing multiple turtle objects (squared shaped segments)
    def create_snake(self):
        x = 0
        y = 0
        for i in range(0, 3):
            position = (x, y)
            x -= 20
            self.add_segment(position)

    # creates new segment
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    # sends new segment to the snake's tail
    def grow(self):
        go_to_x = self.snake[len(self.snake)-1].xcor()
        go_to_y = self.snake[len(self.snake) - 1].ycor()
        position = (go_to_x, go_to_y)
        self.add_segment(position)

    # checks if tail was hit
    def tail_hit(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True

    # moving of the snake is based on segments going to coordinates of segment above
    # so, second first segment moves, second segment goes to first segment's previous position and so on
    def move(self):
        for n in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[n - 1].xcor()
            new_y = self.snake[n - 1].ycor()
            self.snake[n].goto(new_x, new_y)
        self.snake[0].forward(20)

    # functions under are responsible for changing snakes moving direction
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    # this function allows snake go through walls
    def go_through_wall(self):
        if self.head.xcor() > 280:
            self.head.setx(-280)
        elif self.head.xcor() < -280:
            self.head.setx(280)
        elif self.head.ycor() < -280:
            self.head.sety(280)
        elif self.head.ycor() > 280:
            self.head.sety(-280)

    # this function takes snake out of the screen when user loses. afterwards it creates a new snake
    def reset(self):
        for item in self.snake:
            item.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
