README
STEFANO PALAZZO

# Main
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-StefanoPalazzo/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-StefanoPalazzo/tree/main)


# The Scrabble Game
Scrabble is a word game in which two to four players score points by placing tiles, each bearing a single letter, onto a game board divided into a 15×15 grid of squares. The tiles must form words that, in crossword fashion, read left to right in rows or downward in columns and are included in a standard dictionary or lexicon. 

## Rules

The Spanish-language games use these 98 tiles:

- 2 WildCards (0 points)
- 1 point: A×12, E×12, O×9, I×6, S×6, N×5, L×4, R×5, U×5, T×4
- 2 points: D×5, G×2
- 3 points: C×4, B×2, M×2, P×2
- 4 points: H×2, F×1, V×1, Y×1
- 5 points: CH×1, Q×1
- 8 points: J×1,  Ñ×1, X×1
- 10 points: Z×1

## Remember

- The game is in English but it is played in Spanish, the dictionary is based in the RAE (Real Academia Española) dictionary.
- Words are read from left to right in rows or from top to bottom in columns.
- ScrabbleGame does not have tiles with acute accents, but these words are supported and differentiated. For example, if you have the following tiles:
        "[P],[A],[P],[A]"
    you can create 'papa' or 'papá' words
- The letters K and W are not included since they are rarely used in Spanish words.
- According to the rules of FISE (Federación Internacional de Scrabble en Español), a blank tile cannot be used to represent K or W.
- Game does not have 'LL','CH' or 'RR' tiles, you can use two 'L', 'C' or 'R' tiles to create these words.

#### Complete guide of the rules of the game [here](https://service.mattel.com/instruction_sheets/51280.pdf)

## How to run the game

Execute the following commands in a Command Line Interface (CLI):


```bash
docker build --no-cache -t juegoscrabbledocker .

```

```bash
docker run -it juegoscrabbledocker
```

## Sources
- The [Wikipedia (EN)](https://en.wikipedia.org/wiki/Scrabble)
- The [Wikipedia (ES)](https://es.wikipedia.org/wiki/Scrabble)

# Author Information

- Name: Stefano Palazzo
- Instagram: @stefanopalazzo_
- Country: Argentina
- Year: 2023

[![StefanoPalazzo's github stats](https://github-readme-stats.vercel.app/api?username=StefanoPalazzo&theme=blue-green)](https://github.com/um-computacion-tm/scrabble-2023-StefanoPalazzo)
