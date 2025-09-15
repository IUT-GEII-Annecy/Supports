---
title: TP 2 - Se répéter - Les boucles
description: Ce premier TP est une introduction à la programmation.
date: 2025-09-22
draft: false
weight: 101
---

# Nos premières boucles While, For et Do...While

## Miauler n fois. 

> [!todo] Un chat qui miaule
> Le programme `miauler.c` contient le code suivant, qui fait miauler un chat 3 fois :
> ```c
> #include <stdio.h>
> int main(void) {
>     int i = 0;
>     while (i < 3) {
>         printf("Miaou !\n");
>         i++;
>     }
>     return 0;
> }
> ```
> - [ ] Tester le programme miauler.c
> - [ ] Modifier le programme pour qu'il miaule 5 fois.
> - [ ] Modifier le programme pour qu'il miaule `n` fois, où `n` est un entier entré par l'utilisateur.
> --- 
> check50 IUT-GEII-Annecy/squelettes/branch-2025/tp3/animaux/while

> [!todo] Un chien qui aboie
> Le programme `aboyer.c` contient le code suivant, qui fait aboyer un chien 3 fois :
> ```c
> #include <stdio.h>   
> int main(void) {
>     for (int i = 0; i < 3; i++) {
>         printf("Ouaf !\n");
>     }
>     return 0;
> }
> ```
> - [ ] Tester le programme aboyer.c
> - [ ] Modifier le programme pour qu'il aboie 5 fois.
> - [ ] Modifier le programme pour qu'il aboie `n` fois, où `n` est un entier entré par l'utilisateur.
> ---
> check50 IUT-GEII-Annecy/squelettes/branch-2025/tp3/animaux/for

> [!todo] Un oiseau qui chante
> Le programme `chanter.c` contient le code suivant, qui fait chanter un oiseau 3 fois :
> ```c
> #include <stdio.h>
> int main(void) {
>     int i = 0;
>     do {
>         printf("Cui-cui !\n");
>         i++;
>     } while (i < 3);
>     return 0;
> }
> ```
> - [ ] Tester le programme chanter.c
> - [ ] Modifier le programme pour qu'il chante 5 fois.
> - [ ] Modifier le programme pour qu'il chante `n` fois, où `n` est un entier entré par l'utilisateur.
> ---
> check50 IUT-GEII-Annecy/squelettes/branch-2025/tp3/animaux/do_while

Question : Rappeler le principe de chaque boucle et, pour chacune, dire quand elle est le plus adaptée. 


## Exercice 1 — Compter jusqu'à 10
Util
> [!tip] Indice
