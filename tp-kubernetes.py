from flask import Flask, jsonify
import os

app = Flask(__name__)

# Lecture des variables d'environnement
port = os.getenv("APP_PORT")
message = os.getenv("MESSAGE")

# Vérifier si les variables d'environnement sont définies
if port is None:
    raise ValueError("Variable d'environnement APP_PORT non définie")
if message is None:
    raise ValueError("Variable d'environnement MESSAGE non définie")

# Route pour retourner le message
@app.route('/')
def get_message():
    return jsonify({"message": message})

# Démarrage du serveur Flask
if __name__ == '__main__':
    print(f"Starting app on port {port}")
    app.run(port=int(port), host="0.0.0.0")
