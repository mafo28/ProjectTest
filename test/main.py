#create the API
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify

# Charger le modèle
modele = joblib.load('random_forest_model.pkl')

# Définir la structure des données d'entrée avec Pydantic
class InputData(BaseModel):
    installment: float
    revol_util: float
    revol_bal: float
    fico: float
    purpose_debt_consolidation: float

app = Flask(__name__)

@app.route("/", methods=["GET"])
def accueil():
    """Fournit un message de bienvenue."""
    return jsonify({"message": "Bienvenue sur l'API de prediction du remboursement de credit"})

@app.route("/", methods=["POST"])
def predire():
    """Prédire si un patient a remboursé son crédit."""
    try:
        # Valider les données d'entrée
        data = request.get_json()
        input_data = InputData(**data)

        # Convertir les données en DataFrame pour le modèle
        df = pd.DataFrame([input_data.dict()])

        # Faire la prédiction
        prediction = modele.predict(df)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8000)

