class Piece:
    def __init__(self, color):
        if color == "Red":
            self.color = 'R'
        elif color == "Yellow":
            self.color = 'Y'

    def show_icon(self):
        if self.color == 'R':
            return "Red"
        elif self.color == 'Y':
            return "Yellow"


class Board:
    def __init__(self):
        self.grid = [['O' for _ in range(7)] for _ in range(6)]

    def __repr__(self):
        grid_string = ""
        for row in self.grid:
            grid_string += str(row) + "\n"
        return grid_string

    def place_piece(self, piece, col):
        row = 5
        while row > 0:
            if self.grid[row][col-1] == 'O':
                self.grid[row][col-1] = piece.color
                break
            row -= 1
        return row

    def check_win(self, color, row, col):
        # Check horizontal
        row_pieces = self.grid[row]
        for i in range(4):
            if row_pieces[i:i+4] == [color for _ in range(4)]:
                return True

        # Check vertical
        col_pieces = [i[col] for i in self.grid]
        for i in range(3):
            if col_pieces[i:i+4] == [color for _ in range(4)]:
                return True


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'R'
        self.game_over = False

    def display(self):
        print(self.board)

    def take_turn(self, color):
        piece = Piece(color)
        column = int(input(f"{color} turn\nColumn to place (1-7): "))
        row = self.board.place_piece(piece, column)
        if self.board.check_win(row, column):
            self.game_over = True


board = Board()
red_piece = Piece("Red")
board.place_piece(red_piece, 5)
board.place_piece(red_piece, 5)
board.place_piece(red_piece, 5)
board.place_piece(red_piece, 5)
print(board)
print(board.check_win('R', 5, 4))
