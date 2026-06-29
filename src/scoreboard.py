"""Tracks wins. Also depends on src.board."""

from .board import check_winner


class Scoreboard:
    def __init__(self):
        self.wins = {'X': 0, 'O': 0, 'Tie': 0}

    def record(self, board):
        result = check_winner(board)
        if result is not None:
            self.wins[result] += 1
        return result