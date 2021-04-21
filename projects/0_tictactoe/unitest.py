import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

boards = [
    [[EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY]],

    [[O, X, O],
     [X, EMPTY, X],
     [X, O, X]],

    [[O, X, O],
     [X, O, X],
     [X, O, O]],

    [[X, X, O],
     [X, O, X],
     [X, O, EMPTY]],
]


for board in boards:
    print('Board:')
    for row in board:
        print(row)
    print(f'winner: {ttt.winner(board)} - terminal: {ttt.terminal(board)}\n')
