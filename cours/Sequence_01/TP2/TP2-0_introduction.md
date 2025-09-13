---
title: TP 2 - Un cas simple
description: Quelques switch cases
date: 2025-08-31
draft: false
weight: 1
---

> [!important] Le type `char`
> Dans cet exercice, vous aurez besoin de demander un caractère simple. Le type le plus adapté est le type `char`. 
> C'est un type qui peut contenir un caractère codé sur 1 octet (ASCII)
> 
> **Attention** : En langage C, un caractère s'entoure d'apostrophes `' '` et non avec des guillements.
> *Exemple :* `char caractere = 'A'`

# Convertisseur de température - Echauffement ! 
## Exercice 1 : Conversion Celsius - Fahrenheit 
On souhaite créer un programme permettant de convertir une température en degrés Celsius en degrés Fahrenheit et vice versa.

On donne la formule de conversion suivante : 
- Pour convertir des degrés Celsius (C) en degrés Fahrenheit (F) : F = C * 9/5 + 32

Question : Donner la formule de conversion inverse (Fahrenheit vers Celsius).

> [!todo] Conversion de température
> Dossier : 1_conversion
> Le programme affichera un menu permettant à l'utilisateur de choisir entre deux options : 
> - F : Convertir Celsius en Fahrenheit
> - C : Convertir Fahrenheit en Celsius
> L'utilisateur entrera son choix (F ou C) puis appuiera sur Entrée. Ensuite, le programme demandera la température à convertir.
> Le programme effectuera la conversion et affichera le résultat.
> **Attention :** Le choix de l'opération doit être fait avec un `switch case`. Structure `if` interdite.
>
> La dernière sortie doit être de la forme : 
> `<temperature_utilisateur> <unite_utilisateur> = <temperature_convertie> <unite_convertie> 
>
> Exemple d'exécution :
> ```bash
> Choisissez l'opération (F pour Celsius->Fahrenheit, C pour Fahrenheit->Celsius) :
> F 
> Entrez la température en degrés Celsius :
> 25
> 25.00 C = 77.00 F
> ```
> ---
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp2/temperatures


# Calculatrice - Entrainement ! 
On souhaite créer une calculatrice basique qui effectue les opérations addition, soustraction, multiplication et division. 


## Niveau 1 : Opérations
> [!todo] Calculatrice 
> Dossier : 2_calculatrice 
> Écrire un programme qui demande à l'utilisateur un nombre, une opération (addition, soustraction, multiplication, division), puis un second nombre. **L'utilisateur appuiera sur Entrée après chaque nombre/opération**.
> Pour choisir l'opération, l'utilisateur entrera `+`, `-`, `*`ou `/` respectivement. 
> Le programme affichera alors l'opération et son résultat sur une ligne
> 
> | Entrée 1 | Entrée 2 | Entrée 3 | Sortie |
> | --- | --- | --- | --- |
> | `<n1>` | `<operation>` | `<n2>` | `<n1> <operation> <n2> = <resultat>` |
>
> Avec `<n1>` et `<n2>` les deux nombres entrés par l'utilisateur, `<operation>` l'opération choisie et `<resultat>` le résultat de l'opération.
> **Attention :** Le choix de l'opéaration doit être fait avec un `switch case`. Structure `if` interdite. 
> Exemple : 
> ```bash
> Bonjour, entrez votre opération : 
> 3
> * 
> 2
> Merci. Voici le résultat de votre opération : 
> 3 * 2 = 6
> ```
> --- 
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp2/calculatrice/niveau1

## Niveau 2 : Gestion des erreurs

> [!todo] Gestion des erreurs
> - [ ] Ajouter la gestion des erreurs dans le programme de la calculatrice
>     - Si l'utilisateur entre une opération invalide, le programme doit afficher `ERREUR : Opération invalide` et terminer.
>     - Si l'utilisateur entre une division par zéro, le programme doit afficher `ERREUR : Division par zéro` et terminer.
> L'utilisation de `if` est autorisé pour cette partie.
> - [ ] Après avoir vérifié manuellement votre programme, faire valider par l'enseignant. 
> ---
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp2/calculatrice/niveau2










