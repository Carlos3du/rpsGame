
from random import randint as Rnum
import os
os.system("cls")

#0 = scissors, 1 = paper and 2 = rock
scoreComp = 0
scoreYou = 0
bieMsg = True

#Welcome message
start = int(input('Welcome to RPS game, do you wanna play against the computer?\n[1]-Yes [2]-No: '))
if start == 1:
    times = int(input('\nInsert how many rounds do u wanna play: '))
else:
    times = 0
    bieMsg = False
    
for i in range(times):
    
    #Generate random computer choice
    computer = Rnum(0,2)
    
    #User choice imput
    you = int(input('\nChoose one option:\n[0]-scissors [1]-paper [2]-rock\nYour turn: '))
    
    while you != 0 and you != 1 and you !=2 and you !=3:
        print('\nI dont understand, please try again by choosing a valid option: ')
        you = int(input('[0]-scissors [1]-paper [2]-rock\nYour turn: '))
        
    else:
        print(f'Computers turn: {computer}')
        
    #Check the conditions
    if computer == you:
        result = 'Draw, no points for both'
    elif (computer == 0 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 0):
        result = 'Computer scores'
        scoreComp += 1
    else:
        result = 'You scores'
        scoreYou += 1
    
    #Check the final result
    print(result)
    #ScoreBoard
    print(f'\nGameScore:\nYou: {scoreYou} || Computer: {scoreComp}')
        
#End of the game
if bieMsg:
    os.system("cls")
    print(f'\nFinal Score:\nYou: {scoreYou} || Computer: {scoreComp}')
    if scoreYou > scoreComp:
        print('You beat the computer, congrants *-* ')
            
    elif scoreYou == scoreComp:
        print('Theres a tie ^-^ ')
            
    else:
        print('The computers are our leaders now, you lose -_- ')
        
    print('\nThanks for playing S2 ')
else:
    print('\nOkay, see u soon ;-; ')
    
