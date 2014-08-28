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

def compare(letter,word,hidden):
    counter = 0
    for i in word:
        if letter == i:
            hidden[counter]=word[counter]
        counter= counter +1
        
    return hidden

def printGuess(result):
    for i in result[0:]:
        print (' '.join(i),end=" ")
    
def roundCounter(i):
    count = len(i)
    return count

def generate(word):
    result = []
    for i in range(len(word)):
        result.append("_")
    return result


    
i = 1
counter = roundCounter(theWord)
hiddenWord = generate(theWord)
printGuess(hiddenWord)
while i <= counter :
    guess = singleChar()
    result = compare(guess, theWord, hiddenWord)
    printGuess(result)
    i = i + 1
    if i==(counter +1):
        print("\n\nYou lose, game over!!")
