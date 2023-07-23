class Piece:
    def __init__(self, color):
        if color == "Red":
            self.color = 'R'
        elif color == "Yellow":
            self.color = 'Y'

    def show_icon(self):
        return self.color


class Board:
    def __init__(self, rows, columns):
        self.grid = [['O' for _ in range(columns)] for _ in range(rows)]
        self.rows = rows
        self.columns = columns

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
        col_pieces = [i[col-1] for i in self.grid]
        for i in range(len(col_pieces) - 3):
            if col_pieces[i:i+4] == winning_set:
                return True

        # Check left diagonal
        l_diag_pieces = []
        l_diag_row = row - min(row, col)
        l_diag_col = col - min(row, col) - 1
        while l_diag_row < self.rows and l_diag_col < self.columns:
            l_diag_pieces.append(self.grid[l_diag_row][l_diag_col])
            l_diag_row += 1
            l_diag_col += 1
        for i in range(len(l_diag_pieces) - 3):
            if l_diag_pieces[i:i+4] == winning_set:
                return True

        # Check right diagonal
        r_diag_pieces = []
        distance = min(row, self.columns - col)
        r_diag_row = row - distance
        r_diag_col = col + distance - 1
        while r_diag_row < self.rows and r_diag_col >= 0:
            r_diag_pieces.append(self.grid[r_diag_row][r_diag_col])
            r_diag_row += 1
            r_diag_col -= 1
        for i in range(len(r_diag_pieces) - 3):
            if r_diag_pieces[i:i+4] == winning_set:
                return True

        return False


class Game:
    def __init__(self):
        self.board = Board(6, 7)
        self.game_over = False
        self.winner = ""

    def display(self):
        print(self.board)

    def take_turn(self, color):
        piece = Piece(color)
        column = int(input(f"{color} turn\nColumn to place (1-7): "))
        row = self.board.place_piece(piece, column)
        if self.board.check_win(piece.show_icon(), row, column):
            self.game_over = True
            self.winner = color


def play():
    game = Game()
    is_red_turn = True
    while not game.game_over:
        game.display()
        if is_red_turn:
            game.take_turn("Red")
        else:
            game.take_turn("Yellow")
        is_red_turn = not is_red_turn
    game.display()
    print(f"{game.winner} is the winner!")


play()
