# TATIA
### COMPTE RENDU DE PROJET
#### SAMAK Maxime
#### MUNIER Remy

## Sujet du projet
Dans le cadre du projet de Traitement automatique du texte en IA nous avons décidé de concevoir un mini moteur de recherche destiné à trouver des articles d’information à partir d’un flux RSS, dans le cas présent le journal “Le Monde” sera la source de ce flux.
## Introduction
Mener à bien ce projet nous a mis face à différents problèmes que nous nous sommes efforcés de traiter de la manière la plus optimale possible. Dans la mesure du possible nous avons essayé d’avoir le moins  possible recours à des librairies offrant une solution clé en main dans le but de conserver un aspect d’apprentissage et de découverte du Traitement Automatique du Langage Naturel (TALN).

Ainsi au cours de ce compte rendu, il sera exposé les difficultés rencontrées de même les solutions ou tentatives de solutions apportées lors de l’élaboration de ce projet.

## Gestion des données
Pour pouvoir démarrer un tel projet il est en premier lieu nécessaire de se constituer un jeu de données et de mettre en forme ces dernières pour faciliter leur utilisation.

La norme de stockage de l’information des flux RSS étant les fichiers au format XML, il a été dans premier temps notre priorité de pouvoir lire et traiter ce type de fichier d’une manière simple et efficace.

