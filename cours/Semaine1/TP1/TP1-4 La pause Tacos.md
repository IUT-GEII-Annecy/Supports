---
title: TP 1 - La pause Tacos
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 140
---
C'est parti pour notre premier problème ! 

## Niveau 1
> [!todo] Enoncé du problème : 
> Votre programme tient un Tacos dont vous devez inventer le nom. 
> Il reçoit un client, qui lui commande un certain nombre de tacos et de kebab. 
> Il doit alors lui dire quel est le montant total de la commande 

> [!warning] Cahier des charges - Pause Tacos - Niveau 1
> Le programme Affiche d'abord une phrase de bienvenue 
> ```bash
> Bonjour, bienvenu chez <nom_du_tacos>
> ```
> - [ ] Le programme demande alors le nombre de Tacos, puis le nombre de Kebab voulu 
> - [ ] Le programme écrit alors le prix total de la commande, arrondi au centième. 
> 
> |Produit|Prix|
> |---|---|
> |Tacos|6,30 €|
> |Kebab|5,50 €|
> 
> - [ ] Le programme écrit ensuite le message de remerciement 
> ```
> Montant total : <montant_total> euros
> Merci pour votre commande chez <nom_du_tacos>
> ```
>---
>**Checks:**
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau1
> ```


> [!exemple]
> [![asciicast](https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj.svg)](https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj)

> [!todo]- Un peu d'aide ? 
> - [ ] De quelles variables avez-vous besoin ? 
> 	- [ ] Lesquelles sont des entiers `int` ? 
> 	- [ ] Lesquelles sont des nombres à virgule `float` ? 
> 	- [ ] Autres ? 

## Niveau 2 
Même chose avec gestion des stocks

>[!warning] Cahier des charges - Pause Tacos - Niveau 2
> - [ ] Même cahier des charges que le niveau 1 auquel s'ajoute :
> - [ ] Le restaurant a un stock limité. 
> 	- [ ] Après avoir demandé le nombre de tacos et de kebab :
> 		- [ ] Si le client demande un nombre négatif de l'un, l'autre ou les deux : 
> 			- [ ] affiche le message 
> 			```bash
> 			ERREUR : Valeurs négatives interdites.
> 			```
> 			- [ ] Arrête le programme sans autre affichage -> `return 1;`
> 		- [ ] Si les stocks sont insuffisant, le programme
> 			- [ ] affiche un message selon le tableau ci-dessous
> 			- [ ] affiche ensuite le message de remerciement du Niveau 1
> 		- [ ] Sinon, pas de changement par rapport au niveau 1
> 
> | Produit hors stock | Sortie attendue |
> |---|---|
> | Kebab | `Désolé, nous n'avons pas assez de Kebab`|
> | Tacos | `Désolé, nous n'avons pas assez de Tacos`|
> |Tacos et Kebab | `Désolé, nous n'avons pas assez de Tacos, ni de Kebab` |
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau2
> ```

## Bonus : Niveau 3

> [!warning] Cahier des charges - Pause Tacos - Niveau 3
> - [ ] Même cahier des charges que précédemment 
> - [ ] Si le client commande plus de 5 articles au total, une réduction de 10% est appliquée sur le montant total de la commande 
> - [ ] Les sorties attendues sont identiques aux cahiers des charges précédents
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau3
> ```
