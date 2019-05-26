import unittest
import sys
sys.path.append("../")
from exercises.exercise_7 import find_nth_prime

class TestExercise7(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(find_nth_prime(1), 2)
        self.assertEqual(find_nth_prime(6), 13)
