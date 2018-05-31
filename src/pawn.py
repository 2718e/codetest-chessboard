from src.chess_piece import ChessPiece
from src.movement_type import MovementType
from src.piece_color import PieceColor

class Pawn(ChessPiece):
    def __init__(self, piece_color):
        super().__init__(piece_color)

    def check_move_is_allowed(self, movement_type, new_x, new_y):
        if (movement_type == MovementType.MOVE):
            if (self.piece_color == PieceColor.BLACK):
                return self.y_coordinate - new_y == 1 and self.x_coordinate == new_x
            else: # White Pawns move in the opposite direction
                return new_y - self.y_coordinate == 1 and self.x_coordinate == new_x
        else:
            raise NotImplementedError() # the spec for the coding challenge says not to implement capture

    @classmethod
    def piece_name_long(self):
        return "Pawn"

    @classmethod
    def piece_name_short(self):
        return "P"