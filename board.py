import numpy as np
from enum import Enum
import pieces

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
                        lineOutput += (" | " + j.name + " | ")
                  lineOutput += "\n"
                  for j in i:
                        lineOutput += ("   -   ")
                  print(lineOutput)

      @classmethod
      def isPieceAt(cls,row,col):
            if cls.board[row][col] == 0:
                  return False
            else:
                  return True

      @classmethod
      def getPiece(cls,row,col):
            if cls.isPieceAt(row,col):
                  if cls.board[row][col] == 1 :
                        return "Pawn"
                  elif cls.board[row][col] == 2:
                        return "Rook"
                  elif cls.board[row][col] == 3:
                        return "Bishop"
                  elif cls.board[row][col] == 4:
                        return "Knight"
                  elif cls.board[row][col] == 5:
                        return "Queen"
                  elif cls.board[row][col] == 6:
                        return "King"
                  else:
                        return "Black Magic Fuckery"


      @classmethod
      def initializeBoard(cls):
            
            for i in range(0,8):
                  cls.board[1][i] = pieces.Pawn
                  cls.board[6][i] = pieces.Pawn
                  
            
            cls.board[0][0] = pieces.Rook
            cls.board[0][1] = pieces.Knight
            cls.board[0][2] = pieces.Bishop
            cls.board[0][3] = pieces.Queen
            cls.board[0][4] = pieces.King
            cls.board[0][5] = pieces.Bishop
            cls.board[0][6] = pieces.Knight
            cls.board[0][7] = pieces.Rook

            cls.board[7][0] = pieces.Rook
            cls.board[7][1] = pieces.Knight
            cls.board[7][2] = pieces.Bishop
            cls.board[7][3] = pieces.Queen
            cls.board[7][4] = pieces.King
            cls.board[7][5] = pieces.Bishop
            cls.board[7][6] = pieces.Knight
            cls.board[7][7] = pieces.Rook


            return cls

            

print(pieces.Rook.name)
            

test1 = ChessBoard(ID="Test1")
test1 = test1.initializeBoard()
test1.display()



      