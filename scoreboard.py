from turtle import Turtle, Screen

# class is used fot keeping points record
class Score(Turtle):

    # the highest score is taken from txt file
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highest_score.txt', mode="r") as file:
            self.high_score = int(file.read())
        # placing "score" ob the screen
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-15, 270)
        self.speed("fastest")
        self.update()

    # if user reached new record, it will be written to txt file
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    # updates score on the screen
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, "center", ('Times New Roman', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.update()



