import unittest

from src.chess_board import ChessBoard
from src.movement_type import MovementType
from src.pawn import Pawn
from src.piece_color import PieceColor


class TestPawn(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.chess_board = ChessBoard()
        self.pawn = Pawn(PieceColor.BLACK)

    def test_that_add_sets_x_coordinates(self):
        self.chess_board.add(self.pawn, 6, 3)

        self.assertEqual(self.pawn.x_coordinate, 6)

    def test_that_add_sets_y_coordinate(self):
        self.chess_board.add(self.pawn, 6, 3)

        self.assertEqual(self.pawn.y_coordinate, 3)

    def test_that_illegal_move_right_right_does_not_move(self):
        self.chess_board.add(self.pawn, 6, 3)
        self.pawn.move(MovementType.MOVE, 7, 3)

        self.assertEqual(self.pawn.x_coordinate, 6)
        self.assertEqual(self.pawn.y_coordinate, 3)

    def test_that_illegal_move_left_does_not_move(self):
        self.chess_board.add(self.pawn, 6, 3)
        self.pawn.move(MovementType.MOVE, 4, 3)

        self.assertEqual(self.pawn.x_coordinate, 6)
        self.assertEqual(self.pawn.y_coordinate, 3)

    def test_that_legal_move_forward_does_move(self):
        self.chess_board.add(self.pawn, 6, 3)
        self.pawn.move(MovementType.MOVE, 6, 2)

        self.assertEqual(self.pawn.x_coordinate, 6)
        self.assertEqual(self.pawn.y_coordinate, 2)
    
    # what about the case where the piece can move in that way but is trying to move off the board.
    def test_that_legal_move_to_out_of_bounds_does_not_move(self):
        self.chess_board.add(self.pawn, 6, 0)
        self.pawn.move(MovementType.MOVE, 6, -1)

        self.assertEqual(self.pawn.x_coordinate, 6)
        self.assertEqual(self.pawn.y_coordinate, 0)

    