---
title: C01 - Les variables 
description: Notes relatives au premier cours 
date: 2025-08-31
draft: false
weight: 103
---
# Types et Variables
> [!info] Encore une histoire de binaire
>On l'a vu, toutes les données sont représentées sous forme binaire (des 1 et des 0). C'est aussi le cas pour les variables que l'on utilisera. 
>Or, l'ordinateur doit pouvoir déterminer s'il faut interpréter le mot binaire de cette variable comme un nombre, une lettre, une couleur ou autre.  
>
>Il donc faut préciser à quel type est associé chacune des variables que l'on déclare. 

## Les types de données en C

Chaque variable a un type précis :  
| Type    | Description                              | Exemple     |
|---------|------------------------------------------|-------------|
| `int`   | nombres entiers                          | `10`, `-5`  |
| `char`  | un seul caractère                        | `'a'`, `'Z'`|
| `float` | nombres décimaux approximatifs           | `3.14`      |
| `double`| nombres décimaux avec plus de précision  | `3.141592`  |
| `long`  | entiers plus grands que `int`            | `123456789` |
| `string`| texte (via la bibliothèque CS50)         | `"Hello"`   |
| `bool`  | vrai/faux (via la bibliothèque CS50)     | `true`      |


## Déclaration et utilisation

> [!info] Déclaration de variable  
> Syntaxe : `<type> <nom>;`  
> Exemple :  
> ```c
> int nombre;
> ```  
> On peut affecter une valeur en même temps :  
> ```c
> int nombre = 42;
> ```  

## Afficher une variable dans un texte 
Pour afficher une variable dans une phrase, on utilise `printf` avec un **placeholder**.  

```c
#include <stdio.h>

int main(void)
{
    int age = 20;
    printf("J'ai %i ans.\n", age);
}
```


### Placeholders courants

| Spécificateur | Description                           | Exemple d'utilisation                      | Sortie                |
|---------------|---------------------------------------|--------------------------------------------|-----------------------|
| `%i`          | entier                                | `printf("Valeur : %i\n", 42);`             | `Valeur : 42`         |
| `%f`          | flottant (nombre à virgule)           | `printf("Pi = %f\n", 3.141593);`           | `Pi = 3.141593`       |
| `%.2f`        | flottant arrondi à 2 décimales        | `printf("Pi = %.2f\n", 3.141593);`         | `Pi = 3.14`           |
| `%c`          | caractère                             | `printf("Lettre : %c\n", 'A');`            | `Lettre : A`          |
| `%s`          | texte (string)                        | `printf("Bonjour %s\n", "Alice");`         | `Bonjour Alice`       |


> [!example] Exemple  
> ```c
> float pi = 3.14159;
> printf("Pi = %.2f\n", pi);
> ```  
> Affiche : `Pi = 3.14`  


### Imprécision des flottants
Puisqu'ils sont codés sur un nombre de bits finis, les nombres à virgule ont une précision limitée : 

```c
float x = 1.0 / 10.0;
printf("%.20f\n", x);
```

Affiche par exemple :  
```
0.10000000149011611938
```

> [!tip] Conseil  
> Toujours limiter l’affichage des décimales avec `%.2f`, `%.3f`, etc.  