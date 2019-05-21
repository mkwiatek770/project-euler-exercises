import unittest
import sys
sys.path.append("../")
from exercises.exercise_2 import sum_even_in_fib

class TestExercise2(unittest.TestCase):

    def test_correct_value(self):
        self.assertEqual(sum_even_in_fib(), 4613732)
