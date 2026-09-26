import random

board=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

moves=0

while True:
    print()
    print(board[0])
    print(board[1])
    print(board[2])

    n=int(input("Choose a position (1-9): "))

    r=(n-1)//3
    c=(n-1)%3

    if board[r][c]!=" ":
        print("Already taken!")
        continue

    board[r][c]="X"
    moves+=1

    if any(row==["X","X","X"] for row in board):
        print("You win!")
        break

    won=False

    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]=="X":
            won=True

    if won:
        print("You win!")
        break

    if (board[0][0]==board[1][1]==board[2][2]=="X" or
        board[0][2]==board[1][1]==board[2][0]=="X"):
        print("You win!")
        break

    if moves==9:
        print("Draw!")
        break

    while True:
        n=random.randint(1,9)

        r=(n-1)//3
        c=(n-1)%3

        if board[r][c]==" ":
            board[r][c]="O"
            moves+=1
            break

    if any(row==["O","O","O"] for row in board):
        print(board[0])
        print(board[1])
        print(board[2])
        print("Bot wins!")
        break

    bot_won=False

    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]=="O":
            bot_won=True

    if bot_won:
        print(board[0])
        print(board[1])
        print(board[2])
        print("Bot wins!")
        break

    if (board[0][0]==board[1][1]==board[2][2]=="O" or
        board[0][2]==board[1][1]==board[2][0]=="O"):
        print(board[0])
        print(board[1])
        print(board[2])
        print("Bot wins!")
        break

    if moves==9:
        print(board[0])
        print(board[1])
        print(board[2])
        print("Draw!")
        break
