Déploiement et gestion de l'application
=======================================
Déploiement
-----------

Une pipeline CI/CD est utilisé pour automatiser le déploiement de l'application. 
Quand les modifications sont publiées sur le répertoire GitHub, le pipeline installe
les dépendances, paramère les variables d'environnement, lance les tests et le linting
du code. Ces tâches sont réalisées dans toutes les parties du projet. Si le coverage des
tests est inférieur à 80%, la pipeline échouera.

Une image Docker sera créé et sauvegardée sur Docker Hub lorsque des modifications sont
apportées à la branche master, et seulement si les tests et le linting sont réussis.

Azure ira récupérer l'image Docker la plus fraiche sur Docker hub via un webhook.

La pipeline CI/CD vérifie la qualité du code et automatiser le déploiement. Le pipeline effectue les actions suivantes :

- Linting du code pour vérifier les erreurs de style.
- Exécution des tests unitaires pour vérifier la couverture des tests.
- Construction et push de l'image Docker sur Docker Hub pour chaque commit sur la branche main.

Pré-requis
++++++++++

Pour assurer le déploiement et l'intégration continue, voici les prérequis nécessaires :

- Docker installé sur votre machine
- Compte Docker pour accéder aux images sur docker hub
- Compte Github pour le CI/CD
- Compte Azure pour l'hébergement
- Compte Sentry pour le monitoring de l'application

Publier l'image docker sur Docker Hub
++++++++++++++++++++++++++++++++++++++

1. Build l'image en local avec la commande. Vous pouvez ajouter un tag pour retrouver l'image facilement.
   ``docker build --platform=linux/amd64 .``
2. Push l'image sur Docker hub
    ``docker push <nom-du-repo-docker-hub>``

Utilisation de l'image stockée sur Docker Hub
++++++++++++++++++++++++++++++++++++++++++++++
1. Ouvrez un terminal.
2. Exécutez la commande suivante pour télécharger la dernière image :
   ``docker pull claireruysschaert/p13oc:latest``
3. Lancez un conteneur avec l'image téléchargée
   ``docker run -p 8080:8080 claireruysschaert/p13oc:latest``
4. Accédez au site sur http://localhost:8000.

Déploiement en production avec Azure
+++++++++++++++++++++++++++++++++++++

- Configurer les fichiers static avec whitenoise
- Connectez-vous au portail Azure
- Créer le plan de service d'application. Dans le portail Azure, cliquez sur « App services », puis sur « create » pour lancer le processus de configuration. Remplissez les détails requis, tels que le nom, l'abonnement, le groupe de ressources et le système d'exploitation pour le plan. Choisissez le niveau de prix minimal. Vérifiez vos paramètres et cliquez sur « Créer » pour provisionner le plan de service App.
- Déployer votre application Web. Dans le portail Azure, accédez à l'application Web que vous venez de créer. Dans le menu de gauche, sélectionnez « Deployment Center ». Sélectionnez le registre de conteneurs avec ces paramètres pour vous connecter à Docker Hub : 

* Type de conteneur : Conteneur unique
* Source du registre : Docker Hub
* Accès au registre : Public
* Full Image name and Tag : <nom-du-repo-docker-hub>
* URL du webhook : copier

- Ajouter un nouveau webhook sur DokerHub. Copier l'URL du webhook de l'application et l'utiliser pour créer un nouveau webhook sur la plateforme Docker Hub.
- Ajouter des variables d'environnement dans les paramètres de l'application Azure

* SENTRY_DSN : URL du projet Sentry
* SECRET_KEY : Clé secrète du compte Sentry
* DOCKER_PASSWORD : Mot de passe du compte Docker
* DOCKER_USERNAME : Nom d'utilisateur du compte Docker
* DEBUG : Option de settings pour le déploiement 

- Le déploiement se lance automatique et le site est disponible sur le lien affiché dans "Overview".

Gestion de l'application
------------------------

Accès à l'interface d'administration
++++++++++++++++++++++++++++++++++++

Veuillez vous rendre sur l'URL suivant :

- ``http://<adresse-ip-publique-fournie-par-l'hébergeur>:8000/admin/``

  - Exemple : `http://54.159.98.184:8000/admin/ 
    <http://54.159.98.184:8000/admin/>`_

Connectez-vous avec les informations suivantes :

- Login : admin
- Mot de passe : admin

Ajout d'un objet
::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Add`` en face du type de modèle que vous souhaitez ajouter.
- Remplissez le formulaire.
- Cliquez sur le bouton ``SAVE``.

Modification d'un objet
:::::::::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Change`` en face du type de modèle que vous souhaitez modifier.
- Cliquez sur l'objet à modifier.
- Remplissez le formulaire.
- Cliquez sur le bouton ``SAVE``.

Suppression d'un objet
::::::::::::::::::::::

- Une fois connecté sur l'interface d'administration, veuillez cliquer 
  sur le bouton ``Change`` en face du type de modèle que vous souhaitez supprimer.
- Cliquez sur l'objet à supprimer.
- Cliquez sur le bouton ``Delete``.
- Confirmez votre choix en cliquant sur le bouton ``Yes, I'm sure``.

Journalisation
--------------

Une journalisation a été mise en place en utilisant Sentry. Celle-ci renvoie 
les erreurs et exceptions levées (erreurs 404 & 500, …) lors de l'utilisation 
du site par un utilisateur.

Base de données
---------------

Les données du site sont stockées sur un fichier SQLite nommé 
``oc-lettings-site.sqlite3``. Il s'agit d'une solution temporaire en attendant 
une utilisation plus accrue du site qui justifierait l'adoption d'une technologie 
plus adaptée.
