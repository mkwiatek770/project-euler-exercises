import unittest
import sys
sys.path.append("..")
from exercises.exercise_14 import find_highest_colatz

class TestExercise14(unittest.TestCase):
    
    def test_valid_score(self):
        self.assertEqual(find_highest_colatz(14), 9)
