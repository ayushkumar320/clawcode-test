"""Tic-Tac-Toe entrypoint. Depends on src.board."""

from .board import empty_board, print_board, check_winner, is_valid_move


def main():
    board = empty_board()
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe!")
    print("Enter row and column numbers (0-2) separated by space.")
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        try:
            move = input("Enter your move (row col): ").split()
            if len(move) != 2:
                print("Please enter exactly two numbers separated by space.")
                continue
            row, col = int(move[0]), int(move[1])
            if not is_valid_move(board, row, col):
                print("Invalid move! Try again.")
                continue
            board[row][col] = current_player
            result = check_winner(board)
            if result:
                print_board(board)
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {result} wins!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Please enter valid integers.")
        except KeyboardInterrupt:
            print("\nGame interrupted.")
            break


if __name__ == "__main__":
    main()