"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of 'X' in the board
    x_count = sum(x.count(X) for x in board)

    # Count the number of 'O' in the board
    o_count = sum(x.count(O) for x in board)

    # Given that 'X' always plays first,
    # if 'X' and 'O' have the same count, it's X's turn
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    # Iterate over the board. If a cell is empty, it's a possible move
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Get a set of available valid actions
    valid_actions = actions(board)

    # Raise an exception if action is not valid
    if action not in valid_actions:
        raise NotValidActionError

    # Create a deep copy of the board
    new_board = deepcopy(board)

    # Update the board with the player's value
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(0, 3):
        # Search in rows
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        # Search in columns
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Search in diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    # No winner
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X, O) or EMPTY not in [column for row in board for column in row]:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    available_actions = {}

    # for action in list(actions(board)):
    #     # print(f'action: {action} \t', end="")
    #
    #     if player(board) == X:
    #         available_actions[action] = max_value(board)
    #     elif player(board) == O:
    #         available_actions[action] = min_value(board)
    #     # else:
    #     #     print(player(board))
    #     #     print(terminal(board))
    #     #
    #     print(available_actions)
    #
    #     print(available_actions.values())

    if player(board) == X:
        max_value(board)
    elif player(board) == O:
        min_value(board)

    print(available_actions)

    print(available_actions.values())


def max_value(board):
    """
    Returns the max-value of the state
    """
    # if terminal(board):
    #     print(f'max board: {board} --- utility: {utility(board)}')
    #     return utility(board)
    v = -100
    for action in list(actions(board)):
        if terminal(result(board, action)):
            print(f'max board: {board} --- utility: {utility(board)}')
            v = max[v, utility(result(board, action))]
        else:
            v = max([v, min_value(result(board, action))])
        print(f'v: {v}')
    print(f'final max v: {v}')
    return v


def min_value(board):
    """
    Returns the min-value of the state
    """
    # if terminal(board):
    #     print(f'min board: {board} --- utility: {utility(board)}')
    #     # print(f'utility: {utility(board)}')
    #     return utility(board)
    v = 100
    # for action in list(actions(board)):
    #     v = min([v, max_value(result(board, action))])
    #     print(f'v: {v}')
    for action in list(actions(board)):
        if terminal(result(board, action)):
            print(f'max board: {board} --- utility: {utility(board)}')
            v = min[v, utility(result(board, action))]
        else:
            v = min([v, max_value(result(board, action))])
        print(f'v: {v}')
    print(f'final min v: {v}')

    return v


class NotValidActionError(Exception):
    """
    A custom Exception class
    """
    pass
