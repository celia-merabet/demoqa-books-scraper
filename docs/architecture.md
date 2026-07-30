
# Architecture du scraper DemoQA Books

## Flux général

```
DemoQA Books API
        |
        v
   scraper.py
        |
        v
   parser.py
        |
        v
   models.py
        |
        v
   exporter.py
        |
        v
 output/books.jsonl
```

---

# Organisation des modules

## main.py

Point d'entrée du programme.

Responsabilités :

* lancer la collecte
* appeler les différents modules
* afficher le résultat

## config.py

Contient :

* URL cible
* paramètres de collecte
* chemin de sortie

## scraper.py

Responsabilités :

* envoyer les requêtes
* récupérer les données

## parser.py

Responsabilités :

* extraire les champs nécessaires
* nettoyer les valeurs

## models.py

Définit le modèle Book.

Champs :

* isbn
* title
* author
* publisher
* pages
* url

## exporter.py

Responsabilité :

* générer le fichier JSONL

## logger.py

Responsabilité :

* enregistrer :

  * nombre d'objets vus
  * objets exportés
  * erreurs

---

# Choix techniques

## Choix 1 : utilisation JSON plutôt que DOM

La source JSON a été choisie car elle fournit directement les données structurées.

Alternative écartée :

Selenium + extraction DOM.

Raison :

* plus complexe
* plus lent
* dépend du navigateur

## Choix 2 : export JSONL

Le format JSONL permet :

* traitement ligne par ligne
* compatibilité avec les outils data
* simplicité d'utilisation
