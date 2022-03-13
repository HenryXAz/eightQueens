from re import L
import numpy as np


class Board:
    def __init__(self):
        self.availableBoxes = np.arange(0,64)
        self.unavailableBoxes = []


    def printBoard(self):
        print('')
        print(self.availableBoxes[0], '\t', self.availableBoxes[1], '\t', self.availableBoxes[2], '\t', self.availableBoxes[3], '\t', self.availableBoxes[4], '\t', self.availableBoxes[5], '\t', self.availableBoxes[6], '\t', self.availableBoxes[7])
        print(self.availableBoxes[8], '\t', self.availableBoxes[9], '\t', self.availableBoxes[10], '\t', self.availableBoxes[11], '\t', self.availableBoxes[12], '\t', self.availableBoxes[13], '\t', self.availableBoxes[14], '\t', self.availableBoxes[15])
        print(self.availableBoxes[16], '\t', self.availableBoxes[17], '\t', self.availableBoxes[18], '\t', self.availableBoxes[19], '\t', self.availableBoxes[20], '\t', self.availableBoxes[21], '\t', self.availableBoxes[22], '\t', self.availableBoxes[23])
        print(self.availableBoxes[24], '\t', self.availableBoxes[25], '\t', self.availableBoxes[26], '\t', self.availableBoxes[27], '\t', self.availableBoxes[28], '\t', self.availableBoxes[29], '\t', self.availableBoxes[30], '\t', self.availableBoxes[31])
        print(self.availableBoxes[32], '\t', self.availableBoxes[33], '\t', self.availableBoxes[34], '\t', self.availableBoxes[35], '\t', self.availableBoxes[36], '\t', self.availableBoxes[37], '\t', self.availableBoxes[38], '\t', self.availableBoxes[39])
        print(self.availableBoxes[40], '\t', self.availableBoxes[41], '\t', self.availableBoxes[42], '\t', self.availableBoxes[43], '\t', self.availableBoxes[44], '\t', self.availableBoxes[45], '\t', self.availableBoxes[46], '\t', self.availableBoxes[47])
        print(self.availableBoxes[48], '\t', self.availableBoxes[49], '\t', self.availableBoxes[50], '\t', self.availableBoxes[51], '\t', self.availableBoxes[52], '\t', self.availableBoxes[53], '\t', self.availableBoxes[54], '\t', self.availableBoxes[55])
        print(self.availableBoxes[56], '\t', self.availableBoxes[57], '\t', self.availableBoxes[58], '\t', self.availableBoxes[59], '\t', self.availableBoxes[60], '\t', self.availableBoxes[61], '\t', self.availableBoxes[62], '\t', self.availableBoxes[63])
        print('')

    def move(self, token, position):
        self.availableBoxes[position] = token

    def traceMovements(self):
        for i in range(len(self.unavailableBoxes)):
            movement = self.unavailableBoxes[i]
            
            if self.availableBoxes[movement] != -2:
                self.availableBoxes[movement] = -1 


    def getQueenMoves(self):
        return self.unavailableBoxes;

    def calculateMovements(self, box):
        rows = self.getRows( box)
        columns = self.getColumns(box)
        lowerLeftDiagonal = self.getLowerLeftDiagonal(box)
        topLeftDiagonal = self.getTopLeftDiagonal(box)
        lowerRightDiagonal = self.getLowerRightDiagonal(box)
        topRightDiagonal = self.getTopRightDiagonal(box)

        self.__addMovements(rows, columns, lowerLeftDiagonal, topLeftDiagonal, lowerRightDiagonal, topRightDiagonal)


    def __addMovements(self, rows, columns, lowerLeftDiagonal, lowerRightDiagonal, topLeftDiagonal, topRightDiagonal):
        for i in range(len(rows)):
           self.unavailableBoxes.append(rows[i])

        for i in range(len(columns)):
            if not columns[i] in self.unavailableBoxes:
                self.unavailableBoxes.append(columns[i])

        for i in range(len(lowerLeftDiagonal)):
            if not lowerLeftDiagonal[i] in self.unavailableBoxes:
                self.unavailableBoxes.append(lowerLeftDiagonal[i])

        for i in range(len(lowerRightDiagonal)):
            if not lowerRightDiagonal[i] in self.unavailableBoxes:
                self.unavailableBoxes.append(lowerRightDiagonal[i])

        for i in range(len(topLeftDiagonal)):
            if not topLeftDiagonal[i] in self.unavailableBoxes:
                self.unavailableBoxes.append(topLeftDiagonal[i])
        
        for i in range(len(topRightDiagonal)):
            if not topRightDiagonal[i] in self.unavailableBoxes:
                self.unavailableBoxes.append(topRightDiagonal[i])

    def isNotAvailableMovement(self, box):
        return box in self.unavailableBoxes

    def isBoardFull(self):
        boxes = 0

        for i in range(len(self.availableBoxes)):
            if(self.availableBoxes[i] == -1) or (self.availableBoxes[i] == -2):
                boxes +=1

        return boxes == 64

    def getRows(self, box):
        
        rows = []
        i = box

        while i % 8 != 0 or i == 0:

            rows.append(i)
            i+=1

        i = box

        while i%8 != 0:
            if not i in rows: 
                rows.append(i)
            
            i-=1

            if i% 8 == 0:
                rows.append(i)

        return rows

    def getColumns(self, box):
        columns = []

        i = box

        while i >=0:
            columns.append(i)
            i-=8

        i = box

        while i <= 63:
            if not i in columns:
                columns.append(i)
            
            i+=8

        return columns

    def getLowerLeftDiagonal(self, box):
        leftDiagonal = []

        i = box

        while (i+8) % 8 !=0 and i < 63:
            leftDiagonal.append(i)
            i+=7

            if(i%8 == 0 and i < 63):
                leftDiagonal.append(i)

        return leftDiagonal

    def getTopLeftDiagonal(self, box):
        leftDiagonal = []

        i = box

        while i % 8 != 0 and i > 0:
            leftDiagonal.append(i)
            
            i-=9

        if i % 8 == 0 and i >= 0:
            leftDiagonal.append(i)

        return leftDiagonal

    def getLowerRightDiagonal(self, box):
        rightDiagonal = []

        i = box

        while (i + 9) % 8 != 0 and i <= 63:
            rightDiagonal.append(i)
            i+=9

            if((i+1) % 8 == 0 and i <= 63):
                rightDiagonal.append(i)

        return rightDiagonal

    def getTopRightDiagonal(self, box):
        rightDiagonal = []

        i = box

        while i % 8 != 0 and i >= 0:
            rightDiagonal.append(i)
            i-=7
        return rightDiagonal