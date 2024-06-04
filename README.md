# Rock Paper Scissors - by Zach
### Zahari Dimitrov
#### SoftUni - Python Fundamentals Course - Educational Project
This is a simple version of the classic game "Rock Paper Scissors".

## Introduction
[Rock - Paper - Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) is a classic game for **two players**, who simultaniously chose one of the following:
- **rock** - beats the scissors (smashes them)
- **scissors** - beats thte paper (cuts it)
- **paper** - beats the rock (covers it)

After one or a number of games the player who beated for most of the games wins.
In a certain game if both players select the same weapon the game is a **DRAW** and no points are won!

## Gameplay
When you start the game you will receive a prompt:

`> Choose [r]ock, [p]aper, [s]cissors [t]est or [Q]uit: `

Make your choise like  this:

`> Choose [r]ock, [p]aper, [s]cissors [t]est or [Q]uit:` `r`

If you chose `q` the game will end and final result will be presented:

```
Final score:  
you 17 : 16 computer  
YOU WON THE GAME!
```

If the input is wrong, a second prompt will appear:
`> Please choose again - [r][p][s][t][q]: `

### Test mode
If you select `t` at the begining, a **tets mode** is executed

`> Select number of tests and command separated by interval [number] [r][p][s]: `

This means that you can play a given number of games automatically with a selected weapon (rock, paper or scissors) and see the final result.

Your input should look like this example: `1000 r`.
This means that 1000 games will be played with **rock** as your selection (the computer will select its weapon randomly).
If the input is wrong, a second prompt will appear:
`> Please try again - [number] [r][p][s]: `
