# Boucles en C — while, for, do...while

> [!info] Objectifs
> - Comprendre le fonctionnement de la boucle concernée.
> - Savoir **quand** l'utiliser par rapport aux alternatives.
> - Éviter les boucles infinies et apprendre à **déboguer**.

## Une boucle, c'est quoi ?
Les boucles permettent de **répéter** un bloc d'instructions tant qu'une condition est vraie
(ou un compteur pas encore à terme).

## Exemple rapide : Miauler 3 fois avec `while`

```c
#include <stdio.h>
int main(void) {
    int i = 0;
    while (i < 3) {
        printf("Miaou !\n");
        i++;
    }
    return 0;
}
```
Ici, tant que `i` est inférieur à 3, on affiche "Miaou !" et on incrémente `i` de 1. 
Cela produit l'affichage suivant :
```bash
Miaou !
Miaou !
Miaou ! 
```


```c
#include <stdio.h>

int main(void) {
    int i = 0;
    while (i < 3) {
        printf("i = %d\n", i);
        i++;
    }
    return 0;
}
```



> [!warning] Pièges
> - Condition mal mise à jour ⇒ **boucle infinie**.
> - Off‑by‑one (`<` vs `<=`).
> - Variables modifiées **dans** la condition.

## Exercices flash
1. Afficher les nombres de 1 à 10 sur une ligne.
2. Somme des entiers de 1 à `n` (entré par l'utilisateur).
3. Lire jusqu'à ce que l'utilisateur tape `0`, puis afficher le comptage.