import unittest
import sys
sys.path.append("../")
from exercises.exercise_3 import largest_prime_factor

class TestExercise3(unittest.TestCase):

    def test_valid_result(self):
        self.assertEqual(largest_prime_factor(), 6857)
