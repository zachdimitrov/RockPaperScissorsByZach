import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')
if player_move != 'r' and player_move != 'p' and player_move != 's':
    player_move = input('Please choose again [r][p][s]: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors

random_number = random.randint(1, 3)
computer_move = ''
if random_number == 1:
    computer_move = rock
elif random_number == 2:
    computer_move = paper
elif random_number == 3:
    computer_move = scissors

print(f'You chose {player_move}!')
print(f'The computer chose {computer_move}!')

if computer_move == player_move:
    print(f'Both player chose {player_move}! Yhe game is DRAW!')
elif player_move == rock and computer_move == scissors:
    print(f'The Rock smashes the Scissors - YOU WIN!')
elif player_move == paper and computer_move == rock:
    print(f'The Paper covers the Rock - YOU WIN!')
elif player_move == scissors and computer_move == paper:
    print(f'The Scissors cuts the Paper - YOU WIN!')
elif computer_move == paper and player_move == rock:
    print(f'The Rock is covered by the Paper - YOU LOSE!')
elif computer_move == scissors and player_move == paper:
    print(f'The Paper is cut by the Scissors - YOU LOSE!')
elif computer_move == rock and player_move == scissors:
    print(f'The Scissors are smashed by the Rock - YOU LOSE!')

