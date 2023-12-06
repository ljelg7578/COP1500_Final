#Prints the board every round.
def show_board(board):
    print('  '+board[0]+'  |  '+board[1]+'  |  '+board[2])
    print('-----------------')
    print('  '+board[3]+'  |  '+board[4]+'  |  '+board[5])
    print('-----------------')
    print('  '+board[6]+'  |  '+board[7]+'  |  '+board[8])
    print('\n')

#Lists out every possible win condition for the players
#and checks if the same mark is in every location.
def has_won(board,mark):
    return ((board[0]==board[1]==board[2]==mark) or  #Top row
            (board[3]==board[4]==board[5]==mark) or  #Center row
            (board[6]==board[7]==board[8]==mark) or  #Bottom row
            (board[0]==board[3]==board[6]==mark) or  #Left Column
            (board[1]==board[4]==board[7]==mark) or  #Center column
            (board[2]==board[5]==board[8]==mark) or  #Right column
            (board[0]==board[4]==board[8]==mark) or  #Left to right diagonal
            (board[2]==board[4]==board[6]==mark))  #Right to left diagonal

#Checks if there are any blank spaces. If not,
#and no one has won, then a draw is called.
def full_board(board):
    return " " not in board


#Produces temporary list copy of the board within Python logic
#to test which is the best move for the unbeatable AI.
def duplicate_board(board):
    duplicate=[]
    for j in board:
        duplicate.append(j)
    return duplicate
#Logic to find a potential winning move for AI.
# Checks each square against winning combinations.
def winning_move(board,mark,i):
    board_copy=duplicate_board(board)
    board_copy[i]=mark
    return has_won(board_copy,mark)
#A checkmate (or fork) is a kind of ideal move in tic-tac-toe
#where a player has two opportunities lined up to win.
#This creates a situation where the other player cannot
#fill both locations, resulting in a win for the bot.
def checkmate(board,mark,i):
    #Checks if a checkmate is possible.
    board_copy=duplicate_board(board)
    board_copy[i]=mark
    forks=0
    for j in range(0,9):
        #Checks if winning move is open.
        if winning_move(board_copy,mark,j) and board_copy[j]==' ':
            forks+=1
    #Activates a fork if there are two or more winning moves available.
    return forks>=2
#Final function called in game that determines
#where the computer should play.
def next_move(board):
    #Checks if computer can make a winning move and plays there.
    for i in range(0,9):
        if board[i]==' ' and winning_move(board,'X',i):
            return i
    #Checks if player can make a winning move and plays there.
    for i in range(0,9):
        if board[i]==' ' and winning_move(board,'0',i):
            return i
    #Checks if computer can checkmate.
    for i in range(0,9):
        if board[i]==' ' and checkmate(board,'X',i):
            return i
    #Checks if player can checkmate with two forks.
    player_forks=0
    for i in range(0,9):
        if board[i]==' ' and checkmate(board,'0',i):
            player_forks+=1
            temporary_move=i
    #If player is about to fork, make that move first.
    if player_forks==1:
        return temporary_move
    #Block the fork.
    elif player_forks==2:
        for j in [1,3,5,7]:
            if board[j]==' ':
                return j
    #Plays the center location if possible.
    if board[4]==' ':
        return 4
    #Plays a corner if possible.
    for i in [0,2,6,8]:
        if board[i]==' ':
            return i
    #Play a side location if possible.
    for i in [1,3,5,7]:
        if board[i]==' ':
            return i


#Game starts.
playing_game=True
while playing_game:
    round=True
    #Board is cleared.
    board=[" "]*9
    #Markers are chosen.
    order=input(('Would you like to go first or second? 1/2: '))
    if order=="1":
        player_marker="0"
    elif order=="2":
        player_marker='X'
    else:
        continue
    show_board(board)

    while round:
        if player_marker=='0':
            #Player makes move.
            move=int(input('Player\'s turn. Enter 0-8: '))
            #Checks for move in full location.
            if board[move]!=' ':
                print('Invalid move. Try again!')
                continue
        else:
            #Computer goes first if they are 0.
            move = next_move(board)
        board[move]=player_marker
        if has_won(board,player_marker):
            #Game is over and displays win.
            round=False
            show_board(board)
            if player_marker=='0':
                print('Noughts wins!')
            else:
                print('Crosses wins!')
            continue
        #Checks if board is full and no one won.
        if full_board(board):
            round=False
            show_board(board)
            print(('It was a draw!\n'))
            continue
        show_board(board)
        #Resets markers at end of game.
        if player_marker=='0':
            player_marker='X'
        else:
            player_marker='0'
    #Asks for rematch.
    answer=input("Would you like to play again? Y/N ")
    if answer.upper() != 'Y':
        playing_game=False