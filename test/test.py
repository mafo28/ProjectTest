import unittest
import pickle
import pandas as pd

class TestModel(unittest.TestCase):
    def setUp(self):
        with open('../random_forest_model.pkl', 'rb') as file:
            self.model = pickle.load(file)
    
    def test_prediction(self):
        data = {'feature1': [value1], 'feature2': [value2], ...}  # Remplacez par vos features
        df = pd.DataFrame(data)
        prediction = self.model.predict(df)
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()
