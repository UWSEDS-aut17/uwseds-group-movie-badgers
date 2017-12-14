import unittest
import pandas as pd
import sklearn
import sys
sys.path.append('../')
import regression_model as rm  # noqa


TEST_DATA = pd.read_csv("./df_example.csv")
MODEL_NAME_1 = "linear"
MODEL_NAME_2 = "lasso"
MODEL_NAME_3 = "ridge"
MODEL_NAME_4 = "tree"
MODEL_NAME_5 = "random forest"
FOLD_NUM = 10
NEW_MODEL = "lrm"
PATH = "saved_model.pkl"


class ModelTest(unittest.TestCase):

    def test_smoke(self):
        rm.model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        rm.model_evaluation(MODEL_NAME_2, TEST_DATA, FOLD_NUM)
        rm.model_evaluation(MODEL_NAME_3, TEST_DATA, FOLD_NUM)
        rm.model_evaluation(MODEL_NAME_4, TEST_DATA, FOLD_NUM)
        rm.model_evaluation(MODEL_NAME_5, TEST_DATA, FOLD_NUM)
        model_1 = rm.model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        rm.save_model(model_1, NEW_MODEL, PATH)

    def test_one_shot(self):
        model = rm.model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        self.assertTrue(isinstance(model,
                                   sklearn.linear_model.base.LinearRegression))
        model = rm.model_evaluation(MODEL_NAME_2, TEST_DATA, FOLD_NUM)
        self.assertTrue(isinstance(model,
                                   sklearn.linear_model.
                                   coordinate_descent.Lasso))
        model = rm.model_evaluation(MODEL_NAME_3, TEST_DATA, FOLD_NUM)
        self.assertTrue(isinstance(model,
                                   sklearn.linear_model.ridge.Ridge))
        model = rm.model_evaluation(MODEL_NAME_4, TEST_DATA, FOLD_NUM)
        self.assertTrue(isinstance(model,
                                   sklearn.tree.tree.DecisionTreeRegressor))
        self.assertRaises(NameError,
                          model_evaluation(MODEL_NAME_5, TEST_DATA, FOLD_NUM))
        model_1 = rm.model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        self.assertEquals(rm.save_model(model_1, NEW_MODEL, PATH),
                          "model save complete!")
