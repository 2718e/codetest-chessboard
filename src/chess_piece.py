from abc import ABC, abstractmethod, abstractclassmethod

class ChessPiece(ABC):
    def __init__(self, piece_color):
        self._piece_color = piece_color
        self._chess_board = None
        self._x_coordinate = None
        self._y_coordinate = None

    @property
    def chess_board(self):
        return self._chess_board

    @chess_board.setter
    def chess_board(self, value):
        self._chess_board = value

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, value):
        self._x_coordinate = value

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, value):
        self._y_coordinate = value

    @property
    def piece_color(self):
        return self._piece_color

    @piece_color.setter
    def piece_color(self, value):
        self.piece_color = value

    def move(self, movement_type, new_x, new_y):
        if (self.chess_board.is_legal_board_position(new_x, new_y) and self.check_move_is_allowed(movement_type,new_x,new_y) ):
            self.x_coordinate = new_x
            self.y_coordinate = new_y

    @abstractmethod    
    def check_move_is_allowed(self, movement_type, new_x, new_y):
        pass

    @abstractclassmethod
    def piece_name_long(self):
        pass

    # not used yet, plan is to give each piece a 1-letter abbreviation so could make an ascii representation of the board (with a colored console at least)
    @abstractclassmethod
    def piece_name_short(self):
        pass

    def __unicode__(self):
        return 'Current X: {}\nCurrent Y: {}\nPiece Color: {}\n Piece Type: {}'.format(
            self.x_coordinate, self.y_coordinate, self.piece_color, self.piece_name_long()
        )
