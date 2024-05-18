import unittest
import json
from flask import Flask
from flask.testing import FlaskClient

# Importer l'application Flask
from main import app, InputData

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Configurer l'application pour le test
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_accueil(self):
        # Test de la route d'accueil
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Bienvenue sur l\'API de prediction du remboursement de credit')

    def test_predire_valid(self):
        # Test de la route de prédiction avec des données valides
        valid_data = {
            "installment": 250.0,
            "revol_util": 45.0,
            "revol_bal": 5000.0,
            "fico": 700.0,
            "purpose_debt_consolidation": 1.0
        }
        response = self.client.post('/', json=valid_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('prediction', data)

    def test_predire_invalid(self):
        # Test de la route de prédiction avec des données invalides
        invalid_data = {
            "installment": "invalid_data",  # Installment devrait être un float
            "revol_util": 45.0,
            "revol_bal": 5000.0,
            "fico": 700.0,
            "purpose_debt_consolidation": 1.0
        }
        response = self.client.post('/', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()

