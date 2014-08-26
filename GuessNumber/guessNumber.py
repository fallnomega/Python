from random import randint

def isNumber(a):
    if a.isdigit()==False:
        return False
    return True

def compareNums(guess,number):
    if int(guess)==int(number):
        return "\nYou guessed correct!\n\n\n"
    else:
        result = hotCold(guess,number)
        return result

def hotCold(guess,number):
    if int(guess)>int(number):
        return "\nToo High!\n\n\n"
    else:
        return "\nToo Low!\n\n\n"
    
while True:
    theNumber = randint(1,6)
    guess = input('0 to Quit.Guess a number between 1 - 6 that I am thinking of: ')
    if isNumber(guess)==False:
        print ('\nPlease provide a number between 1 - 6!\n\n\n')
    elif guess=='0':
        print("\nGoodbye!")
        break
    else:
        print (compareNums(guess,theNumber))
