---
title: TP 2 - Validateur de date
description: On met en pratique 
date: 2025-09-10
draft: false
weight: 11
---

# Validateur de date - Prêt ? Feu.. Partez ! 

## Niveau 1 — Valider une date (jour/mois/année)

> [!todo] Validateur de date  
> **Dossier :** `2_dates`  
> Écrire un programme qui lit trois entiers dans cet ordre : **jour**, **mois**, **année** (l’utilisateur appuie sur Entrée après chaque saisie).  
> Le programme doit **vérifier** si la date est **valide** en tenant compte des différentes longueurs de mois **et** des **années bissextiles**.  
> 
> **Contraintes / attentes :**
> - Utiliser un **`switch (mois)`** pour déterminer **le nombre de jours** dans le mois (`maxJours`).  
> - Penser aux cas particuliers : 
>   - Le `mois` doit être valide
>   - Le `jour` doit exister (attention aux années bixestiles)
>   - 
> - **Affichages attendus :**
>   - Si la date est valide : `Date valide`
>   - Sinon : `ERREUR : Date invalide.`
>
> **Rappels utiles :**  
> - **Année bissextile** :  
>   Une année est bissextile si l'une de ces deux conditions est remplie : 
>   - L'année est un mutiple de 400
>   - L'année est un multiple de 4 mais pas un multiple de 100. 
>   `(année % 400 == 0) || (année % 4 == 0 && année % 100 != 0)`
> - **Longueur des mois** (hors février) :  
>   - 31 jours : 1, 3, 5, 7, 8, 10, 12  
>   - 30 jours : 4, 6, 9, 11
>
> **Exemples d’exécution :**
> ```text
> Entrez le jour :
> 29
> Entrez le mois :
> 2
> Entrez l'année :
> 2024
> Date valide
> ```
> ```text
> Entrez le jour :
> 31
> Entrez le mois :
> 4
> Entrez l'année :
> 2025
> ERREUR : Date invalide.
> ```
>
> **Types conseillés :** `int` pour jour, mois, année.  
> **Pas de boucles ni de tableaux** nécessaires pour ce niveau.
>
> ---
> check50 `IUT-GEII-Annecy/exercices/2025/info1/tp2/date_validator/niveau1`

> [!tip] Structure possible (pseudo‑code)
> 1) Lire `jour`, `mois`, `annee`  
> 2) `Si mois n'est pas entre 1 et 12` → invalide  
> 3) `switch (mois)` → donner `maxJours` (28 par défaut pour février)  
> 4) `Si l'année est bissextile` → `maxJours = 29`  
> 5) `Si le jour est plus grand que maxJours (ou inférieur à 1)` → invalide, sinon valide

---

## Niveau 2 — Ajouter la saison (météorologique)

> [!todo] Saison (en plus de la validation)  
> **Dossier :** `2_date`  
> Reprendre le programme du **Niveau 1**. S’il détecte une **date valide**, il doit **afficher** la **saison météorologique** correspondante en **France** :  
> - **Printemps** : du **21 mars** au **20 juin**  
> - **Été** : du **21 juin** au **20 septembre**  
> - **Automne** : du **21 septembre** au **20 décembre**  
> - **Hiver** : du **21 décembre** au **20 mars**  
> 
> - **Affichages attendus :**
>   - Si la date est valide :  
>     `Date valide` (à la ligne suivante) `Saison : <saison>`  
>   - Sinon : `ERREUR : Date invalide`
>
> **Exemples d’exécution :**
> ```text
> Entrez le jour :
> 15
> Entrez le mois :
> 6
> Entrez l'année :
> 2025
> Date valide
> Saison : Été
> ```
> ```text
> Entrez le jour :
> 1
> Entrez le mois :
> 12
> Entrez l'année :
> 2025
> Date valide
> Saison : Hiver
> ```
>
> ---
> check50 `IUT-GEII-Annecy/exercices/2025/info1/tp2/date/niveau2`

