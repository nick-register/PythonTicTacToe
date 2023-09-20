import random

print("Let's play Tic-Tac-Toe")

numbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
columns = 3

def printBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(columns):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")

def modifyBoard(num, turn):
    num -= 1
    if(num == 0):
        board[0][0] = turn
    elif(num == 1):
        board[0][1] = turn
    elif(num == 2):
        board[0][2] = turn
    elif(num == 3):
        board[1][0] = turn
    elif(num == 4):
        board[1][1] = turn
    elif(num == 5):
        board[1][2] = turn
    elif(num == 6):
        board[2][0] = turn
    elif(num == 7):
        board[2][1] = turn
    elif(num == 8):
        board[2][2] = turn

def checkWin(board):
    ### X
    if(board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
        print("O wins!")
        return "O"
    elif(board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"):
        print("X wins!")
        return "X"
    elif(board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        print("O wins!")
        return "O"
    elif(board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        print("X wins!")
        return "X"
    elif(board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        print("O wins!")
        return "O"
    ### Y
    elif(board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        print("O wins!")
        return "O"
    elif(board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        print("O wins!")
        return "O"
    elif(board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        print("O wins!")
        return "O"
    ### Cross
    elif(board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        print("O wins!")
        return "O"
    elif(board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print("X wins!")
        return "X"
    elif(board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print("O wins!")
        return "O"
    else:
        return 'N'
        print("TIE!")

leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  ### It's the player turn
  if(turnCounter % 2 == 0):
    printBoard()
    numberPicked = int(input("\nChoose a number [1-9]: "))
    if(numberPicked >= 1 and numberPicked <= 9):
      modifyBoard(numberPicked, 'X')
      numbers.remove(numberPicked)
      winner = checkWin(board)
      if(winner != "N"):
        print("\nGame Over!")
        break
    else:
      print("Invalid input. Please try again.")
    turnCounter += 1
  ### It's the computer's turn
  else:
    while(True):
      cpuChoice = random.choice(numbers)
      print("\nCpu choice: ", cpuChoice)
      if(cpuChoice in numbers):
        modifyBoard(cpuChoice, 'O')
        numbers.remove(cpuChoice)
        winner = checkWin(board)
        if(winner != "N"):
            print("\nGame Over!")
            break
        turnCounter += 1
        break


