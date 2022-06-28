import numpy as np
import pieces
from enum import Enum

class ePiece(Enum):
      EMPTY = 0
      PAWN = 1
      ROOK = 2
      BISHOP = 3
      KNIGHT = 4
      QUEEN = 5
      KING = 6


class ChessBoard:

      def __init__(self, ID):
          self.ID = ID
          self.board = np.full((8, 8), 0)
          

      def display(self):
            for i in self.board:
                  lineOutput = ""
                  for j in i:
                       if j == 0:
                            lineOutput += (" | " + "EMPTY" + " | ")
                       else:
                            lineOutput += (" | " + j.name + " | ")
                  lineOutput += "\n"
                  for j in i:
                        lineOutput += ("   -   ")
                  print(lineOutput)


      def isPieceAt(self,row,col):
            if self.board[row][col] == 0:
                  return False
            else:
                  return True


      def getPiece(self,row,col):
            if self.isPieceAt(row,col):
                  return self.board[row][col]


      def initializeBoard(self):

            for i in range(0,8):
                  self.board[1][i] = pieces.Pawn('b',1 ,i)
                  self.board[6][i] = pieces.Pawn('w',1 ,i)



            self.board[0][0] = pieces.Rook('b',0 ,0)
            self.board[0][1] = pieces.Knight('b',0 ,1)
            self.board[0][2] = pieces.Bishop('b',0 ,2)
            self.board[0][3] = pieces.Queen('b',0 ,3)
            self.board[0][4] = pieces.King('b',0 ,4)
            self.board[0][5] = pieces.Bishop('b',0 ,5)
            self.board[0][6] = pieces.Knight('b',0 ,6)
            self.board[0][7] = pieces.Rook('b',0 ,7)

            self.board[7][0] = pieces.Rook('w',7 ,0)
            self.board[7][1] = pieces.Knight('w',7 ,1)
            self.board[7][2] = pieces.Bishop('w',7 ,2)
            self.board[7][3] = pieces.Queen('w',7 ,3)
            self.board[7][4] = pieces.King('w',7 ,4)
            self.board[7][5] = pieces.Bishop('w',7 ,5)
            self.board[7][6] = pieces.Knight('w',7 ,6)
            self.board[7][7] = pieces.Rook('w',7 ,7)



test1 = ChessBoard(ID="Test1")
test1.initializeBoard()
test1.display()



      