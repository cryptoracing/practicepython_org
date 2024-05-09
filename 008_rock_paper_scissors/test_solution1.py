import unittest
from solution1 import determine_winner

class TestGame(unittest.TestCase):

    def test_rock_vs_scissors(self):
        result = determine_winner('rock', 'scissors')
        self.assertEqual(result, "You win!")

    def test_paper_vs_rock(self):
        result = determine_winner('paper', 'rock')
        self.assertEqual(result, "You win!")

    def test_scissors_vs_paper(self):
        result = determine_winner('scissors', 'paper')
        self.assertEqual(result, "You win!")

    def test_tie(self):
        result = determine_winner('rock', 'rock')
        self.assertEqual(result, "It's a tie!")

if __name__ == '__main__':
    unittest.main()
