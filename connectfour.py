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
    def __init__(self, rows, columns):
        self.grid = [['O' for _ in range(columns)] for _ in range(rows)]

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
        winning_set = [color for _ in range(4)]

        # Check horizontal
        row_pieces = self.grid[row]
        for i in range(len(row_pieces) - 3):
            if row_pieces[i:i+4] == winning_set:
                return True

        # Check vertical
        col_pieces = [i[col] for i in self.grid]
        for i in range(len(col_pieces) - 3):
            if col_pieces[i:i+4] == winning_set:
                return True

        # Check left diagonal
        l_diag_pieces = []
        l_diag_row = row - min(row, col)
        l_diag_col = col - min(row, col)
        while l_diag_row < len(self.grid) and l_diag_col < len(self.grid[l_diag_row]):
            l_diag_pieces.append(self.grid[l_diag_row][l_diag_col])
            l_diag_row += 1
            l_diag_col += 1
        for i in range(len(l_diag_pieces) - 3):
            if l_diag_pieces[i:i+4] == winning_set:
                return True

        return False


class Game:
    def __init__(self):
        self.board = Board(6, 7)
        self.turn = 'R'
        self.game_over = False

    def display(self):
        print(self.board)

    def take_turn(self, color):
        piece = Piece(color)
        column = int(input(f"{color} turn\nColumn to place (1-7): "))
        row = self.board.place_piece(piece, column)
        if self.board.check_win(color, row, column):
            self.game_over = True


board = Board(6, 7)
red_piece = Piece("Red")
yellow_piece = Piece("Yellow")
board.place_piece(yellow_piece, 4)
board.place_piece(yellow_piece, 4)
board.place_piece(yellow_piece, 4)
board.place_piece(yellow_piece, 5)
board.place_piece(yellow_piece, 5)
board.place_piece(yellow_piece, 6)
board.place_piece(red_piece, 4)
board.place_piece(red_piece, 5)
board.place_piece(red_piece, 6)
board.place_piece(red_piece, 7)
print(board)
print(board.check_win('R', 5, 0))
