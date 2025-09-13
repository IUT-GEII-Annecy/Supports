---
title: C01 - Concepts généraux
description: Notes relatives au premier cours 
date: 2025-08-31
draft: false
weight: 100
---

# Introduction à l’informatique
## Objectifs généraux   

L'objectif de ce module est, avant tout, d'apporter des compétences de réflexion pour la résolution de problèmes. En effet, écrire un code informatique, c'est d'abord écrire un algorithme qui répond à une problématique.

Durant ce module, nous verrons le langage C car il est suffisamment bas niveau pour illustrer le fonctionnement des systèmes informatiques. C'est, par ailleurs, le langage utilisé pour développer les systèmes embarqués.


## Systèmes de comptage  
### Le système unaire  

Quand on compte sur nos doigts, on utilise un système **unaire** (base 1) :  
- Chaque doigt levé représente une unité.  
- Exemple : 3 doigts levés = le nombre 3.  

### Le système binaire  

En binaire, chaque chiffre (appelé **bit**) peut prendre deux valeurs :  
- `0` → inactif, éteint, faux  
- `1` → actif, allumé, vrai  

> [!example] Exemple des ampoules  
> Si on a **3 ampoules** qui peuvent être allumées (1) ou éteintes (0) :  
> - `000` = 0  
> - `001` = 1  
> - `010` = 2  
> - ...  
> - `111` = 7  
>   
> Avec 3 ampoules, on peut donc compter de 0 à 7.  

> [!info] A retenir : Le binaire en informatique
> Tous les systèmes informatiques utilisent le binare pour encoder toutes les informations 
> Les données sont stoquée grâce à des **transistors** qui se comportent comme de minuscules interrupteurs.  

### L’octet  

Historiquement, les données étaient envoyées par groupes de 8 bits sur les bus des premiers processeurs. 
Ces groupes ont été appelés des `octet` (`oct` pour "huit" et `et` pour "petit").
C'est depuis devenu une unité de mesure de la taille des données (octet, kilo-octet, Mega-octet, etc.).

> [!info] A retenir : Un octet (byte)
> Un octet est un groupe de huit bits. Il peut représenter 256 valeurs différentes (de 0 à 255).  
> - Exemple :  
>  - `00000101` = 5  
>  - `11111111` = 255  

### Conversion en décimal 
Chaque bit a un **poids** qui correspond à une puissance de 2 :  

| 2^7<br> 128 | 2^6<br>  32 | 2^5<br> 64  | 2^4<br> 16  | 2^3<br> 8   | 2^2 <br> 4 | 2^1<br> 2 | 2^0 <br>1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |

> [!example] Exemple  
> | 2^7<br> 128 | 2^6<br>  32 | 2^5<br> 64  | 2^4<br> 16  | 2^3<br> 8   | 2^2 <br> 4 | 2^1<br> 2 | 2^0 <br>1 |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> |  0  |  1  |  0  |  0  |  1  |  0  |  0  |  1  |
> `01001001` = 64 + 8 + 1 = **73**  

## Représentation de l’information  
Pour résumer : un système informatique n'a qu'une seule façon d'encoder une information : le binaire.

Pour chaque type de données, une convention est mise en place pour savoir comment un ordinateur comprendra cette information.
Que ce soit pour manipuler un nombre entier, un nombre à virgule, du texte, une image, une vidéo, du sons, ou n'importe quel type de donnée, un système informatique utilisera des 0 et des 1 pour le représenter. 

Quelques exemples sont donnés dans cette section 
### ASCII : Représenter du texte

- Les lettres peuvent être codées en binaire via la norme **ASCII**, qui associe des nombres aux caractères. Par exemple, `A` correspond à 65 : `01000001`.  
- Exemple : un message texte pourrait avoir pour valeurs binaires 72, 73 et 33, correspondant aux caractères `H`, `I` et `!`.  
- Voici une carte étendue des valeurs ASCII (0 à 127).  

![Table ASCII](ASCII-Table.png)

### Unicode : Représenter plus de caractères

- Le binaire traditionnel ne permettait pas de représenter tous les caractères humains. **Unicode** a donc étendu ce système (plus de bits), intégrant notamment les lettre avec accents, les symbôles de nombreuse langues ainsi que des emoji.  
- Chaque plate-forme peut afficher les emoji différemment. 

### RGB : Représenter les couleurs

- Les images numériques se construisent à partir de trois composantes : Rouge, Vert, Bleu (**RGB**).  
- Si on prend les valeurs 72, 73 et 33 (les mêmes que pour “HI!”), on obtient une nuance de jaune clair.  
- Une image est simplement une collection de ces valeurs RGB. Une vidéo = une séquence d’images. La musique peut être codée de manière similaire. 


## Algorithmes  

Un **algorithme** est une suite d’instructions logiques, organisées et ordonnées, permettant la résolution d'un problème. 

Ce problème peut être très simple (ex : *Compter le nombre d'étudiant* ), ou très complexe (ex : *Générer une image à partir d'un prompt de l'utilisateur*)

> [!info] Propriétés d’un algorithme  
> - **Lisible** : Il doit être compréhensible par tout le monde. 
> - **Exécutablee** : Chaque étape doit correspondre à une opération logique ou mécanique que le système peut réaliser
> - **Fini** : L'algorithme doit pouvoir aboutir à une solution après un nombre fini d'étapes.  
> - **Déterministe** : A chaque étape, pour des entrées données, un seul chemin doit être possible
> - **Détermination** : Avec les même conditions, un algotithme doit toujours produire les même résultats. *(Cette propriété ne s'applique pas aux algorithmes probabilistes, type IA)*

### Exemples d’algorithmes  

- **Dans la vie quotidienne :**  
  - Une recette de cuisine (étapes précises à suivre).  
  - Changer une roue (suite d’actions logiques).  

- **En informatique :**  
  - Trier des cartes par ordre croissant.  
  - Chercher un nom dans un annuaire.  

> [!example] Algorithme de recherche dichotomique  
> 1  Prendre l'annuaire
> 2  Ouvrir l'annuaire au milieu 
> 3  Chercher la personne dans la page
> 4  *Si* la personne se trouve dans la page
> 5      Appeler la personne
> 6  *Sinon, si* la personne se trouve plus tôt dans l'annuaire (alphabétiquement)
> 7      Ouvrir le livre au milieu de la partie gauche
> 8      Retourner à l'étape 3
> 9  *Sinon, si* la personne se trouve plus tard dans l'annuaire (alphabétiquement)
> 10     Ouvrir le livre au milieu de la partie droite
> 11     Retourner à l'étape 3
> 12 *Sinon*
> 13     Quitter *(La personne n'a pas été trouvée dans l'annuaire)*

C’est un **algorithme efficace** : au lieu de parcourir chaque nom un par un, on élimine la moitié des candidats à chaque étape.  
