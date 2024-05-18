import requests

data = [
    {'feature1': value1, 'feature2': value2, ...},  # Remplacez par vos features
    ...
]

response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())
