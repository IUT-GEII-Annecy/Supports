---
title: TP 0.1 Les Variables
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
weight: 11
---


# 1. Un premier pas vers la mémoire : les variables 
> [!info] Qu'est-ce qu'une variable ?
> 
> Une variable est un espace de stockage pour des données qui peuvent changer au cours de l'exécution du programme. Par exemple, vous pouvez utiliser une variable pour stocker le score d'un jeu ou le nom d'un utilisateur.
> On peut imaginer une variable comme une boîte dans laquelle on peut mettre des informations. On peut ouvrir cette boîte pour voir ce qu'il y a à l'intérieur, ou y mettre de nouvelles informations.
> Sur scratch, on affecte une valeur à une variable en utilisant le bloc "mettre [nom de la variable] à [valeur]".


## 1.1. Notre première variable
> [!todo] Comment créer une variable Scratch ?
> - [ ] Dans la palette de blocs, trouvez la catégorie "Variables".
> - [ ] Cliquez sur "Créer une variable" et nommez-la comme vous le souhaitez.   
> Un bloc orange arrondi apparaît alors dans la palette de blocs, c'est votre variable.
![[Scratch3-Blocks/iCompute-Scratch3-Blocks/png/Variables/my-variable@4x.png]]


Notre premier programme était très impersonnel ! Accueillons l'utilisateur avec un message personnalisé. 
> [!todo] Personnaliser le message
> - [ ] Créez une variable appelée "Nom".
> - [ ] Ajoutez un bloc "demander [Quel est votre nom ?] et attendre" avant le bloc "dire".
> ![[ask-and-wait@4x.png]]
> - Le bloc Demander est associé à une variable spéciale appelée "réponse". Ces deux blocs se trouvent dans la catégorie Capteur ("Sensing").
> - [ ] Utilisez le bloc "mettre [Nom] à [réponse]" pour stocker la réponse de l'utilisateur dans la variable "Nom".
>  ![[set-variable@4x.png]]
> - [ ] Utiliser un bloc "regrouper" pour rassembler "Bonjour" et la variable "Nom" dans le bloc "dire".
> ![[join@4x.png]]
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite demander votre nom et afficher un message personnalisé.

## 1.2. Nos premiers calculs 
Notre première variable était un texte, mais on peut aussi utiliser des nombres.
> [!todo] Calculer l'année de naissance
> - [ ] Créez une variable appelée "Âge" ainsi qu'une variable "Année de naissance".
> - [ ] Ajoutez un bloc "demander [Quel est votre âge ?] et attendre" avant le bloc "dire".
> - [ ] Utilisez le bloc "mettre [Âge] à [réponse]" pour stocker la réponse de l'utilisateur dans la variable "Âge".
> - [ ] Utilisez un bloc "mettre [Année de naissance] à [2025 - Âge]" pour calculer l'année de naissance de l'utilisateur.
> - [ ] Utilisez un bloc "dire" pour afficher "Vous êtes né en [Année de naissance]".
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite demander votre âge et afficher l'année de naissance calculée.

## 1.3. A vous de jouer 

> [!todo] Sprite tient un tacos
> - [ ] Créer un programme qui demande à l'utilisateur combien de tacos et de kebab il veut commander. 
> - Ce programmme répondra le montant total de la commande.
> - [ ] Faire valider votre programme par l'enseignant.