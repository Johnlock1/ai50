import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

a = (1, 1)
b = (2, 0)

board = ttt.initial_state()
board = [[O, X, O],
         [X, EMPTY, X],
         [X, EMPTY, O]]

# board = [[EMPTY, EMPTY, EMPTY],
#          [EMPTY, EMPTY, EMPTY],
#          [EMPTY, EMPTY, EMPTY]]


# print(ttt.actions(board))
#
# new_board = ttt.result(board, a)
# print(new_board)
#
# new_board = ttt.result(new_board, b)
# print(new_board)


print(ttt.player(board))
print(ttt.minimax(board))
# print(ttt.winner(board))
# print(ttt.terminal(board))
# print(ttt.utility(board))
