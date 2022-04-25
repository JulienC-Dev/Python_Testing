# Amélioration d'une application Web par des tests et du débogage

## Overview

Ce projet a été implémenté par OpenClassRoom dans le but de s'entraîner à la réalistation de tests unitaires et d'intégrations à l'aide de Pytest.
Le projet est réalisé sous le framework Flask. L'application est une version légère d'une plateforme de booking pour des compétitions de force(deadlifting, strongman).
L'objectif est de corriger les nombreux bugs de l'application et de réaliser un maximun de tests cohérents.
Une liste d'exigences fonctionnelles a dû être respectés pour la correction des bugs.
Les rapports de tests et de performances Locust se trouvent dans ce repo.

## Tests et developpement

1. Pré-requis pour le lancement du serveur local:
   
    * Installer la dernière version de Python sur le site - https://www.python.org
    * Ouvrir l'interpréteur de commandes de Python
    * Créer un nouveau repertoire via la commande : ```cd mkdir projet11```
    * Initialiser un environnement virtuel via la commande : ```python -m venv```
    * Tapez dans la console et au niveau du dossier racine : ```git init```
    * Cloner le dépo via la console : ```https://github.com/JulienC-Dev/Python_Testing/tree/dev```
    * Puis installer les dépendances: ```pip install -r requirements.txt```
    

2. Connection au serveur local http://127.0.0.1:5000/
   * Aller sur le sous-dossier - Projet9 via la commande  : ```cd projet11```
   * lancer le serveur local via la commande : ```flask run```
   * Ouvrir le naviguateur web puis tapez dans la barre de recherche : ```http://127.0.0.1:5000/```
   
3. Lancement des tests via Pytest
   * Exécuter l'ensemble des tests du projet via la commande ```pytest```
   * la commande ```pytest tests/unitaires_tests``` permet de lancer les tests unitaires 
   et la commande ```pytest tests/integrations_tests``` les tests d'intégrations
     
## Ressources

Vous pouvez trouver ces ressources utiles:

* Full doc Pytest : https://docs.pytest.org/en/6.2.x/contents.html
* Full doc Flask : https://flask.palletsprojects.com/en/2.1.x/ 

## Version 1.0.0

Auteur JulienC-Dev - github : https://github.com/JulienC-Dev/Python_Testing/tree/dev


