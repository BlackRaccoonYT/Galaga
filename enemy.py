import turtle
import enemyPart
import movabeObj
import random

class Enemy(movabeObj.Movable):
    def __init__(self, speed, parts):
        self.startingxcor = random.randint(-700, 700)
        self.startingycor = 400
        self.speed = speed

        for part in parts:
            part.turtle.goto(part.xcor + self.startingxcor, part.ycor + self.startingycor)

        movabeObj.Movable.__init__(self, parts)

    def moveFrequency(self):
        modifier = 10 - self.speed
        steps = 3 * modifier
        return self.speed - (8 - steps)

class Boomyzoomy(Enemy):
    def __init__(self):
        parts = [
           enemyPart.EnemyPart(4, 5.2, "yellow", 0, -124),
           enemyPart.EnemyPart(4, 1, "blue", 0, -61),
           enemyPart.EnemyPart(2, 1, "blue", -21, 0),
           enemyPart.EnemyPart(2, 1, "blue", 21, 0),
           enemyPart.EnemyPart(1, 2, "blue", -73, -31),
           enemyPart.EnemyPart(1, 2, "blue", 73, -31),
           enemyPart.EnemyPart(1, 5.2, "blue", 0, -72),
           enemyPart.EnemyPart(1, 1, "blue", -63, -52),
           enemyPart.EnemyPart(1, 1, "blue", 63, -52),
           enemyPart.EnemyPart(2, 2, "red", 32, -41),
           enemyPart.EnemyPart(2, 2, "red", -31, -41),
           enemyPart.EnemyPart(2, 2, "red", -31, -41)
        ]
        Enemy.__init__(self, 7, parts)