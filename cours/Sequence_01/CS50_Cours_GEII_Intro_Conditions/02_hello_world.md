---
title: C01 - Hello world
description: Notes relatives au premier cours 
date: 2025-08-31
draft: false
weight: 102
---

# Hello, World : Premier programme

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

## Explications
Le programme précédent peut se décomposer de la façon suivante : 

- Import de la bibliothèque pour afficher du texte.  
```c
#include <stdio.h>
```

- Fonction principale :
```c
int main(void)
```   
    - Le contenu de cette fonction est compris entre les accolades : `{ ... }`  

- Appel de la fonction `printf`
```c
printf("...");  
```   
- `\n` demande un retour à la ligne.  
- En C, chaque instruction se termine par un `;`

## Compilation et exécution
`Encore une histoire de 1 et de 0 !`
Pour le moment, notre programme est écrit sous la forme de texte. Il est compréhensible par les humains (développeurs). Il faut, à présent, le convertir en un langage que le processeur comprend : des instructions binaires.

C'est le rôle du `compilateur` : Créer un fichier exécutable à partir d'un code `.c`. Dans ce module, cela se fera avec la commande `make`. Ensuite, on peut exécuter le programme.
```bash
make hello
./hello
```

> [!tip] Étapes  
> 1. `make hello` → compile.  
> 2. `./hello` → exécute.  

Résultat :  
```
hello, world
```

> [!warning] Erreurs fréquentes
> 
> - Oublier le `;` → erreur de compilation.  
> - Oublier `#include <stdio.h>` → `printf` inconnu.  
> - Écrire le texte à afficher sans guillemets → interprété comme variable.  
