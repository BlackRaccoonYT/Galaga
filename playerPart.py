import turtle
import part

class PlayerPart(part.Part):
    def __init__(self, width, length, color, xcor, ycor):
        part.Part.__init__(self, width, length, color, xcor, ycor - 200)