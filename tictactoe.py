board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9", ]

isGameGoingOn = True

winner = None

x = 0

currentPlayer = input("Play with what? Choose X or O:")


def displayBoard():
    print(board[0], " | ", board[1], " | ", board[2])
    print(board[3], " | ", board[4], " | ", board[5])
    print(board[6], " | ", board[7], " | ", board[8])


def chakkiOrSuna(xoro):
    global currentPlayer
    choice = input("choose a no. from 1 to 9:")
    currentPlayer = xoro
    board[int(choice) - 1] = currentPlayer

    displayBoard()


def checkIfWinOrTie():
    global isGameGoingOn
    global winner
    # Checking rows
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    # Checking cols
    col1 = board[0] == board[3] == board[6] != "_"  # 036
    col2 = board[1] == board[4] == board[7] != "_"  # 147
    col3 = board[2] == board[5] == board[8] != "_"  # 258
    # Checking diags
    diag1 = board[0] == board[4] == board[8] != "_"  # 048
    diag2 = board[2] == board[4] == board[6] != "_"  # 246

    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        isGameGoingOn = False

    if row1:
        winner = board[0]

    elif row2:
        winner = board[3]

    elif row3:
        winner = board[6]

    elif col1:
        winner = board[0]

    elif col2:
        winner = board[1]

    elif col3:
        winner = board[2]

    elif diag1:
        winner = board[0]

    elif diag2:
        winner = board[2]
    else:
        winner = None

    return


def playGame():
    global currentPlayer, isGameGoingOn
    global x
    displayBoard()
    while isGameGoingOn:
        chakkiOrSuna(currentPlayer)
        x += 1
        checkIfWinOrTie()
        if currentPlayer == 'X':
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'

        if x == 9:
            isGameGoingOn = False

    if winner == 'X' or winner == 'O':
        print("WINNER IS " + str(winner))
    elif winner is None:
        print("TIE GAME")


playGame()
