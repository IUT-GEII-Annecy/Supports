---
title: C01 - Les conditions
description: Notes relatives au premier cours 
date: 2025-08-31
draft: false
weight: 101
---

# Les conditions en C

En C, les conditions permettent d'exécuter certaines parties du programme uniquement si des critères sont vérifiés.

## Structure générale : if / else



```c
if (<condition1>) // Si la condition 1 est vraie
{
    // Partie exécutée si la <condition1> est vérifiée
}
else if (<condition2>) // Sinon, si la condition 2 est vraie
{
    // Partie exécutée si la <condition2> est vérifiée
}
else // Sinon, dans tous les autres cas
{
    // Partie exécutée par défaut
}
```

La structure `if` peut prendre plusieurs formes : 

- `if` seul
- `if` puis `else`
- `if` puis `else if` puis `else`

On peut placer autant de `else if` que l'on veut à la suite.
## Opérateurs de comparaison

Les comparaisons sont faites à l'aide des opérateurs suivants :

| Symbole | Signification       | Exemple (`x=5`, `y=10`) | Résultat |
|---------|---------------------|--------------------------|----------|
| `==`    | égal                | `x == 5`                | vrai     |
| `!=`    | différent           | `x != y`                | vrai     |
| `<`     | inférieur           | `x < y`                 | vrai     |
| `>`     | supérieur           | `x > y`                 | faux     |
| `<=`    | inférieur ou égal   | `x <= 5`                | vrai     |
| `>=`    | supérieur ou égal   | `y >= 11`               | faux     |

> [!warning] Piège ! Ne pas confondre affectation et comparaison  
> L'opérateur `=` sert à affecter une variable et l'opérateur `==` sert à comparer deux variables ! Si vous les confondez, rien ne fonctionnera...

## Opérateurs logiques

On peut combiner plusieurs conditions avec les opérateurs logiques :

| Symbole | Signification | Exemple (x=5, y=10)          | Résultat attendu |
|---------|---------------|------------------------------|------------------|
| `&&`    | ET logique    | `(x > 0 && y < 20)`          | vrai             |
| `\|\|`    | OU logique    | `(x < 0 \|\| y > 100)`         | vrai             |

```c
if ((x > 0) && (x < 10))
{
    printf("x est compris entre 0 et 10\n");
}

if ((x < 0) || (x > 100))
{
    printf("x est en dehors de l'intervalle [0,100]\n");
}
```

## Un exemple simple

Si `x` est une variable entière, le code suivant vérifie si `x` est positif, négatif ou nul.

```c
if (x > 0)
{
    printf("x est positif\n");
}
else if (x < 0)
{
    printf("x est négatif\n");
}
else
{
    printf("x vaut zéro\n");
}
```
