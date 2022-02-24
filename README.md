# Projet 4 : Développez un programme logiciel en Python
*par Jean-Corentin Loirat
le 21/02/2022

Lien du repository git hub : https://github.com/BeanEden/OC_Project_4

## Description de l'application :
Il s'agit d'un programme permettant la tenue de tournoi d'échec et la sauvegarde de ces informations (joueurs, tournois, rounds et matchs).
Ce tournoi comporte 8 joueurs et 4 tours.

L'ensemble des données (tournois, matchs, rounds et joueurs) est consultable de la base de données "database".json.
Les différentes instances sont stockées par table (une table "Tournament" pour les tournois "Player" pour les joueurs"...).


## Utilisation :

### 1 - Créez un environement virtuel dans le dossier de votre choix et activez le :
* Commande terminal : `mkdir projects`
* Commande terminal : `cd projects`
* Commande terminal : `python -m venv env`
* Commande terminal : `env/Scripts/activate.bat` (sous Windows)

### 2 - Importez les packages :
* Commande terminal : `pip install -r requirements.txt`

Importez dans votre environnement virtuel les packages nécessaires au script (tinydb, datetime), tels que présents dans le fichier requirements.txt
Il est possible d'utiliser la ligne de commande "pip install -r requirements.txt",
ou d'installer les packages un par un : "pip install requests"

### 3 - Lancez l'application : 
* Commande terminal : `python main.py`


## Déroulement
Lors du lancement du programme, l'utilisateur arrive sur le menu principal du programme.

Il peut alors saisir l'action de son choix :
* 1 - Start a tournament
* 2 - Add a player
* 3 - Update a player
* 4 - Consult a tournament / player / matches report
* 5 - Exit program

L'utilisateur navigue alors entre les différents menus selon ses choix.

Pour sortir du programme, il faut revenir au menu principal et entrer "5".

  

## Database :
La base de donnée est gérée par TinyDB en format .json.
Les données sont classées par tables.
* Player
* Tournament
* Round
* Match

Si aucune database n'existe dans le dossier du programme, une database sera créée.
Il est possible de générer une nouvelle base de donnée en changeant le nom de la database dans le fichier main.py.

## Mise en forme du code :
Le code est mis en forme selon de modèle MVC.

* Model (one per class) :
  * tournament.py 
  * player.py 
  * round.py 
  * match.py 
  * database.py
* View:
  * view.py
* Controller:
  * menu.py
  * creation.py

## En savoir plus :
Les fonctions et méthodes sont documentées via docstrings avec leurs utilisations, arguments et retours.


## Générer un report flake8:
Installez flake8

* Commande terminal : `pip install pip install flake8-html`

Lancez le report flake8 avec une longueur de ligne de 119 caractères.
* Commande terminal :`flake8 --max-line-length=119 --format=html --htmldir=flake-report`

Un nouveau dossier flake-report est créé, contenant index.html.

## Contenu du repository git hub: 
* main.py
* Model Package
* Controller Package
* View Package
* requirements.txt
