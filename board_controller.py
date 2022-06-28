from mimetypes import init
import board
import pieces


class BoardController:

     def __init__(self, ID):
          self.ID = ID
          self.chessBoard = board.ChessBoard(ID)

     def AttemptMove(self, startRow, startCol, endRow, endCol):
          if self.chessBoard.isPieceAt(startCol, startRow):
               piece = self.chessBoard.getPiece(startRow, startCol)
               if piece.legalMove(startRow, startCol, endRow, endCol):
                    piece.move(startRow, startCol, endRow, endCol)

                    return True
          else:
               return False


BoardController = BoardController("123")
print(BoardController.AttemptMove(1,1,2,1))

