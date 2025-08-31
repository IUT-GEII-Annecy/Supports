---
title: TP 1 - Configuration
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 100
---
# Un peu de configuration 
## Avant toute chose : Un compte GitHub !

> [!info] GitHub ? Qu'est-ce que c'est ?
> GitHub est une plateforme de développement collaboratif qui permet de stocker et de partager du code. 
> Vous l'utiliserez pour soumettre vos travaux pratiques et collaborer avec vos camarades.
>
> Dans le monde professionnel, GitHub est un outil incontournable pour le développement logiciel. Il sert notamment à gérer les versions du code, à collaborer avec d'autres développeurs et à partager des projets open source.

> [!todo] Créer un compte GitHub
> Si vous n'avez pas encore de compte GitHub, créez-en un. C'est essentiel pour suivre ce TP et les suivants. 
> **Attention, ce compte vous sera utile dans votre vie professionnelle, choisissez votre pseudo avec soin !**
> - [ ] Utilisez votre **adresse email académique** pour créer votre compte sur [GitHub](https://github.com).


## Configurons votre espace CS50

> [!todo] Rejoindre le cours du semestre 1
>  - [ ] Cliquez sur ce lien [submit.cs50.io](https://submit.cs50.io/invites/61a963c727374a32aa487ead18d908c5) et connectez votre compte GitHub
>  Ce site contiendra vos rendu et les retours des enseignants. 

## Lancer vsCode pour les TPs de ce module


Visual Studio Code (vsCode) est un éditeur de code très utilisé dans l'industrie de la programmation. 
Il offre de nombreuses extensions pour faciliter la programmation, comme la coloration syntaxique, l'autocomplétion et le débogage.
Il est compatible avec de nombreux langages de programmation.

> [!todo] Lançons votre espace de travail ! 
> - [ ] Lancez vsCode depuis la page de [cs50](https://cs50.dev). Cliquez sur Log in





## Votre premier programme : Hello World

### Le terminal 

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

>[!exemple] Exemple de comande
>La commande suivante rentre dans le dossier tp1 puis 0_hello
>```bash
>cd tp1/0_hello
>```




> [!warning] Informations importantes à propos du terminal : 
>  - Certains raccourcis ne sont pas les même qu'habituellement 
> 	 - `Ctrl-Maj-C` pour copier 
> 	 - `Maj-INSER` pour coller 
>  - Les commandes ne répondent souvent rien lorsqu'elle réussissent
>  - Il est impossible de bouger le curseur avec la souris. Il faut utiliser les flèches

> [!tip] L'autocomplétion dans le terminal
> Bien souvent, le terminal peut deviner ce que vous voulez faire à partir du début de la commande, à l'aide de la touche `Tab`. 

Prêts ? Allons-y ! Nous allons écrire nos premières commandes dans le terminal ... 

> [!todo] Premières commandes dans le terminal
> [![asciicast](https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZ.svg)](https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZ)
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


### Hello World en C    

> [!todo] Écrire le programme Hello World se fait en trois étapes :
> 1. Inclure la bibliothèque standard d'entrée/sortie (`stdio.h`). -> Ecrire `#include <stdio.h>` en haut du fichier
> 2. Définir la fonction principale `main`. -> `int main(void) { ... }`
> 3. Utiliser la fonction `printf` à l'intérieur de la fonction main pour afficher le message.
> 	- `printf("Hello, World!\n");`
> 4. Ajouter `return 0;` à la fin pour indiquer que le programme est terminé. 

Votre programme devra donc ressembler à ça : 
```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");
    return 0;
}
```

> [!todo] Compiler et exécuter le programme 
> - [ ] Dans le terminal, assurez-vous d'être dans le dossier `TP1` où se trouve votre fichier `hello.c`. (Sinon, utilisez la commande `cd` pour naviguer jusqu'à ce dossier.
> - [ ] Compiler le programme avec la commande `make hello`. Cette commande utilise le Makefile fourni par cs50 pour compiler le code C.    
> - [ ] Exécuter le programme compilé avec la commande `./hello`. Vous devriez voir "Hello, World!" s'afficher dans le terminal.
> ```bash
> make hello
> ./hello
> ```
> - Si vous voyez le message, félicitations ! Vous venez d'écrire   votre premier programme en C. **Dans le cas contraire, demandez de l'aide à l'enseignant, à vos camarades ou au CS50 Duck Debugger.**   

