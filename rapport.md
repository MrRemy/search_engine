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

![alt text](https://github.com/maxime-samak/search_engine/blob/master/resources/xml%20file.PNG "Format du fichier xml")

Nous avons donc commencé par créer un parseur permettant d’isoler les éléments pertinents de ces fichiers, à savoir le contenue des différentes balises <item>. En effet ces balises constituent l’ensemble des données utiles, c’est à dire le titre de l’article d’information, une description courte de son contenu et enfin le lien vers la page web de l’article en question. 

Une fois ces balises isolées pour l’ensemble des fichiers xml de notre jeu de données, des objets sont créés avec pour attributs les 3 informations présentant un intérêt. 
Une collection constituée de l’ensemble de tous les objets Article ainsi obtenue devient alors la base de notre moteur de recherche. 

## Acquisition des mots clés 

Pour effectuer une recherche il est impératif d’avoir des mots clés constituant l’objet de la recherche à effectuer. 
Pour cela une simple lecture d’un fichier “.in” est la solution qui nous a paru être la plus optimale. 

## Génération de synonymes 

La langue Française étant très riche les mots clés saisies peuvent ne pas trouver d’homologue dans les différents articles d’information à notre disposition tout en ayant un sens presque similaire voir totalement identique à ceux présents dans la description / titre de ces dits articles. 

 

Une solution à ce problème est de générer une liste de synonymes pour chaque mot de notre recherche de manière à étendre les chances de trouver un mot similaire dans les articles. 

Pour cela l’utilisation de la librairie nltk wordnet s’est révélé très importante. 

Ainsi lors d’une recherche avec le mot clé “voiture” on peut générer quelques synonymes susceptibles de nous intéresser : “wagon, entraîneur, véhicule, voiture, auto, carrosse, automobile”  
On peut alors couvrir un étendu plus large lors de notre recherche 

Cet exemple illustre l’utilisation que nous avons fait de cet outil durant le projet. Et même si cette utilisation présente des bénéfices elle s’accompagne également d’un problème assez important. Il s’agit d’un effet qu’on pourra qualifier de “dérive de la recherche” qui provoquera parfois la découverte d’un article peu corrélé à l’intention de notre recherche. Cet effet est très sensible à la qualité ainsi qu’à la quantité des synonymes obtenues avec wordnet et il s’est avéré que l’utilisation du Français ne nous est ici pas favorable.

## TF-IDF et COSINE SIMILARITY 

Pour procéder à la recherche et la découverte un article pertinent il est important de mesurer le “poids” des mots par rapport à l’article dans son ensemble de même que la totalité des articles. 

Nous avons donc fait usage de la méthode TF-IDF (term frequency-inverse document frequency) permttant de pondérer les termes contenus dans un document. 

![alt text](https://github.com/maxime-samak/search_engine/blob/master/resources/inverse_document_frequency.PNG "Formule TF-IDF")

Nous avions dans un premier temps fait usage de de la méthode NTF (normalized term frequency) : 
![alt text](https://github.com/maxime-samak/search_engine/blob/master/resources/normalized_term_frequency.PNG "Formule NTF")

Mais avons vite réaliser notre erreur et transitionner vers une méthode plus correcte et prenant en compte la différence de taille entre nos documents et notre entrée. 

Une fois cette étape complétée on peut alors transformer chaque description et titre d’article (et notre entrée) en un vecteur représenté par nos pondérations TF-IDF. La suite consiste simple à trouver le vecteur de document le plus proche de notre vecteur de recherche. 
![alt text](https://github.com/maxime-samak/search_engine/blob/master/resources/vector.PNG "Vectorisation")

Sickit learn nous offre alors la solution la plus efficace avec la méthode de mesure de distance cosinus (cosine_similarity) 
![alt text](https://github.com/maxime-samak/search_engine/blob/master/resources/cosine_distance.PNG "Cosine distance")

On peut alors identifier quel article est le plus pertinent par rapport à notre recherche initiale. 

On retourne alors le lien menant à sa page web. 

Une observation intéressante est qu’il existe des méthodes plus poussées (et plus rapide) au sein de SpaCy cependant leur utilisation nous a été rendu difficile voire impossible au vu de la langue choisie pour ce projet. 

## Conclusion

Ce projet s’est révélé être des plus instructifs notamment en ce qui concerne les méthodes de recherche d’information et d’étude des langages naturels. 

De même de nombreuses méthodes et outils ayant été exploré mais n’ayant pas abouti à un résultat qui nous paraissait satisfaisant pour ce projet nous ont permis d’acquérir des connaissances plus vastes que ce compte rendu de projet seul pourrait le laisser entendre. Et nous avons donc pu nous familiariser avec des outils, méthodes et librairies tel que : SpaCy, TreeTagger, Numpy, Scipy, NTF, RFrequency, … 

 

Dans une autre mesure il faut toutefois rappeler que même si dans l’ensemble nous sommes assez satisfaits du stade auquel nous sommes arrivés pour ce projet, il existe une marge d’amélioration assez grande. 

En effet on pourrait améliorer le modèle actuel en y intégrant l’identification des entités nommés ainsi que de la désambiguïsation (l’utilisation du Français représentant toutefois un frein à ces deux améliorations). 
 
### Note

La description des tâches, les informations sur le jeu de données ainsi que les démarches d'installations et d'utilisations du projet se trouvent sur le readme.md
