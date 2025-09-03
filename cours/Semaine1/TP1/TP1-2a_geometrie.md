---
title: TP 1 - Un peu de géométrie
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 120
---
# Parlons surface ! 
## Premier calculs : aires et périmètres

> [!todo] Géométrie - Niveau1
> - [ ] Rendez-vous dans le dossier `tp1/2_geometrie`
> - [ ] Compléter le programme `rectangle.c` pour qu'il respecte le cahier des charges [Rectangle - Niveau 1](#aire-dun-rectangle)
> - [ ] Compléter le programme `cercle.c` pour qu'il respecte le cahier des charges [Cercle - Niveau 1](#aire-et-périmètre-dun-cercle)

### Aire d'un rectangle
> [!attention] Aire d'un rectangle
> - Le programme doit demander la largueur et la longueur du rectangle
> - Le programme calcule alors l'aire du rectangle. 
>
> **Sortie attendue :**
> | Entrée 1 | Entrée 2 |  Affichage attendue | 
> | --- | --- | --- |
> | `<largeur>` | `<longueur>` | Aire : `<aire>` |  
> Avec `<aire>` L'aire du rectangle **arrondie au centième**.
> 
> **Exemples de tests :**  
> | Entrée 1 | Entrée 2 |  Affichage attendue | 
> | --- | --- | --- |
> | 10 | 13 | Aire : 130.00 | 
> | 5.5 | 3 | Aire : 16.50 |
>---
> **Check :** 
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/2_geometrie/rectangle/niveau1
> ```





### Aire et périmètre d'un cercle

> [!attention] Cercle Niveau 1  
> - Le programme doit demander le rayon du cercle puis afficher l'aire et le périmètre. 
> 
> Avec [aire] et [perimetre] respectivement l'aire et le périmètre du cercle. 
> 
> **Sortie attendue :**
> | Entrée |   Affichage attendue | 
> | --- |  --- |
> | `<rayon>` |  Aire : `<aire>`<br>Périmètre : `<perimetre>` |  
> Avec `<aire>` et `<perimetre>` **arrondis au centième**.
> 
> **Exemples de tests :**  
> | Entrée 1 |   Affichage attendue | 
> | --- |  --- |
> | 10 |  Aire : 314.16 <br>Périmètre : 62.83 |
>
>  ---
> **Check :** 
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/2_geometrie/cercle/niveau1
> ```







