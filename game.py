import turtle
class Game:
    def __init__(self,player,enemies):
        self.player = player
        self.enemies = enemies

    def moveEnemies(self, loopCounter):
        for enemy in self.enemies:
            if loopCounter % enemy.moveFrequency() == 0:
                enemy.down()
                self.checkCollision(enemy)

    def checkCollision(self, enemy):
        for enemyPart in enemy.parts:
            for part in self.player.parts:
                if (enemyPart.turtle.distance(part.turtle) < 20):
                    self.gameOver()

    def gameOver(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write('''
         _______                      
        |   _   .---.-.--------.-----.
        |.  |___|  _  |        |  -__|
        |.  |   |___._|__|__|__|_____|
        |:  1   |                     
        |::.. . |                     
        `-------'                     
         _______                      
        |   _   .--.--.-----.----.    
        |.  |   |  |  |  -__|   _|    
        |.  |   |\___/|_____|__|      
        |:  1   |                     
        |::.. . |                     
        `-------'                     
        ''') 
