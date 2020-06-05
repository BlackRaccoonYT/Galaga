import turtle
import playerPart
import movabeObj

class Player(movabeObj.Movable):
    def __init__(self):
        parts = [
            playerPart.PlayerPart(2, 0.5, "white", 0, -175),
            playerPart.PlayerPart(1.5, 0.5, "white", 31.5, -129),
            playerPart.PlayerPart(1.5,0.5,"white",-31.5,-129),
            playerPart.PlayerPart(1,0.5,"white",-21,-154.5),
            playerPart.PlayerPart(1,0.5,"white",21,-154.5),
            playerPart.PlayerPart(0.5,0.5,"white",31.5,-159.5),
            playerPart.PlayerPart(0.5,0.5,"white",-31.5,-159.5),
            playerPart.PlayerPart(0.5,0.5,"white",42,-180.5),
            playerPart.PlayerPart(2,0.5,"white",52.5,-175),
            playerPart.PlayerPart(0.5,0.5,"white",-42,-180.5),
            playerPart.PlayerPart(2,0.5,"white",-52.5,-175),
            playerPart.PlayerPart(0.5,5,"white",0, -170),
            playerPart.PlayerPart(2.5,0.5,"white",0,-109),
            playerPart.PlayerPart(1.5,0.5,"white",10.5,-129),
            playerPart.PlayerPart(1.5,0.5,"white",-10.5,-129),
            playerPart.PlayerPart(0.5,0.5,"blue",21,-139),
            playerPart.PlayerPart(0.5,0.5,"blue",31.5,-149.5),
            playerPart.PlayerPart(0.5,0.5,"blue",-21,-139),
            playerPart.PlayerPart(0.5,0.5,"blue",-31.5,-149.5),
            playerPart.PlayerPart(1,0.5,"red",0,-144.5),
            playerPart.PlayerPart(0.5,0.5,'red',52.5,-149.5),
            playerPart.PlayerPart(0.5,0.5,'red',-52.2,-149.5),
            playerPart.PlayerPart(1,0.5,'red',10.5,-154.5),
            playerPart.PlayerPart(1,0.5,'red',-10.5,-154.5),
            playerPart.PlayerPart(0.5,1,'red',-15.5,-180.5),
            playerPart.PlayerPart(0.5,1,'red',15.5,-180.5),
            playerPart.PlayerPart(0.5,0.5,'red',31.5,-108.5),
            playerPart.PlayerPart(0.5,0.5,'red',-31.5,-108.5)
        ]
        movabeObj.Movable.__init__(self, parts)