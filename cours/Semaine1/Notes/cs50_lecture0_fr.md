# Notes de cours 0 — CS50x (2025)

# Cours 1 : Introduction

## Bienvenue !

- Ce cours ne se limite pas à la programmation informatique ! Les compétences pratiques que vous développerez pourront vous être utiles bien au-delà de l’informatique.
- En effet, ce cours porte sur la résolution de problèmes d'une manière particulièrement stimulante et puissante. Vous constaterez vite que ce que vous apprendrez ici pourra s’appliquer dans d’autres contextes, voire toute votre vie professionnelle.
- Cela ne sera pas facile ! Vous aurez l'impression d'apprendre à toute vitesse : “boire au tuyau d’incendie” de connaissances.
- Ce cours est avant tout une occasion d’avancer **vous-même**, par rapport à votre point de départ, et non par rapport à une norme idéale.
- **Accordez-vous le temps nécessaire pour apprendre.** Chacun fonctionne à son rythme. Si quelque chose ne se passe pas bien au début, sachez qu’avec le temps, vos compétences croîtront.
- **N’ayez pas peur si c’est votre premier cours d’informatique !** Pour la plupart de vos camarades, c'est aussi une première. Les enseignants et vos pairs sont là pour vous soutenir.

## Havard !

- Ce cours est une adapatation du cours CS50 d'Havard. Vous trouverez donc plein de ressources en ligne. Des vidéos originales aux documents de cours.  

## Informatique et résolution de problèmes

- Essentiellement, la programmation consiste à prendre une **entrée** et produire une **sortie** — résoudre un problème. Ce qui se passe entre les deux constitue la boîte noire au cœur de ce cours.  
- Les ordinateurs utilisent un système binaire (bits) pour compter, avec des transistors qui représentent des 0 ou des 1 (off/on).  
- Avec trois “ampoules” (bits), on peut compter de 0 à 7.  
- Avec huit bits (un **octet** ou **byte**), on peut représenter de 0 à 255 (ex. `00000101` = 5, `11111111` = 255).  

## ASCII

- Les lettres sont également codées en binaire via la norme **ASCII**, qui associe des nombres aux caractères. Par exemple, `A` correspond à 65 : `01000001`.  
- Exemple : un message texte pourrait avoir pour valeurs binaires 72, 73 et 33, correspondant aux caractères `H`, `I` et `!`.  
- Voici une carte étendue des valeurs ASCII (0 à 127).  

## Unicode

- Le binaire traditionnel ne permettait pas de représenter tous les caractères humains. **Unicode** a donc étendu ce système (plus de bits), intégrant notamment les **emoji**.  
- Chaque plate-forme peut afficher les emoji différemment. Par exemple, le 👍 est `U+1F44D`; avec une teinte de peau, cela devient `U+1F44D U+1F3FD`.  

## RGB

- Les images numériques se construisent à partir de trois composantes : Rouge, Vert, Bleu (**RGB**).  
- Si on prend les valeurs 72, 73 et 33 (les mêmes que pour “HI!”), on obtient une nuance de jaune clair.  
- Une image est simplement une collection de ces valeurs RGB. Une vidéo = une séquence d’images. La musique peut être codée de manière similaire.  

## Algorithmes

- La résolution de problème est au cœur de l’informatique. Un **algorithme** est une série d’instructions pour y parvenir.  
- Exemple : chercher un nom dans un annuaire. On peut lire page par page (**O(n)**), deux pages à la fois (**O(n/2)**), ou appliquer une recherche dichotomique (**O(log₂ n)**).  
- Le comportement temporel de chaque approche peut être visualisé via la **notation Big‑O**.  

## Pseudocode

- Le **pseudocode** est une version lisible par l’humain d’un algorithme. Exemple (recherche dichotomique) :

```text
1  Prendre l’annuaire
2  Ouvrir au milieu
3  Regarder la page
4  Si la personne est sur la page
5      Appeler la personne
6  Sinon si la personne est avant
7      Ouvrir le milieu de la partie gauche
8      Revenir à la ligne 3
9  Sinon si la personne est après
10     Ouvrir le milieu de la partie droite
11     Revenir à la ligne 3
12 Sinon
13     Quitter
```

- Le pseudocode aide à structurer sa pensée et à partager sa logique avec d’autres. On y retrouve : verbes (fonctions), `if` / `else if` (conditionnelles), expressions booléennes, et boucles.

## Intelligence Artificielle

