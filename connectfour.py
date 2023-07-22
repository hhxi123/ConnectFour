class Piece:
    def __init__(self, color):
        self.color = color


class Board:
    def __init__(self):
        self.grid = [['O' for i in range(7)] for i in range(6)]

    def __repr__(self):
        return self.grid

    def place_piece(self, piece, col):
        row = 5
        while row > 0:
            if self.grid[row][col] == 'O':
                self.grid[row][col] = piece.color
                break
            row = row - 1

    def check_win(self, row, col):
        color = self.grid[row][col]
        # TODO: Finish this


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'R'

    def display(self):
        print(self.board)

    def play(self):
        done = False
        while not done:
            piece = Piece(self.turn)
            self.board.place_piece(piece, input("Red turn\nColumn to place: "))
            # TODO: Finish this too


