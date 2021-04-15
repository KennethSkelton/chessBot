import chess
from Game import Game


class GameController:

    def __init__(self):
        self.gameDict = {}

    def addToGameList(self, playerID, difficulty, color = "random"):

        if playerID not in self.gameDict:
            
            self.gameDict[playerID] = Game(chess.Board, difficulty, "white")
