# Rock Paper Scissors - by Zach
### Zahari Dimitrov
#### SoftUni - Python Fundamentals Course - Educational Project
This is a simple version of the classic game "Rock Paper Scissors".

![image](https://github.com/zachdimitrov/RockPaperScissorsByZach/assets/11989564/93f348bc-ec15-4b46-a908-8c9f0158c458)

## Introduction
[Rock - Paper - Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) is a classic game for **two players**, who simultaniously chose one of the following weapons:
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

## Code
All of the game code is written in **Python 3.9**.
There are a number of methods for selecting text color using escape codes like this:
```py
def pr_red(skk): print(f"\033[91m{skk}\033[00m")
def pr_green(skk): print(f"\033[92m{skk}\033[00m")
def pr_yellow(skk): print(f"\033[93m{skk}\033[00m")
```

The computer selects its weapon randomly using this method:

```py
import random
def computer_move_selector():
    random_number = random.randint(1, 3)
    cm = ''
    if random_number == 1:
        cm = rock
    elif random_number == 2:
        cm = paper
    elif random_number == 3:
        cm = scissors
    return cm
```
## Live Demo
You can play the game in browser here:
[<img alt="Play Button" width=100 src="https://github.com/zachdimitrov/RockPaperScissorsByZach/assets/11989564/e8ca0896-47fc-428a-ba86-60ac7531cc2a" />](https://replit.com/@zaharid/RockPaperScissorsGame#main.py)
