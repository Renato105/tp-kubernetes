# Utilisez une image de base légère
FROM python:3.8-alpine

# Définissez le répertoire de travail
WORKDIR /app

# Copiez le script Python dans le conteneur
COPY tp-kubernetes.py .

# Installez les dépendances Python si nécessaire
# (si votre script a des dépendances externes)
# RUN pip install -r requirements.txt
RUN pip install flask

# Définissez les variables d'environnement
ENV APP_PORT=5555 \
    MESSAGE="Hello World!"

# Exposez le port sur lequel le service s'exécute
EXPOSE 5555

# Commande pour exécuter le script Python
CMD ["python", "tp-kubernetes.py"]
