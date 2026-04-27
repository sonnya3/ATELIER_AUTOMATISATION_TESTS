from flask import Flask, render_template, render_template_string, jsonify, request, redirect, url_for, session, json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3
import os

# Import de ta logique de test (Séquence 4)
try:
    from tester.runner import run_all_tests
except ImportError:
    # Sécurité au cas où les fichiers ne sont pas encore déployés
    def run_all_tests():
        return {"status": "Erreur d'importation des fichiers de test"}

app = Flask(__name__)

# --- Tes routes existantes ---

@app.get("/")
def consignes():
    return render_template('consignes.html')

# --- Nouvelle route pour ton Dashboard QA ---

@app.get("/dashboard")
def dashboard():
    # Cette fonction appelle la logique située dans tester/runner.py
    report = run_all_tests()
    return render_template('dashboard.html', report=report)

# --- Conservation de la logique locale ---

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
