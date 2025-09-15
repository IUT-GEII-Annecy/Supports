---
title: TP 1 - Premières variables
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 103
---
# Notre première variable 
Nous allons à présent utiliser nos premières variables. Pour cela, commençons simplement avec l'exemple du cours et le cahier des charges suivant : 
> [!attention] Afficher le nom de l'utilisateur
> - Le programme doit demander le nom de l'utilisateur avec le message de votre choix.
> - Le programme doit afficher "Hello, \<nom\>" où \<nom\> est le nom entré par l'utilisateur.
>
> **Sortie attendue :**
> | Entrée | Affichage attendue | 
> | --- | --- |
> | <nom> | Hello, <nom>|  
>
> **Exemples de tests :**  
> | Entrée | Affichage attendue | 
> | --- | --- |
> | Alice | Hello, Alice |  
>
> ---
> Pour lancer les tests : 
>   ```bash
> 	check50 iut-geii-annecy/exercices/2025/info1/tp1/0_hello/variable
> 	```

Le cahier des charges mentionne la sortie attendue. **Votre programme doit ABSOLUMENT afficher la sortie attendue pour être correct.**

> [!todo] Afficher le nom de l'utilisateur
> 
> Pour répondre à ce cahier des charges, vous devez réaliser les 4 prochaines étapes. A vous de trouver où effectuer chacune des modifications. 
>
> - [ ] Inclure la bibliothèque `cs50.h` pour utiliser la fonction `get_string`. 
> 	```c
> 	#include <cs50.h>
> 	```
> - [ ] Déclarer une variable de type `string` pour stocker le nom de l'utilisateur.  
> 	```c
> 	string nom;
> 	```
> - [ ] Utiliser `get_string` pour obtenir le nom de l'utilisateur.  
> 	```c
> 	nom = get_string("Entrez votre nom : ");
> 	```
> - [ ] Modifier `printf` pour afficher le message "Hello , [nom]!" où [nom] est le nom entré par l'utilisateur.


> [!todo] Vérification 
> A l'aide de la fiche "Aide Mémoire" : 
> - [ ] Vérifier la mise en page de votre code (`style50`)
> - [ ] Faire passer les tests automatiques (`check50`)





