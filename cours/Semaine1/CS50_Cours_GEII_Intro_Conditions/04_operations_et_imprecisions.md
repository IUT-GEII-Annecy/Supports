---
title: C01 - Opérations mathématiques 
description: Notes relatives au premier cours 
date: 2025-08-31
draft: false
weight: 104
---

# Quelques opérateurs mathématiques 

En C, on dispose d’opérateurs de base pour manipuler des nombres.  
Pour des calculs plus avancés (racines, puissances, arrondis…), il existe la bibliothèque standard `math.h`.  
Elle fournit de nombreuses fonctions que l’on peut appeler dans nos programmes.
## Opérateurs

| Symbole | Opération                             |
|---------|---------------------------------------|
| `+`     | addition                              |
| `-`     | soustraction                          |
| `*`     | multiplication                        |
| `/`     | division                              |
| `%`     | modulo (reste de la division entière) |

```c
int a = 7;
int b = 2;
printf("a / b = %i\n", a / b); // !! Affiche 3 !!
printf("a %% b = %i\n", a % b);
```

> [!warning] Attention  
> La division entre entiers **supprime la partie décimale**.  

## Fonctions usuelles de `math.h`

Vous pourrez trouver plus de fonctions usuelles (mathématiques ou non) sur le site [manual.cs50.io](https://manual.cs50.io/)
Pour utiliser ces fonctions, il faut inclure la bibliothèque `math.h`

```c
#include <math.h>
```

| Fonction   | Description                                   | Exemple       | Résultat |
|------------|-----------------------------------------------|---------------|----------|
| `sqrt(x)`  | Racine carrée de `x`                         | `sqrt(9)`     | `3.0`    |
| `pow(x,y)` | Puissance : `x` élevé à `y`                  | `pow(2, 3)`   | `8.0`    |
| `fabs(x)`  | Valeur absolue (flottant)                    | `fabs(-5.5)`  | `5.5`    |
| `floor(x)` | Arrondi par défaut (partie entière inférieure)| `floor(3.7)`  | `3.0`    |
| `ceil(x)`  | Arrondi supérieur                            | `ceil(3.2)`   | `4.0`    |
| `round(x)` | Arrondi à l’entier le plus proche            | `round(3.6)`  | `4.0`    |

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    printf("sqrt(9) = %.1f\n", sqrt(9));
    printf("pow(2, 3) = %.1f\n", pow(2, 3));
    printf("fabs(-5.5) = %.1f\n", fabs(-5.5));
    printf("floor(3.7) = %.1f\n", floor(3.7));
    printf("ceil(3.2) = %.1f\n", ceil(3.2));
    printf("round(3.6) = %.1f\n", round(3.6));
}
```
