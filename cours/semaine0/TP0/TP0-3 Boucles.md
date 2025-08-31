---
title: TP 0.3 Les Boucles
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
weight: 13
---


# 3. Boucles et répétitions
## Introduction : Un peu de mouvement
> [!todo] Ajouter du mouvement
> - [ ] Ajoutez un bloc "quand le drapeau vert est cliqué"
> - [ ] Ajoutez un bloc "aller à x: [0] y: [0]"
> - [ ] Ajoutez un bloc "tourner de 15 degrés"
> - [ ] Ajoutez un bloc "avancer de 10 pas"
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite se déplacer et tourner.
> - [ ] Cliquer autant de fois que vous voulez pour faire faire un tour complet à votre sprite.

Répondre à la question suivante avant de regarder la réponse :
> [!question]- Combien de fois faut-il cliquer pour faire un tour complet ?
> Il faut cliquer 24 fois pour faire un tour complet, car 360 degrés divisé par 15 degrés donne 24.

> [!question]- Comment faire pour que le sprite fasse un tour complet sans avoir à cliquer 24 fois ?
> Pour faire faire un tour complet à votre sprite sans avoir à cliquer 24 fois, on peut simplement copier le bloc "tourner de 15 degrés" et le bloc "avancer de 10 pas" 24 fois.
> Vous pouvez faire l'esai. 
> 
> Il y a une meilleure solution : utiliser une boucle.

## 3.1. Boucles
> [!info] Qu'est-ce qu'une boucle ?
> Une boucle est une structure de programmation qui permet de répéter un bloc de code plusieurs fois sans avoir à le réécrire. 
> Par exemple, si vous voulez faire tourner un sprite de 15 degrés 24 fois, vous pouvez utiliser une boucle pour éviter de répéter le bloc "tourner de 15 degrés" 24 fois.
> Sur Scratch, on utilise le bloc "répéter [nombre] fois" pour créer une boucle.

> [!todo] Utiliser une boucle
> - [ ] Ajoutez un bloc "répéter 24 fois" autour des blocs "tourner de 15 degrés" et "avancer de 10 pas".
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite faire un tour complet en 24 étapes.
> - [ ] Modifier le programme pour que le sprite fasse deux tours complets. 

## 3.2. Boucles infinies
> [!info] Qu'est-ce qu'une boucle infinie ?
> Une boucle infinie est une boucle qui ne s'arrête jamais.
> Par exemple, si vous utilisez le bloc "répéter indéfiniment", le programme continuera à exécuter le bloc de code à l'intérieur de la boucle sans jamais s'arrêter.
> Sur Scratch, on utilise le bloc "répéter indéfiniment" pour créer une boucle infinie.

### 3.2.1. Déplacer un sprite au clavier

> [!todo] Déplacer un sprite au clavier
> - [ ] Copier le code ci-dessus. 

> [!question]- Que se passe-t-il si vous appuyez sur la touche "flèche droite" ?
> Il ne se passe rien... 
> 
> **Pourquoi ?**
> Lorsque le programme est lancé, il vérifie si la touche "flèche droite" est pressée. Si c'est le cas, il déplace le sprite de 10 pas vers la droite. Sinon, il ne fait rien.
> Le problème est que le programme ne vérifie pas en continu si la touche "flèche droite" est pressée. Il ne le fait qu'une seule fois au début du programme.
> Vous pouvez le vérifier en maintenant la touche "flèche droite" pendant que vous lancez le programme. Le sprite se déplace car la touche est pressée au moment du lancement du programme. Il ne le fait qu'une seule fois, et ne continue pas à vérifier si la touche est pressée.

> [!todo] Corriger le programme
> - [ ] Entourez le bloc "si [touche flèche droite pressée] alors" avec un bloc "répéter indéfiniment".
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez maintenant pouvoir déplacer le sprite en maintenant la touche "flèche droite" enfoncée.
> - [ ] Ajoutez des blocs similaires pour les touches "flèche gauche", "flèche haut" et "flèche bas" pour déplacer le sprite dans toutes les directions.
> - **ASTUCE** : Vous pouvez dupliquer tout le bloc "si [touche flèche pressée] alors" avec un clic droit et en sélectionnant "Dupliquer". Cela vous permettra de gagner du temps pour créer les autres directions.
> - [ ] Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez maintenant pouvoir déplacer le sprite dans toutes les directions en utilisant les touches fléchées.

### 3.2.2. Un premier jeu

Nous allons ajouter un second sprite qu'il faudra attraper. 

> [!info] Un code pour chaque sprite
> Chaque sprite peut avoir son propre code. Vous pouvez ajouter un nouveau sprite en cliquant sur le bouton "Choisir un sprite" en bas à droite de l'interface. 
> Chaque sprite peut avoir son propre code, ce qui permet de créer des interactions entre les sprites. 

> [!todo] Attraper le sprite
> - [ ] Ajoutez un nouveau sprite (par exemple, un chat) à votre projet
>
> **Dans le code de ce nouveau sprite :**
> - [ ] Ajoutez un bloc "quand le drapeau vert est cliqué"
> - [ ] Ajoutez un bloc "Aller à position aléatoire" pour que le sprite apparaisse à une position aléatoire sur la scène.
> - [ ] Ajoutez un bloc "répéter indéfiniment" à l'intérieur duquel vous ajouterez un bloc si touche [votre sprite] alors aller à une position aléatoire.
> - [ ] Testez votre programme et faites valider votre programme par l'enseignant.

