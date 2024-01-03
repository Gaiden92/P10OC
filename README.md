# Projet 10 DA-Python OC (Sami Fouchal)

***Livrable du Projet 10 du parcours D-A Python d'OpenClassrooms***

API-SoftDesk est une API RESTful permettant de remonter et suivre des problèmes 
techniques pour les trois plateformes (site web, applications Android et iOS).

L'application permet aux utilisateurs authentifiés de créer divers projets, 
d'ajouter des utilisateurs (contributeurs) à des projets spécifiques, 
de créer des problèmes au sein des projets, d'attribuer des libellés 
à ces problèmes en fonction de leurs priorités, de balises,...Et enfin de
créer des commentaires pour chaque problèmes.

_Testé sous Windows 10 - Python 3.11.1 - Django 5.0 - Django Rest Framework 3.14.0_

## Initialisation du projet

### Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.
###### • Récupération du projet

```
git clone https://github.com/Gaiden92/P10OC.git
```

###### • Créer et activer un environnement virtuel

```

python -m venv env 
env\Scripts\activate
```

###### • Installer poetry et les paquets requis

```
pip install poetry
poetry shell (activation de l'environnement virtuel)
poetry install (installation des paquets requis)

```


### MacOS et Linux :
Dans le terminal, naviguer vers le dossier souhaité.
###### • Récupération du projet
```
git clone https://github.com/Gaiden92/P10OC.git
```

###### • Créer et activer un environnement virtuel
```
python3 -m venv env 
source env/bin/activate
```

###### • Installer les paquets requis
```
pip install poetry
poetry shell (activation de l'environnement virtuel)
poetry install (installation des paquets requis)

```

## Utilisation

#### Faire les migrations (si nécessaire) :

```
python manage.py migrate
```

#### Lancer le serveur Django :

```
python manage.py runserver
```

Il est possible de naviguer dans l'API avec différents outils :

- la plateforme [Postman](https://www.postman.com/) ;
- l'interface intégrée Django REST framework à l'adresse http://127.0.0.1:8000/ (adresse par défaut, cf. points de terminaison ci-dessous).

## Informations

#### Liste des utilisateurs existants :

| *ID* | *Identifiant* | *Mot de passe* |
|------|---------------|----------------|
| 1    | Terry         | password123    |
| 2    | Doris         | password123    |
| 3    | Thomas        | password123    |
| 4    | Samir         | password123    |
