import unittest
import sys
import datetime
sys.path.append("..")
from exercises.exercise_19 import number_of_first_sundays

class TestExercise(unittest.TestCase):

    def test_exercise_19_valid(self):
        result = number_of_first_sundays()

        self.assertEqual(result, 171)
    
    def test_exercise_19_valid_for_custom_range(self):
        from_date = datetime.datetime(2020, 1, 1)
        to_date = datetime.datetime(2020, 12, 31)

        result = number_of_first_sundays(from_date, to_date)

        self.assertEqual(result, 2)
