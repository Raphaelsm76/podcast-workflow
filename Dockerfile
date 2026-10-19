# Image Python ultra-légère
FROM python:3.11-alpine

# Répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances
RUN pip install fastapi uvicorn

# Lancer l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
