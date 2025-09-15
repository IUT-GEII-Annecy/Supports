# Archive — Boucles (while, for, do…while)

Ce paquet reprend **la structure** et **le style** de l'archive *Intro_Conditions*,
en l'appliquant aux **boucles**.

## Contenu
- `00_intro/intro.md` — rappel des objectifs, quand utiliser une boucle
- `01_while/while.md` — boucle `while` (schéma, pièges, exemples)
- `02_for/for.md` — boucle `for` (schéma, incréments, portées)
- `03_do_while/do_while.md` — boucle `do…while` (menus, saisie sécurisée)
- `04_comparatif/comparatif.md` — choisir la bonne boucle
- `05_erreurs_courantes/pitfalls.md` — erreurs fréquentes et debug
- `exemples/` — petits programmes commentés
- `exercices/` — exercices progressifs + corrigés minimalistes
- `assets/` — schémas (placeholders)

## Pré‑requis
- Variables, conditions (`if`, `else if`, `else`), opérateurs de comparaison

## Compilation (CS50 / gcc)
```bash
make program    # si Makefile fourni
# ou :
gcc -Wall -Wextra -Werror -std=c17 -o program program.c
```