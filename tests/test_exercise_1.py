import unittest
import sys
sys.path.append("../")
from exercises.exercise_1 import find_sum_of_multiples


class TestExercise1(unittest.TestCase):

    def test_valid_score(self):
        self.assertEqual(find_sum_of_multiples(), 233168)

