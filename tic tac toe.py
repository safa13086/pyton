# Tic-Tac-Toe Game

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return " " not in board

def main():
    board = [" "] * 9  # Empty board
    current_player = "X"  # X starts first
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] != " ":
                print("That spot is already taken! Try again.")
                continue
            board[move] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 9.")

if __name__ == "__main__":
    main()
