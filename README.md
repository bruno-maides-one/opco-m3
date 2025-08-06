# OPCO Module 3

## Choix de la base de données

J'ai choisi SQLite pour faciliter la distribution de la base de données dans un simple fichier.

## Structure du projet
* ai_models : dossier stockants les models
* data : ensemble des dataset au format .csv et la base de donnée SQLite database.db
* models : modeles SQLalchemy et pydantic de la base de données

## Point de focus

J'ai principalement porter mon interet sur le training.

Fichier de travail principal :
* [m2-brief2-revisited.ipynb](m2-brief2-revisited.ipynb) : retravail sur le datset original, script récupérer du module précédent et retouché.
* [m3-brief3-preparation-datasets-training.ipynb](m3-brief3-preparation-datasets-training.ipynb) : Travail sur le dataset étendu
* [m3-brief3-training-model.ipynb](m3-brief3-training-model.ipynb) : Training du model + training d'un second model en récupérant les connaissance du model precedemment créé.

Fichier notable :
* [m3-brief3-autre-approche-analytique.ipynb](m3-brief3-autre-approche-analytique.ipynb) : tentative d'utiliser les outils de data-analyse mais difficulté a le faire trouner.
* [backend.py](backend.py) : implémentation ultra-light du model pydantic servi par fastapi

## Lancement du projet

### API

```shell
uvicorn backend:app
```

TODO : 

[ ] : Finir les tests pour automatiser l'export des models SQLalchemy en class pydantic.
[ ] : Ajout d'autres routes pour interagir avec la base

### Training des  modeles

Le training passe par [m3-brief3-preparation-datasets-training.ipynb](m3-brief3-preparation-datasets-training.ipynb) il est necessaire de lancer mlflow pour suivre l'évolution des performances des models.

Il faut lancer mlflowui en ouvrant la console et en entrant

```shell
mlflow ui
```

L'acces a mlflow se fait via http://127.0.0.1:5000/

## Conclusion.

J'ai réussis à entrainer le model initial avec le dataset "réduit", j'obtiens un R² de 0.35 avec ce jeu de donner.

J'ai ensuite été capable d'étendre le dataset en ajoutant des features et de réentrainer le model existant sans perte de connaissances pour améliorer les performances globale du model. 

Apres avoir étoffé les connaissance du modèle je suis passé à un R² de 0.46.
