---
title: TP 1 - Configuration
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 101
---

# Environnement de Trvail

## Première configuration

> [!todo] Créer un compte GitHub
>
> - [ ] Si vous n'avez pas encore de compte GitHub, créez-en un :
>   - **Nom d'utilisateur :** `<p>-<nom>` avec p, la première lettre de votre prénom, puis votre nom.
>     - Exemple : j-doe pour John Doe
>   - **Adresse Mail :** `<adresse email académique>`
>   - [ ] Lien pour inscription : [GitHub.com](https://github.com).
> - [ ] Rejoignez le cours du semestre 1, en cliquant sur le lien correspondant à votre groupe.
> | Groupe | Lien                                                                        |
> |--------|-----------------------------------------------------------------------------|
> | A      | [Groupe A](https://submit.cs50.io/invites/9a6f6de5408b4022baebeb336f409261) |
> | B      | [Groupe B](https://submit.cs50.io/invites/f70e5bcd71c941a7acd2cbd7739218d8) |
> | C      | [Groupe C](https://submit.cs50.io/invites/88bf318c8b054f7a959ea7371f2b8011) |
> | D      | [Groupe D](https://submit.cs50.io/invites/e58130b1d7874ca481da62a0795da120) |
> - [ ] Lancez l'IDE, pour cela :
>   - [ ] Rendez-vous sur la page de [cs50.dev](https://cs50.dev).
>   - [ ] Cliquez sur `Log in`. _La première ouverture peut prendre quelques minutes_

> [!info] GitHub ? Qu'est-ce que c'est ?
> GitHub est une plateforme de développement collaboratif qui permet de stocker et de partager du code.
>
> Elle permet notamment le versionning _(Pouvoir revenir à toutes les versions précédentes du code)_, le suivi des modifications et facilite grandement la collaboration.
> C'est un outil incontournable dans le monde professionnel du développement logiciel.
>
> Pour ce premier semestre, l'utilisation de GitHub est invisible pour vous. Elle se fait via les commande de cs50

## Le terminal

### Présentation

En bas de la fenêtre de vsCode, vous trouverez un terminal. C'est un outil qui vous permet d'interagir avec votre système d'exploitation en utilisant des commandes textuelles.

> [!important] Liste des commandes utiles
> Voici quelques commandes de base que vous utiliserez fréquemment :
>
> - `clear` : nettoie l'affichage dans le terminal
>   Les éléments entre chevrons <>, sont à remplacer en fonction du contexte
> - `cd <nom_du_dossier>` : change le répertoire courant pour `<nom_du_dossier>`.
>   - `cd ..` permet de remonter dans le dossier parent
> - `code <nom_du_fichier>` permet d'ouvrir le fichier `<nom_du_fichier>` en le créant si besoin
> - `cp <source> <destination>` : copie un fichier ou dossier de `<source>` à `<destination>`.
> - `ls` : liste les fichiers et dossiers dans le répertoire courant.
> - `mv <source> <destination>` : déplace ou renomme un fichier ou dossier de `<source>` à `<destination>`.
> - `mkdir <nom_du_dossier>` : crée un nouveau dossier nommé `<nom_du_dossier>`.
> - `rm <nom_du_fichier>` : supprime le fichier nommé `<nom_du_fichier>`.
> - `rmdir <nom_du_dossier>` : supprime un dossier nommé `<nom_du_dossier>` (le dossier doit être vide).

> [!tip] L'autocomplétion dans le terminal
> Bien souvent, le terminal peut deviner ce que vous voulez faire à partir du début de la commande, à l'aide de la touche `Tab`.

> [!todo] On s'exerce !
>
> - [ ] Exécuter les lignes suivantes, **les unes après les autres**.
>   - [ ] Pour chacune, écrire ce que fait la commande.
>
> ```bash
> mkdir monPremierDossier
> ls
> cd monPremierDossier
> mkdir sous-dossier1 sous-dossier2
> ls
> cd ..
> ls
> cd monPremierDossier/sous-dossier1
> cd ../sous-dossier2
> cd ..
> mv sous-dossier1 nouveau-nom
> ls
> cd
> rm monPremierDossier
> rm -r monPremierdossier
> ```
>
> A vous de jouer !!
>
> - [ ] Créer un dossier portant votre nom, à l'intérieur duquel vous créerez deux dossiers : un à votre prenom, l'autre tp1
> - [ ] Faire vérifier par l'enseignant

> [!warning] Informations importantes à propos du terminal :
>
> - Certains raccourcis ne sont pas les même qu'habituellement
>   - `Ctrl-Maj-C` pour copier
>   - `Maj-INSER` pour coller
> - Les commandes ne répondent souvent rien lorsqu'elle réussissent
> - Il est impossible de bouger le curseur avec la souris. Il faut utiliser les flèches

## Téléchargement du dossier de TP

Prêts ? Allons-y ! Récupérons les fichiers pour commencer à coder !

> [!todo] Premières commandes dans le terminal
> [![asciicast](https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZ.svg)](https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZ)
>
> - [ ] Télécharger les fichiers du tp1 :
>   - [ ] Copier la commande suivante puis la coller la dans le terminal `Maj-INSER`. Appuyer sur Entrée
>   ```bash
>   wget https://github.com/IUT-GEII-Annecy/squelettes/releases/download/branch-2025/tp1.zip
>   ```
> - [ ] Décompresser le dossier et supprimer le _.zip_
>   - [ ] **(Essayer l'autocomplétion en tapant `unzip t` puis en appuyant sur `Tab`)** :
>     ```bash
>     unzip tp1.zip
>     ```
>   - [ ] Supprimer le fichier `tp1.zip` :
>     ```bash
>     rm tp1.zip
>     ```
>   - [ ] Répondre `y` s'il demande confirmation
> - [ ] Vous pouvez afficher la liste des fichiers et dossiers avec la commande `ls`.
>   ```bash
>   ls
>   ls tp1/
>   ```
> - [ ] Naviguer dans le dossier `tp1/0_hello`
>   ```bash
>   cd tp1/0_hello
>   ```
> - [ ] Créer un fichier `hello.c` :
>   ```bash
>   code hello.c
>   ```
>   - [ ] Un nouvel onglet devrait s'ouvrir dans vsCode avec un fichier vide nommé `hello.c`.
>   - _Vous pouvez également créer un fichier en cliquant sur l'icône "Nouveau fichier" dans l'explorateur de fichiers à gauche._
