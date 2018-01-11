class ChessBoard:
    MAX_BOARD_WIDTH = 7
    MAX_BOARD_HEIGHT = 7

    def __init__(self):
        self.pieces = [[None] * 7 for _ in range(7)]

    def add(self, pawn, x_coordinate, y_coordinate, piece_color):
        raise NotImplementedError()

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        raise NotImplementedError()
