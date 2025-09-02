---
title: TP 1 - Configuration
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 101
---
# Un peu de configuration 
## Avant toute chose : Un compte GitHub !

> [!info] GitHub ? Qu'est-ce que c'est ?
> GitHub est une plateforme de développement collaboratif qui permet de stocker et de partager du code. 
> Vous l'utiliserez pour soumettre vos travaux pratiques et collaborer avec vos camarades.
>
> Dans le monde professionnel, GitHub est un outil incontournable pour le développement logiciel. Il sert notamment à gérer les versions du code, à collaborer avec d'autres développeurs et à partager des projets open source.

> [!todo] Créer un compte GitHub
> - [ ] Si vous n'avez pas encore de compte GitHub, créez-en un : 
>   - [ ] Nom d'utilisateur : `p-nom` avec p, la première lettre de votre prénom, puis votre nom.  
>   - [ ] Utilisez votre **adresse email académique** pour créer votre compte sur [GitHub](https://github.com).
> - [ ] Rejoignez le cours du semestre 1, cliquer sur le lien correspondant à votre groupe. 
> | Groupe | Lien |
> | --- | ---| 
> | A   | [Groupe A](https://submit.cs50.io/invites/9a6f6de5408b4022baebeb336f409261) |
> | B   | [Groupe B](https://submit.cs50.io/invites/f70e5bcd71c941a7acd2cbd7739218d8) | 
> | C   | [Groupe C](https://submit.cs50.io/invites/88bf318c8b054f7a959ea7371f2b8011) |
> | D   | [Groupe D](https://submit.cs50.io/invites/e58130b1d7874ca481da62a0795da120) |
>   - Ce site contiendra vos rendus et les retours des enseignants. 
> - [ ] Lancez l'IDE
>   - [ ] Rendez-vous sur la page de [cs50.dev](https://cs50.dev). 
>   - [ ] Cliquez sur `Log in`


## Le terminal 
### Présentation
En bas de la fenêtre de vsCode, vous trouverez un terminal. C'est un outil qui vous permet d'interagir avec votre système d'exploitation en utilisant des commandes textuelles. 

> [!important] Liste des commandes utiles
> Voici quelques commandes de base que vous utiliserez fréquemment :    
> - `clear` :  nettoie l'affichage dans le terminal
> Les éléments entre chevrons <>, sont à remplacer en fonction du contexte
> - `cd <nom_du_dossier>` : change le répertoire courant pour `<nom_du_dossier>`.
>    - `cd ..` permet de remonter dans le dossier parent 
> - `code <nom_du_fichier>` permet d'ouvrir le fichier `<nom_du_fichier>` en le créant si besoin
> - `cp <source> <destination>` : copie un fichier ou dossier de `<source>` à `<destination>`.
> - `ls` : liste les fichiers et dossiers dans le répertoire courant.
> - `mv <source> <destination>` : déplace ou renomme un fichier ou dossier de `<source>` à `<destination>`.
> - `mkdir <nom_du_dossier>` : crée un nouveau dossier nommé `<nom_du_dossier>`.
> - `rm <nom_du_fichier>` : supprime le fichier nommé `<nom_du_fichier>`.
> - `rmdir <nom_du_dossier>` : supprime un dossier nommé `<nom_du_dossier>` (le dossier doit être vide).

> [!tip] L'autocomplétion dans le terminal
> Bien souvent, le terminal peut deviner ce que vous voulez faire à partir du début de la commande, à l'aide de la touche `Tab`. 

Par, exemple, la commande suivante rentre dans le dossier `0_hello` se trouvant dans le dossier `tp1`
```bash
cd tp1/0_hello
```

> [!warning] Informations importantes à propos du terminal : 
>  - Certains raccourcis ne sont pas les même qu'habituellement 
> 	 - `Ctrl-Maj-C` pour copier 
> 	 - `Maj-INSER` pour coller 
>  - Les commandes ne répondent souvent rien lorsqu'elle réussissent
>  - Il est impossible de bouger le curseur avec la souris. Il faut utiliser les flèches


### Téléchargement du dossier de TP
Prêts ? Allons-y ! Nous allons écrire nos premières commandes dans le terminal ... 

> [!todo] Premières commandes dans le terminal
> ![asciicast](https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZ.svg)
> - [ ] Télécharger les fichiers du tp1 : 
> 	- [ ] Copier la commande suivante puis la coller la dans le terminal `Maj-INSER`. Appuyer sur Entrée
> 	```bash
> 	wget https://github.com/IUT-GEII-Annecy/squelettes/releases/download/branch-2025/tp1_2025.zip
> 	```
> - [ ] Décompresser le dossier et supprimer le *.zip*
> 	- [ ] Exécuter la commande suivante **(Essayer l'autocomplétion en tapant `unzip t` puis en appuyant sur `Tab`)** : 
> 		```bash
> 		unzip tp1.zip
> 		```
> 	- [ ] Supprimer le fichier `tp1.zip` en exécutant 
> 		```bash
> 		rm tp1.zip
> 		```
> 	- [ ] Répondre `y` s'il demande confirmation
>  - [ ] Vous pouvez afficher la liste des fichiers et dossiers avec la commande `ls`.
> 	 ```bash
> 	 ls
> 	 ```
> - [ ] Naviguer dans le dossier `tp1/0_hello`
> 	  ```bash
> 	  cd tp1/0_hello
> 	  ```
> - [ ] Créer un fichier `hello.c` :
> 	  ```bash
> 	  code hello.c
> 	  ```
>   - [ ] Un nouvel onglet devrait s'ouvrir dans vsCode avec un fichier vide nommé `hello.c`.
>   - *Vous pouvez également créer un fichier en cliquant sur l'icône "Nouveau fichier" dans l'explorateur de fichiers à gauche.*


> [!tip] Besoin d'aide ?
> CS50 Duck Debugger est là pour vous aider ! 
> Cliquer sur l'icône en forme de canard dans la colonne de gauche pour ouvrir l'extension.
> Vous pouvez lui demander "Answer in French" pour obtenir de l'aide en français.  

   

