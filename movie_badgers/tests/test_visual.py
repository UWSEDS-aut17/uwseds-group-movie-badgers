import unittest
import sys
import os
sys.path.append("..//")
from movie_plot import *   # noqa

path = os.getcwd()
input1 = "revenue"
input2 = "budget"
input3 = "imdb_votes"
input4 = "released_on_dump_month"
input5 = "blabla"
x = "Invalid Input. Check Docstring."


class VisualTest(unittest.TestCase):

    def test_smoke(self):
        scatter_plot(path, input2, input1)
        scatter_plot(path, input2, input3)
        box_plot(path, input4)

    def test_one_shot(self):
        self.assertEqual(scatter_plot(path, input2, input1), 1)
        self.assertEqual(box_plot(path, input4), 1)

    def test_exception(self):
        self.assertEqual(scatter_plot(path, input2, input5), x)
        self.assertEqual(box_plot(path, input5), x)
