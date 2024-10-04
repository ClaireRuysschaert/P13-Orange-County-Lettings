Installation
============

- Clonez ce dépôt de code à l'aide de la commande 
  ``$ git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`` 

- Créer l'environnement virtuel à la racine du répertoire 
  ``$ python -m venv env`` sous Windows
  ``$ python3 -m venv env`` sous MacOS ou Linux.

- Activez l'environnement virtuel avec 
  ``$ env\Scripts\activate`` sous Windows
  ``$ source env/bin/activate`` sous MacOS ou Linux.

- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`

- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`

- Pour désactiver l'environnement, `deactivate`

- Installez les dépendances du projet avec la commande 
  ``$ pip install -r requirements.txt``.
 
Vous pouvez maintenant lancer le serveur de développement avec la commande 
``$ python manage.py runserver``.

Le site sera accessible à l'adresse `http://localhost:8000 <http://localhost:8000>`_