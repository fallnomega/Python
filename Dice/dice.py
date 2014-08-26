from random import randint
def printDice(a):
    print('You rolled a', a)
while True:
    playAgain = input('Would you like to roll again [Y/N] :')
    playAgain = playAgain.upper()
    if playAgain=='N':
        break
    elif playAgain=='Y':
        dice = randint(1,6)
        printDice(dice)
    else:
        print ('******************\n******************\nPlease choose Y or N for your response\n******************\n******************\n')
        
