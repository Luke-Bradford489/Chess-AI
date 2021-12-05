# w - white
# b - black
#
# K - King
# Q - Queen
# B - Bishop
# N - Knight
# R - Rook/Castle
# P - Pawn
# 
# Notes:
#     - Need to implement other piece detection
class ChessPiece:
      name = "Pawn"
      side = ''
      row = 0
      col = 0
      doubleMoveFlag = True

      def __init__(self, side, row, col):
        self.side = side
        self.row = row
        self.col = col

      @classmethod
      def move(cls,currRow, currCol, newRow, newCol):
            if cls.legalMove(currRow, currCol, newRow, newCol):
                  cls.row = newRow
                  cls.col = newCol
            return cls

      @staticmethod
      def legalMove(currRow, currCol, newRow, newCol):
            pass
            

class Pawn(ChessPiece):

      doubleMoveFlag = True

      def __init__(self, side, row, col):
          super().__init__(side, row, col)
          if side == 'w':
                self.direction = 1
          else:
                self.direction = -1


      

      @staticmethod
      def legalMove(cls,currRow, currCol, newRow, newCol):
          if cls.doubleMoveFlag :
                if currCol + cls.direction * 2 == newCol:
                      return True
                
class Knight(ChessPiece):
      
      @staticmethod
      def legalMove(currRow, currCol, newRow, newCol):


            if newCol in range(1,8) and newRow in range(1,8):
                  if currCol - 2 == newCol and currRow + 1 == newRow:
                        return True
                  elif currCol - 2 == newCol and currRow - 1 == newRow:
                        return True
                  elif currCol + 2 == newCol and currRow - 1 == newRow:
                        return True
                  elif currCol + 2 == newCol and currRow + 1 == newRow:
                        return True
                  elif currCol + 1 == newCol and currRow + 2 == newRow:
                        return True
                  elif currCol + 1 == newCol and currRow - 2 == newRow:
                        return True
                  elif currCol - 1 == newCol and currRow + 2 == newRow:
                        return True
                  elif currCol - 1 == newCol and currRow - 2 == newRow:
                        return True
                  else:
                        return False
            else:
                  return False
   
class Rook(ChessPiece):
      
      @staticmethod
      def legalMove(currRow, currCol, newRow, newCol):
            if (newCol in range(1,8) and newRow == currRow):
                  return True
            elif (newCol == currCol and newCol in range(1,8)):
                  return True
            else:
                  return False

class Bishop(ChessPiece):

      @staticmethod
      def legalMove(currRow, currCol, newRow, newCol):
            if (newCol in range(1,8) and newRow in range(1,8) ) and (abs(currCol - newCol) == abs(newRow - currRow)):
                  return True

class King(ChessPiece):
      @staticmethod                 
      def legalMove(currRow, currCol, newRow, newCol):
            if (newRow in range(1,8)) and (newCol in range(1,8)):
                  if currRow + 1 == newRow and currCol == newCol:
                        return True
                  elif currRow - 1 == newRow and currCol == newCol:
                        return True
                  elif currRow + 1 == newRow and currCol - 1== newCol:
                        return True
                  elif currRow + 1 == newRow and currCol + 1 == newCol:
                        return True
                  elif currRow - 1 == newRow and currCol + 1 == newCol:
                        return True
                  elif currRow - 1 == newRow and currCol - 1 == newCol:
                        return True
                  elif currRow == newRow and currCol + 1 == newCol:
                        return True
                  elif currRow == newRow and currCol - 1 == newCol:
                        return True
                  else:
                        return False

class Queen(ChessPiece):

      def legalMove(currRow, currCol, newRow, newCol):
            if (newCol in range(1,8) and newRow == currRow):
                  return True
            elif (newCol == currCol and newCol in range(1,8)):
                  return True
            elif (newCol in range(1,8) and newRow in range(1,8) ) and (abs(currCol - newCol) == abs(newRow - currRow)):
                  return True
            else:
                  return False
          

      

      
            


