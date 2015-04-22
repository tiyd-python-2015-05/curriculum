# Tic Tac Toe

## with Python

---

# Lets create python robots to play a game

---

## RULES

* First to 3 in a row wins
* If neither can make 3 in a row the game is a tie

---

# How?

---

## runner.py

```
python runner.py bot_one.py bot_two.py
```

Runner will open a process and send each programs output to the other.

It is readable with a simple `input()` call since it will be coming from standard input.

The first `input()` passed to your bot will be your team identifier `X` or `O` and the next 3 inputs will be each row of the board.

---

## How to read the board

```py
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
```

---

## Get Creative

This is obviously not the only way to read the board so have fun with it.

---

## Every turn is a black box

Every turn is a new run of the program so you can not track the state of the game. Only how it looks for your current turn.

---

## Making your move

Making your move is as simple as doing a `print()` of your board in your `self.init()`.

In fact if you don't want to take an object oriented approach all you will need to do is somewhere in your program send a `print()` of your board.

---

## [fit]Lets get started
