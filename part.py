import turtle

class Part:
    def __init__(self, width, length, color, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape('square')
        self.turtle.shapesize(stretch_wid= width, stretch_len= length)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(xcor, ycor)

    def up_function(self):
        y = self.turtle.ycor()
        y += 5
        self.turtle.sety(y)

    def down_function(self):
        y = self.turtle.ycor()
        y -= 5
        self.turtle.sety(y)

    def left_function(self):
        x = self.turtle.xcor()
        x -= 20
        self.turtle.setx(x)

    def right_function(self):
        x = self.turtle.xcor()
        x += 20
        self.turtle.setx(x)