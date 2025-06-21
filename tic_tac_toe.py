import random


def display_board(board: list[str]) -> None:
    """Prints the 3×3 Tic-Tac-Toe board."""
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")


def player_input() -> tuple[str, str]:
    """
    Ask Player 1 to choose X or O.
    Returns a tuple: (Player1_marker, Player2_marker).
    """
    marker = ""
    while marker not in ("X", "O"):
        marker = input("Player 1: Choose X or O: ").upper()
    return (marker, "O" if marker == "X" else "X")


def place_marker(board: list[str], marker: str, position: int) -> None:
    """Place the player’s marker on the board at the given position."""
    board[position] = marker


def win_check(board: list[str], mark: str) -> bool:
    """Return True if the given mark has three in a row."""
    win_patterns = [
        (7, 8, 9),
        (4, 5, 6),
        (1, 2, 3),  # rows
        (7, 4, 1),
        (8, 5, 2),
        (9, 6, 3),  # columns
        (7, 5, 3),
        (9, 5, 1),  # diagonals
    ]
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_patterns)


def space_check(board: list[str], position: int) -> bool:
    """Return True if a given board position is free."""
    return board[position] == " "


def full_board_check(board: list[str]) -> bool:
    """Return True if the board is full."""
    return all(space != " " for space in board[1:])


def player_choice(board: list[str]) -> int:
    """Ask the player for their next move (1–9) and validate it."""
    pos = 0
    while pos not in range(1, 10) or not space_check(board, pos):
        try:
            pos = int(input("Choose your next position (1-9): "))
        except ValueError:
            pos = 0
    return pos


def choose_first() -> str:
    """Randomly choose which player goes first."""
    return "Player 1" if random.choice([True, False]) else "Player 2"


def tic_tac_toe() -> None:
    """Main game loop for playing Tic-Tac-Toe."""
    print("Welcome to Tic-Tac-Toe!")
    board = [" "] * 10
    p1_marker, p2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input("Ready to play? Enter Y or N: ").upper().startswith("Y")
    while play_game:
        print(f"\n>>> {turn}'s turn.")
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_marker(board, p1_marker, position)

            if win_check(board, p1_marker):
                display_board(board)
                print("Congratulations! Player 1 wins!")
                break
            else:
                turn = "Player 2"

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, p2_marker, position)

            if win_check(board, p2_marker):
                display_board(board)
                print("Congratulations! Player 2 wins!")
                break
            else:
                turn = "Player 1"

        if full_board_check(board):
            display_board(board)
            print("The game is a draw!")
            break

    if input("Play again? Enter Y or N: ").upper().startswith("Y"):
        print("\n" * 2)
        tic_tac_toe()


if __name__ == "__main__":
    tic_tac_toe()