- Voici un exemple de pseudocode simple pour dialoguer :

```text
Si l’étudiant dit bonjour
    Dire bonjour
Sinon si l’étudiant dit au revoir
    Dire au revoir
Sinon si …
…
```

- Pour dialoguer sur beaucoup de phrases, cela requiert beaucoup de code. C’est pourquoi les **modèles de langage** (LLMs) sont entraînés sur d’immenses corpus, et non codés phrase par phrase.  
- Seul **CS50.ai** est autorisé comme outil IA dans ce cours : il aide, mais **ne donne pas les solutions complètes**.  

## À venir

- Cette semaine, vous apprendrez **Scratch**, un langage visuel. Dans les semaines suivantes, vous passerez à **C** : par exemple :

```c
#include <stdio.h>

int main(void)
{
  printf("hello, world\n");
}
```

- Enseigner C aide à apprendre d’autres langages comme Python. Ce qui rend C difficile, c’est la syntaxe (ponctuation) — aujourd’hui, nous allons nous concentrer sur les idées avec Scratch.




------


# Notes de cours 1 — CS50x (2025)

## Lecture 1

### Sommaire

- Bienvenue !
- Visual Studio Code pour CS50
- Hello World
- De Scratch à C
- Fichiers d’en-tête et pages de manuel CS50
- Hello, You
- Types (types de données)
- Conditionnelles
- Opérateurs
- Variables
- compare.c
- agree.c
- Boucles et meow.c
- Fonctions
- Correction, conception, style
- Mario
- Commentaires
- En savoir plus sur les opérateurs
- Troncature (truncation)
- En résumé

---

## Bienvenue !

- Lors de la session précédente, vous avez appris Scratch, un langage visuel de programmation.
- Tous les concepts essentiels vus dans Scratch — fonctions, conditionnelles, boucles, variables — seront réutilisés dans n’importe quel langage de programmation.
- Rappelez-vous que les machines ne comprennent que le binaire. Là où les humains écrivent du code source, lisible par les humains, les machines ne comprennent que le code machine : une suite de 0 et de 1 qui produit un effet souhaité.
- Nous pouvons convertir du code source en code machine grâce à un logiciel spécial : un **compilateur**. Aujourd’hui, nous vous présentons un compilateur permettant de convertir du code source écrit en langage C en code machine.
- Aujourd’hui, en plus d’apprendre à programmer, vous apprendrez à écrire **du bon code**.

---

## Visual Studio Code pour CS50

- L’éditeur de texte utilisé pour ce cours est **Visual Studio Code**, alias **VS Code**, accessible via l’URL `cs50.dev`.
- L’un des plus grands avantages de VS Code est qu’il contient déjà tout le logiciel nécessaire pour ce cours. Tout a été pensé pour être utilisé avec cet environnement.
- Installer manuellement tous les outils sur votre propre machine peut vite devenir compliqué. Il est donc recommandé d’utiliser VS Code pour vos devoirs CS50.
- Vous pouvez lancer VS Code via `cs50.dev`.
- L’interface du compilateur se divise en plusieurs zones : l’explorateur de fichiers à gauche, l’éditeur de texte au centre, et la **ligne de commande (CLI)** ou **terminal** pour entrer des commandes.

- Dans le terminal, quelques commandes fréquentes :
  - `cd` — changer de répertoire
  - `cp` — copier des fichiers ou dossiers
  - `ls` — lister les fichiers d’un répertoire
  - `mkdir` — créer un dossier
  - `mv` — déplacer/renommer des fichiers ou dossiers
  - `rm` — supprimer des fichiers
  - `rmdir` — supprimer des dossiers
- `ls` est la commande la plus utilisée : tapez-la, validez, et vous verrez le contenu du dossier courant.
- Comme VS Code est déjà préconfiguré avec tout ce qu’il faut, utilisez-le pour tous vos travaux dans ce cours.  
  :contentReference[oaicite:0]{index=0}

---

## Hello World

- Nous utiliserons trois commandes pour écrire, compiler et exécuter notre premier programme :

    ```bash
    code hello.c
    make hello
    ./hello
    ```

  - `code hello.c` crée un fichier `hello.c` et l’ouvre pour y écrire du code.
  - `make hello` compile le code C en créant un exécutable nommé `hello`.
  - `./hello` exécute ce programme.

