import unittest
import sys
sys.path.append("../")
from exercises.exercise_4 import find_largest_palindrome_product

class TestExercise4(unittest.TestCase):

    def test_valid_score(self):
        self.assertEqual(find_largest_palindrome_product(), 906609)
