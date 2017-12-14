import sys
import unittest
import os
sys.path.append('../')
import clean_data as cd   # noqa

path = ('../data/data_raw_user.csv')
input_path = ('../data/data_clean.csv')
output_path = ('../data/data_for_lr.csv')


class FunctionRunTest(unittest.TestCase):
    """Test if functions run succesfully with correct input"""

    def test_smoke(self):
        cd.clean_director_actor(path)
        cd.clean_regression_data(input_path, output_path)

    def test_one_shot(self):
        df_add_act_dir = cd.clean_director_actor(path)
        self.assertEqual(df_add_act_dir.shape, (20, 20))
        df_for_model = cd.clean_regression_data(input_path, output_path)
        self.assertEqual(df_for_model.shape, (2367, 29))
