import turtle
import player
import enemy

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=1600, height=900)
wn.tracer(0)

enemyTHEM = enemy.Boomyzoomy()
enemyTHEM2 = enemy.Boomyzoomy()
enemyTHEM3 = enemy.Boomyzoomy()

playerME = player.Player()

wn.listen()
wn.onkeypress(playerME.left, 'a')
wn.onkeypress(playerME.right, 'd')

loopCounter = 0

while True:
    loopCounter += 1
    if loopCounter >= 100000:
        loopCounter = 0

    print(enemyTHEM.moveFrequency())
    if loopCounter % enemyTHEM.moveFrequency() == 0:
        enemyTHEM.down()
        enemyTHEM2.down()
        enemyTHEM3.down()

    wn.update()




