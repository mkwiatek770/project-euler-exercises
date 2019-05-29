import unittest
import sys
sys.path.append("../")
from exercises.exercise_10 import sum_primes_below

class TestExercise10(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(sum_primes_below(bound=10), 17)
        self.assertEqual(sum_primes_below(bound=20), 77)
