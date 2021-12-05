import numpy as np
from enum import Enum

class Piece(Enum):
      EMPTY = 0
      PAWN = 1
      ROOK = 2
      BISHOP = 3
      KNIGHT = 4
      QUEEN = 5
      KING = 6


class ChessBoard:
      
      board = np.full((8,8), Piece.EMPTY)
      def __init__(self, ID):
          self.ID = ID
          
          
          
      @classmethod
      def display(cls):
            for i in cls.board:
                  lineOutput = ""
                  for j in i:
                        lineOutput += (" | " + str(j.value) + " | ")
                  lineOutput += "\n"
                  for j in i:
                        lineOutput += ("   _   ")
                  print(lineOutput)

      @classmethod
      def initializeBoard(cls):
            
            for i in range(0,8):
                  cls.board[1][i] = Piece.PAWN
                  cls.board[6][i] = Piece.PAWN
                  
            
            cls.board[0][0] = Piece.ROOK
            cls.board[0][1] = Piece.KNIGHT
            cls.board[0][2] = Piece.BISHOP
            cls.board[0][3] = Piece.QUEEN
            cls.board[0][4] = Piece.KING
            cls.board[0][5] = Piece.BISHOP
            cls.board[0][6] = Piece.KNIGHT
            cls.board[0][7] = Piece.ROOK

            cls.board[7][0] = Piece.ROOK
            cls.board[7][1] = Piece.KNIGHT
            cls.board[7][2] = Piece.BISHOP
            cls.board[7][3] = Piece.QUEEN
            cls.board[7][4] = Piece.KING
            cls.board[7][5] = Piece.BISHOP
            cls.board[7][6] = Piece.KNIGHT
            cls.board[7][7] = Piece.ROOK


            return cls

            


            
            

test1 = ChessBoard(ID="Test1")
test1 = test1.initializeBoard()
test1.display()



      