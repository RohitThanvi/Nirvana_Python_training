"""Tic Tac Toe game"""


def player_markers():
    """Takes Input from the User for there Marker"""
    while True:
        p1 = input("""Player1 Choose your Marker "X" or "O" """)
        if p1.upper() == "X":
            return "x", "O"
        elif p1.upper() == "O":
            return "O", "X"


def print_board(board):

    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")


def check_valid_pos(board, pos):
    # a = board[pos]
    if board[pos] not in ["X", "O"]:
        return True

    return False


def player_input(board, turn, marker):
    """Takes player input for there marker position"""
    valid = False
    while not valid:
        print(f"Player {turn} has to mark")
        pos = int(input("Enter a number between 1-9 "))
        valid = check_valid_pos(board, pos)
        if valid:
            board[pos] = marker.get(turn)
    print_board(board)
    return board, turn


def check_winner(board, turn, marker):
    win_cond = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    for a, b, c in win_cond:
        if board[a] == board [b] == board[c] == marker.get(turn):
            return True, turn
    
    return False, turn
    
    # if any(board[a] == board[b] == board[c] == marker.get(turn) for a, b, c in win_cond)

def draw(board):
    return all(str(x).upper() in ["X", "O"] for x in board[1:])

def tic_tac_toe():
    # board = [" "] * 10
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1, p2 = player_markers()
    marker = {"p1": p1, "p2": p2}
    turn = "p1"
    if p2 == "X":
        turn = "p2"
    while True:
        os.system('cls')
        print_board(board)

        board, turn = player_input(board, turn, marker)

        win, turn = check_winner(board, turn, marker)
        if win:
            print(f"{turn} is winner")
            break
        if draw(board):
            print("Game Draw")
            break
        
        if turn == "p1":
            turn = "p2"
        else:
            turn = "p1"
    
    


if __name__ == "__main__":
    """Here Program starts"""
    print("Welcome Players to Tic Tac Toe")
    tic_tac_toe()

    """File handling"""

    # f = open("demo.txt", "w"). # without context manager

    # f.write("hello world")

    # f.close()
    
    # with context manager
    
    # with open("demo.txt", "w") as f:
    #     # print(f.read())
    #     f.write("/n hello this is Hridesh")

