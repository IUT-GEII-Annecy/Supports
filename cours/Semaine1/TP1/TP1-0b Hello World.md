---
title: TP 1 - Variables
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 102
---

# Votre premier programme : Hello World

## Hello World en C    

> [!todo] Écrire le programme Hello World se fait en trois étapes :
> 1. Inclure la bibliothèque standard d'entrée/sortie (`stdio.h`). -> Ecrire `#include <stdio.h>` en haut du fichier
> 2. Définir la fonction principale `main`. -> `int main(void) { ... }`
> 3. Utiliser la fonction `printf` à l'intérieur de la fonction main pour afficher le message.
> 	```c
>   printf("Hello, World!\n");
>   ```
> 4. Ajouter `return 0;` à la fin pour indiquer que le programme est terminé. 

Votre programme devra donc ressembler à ça : 
```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");
    return 0;
}
```

> [!todo] Compiler et exécuter le programme 
> - [ ] Dans le terminal, assurez-vous d'être dans le dossier `TP1` où se trouve votre fichier `hello.c`. (Sinon, utilisez la commande `cd` pour naviguer jusqu'à ce dossier.
> - [ ] Compiler le programme avec la commande `make hello`. Cette commande utilise le Makefile fourni par cs50 pour compiler le code C.    
> - [ ] Exécuter le programme compilé avec la commande `./hello`. Vous devriez voir "Hello, World!" s'afficher dans le terminal.
> ```bash
> make hello
> ./hello
> ```
> - Si vous voyez le message, félicitations ! Vous venez d'écrire   votre premier programme en C. **Dans le cas contraire, demandez de l'aide à l'enseignant, à vos camarades ou au CS50 Duck Debugger.**