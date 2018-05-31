class ChessBoard:
    MAX_BOARD_WIDTH = 8
    MAX_BOARD_HEIGHT = 8

    def __init__(self):
        # will be indexed as self.pieces[row][column]
        self.pieces = [[None] * self.MAX_BOARD_WIDTH for _ in range(self.MAX_BOARD_HEIGHT)]

    def add(self, piece, x_coordinate, y_coordinate, piece_color):
        if (y_coordinate < len(self.pieces) and 
        x_coordinate < len(self.pieces[y_coordinate]) and 
        self.pieces[y_coordinate][x_coordinate] == None):
            self.pieces[y_coordinate][x_coordinate] = piece
            piece.x_coordinate = x_coordinate
            piece.y_coordinate = y_coordinate
            piece.chess_board = self
        else:
            piece.x_coordinate = -1
            piece.y_coordinate = -1

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        return (x_coordinate >= 0 and y_coordinate >= 0 and y_coordinate < self.MAX_BOARD_HEIGHT and x_coordinate < self.MAX_BOARD_WIDTH)
