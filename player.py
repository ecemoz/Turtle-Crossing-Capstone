from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("turtle")
        super().penup()
        super().color("purple")
        super().setheading(90)
        self.go_to_start()


    def player_forward(self):
        super().forward(20)

    def is_at_finish_line(self):
       if self.ycor() > FINISH_LINE_Y:
           return True
       else:
           return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)