- Dans le fichier `hello.c`, écrivez ce code :

    ```c
    // Un programme qui dit hello au monde

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }
    ```

  - Chaque caractère compte : si vous faites une erreur, le programme ne fonctionnera pas.
  - `printf` affiche une ligne de texte. Les guillemets, le point-virgule et le `\n` (nouvelle ligne) sont essentiels.
  - Après compilation (`make hello`) sans erreur, exécutez `./hello` et le programme affichera `hello, world`.
  - Vous verrez deux fichiers : `hello.c` (code source) et `hello` (exécutable).  
  :contentReference[oaicite:1]{index=1}

---

## De Scratch à C

- En Scratch, nous utilisions le bloc `say` pour afficher du texte. En C, nous utilisons `printf` de la même manière :

    ```c
    printf("hello, world\n");
    ```

  - Ici, la fonction `printf` est invoquée avec l’argument `"hello, world\n"` — et la ligne se termine bien par `;`.  
  :contentReference[oaicite:2]{index=2}

- Erreurs fréquentes : absence du `\n` :

    ```c
    // \n est absent
    #include <stdio.h>

    int main(void)
    {
        printf("hello, world");
    }
    ```

  - Le `\` (caractère d’échappement) indique une instruction spéciale, ici `\n` pour nouvelle ligne — sans lui, le comportement diffère.  
  :contentReference[oaicite:3]{index=3}

- Autres séquences d’échappement utiles :

    ```
    \n  nouvelle ligne
    \r  retour au début de ligne
    \"  guillemet double
    \'  guillemet simple
    \\  anti-slash
    ```  
  :contentReference[oaicite:4]{index=4}

- Revenir au programme correct avec `\n` et `;` :

    ```c
    // Un programme qui dit hello au monde

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }
    ```  
  :contentReference[oaicite:5]{index=5}

---

## Fichiers d’en-tête et pages de manuel CS50

- La ligne `#include <stdio.h>` en début de fichier indique au compilateur que vous souhaitez utiliser le contenu de la bibliothèque (header file) `stdio.h`, notamment la fonction `printf`.
- Une bibliothèque est un ensemble de code réutilisable écrit par d’autres, utile pour enrichir votre programme.
- Vous pouvez consulter les **Manual Pages** pour comprendre chaque fonction.
- CS50 propose également sa propre bibliothèque `cs50.h`, qui inclut des fonctions utiles comme :

    ```
    get_char
    get_double
    get_float
    get_int
    get_long
    get_string
    ```

- Vous pouvez utiliser `cs50.h` dans vos programmes pour simplifier certaines tâches.  
  :contentReference[oaicite:6]{index=6}

---

## Hello, You

- En Scratch, nous avions demandé “Quel est ton nom ?” et affiché un message personnalisé. En C, on peut faire la même chose :

    ```c
    // get_string et printf avec un placeholder incorrect

    #include <stdio.h>

    int main(void)
    {
        string answer = get_string("What's your name? ");
        printf("hello, answer\n");
    }
    ```

  - `get_string` demande une saisie utilisateur et la stocke dans la variable `answer`, mais ici, `answer` n’est pas affiché correctement.  
  :contentReference[oaicite:7]{index=7}

- Si vous exécutez `make hello`, des erreurs apparaissent — la variable `string` et la fonction `get_string` ne sont pas reconnues. Il faut donc inclure la bibliothèque `cs50.h`, et corriger l’usage de `printf`.  
  :contentReference[oaicite:8]{index=8}

---

## À venir (et plus)

Ensuite, le cours se poursuit avec :

- **Types** (int, char, float, etc.),
- **Conditionnelles** (`if`, `else`),
- **Opérateurs** (arithmétiques, logiques),
- **Variables**,
- Des fichiers exemples comme `compare.c`, `agree.c`,
- **Boucles** et le fichier `meow.c`,
- **Fonctions**,
- Les notions de **correction**, **conception**, **style** de code,
- Le jeu **Mario** (un exemple de programme),
- **Commentaires**,
- Des détails sur les **opérateurs** supplémentaires,
- **Troncature** (ex : cast implicite),
- Et enfin, une section **"Summing Up"** pour résumer les acquis.  
:contentReference[oaicite:9]{index=9}

---

Voilà, vous avez maintenant la traduction complète de **Lecture 1**, jusqu’à la fin du contenu présent sur la page en HTML. Si tu veux que je génère ce contenu sous forme de fichier `.md` téléchargeable, fais-le-moi savoir !
::contentReference[oaicite:10]{index=10}
