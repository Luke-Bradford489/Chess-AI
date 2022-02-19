from mimetypes import init
import board
import pieces

class BoardController:
      ID = ""

      def __init__(self,ID):
            self.ID = ID
            self.chessBoard = board.ChessBoard(ID)

      def AttemptMove():
            pass