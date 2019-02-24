import os

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
turns = 0


def display_board(board, message):

    print('****************')
    print('* TIC TAC TOE  *')
    print('****************')
    print(' |', board[0], '|', board[1], '|', board[2], '|')
    print(' -------------')
    print(' |', board[3], '|', board[4], '|', board[5], '|')
    print(' -------------')
    print(' |', board[6], '|', board[7], '|', board[8], '|')
    print(' -------------')
    print('****************')
    print(message)


def play_start(board):
    os.system('cls||clear')
    display_board(board, 'Welcome to TIC TAC TOE')
    print(player(board))
    entry = input('Please enter square number 1 - 9 \n')
    try:
        entry = int(entry)
        if entry in range(1, 10) and board[entry-1] == ' ' and isinstance(entry, int):
            board[entry - 1] = player(board)
            print("you chose: ", entry)
    except:
        play_continue(board, "Invalid choice, choose again please.")
    play_continue(board)


def play_continue(board, message=''):
    os.system('cls||clear')
    display_board(board, message)
    print(player(board))
    entry = input('Please enter square number 1 - 9 \n')
    try:
        entry = int(entry)
        if board[entry-1] != ' ':
            play_continue(
                board, "{e} is already taken, choose again please.".format(e=entry))
        elif entry in range(1, 10) and isinstance(entry, int):
            board[entry - 1] = player(board)
            print("you chose: ", entry)
    except:
        play_continue(
            board, "{e} is not a valid choice, choose again please.".format(e=entry))
    play_continue(board)


def player(board):
    turns = sum(list(map(lambda cell: cell != ' ', board)))
    player = 'X' if turns % 2 == 0 else 'O'
    print("Player {p}, it is your turn.".format(p=player))
    return player


play_start(board)
