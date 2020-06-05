import turtle
import player
import enemy
from game import Game

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=1600, height=900)
wn.tracer(0)

enemyTHEM = enemy.Boomyzoomy()
enemyTHEM2 = enemy.Boomyzoomy()
enemyTHEM3 = enemy.Boomyzoomy()

enemies = [enemyTHEM, enemyTHEM2, enemyTHEM3]

playerME = player.Player()

wn.listen()
wn.onkeypress(playerME.left, 'a')
wn.onkeypress(playerME.right, 'd')

game = Game(playerME, enemies)

loopCounter = 0

while True:
    loopCounter += 1
    if loopCounter >= 100000:
        loopCounter = 0
    game.moveEnemies(loopCounter)


    wn.update()




