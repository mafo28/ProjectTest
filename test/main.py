#create the API
from pydantic import BaseModel
import numpy as np
import pandas as pd

import joblib
from flask import Flask, request, jsonify

modele= joblib.load('random_forest_classifier_modele.pkl')

Class InputData(BaseModel):
    installment: float
    revol.util : float
    revol.bal : float
    fico : float
    purpose_debt_consolidation : float
    
app = Flask(__name__)

@app.route("/", method=["GET"])
def accueil():
    """Fournit un message de bienvenue
    """
    return jsonify({"message": "Bienvenue sur l'API de prediction du remboursement de credit"})

@app.route("/", method=["POST"])
def predire():
    """_summary_
    """
except Exception as e:
    return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8000)
