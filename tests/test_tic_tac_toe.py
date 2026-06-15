import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from tic_tac_toe import check_winner, is_valid_move

def test_check_winner():
    # Test horizontal win
    board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert check_winner(board) == 'X'
    
    # Test vertical win
    board = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
    assert check_winner(board) == 'O'
    
    # Test diagonal win
    board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
    assert check_winner(board) == 'X'
    
    # Test tie
    board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
    assert check_winner(board) == 'Tie'
    
    # Test ongoing game
    board = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    assert check_winner(board) is None

def test_is_valid_move():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    # Valid moves
    assert is_valid_move(board, 0, 0) == True
    assert is_valid_move(board, 2, 2) == True
    
    # Invalid moves
    board[0][0] = 'X'
    assert is_valid_move(board, 0, 0) == False
    assert is_valid_move(board, 3, 3) == False
    assert is_valid_move(board, -1, 0) == False

if __name__ == "__main__":
    test_check_winner()
    test_is_valid_move()
    print("All tests passed!")