import unittest
import sys
sys.path.append("../")
from exercises.exercise_6 import find_difference_100_nums

class TestExercise6(unittest.TestCase):

    def test_valid_res(self):
        self.assertEqual(find_difference_100_nums(), 25164150)
