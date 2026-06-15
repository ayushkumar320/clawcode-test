"""
A simple Tic-Tac-Toe game implementation in Python.
"""

def print_board(board):
    """Print the current state of the board."""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(board):
    """Check if there's a winner or if the game is a tie."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # Check for tie
    for row in board:
        if ' ' in row:
            return None  # Game continues
    
    return 'Tie'  # All spaces filled with no winner

def is_valid_move(board, row, col):
    """Check if the move is valid."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def main():
    """Main game function."""
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter row and column numbers (0-2) separated by space.")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            # Get player input
            move = input("Enter your move (row col): ").split()
            if len(move) != 2:
                print("Please enter exactly two numbers separated by space.")
                continue
                
            row, col = int(move[0]), int(move[1])
            
            # Validate move
            if not is_valid_move(board, row, col):
                print("Invalid move! Try again.")
                continue
            
            # Make move
            board[row][col] = current_player
            
            # Check game status
            result = check_winner(board)
            if result:
                print_board(board)
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {result} wins!")
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Please enter valid integers.")
        except KeyboardInterrupt:
            print("\nGame interrupted.")
            break

if __name__ == "__main__":
    main()