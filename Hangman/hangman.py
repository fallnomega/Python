from random import randint
words = ["TRON","HELLO","GOODBYE","LUCKY","INTERNET",
         "PYTHON","RECURSION","CLASS","VARIABLE","OPERATOR"]
index = randint(0,9)
theWord = words[index]
theWord.upper()
print(theWord)





def singleChar():
    letter = input("\n\nGuess a letter: ")
    letter = letter.upper()
    return letter

def compare(letter,word):
    for i in word:
        if letter == i:
            return "Correct"
    return "Wrong"

def printLetters(selections):
    pass
def counter(i):
    pass

def generate(word):
    result = []
    for i in range(len(word)):
        result.append("_")
    return result

def printGuess(result):
    for i in result[0:]:
        print (' '.join(i),end=" ")
    
    


hiddenWord = generate(theWord)
printGuess(hiddenWord)

guess = singleChar()
print ("That is " + compare(guess, theWord))
