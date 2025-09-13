---
title: TP 2 - Séquences de contrôle - suite
description: Ce TP explore la structure switch case
date: 2025-09-10
draft: false
weight: 1
---


Une structure de contrôle permet de modifier le flux d'exécution d'un programme en fonction de conditions ou de répétitions.
Nous avons déjà vu les structures conditionnelles `if`, `else if` et `else` dans le TP précédent.
Dans ce TP, nous allons explorer une autre structure conditionnelle : `switch case`.


> [!important] La structure `switch case`
> La structure `switch case` est utilisée pour sélectionner l'une parmi plusieurs options basées sur la valeur d'une expression.
> Elle est particulièrement utile lorsque vous avez de nombreuses conditions basées sur la même variable.
> Voici la syntaxe de base d'une structure `switch case` en C :
> ```c
> switch (expression) {
>     case valeur1:
>         // Code à exécuter si expression == valeur1
>         break;
>     case valeur2:
>         // Code à exécuter si expression == valeur2
>         break;
>     // Vous pouvez avoir autant de cases que nécessaire
>     default:
>         // Code à exécuter si aucune des valeurs ne correspond
> }
> ```
> - `expression` est évaluée une fois et comparée aux valeurs dans chaque `case`.
> - Si une correspondance est trouvée, le code associé à ce `case` est exécuté.
> - Le mot-clé `break` est utilisé pour sortir de la structure `switch` après l'exécution d'un `case`. Sans `break`, l'exécution continue dans les `case` suivants (ce comportement est appelé "fall-through").
> - Le `default` est optionnel et s'exécute si aucune des valeurs ne correspond.

## Exercice 0 : Exemple de `switch case`
Compléter l'exemple suivant de `switch case` pour afficher le jour de la semaine en fonction d'un numéro (1 pour lundi, 2 pour mardi, etc.) :

```c
#include <cs50.h>
#include <stdio.h>
int main() {
    int jour; // Variable pour stocker le numéro du jour
    jour = get_int("Entrez un numéro de jour (1-7) : ");

    switch (jour) {
        case 1:
            printf("Lundi\n");
            break;
        case 2:
            // Compléter pour les autres jours
        default:
            printf("Numéro de jour invalide. Veuillez entrer un nombre entre 1 et 7.\n");
    }
}
```
