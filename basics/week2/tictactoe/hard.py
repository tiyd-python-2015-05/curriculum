
class CliGameUi:

    def get_my_marker(self):
        return input("")

    def get_board(self):
        return [list(input("")) for _ in range(3)]


class Game:

    def __init__(self, ui):
        self.ui = ui
        self.my_marker = self.ui.get_my_marker()
        self.opponent = 'O' if self.my_marker == 'X' else 'X'
        self.board = self.ui.get_board()

    def get_move(self):
        winning_move = self.get_winning_move(self.my_marker)

        if winning_move:
            return winning_move

        defensive_move = self.get_winning_move(self.opponent)

        if defensive_move:
            return defensive_move

        if self.board[1][1] == '_':
            if self.board[0][0] == self.opponent and \
               (self.board[0] + self.board[1] + self.board[2]).count(self.my_marker) == 0:
                return (1, 1)

            if self.board[0][1] == self.opponent == self.board[1][0]:
                return (1, 1)

            if self.board[0][1] == self.opponent == self.board[1][2]:
                return (1, 1)

        if self.board[0][0] == '_':
            return (0, 0)

        if self.board[0][2] == '_':
            return (0, 2)

        if self.board[2][0] == '_':
            return (2, 0)

        if self.board[2][2] == '_':
            return (2, 2)

    def get_winning_move(self, marker):
        h_move = self.get_horizonal_winning_move(marker)
        if h_move:
            return h_move

        v_move = self.get_vertical_winning_move(marker)
        if v_move:
            return v_move

        d_move = self.get_diagonal_winning_move(marker)
        if d_move:
            return d_move

    def get_horizonal_winning_move(self, marker):
        row_to_block = [marker] * 2
        for x in range(3):
            for y in range(3):
                if self.board[x] == row_to_block[0:y] + ['_'] + row_to_block[y:]:
                    return x, y

    def get_vertical_winning_move(self, marker):
        for y in range(3):
            for f, s, b in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
                if self.board[f][y] == marker and self.board[s][y] == marker and self.board[b][y] == '_':
                    return b, y

    def get_diagonal_winning_move(self, marker):
        two_in_a_row = (marker,) * 2
        diagonals = ((0, 0), (0, 2), (2, 0), (2, 2))
        for (tx, ty), (bx, by) in zip(diagonals, reversed(diagonals)):
            if self.board[1][1] == marker and self.board[tx][ty] == marker and self.board[bx][by] == '_':
                return bx, by

        if self.board[1][1] == '_':
            if (self.board[2][0], self.board[0][2]) == two_in_a_row or \
               (self.board[0][0], self.board[2][2]) == two_in_a_row:
                return 1, 1

    def is_game_over(self):
        if self.x_wins() or self.y_wins() or self.is_cat_game():
            return True

    def x_wins(self):
        return self.player_wins('X')

    def y_wins(self):
        return self.player_wins('O')

    def player_wins(self, player):
        if self.column_win(player) or self.row_win(player) or self.diagonal_win(player):
            return True

    def is_cat_game(self):
        cat_game = True
        for row in self.board:
            for cell in row:
                if cell == '_':
                    cat_game = False
        return cat_game

    def column_win(self, player):
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

    def row_win(self, player):
        for row in self.board:
            if [player] * 3 == row:
                return True

    def diagonal_win(self, player):
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True

if __name__ == '__main__':
    g = Game(CliGameUi())
    move = g.get_move()
    print("{} {}".format(*move))
