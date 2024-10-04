## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `python manage.py test`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info("oc_lettings_site_profile");`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement du site OC Lettings

### Prérequis

Pour assurer le déploiement et l'intégration continue, voici les prérequis nécessaires :

- Docker installé sur votre machine
- Compte Docker pour accéder aux images sur docker hub
- Compte Github pour le CI/CD
- Compte Azure pour l'hébergement
- Compte Sentry pour le monitoring de l'application

### Description
Une pipeline CI/CD est utilisé pour automatiser le déploiement de l'application. Quand les modifications sont publiées sur le répertoire GitHub, le pipeline installe les dépendances, paramère les variables d'environnement, lance les tests et le linting du code. Ces tâches sont réalisées dans toutes les parties du projet. Si le coverage des tests est inférieur à 80%, la pipeline échouera.

Une image Docker sera créé et sauvegardée sur Docker Hub lorsque des modifications sont apportées à la branche master, et seulement si les tests et le linting sont réussis.

Azure ira récupérer l'image Docker la plus fraiche sur Docker hub via un webhook.

### Publier l'image docker sur Docker Hub
1. Build l'image en local avec la commande. Vous pouvez ajouter un tag pour retrouver l'image facilement.
   `docker build --platform=linux/amd64 .`
2. Push l'image sur Docker hub
    `docker push <nom-du-repo-docker-hub>`

### Utilisation de l'image stockée sur Docker Hub
1. Ouvrez un terminal.
2. Exécutez la commande suivante pour télécharger la dernière image :
   `docker pull claireruysschaert/p13oc:latest`
3. Lancez un conteneur avec l'image téléchargée
   `docker run -p 8080:8080 claireruysschaert/p13oc:latest`
4. Accédez au site sur http://localhost:8000.

### Pipeline CI/CD

La pipeline CI/CD vérifie la qualité du code et automatiser le déploiement. Le pipeline effectue les actions suivantes :

- Linting du code pour vérifier les erreurs de style.
- Exécution des tests unitaires pour vérifier la couverture des tests.
- Construction et push de l'image Docker sur Docker Hub pour chaque commit sur la branche main.

### Déploiement en production avec Azure

1. Configurer les fichiers static avec whitenoise
2. Connectez-vous au portail Azure
3. Créer le plan de service d'application
Dans le portail Azure, cliquez sur « App services », puis sur « create » pour lancer le processus de configuration.
Remplissez les détails requis, tels que le nom, l'abonnement, le groupe de ressources et le système d'exploitation pour le plan. 
Choisissez le niveau de prix minimal. Vérifiez vos paramètres et cliquez sur « Créer » pour provisionner le plan de service App.
4.  Déployer votre application Web
Dans le portail Azure, accédez à l'application Web que vous venez de créer.
Dans le menu de gauche, sélectionnez « Deployment Center ».
Sélectionnez le registre de conteneurs avec ces paramètres pour vous connecter à Docker Hub : 
- Type de conteneur : Conteneur unique
- Source du registre : Docker Hub
- Accès au registre : Public
- Full Image name and Tag : <nom-du-repo-docker-hub>
- URL du webhook -> copier
5. Ajouter un nouveau webhook sur DokerHub
Copier l'URL du webhook de l'application et l'utiliser pour créer un nouveau webhook sur la plateforme Docker Hub.
6. Ajouter des variables d'environnement dans les paramètres de l'application Azure

- SENTRY_DSN : URL du projet Sentry
- SECRET_KEY : Clé secrète du compte Sentry
- DOCKER_PASSWORD : Mot de passe du compte Docker
- DOCKER_USERNAME : Nom d'utilisateur du compte Docker
- DEBUG : Option de settings pour le déploiement 

5. Le déploiement se lance automatique et le site est disponible sur le lien affiché dans "Overview".
