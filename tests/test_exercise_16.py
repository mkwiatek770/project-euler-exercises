from unittest import TestCase
import sys
sys.path.append("..")
from exercises.exercise_16 import power_digit_sum

class TestExercise16(TestCase):

    def test_valid_score(self):
        self.assertEqual(power_digit_sum(2, 15), 26)
