---
title: TP 1 - Hello World
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 102
---

# Votre premier programme : Hello World

## Hello World en C    

> [!todo] Hello World
> Trois étapes sont nécessaires pour créer un Hello World en langage C : 
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

> [!tip] Besoin d'aide ?
> CS50 Duck Debugger est là pour vous aider ! 
> Cliquer sur l'icône en forme de canard dans la colonne de gauche pour ouvrir l'extension.
> Vous pouvez lui demander "En Français" à la fin de votre prompt pour obtenir de l'aide en français.  S'il vous dit qu'il ne parle qu'anglais, insistez, il finit souvent par abdiquer. 



> [!todo] Compiler et exécuter le programme 
> - [ ] Dans le terminal, assurez-vous d'être dans le dossier `TP1/0_hello` (où se trouve votre fichier `hello.c` -- sinon, utilisez la commande `cd` pour naviguer jusqu'à ce dossier).
> - [ ] Compiler le programme avec la commande `make hello`. 
> - [ ] Exécuter le programme compilé avec la commande `./hello`. Vous devriez voir "Hello, World!" s'afficher dans le terminal.
> [![asciicast](https://asciinema.org/a/69XbpUL0KsVsH9V9FqBNHuNUf.svg)](https://asciinema.org/a/69XbpUL0KsVsH9V9FqBNHuNUf)
> - Si vous voyez le message, félicitations ! Vous venez d'écrire   votre premier programme en C. **Dans le cas contraire, demandez de l'aide à l'enseignant, à vos camarades ou au CS50 Duck Debugger.**