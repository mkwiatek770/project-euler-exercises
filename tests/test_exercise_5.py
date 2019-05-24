import unittest
import sys
sys.path.append("../")
from exercises.exercise_5 import find_smallest_div

class TestExercise5(unittest.TestCase):

    def test_valid_res(self):
        self.assertEqual(find_smallest_div(), 232792560)
