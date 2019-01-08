import random


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player : Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

board=[' ']*10

def display_board(board):
    print('   ' + '|' + '    ' + '|' + '   ')
    print(board[7],' |',board[8],' |',board[9])
    print('   '+'|'+'    '+'|'+'   ')
    print('-' *12)
    print('   ' + '|' + '    ' + '|' + '   ')
    print(board[4], ' |', board[5], ' |', board[6])
    print('   ' + '|' + '    ' + '|' + '   ')
    print('-' * 12)
    print('   ' + '|' + '    ' + '|' + '   ')
    print(board[1], ' |', board[2], ' |', board[3])
    print('   ' + '|' + '    ' + '|' + '   ')


def placing(board,mark,position):
    board[position]= mark

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        print("Player 2 moves first")
        return 'Player 2'
    else:
        print("Player 1 moves first")
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for n in range(1,10):
        if space_check(board,n):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
   print("Welcome To Tic Tac Toe")
   display_board(board)
   turn = choose_first()
   player1_marker, player2_marker = player_input()
   game_on = True
   while game_on:
       if turn == "Player 1":
            display_board(board)
            position =player_choice(board)
            placing(board,player1_marker,position)

            if win_check(board,player1_marker):
                print("Congatulations you have won!")
                game_on = False
                break
            else:
                if full_board_check(board):
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'
       else:
           display_board(board)
           position = player_choice(board)
           placing(board, player2_marker, position)

           if win_check(board, player2_marker):
                print("Congatulations you have won!")
                game_on = False
                break
           else:
                if full_board_check(board):
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'













