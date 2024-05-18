import requests
import json

# URL de base de l'API (changez localhost:8000 si vous déployez ailleurs)
BASE_URL = 'http://localhost:8000/'

def test_accueil():
    """Test de la route d'accueil"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert data['message'] == 'Bienvenue sur l\'API de prediction du remboursement de credit'
    print('test_accueil passed.')

def test_predire_valid():
    """Test de la route de prédiction avec des données valides"""
    valid_data = {
        "installment": 250.0,
        "revol_util": 45.0,
        "revol_bal": 5000.0,
        "fico": 700.0,
        "purpose_debt_consolidation": 1.0
    }
    response = requests.post(BASE_URL, json=valid_data)
    assert response.status_code == 200
    data = response.json()
    assert 'prediction' in data
    print('test_predire_valid passed.')

def test_predire_invalid():
    """Test de la route de prédiction avec des données invalides"""
    invalid_data = {
        "installment": "invalid_data",  # Installment devrait être un float
        "revol_util": 45.0,
        "revol_bal": 5000.0,
        "fico": 700.0,
        "purpose_debt_consolidation": 1.0
    }
    response = requests.post(BASE_URL, json=invalid_data)
    assert response.status_code == 400
    data = response.json()
    assert 'error' in data
    print('test_predire_invalid passed.')

if __name__ == '__main__':
    test_accueil()
    test_predire_valid()
    test_predire_invalid()
