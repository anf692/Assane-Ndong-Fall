# Portfolio Assane — Django + Bootstrap

## Installation rapide

```bash
# 1. Installer Django
pip install -r requirements.txt

# 2. Lancer les migrations (base de données)
python manage.py migrate

# 3. Lancer le serveur
python manage.py runserver
```

## Ouvrir dans le navigateur
http://127.0.0.1:8000/

## Personnaliser ton portfolio
Toutes tes infos sont dans le fichier : `main/views.py`
- Nom, titre, description
- Liste de projets
- Technologies
- Formations et certifications
- Liens sociaux (email, LinkedIn, GitHub, WhatsApp)

## Ajouter ta photo
1. Copie ta photo dans `main/static/img/photo.jpg`
2. Dans `main/templates/main/index.html`, trouve le commentaire :
   `<!-- Remplace par : <img src... -->`
3. Décommente cette ligne et supprime l'icône au-dessus

## Déploiement (plus tard)
- Change `DEBUG = False` dans `config/settings.py`
- Configure `ALLOWED_HOSTS` avec ton domaine
- Utilise WhiteNoise pour les fichiers statiques
