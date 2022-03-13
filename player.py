
class Player:
    def __init__(self):
        self.queens = 8;


    def placeQueen(self):
        self.queens -=1

    def isWinner(self):
        return self.queens == 0

    def getQueens(self):
        return self.queens