import random


class TicTaco:

    empty_board = ["___", "___", "___"]

    def __init__(self):
        self.get_inputs()
        if self.board == self.empty_board:
            print(self.first_move())
        else:
            print(self.next_move())

    def get_inputs(self):
        self.me = input()
        if self.me == "X":
            self.you = "O"
        else:
            self.you = "X"
        row_one = input()
        row_two = input()
        row_three = input()
        self.board = self.create_board(row_one, row_two, row_three)

    def create_board(self, row_one, row_two, row_three):
        return [row_one, row_two, row_three]

    def first_move(self):
        possible_moves = ["0 0", "0 2", "2 0", "2 2"]
        return possible_moves[random.randrange(0, 4)]

    def next_move(self):
        x, z = self.make_best_move()
        move = self.illegal_move(x, z)
        while move:
            x, z = self.make_best_move()
            move = self.illegal_move(x, z)
        return "{} {}".format(x, z)

    def illegal_move(self, x, z):
        if self.board[x][z] == "_":
            return False
        return True

    def make_best_move(self,):
        if self.winning_move():
            return self.winning_move()
        x = random.randrange(0, 3)
        z = random.randrange(0, 3)
        return x, z

    def winning_move(self):
        if self.horizontal_win():
            return self.horizontal_win()
        else:
            return self.vertical_win()

    def horizontal_win(self):
        win = [("2", "{}{}_".format(self.me, self.me)),
               ("0", "_{}{}".format(self.me, self.me)),
               (1, "{}_{}".format(self.me, self.me))]
        for idx, row in enumerate(self.board):
            if row == win[idx][1]:
                return int(idx), int(win[idx][0])

    def vertical_win(self):
        win = [("2", "{}{}_".format(self.me, self.me)),
               ("0", "_{}{}".format(self.me, self.me)),
               (1, "{}_{}".format(self.me, self.me))]
        tmp_board = []
        col = ""
        for col_idx, column in enumerate(self.board):
            for row_idx, row in enumerate(self.board):
                col += self.board[row_idx][col_idx]
            tmp_board.append(col)
            col = ""

        for idx, row in enumerate(tmp_board):
            if row == win[idx][1]:
                return int(win[idx][0]), int(idx)


if __name__ == '__main__':
    TicTaco()
