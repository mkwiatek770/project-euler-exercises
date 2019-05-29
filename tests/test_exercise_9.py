import unittest
import sys
sys.path.append("../")
from exercises.exercise_9 import special_pythagorean_triplet


class TestExercise9(unittest.TestCase):

    def test_valid_result(self):
        self.assertEqual(special_pythagorean_triplet(), 31875000)


