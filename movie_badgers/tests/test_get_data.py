import sys
import unittest
import os
sys.path.append('../')
import get_data as gd   # noqa

path = ('../data/data_raw_user.csv')


class FunctionRunTest(unittest.TestCase):
    """Test if functions run succesfully with correct input"""

    def test_smoke(self):
        gd.get_tmdb_id_list(2011, 2012, 1, 2)
        gd.get_profit(2011, 2012, 1, 2)
        gd.get_info(2011, 2012, 1, 2)
        gd.call_data(2011, 2012, 1, 2, path)

    def test_one_shot(self):
        id_list = gd.get_tmdb_id_list(2011, 2012, 1, 2)
        self.assertEqual(len(id_list), 20)
        df_profit = gd.get_profit(2011, 2012, 1, 2)
        self.assertEqual(df_profit.shape, (20, 3))
        df_info = gd.get_info(2011, 2012, 1, 2)
        self.assertEqual(df_info.shape, (20, 14))
        df_combined = gd.call_data(2011, 2012, 1, 2, path)
        self.assertEqual(df_combined.shape, (20, 18))
