import player 
import Board

class EightQueens:
    def __init__(self):
        self.__board = Board.Board()
        self.__player = player.Player()


    def __turn(self):
        while(True):
            try:
                print('Reinas disponibles(',self.__player.getQueens(), ')')
                box = int(input("\nIngrese No. de casilla donde quiere colocar la pieza "))

                if self.__board.isNotAvailableMovement(box):
                    print('Movimiento no permitido, casilla ocupada. Ingrese otra opcion ')
                    break;

                self.__board.move(-2, box)
                self.__board.calculateMovements(box)
                self.__board.traceMovements()
                self.__player.placeQueen()
                
                break

            except ValueError:
                print("\nValor invalido . Ingrese otra opcion\n")



    def play(self):

        print('\n--------------------Puzzle de las 8 Reinas------------------------------\n')

        

        while True:
            self.__board.printBoard()

            if self.__player.isWinner():
                print('\nFelicidades :) logro resolver el puzzle!!\n')
                break

            if self.__board.isBoardFull():
                print('\nQue lastima :( el tablero esta completamente ocupado. Fin del Juego!!\n')
                break

            self.__turn()

            



