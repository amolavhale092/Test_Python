import unittest
from Minigame import RPSGame

class DummyRoot:
    """A dummy Tkinter root for testing logic without GUI."""
    def __init__(self):
        self.title_called = False
    def title(self, _):
        self.title_called = True
    def update(self):
        pass
    def after(self, ms, func):
        func()

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.root = DummyRoot()
        self.game = RPSGame(self.root)

    def test_initial_scores(self):
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_determine_winner_draw(self):
        self.assertEqual(self.game.determine_winner('Rock', 'Rock'), 'draw')
        self.assertEqual(self.game.determine_winner('Paper', 'Paper'), 'draw')
        self.assertEqual(self.game.determine_winner('Scissors', 'Scissors'), 'draw')

    def test_determine_winner_player_win(self):
        self.assertEqual(self.game.determine_winner('Rock', 'Scissors'), 'win')
        self.assertEqual(self.game.determine_winner('Paper', 'Rock'), 'win')
        self.assertEqual(self.game.determine_winner('Scissors', 'Paper'), 'win')

    def test_determine_winner_player_lose(self):
        self.assertEqual(self.game.determine_winner('Rock', 'Paper'), 'lose')
        self.assertEqual(self.game.determine_winner('Paper', 'Scissors'), 'lose')
        self.assertEqual(self.game.determine_winner('Scissors', 'Rock'), 'lose')

    def test_score_update_on_win(self):
        self.game.show_result('Rock', 'Scissors')
        self.assertEqual(self.game.player_score, 1)
        self.assertEqual(self.game.computer_score, 0)

    def test_score_update_on_lose(self):
        self.game.show_result('Rock', 'Paper')
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 1)

    def test_score_update_on_draw(self):
        self.game.show_result('Rock', 'Rock')
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_reset_game(self):
        self.game.player_score = 2
        self.game.computer_score = 1
        self.game.reset_game()
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 0)

if __name__ == "__main__":
    unittest.main()