# Projet TATIA

### Sujet:
Dans le cadre du projet de Traitement automatique du texte en IA nous avons décidé de concevoir un mini moteur de recherche destiné à trouver des articles d’information à partir d’un flux RSS, dans le cas présent le journal “Le Monde” sera la source de ce flux.

# Description des tâches
* Parser les données du flux RSS
* Extraire les informations pertinentes
* Pondérer les mots clés de la recherche par rapport au jeu de données
* Identifier l'article d'information le plus proche (distance des vecteurs)
* Retourner le lien vers la page de l'article

# Setup et utilisation

Avant de pouvoir lancer le projet il faut avant tout s’assurer que nltk ainsi que sickit-learn soient installés.




## Installation

Il faut pour cela exécuter les lignes de commande suivantes à la racine du projet :

1.  `pip  install -U scikit-learn`
    

2.  `pip install  ntlk`

## Utilisation

Une fois ces étapes complétées on peut alors ouvrir le fichier input.in et y écrire les mots clés souhaité pour la recherche.

Exemples :

-   Séisme catastrophe naturel
    
-   Accident voiture paris
    
-   Manifestation accident police
    

A noter que seule la première ligne du fichier input.in est prise en compte. Il est également préférable d’entrer entre 2 et 5 mots clés lors de la recherche pour minimiser les phénomènes de “dérive”.

Il faut alors exécuter les lignes de commandes suivantes :

1.  `cd core`
    

2.  `Python3 search.py < input.in`
    

Il est également possible de lancer directement search.py sans indiquer de fichier .in, il est alors requis de renseigner les mots clés à utiliser directement dans le terminal.

## Résultat

Le lien correspondant à l’article trouvé s’affiche alors dans le terminal.

# Jeu de données

L'ensemble de nos données proviennent du flux RSS du journal d'information en ligne lemonde.fr
Notre projet comporte plus de 60 fichiers xml corespondant aux flux RSS du 16/12 et du 30/12. Les flux RSS de la pèriode en cours peuvent être retrouver à l'adressse suivante: https://www.lemonde.fr/actualite-medias/article/2019/08/12/les-flux-rss-du-monde-fr_5498778_3236.html

