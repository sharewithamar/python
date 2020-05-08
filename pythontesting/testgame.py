import unittest
import guessgame


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = guessgame.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 0
        result = guessgame.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 12
        result = guessgame.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number2(self):
        answer = '5'
        guess = 12
        result = guessgame.run_guess(guess, answer)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
