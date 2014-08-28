'''Check if Palindrome – Checks if the string entered by
the user is a palindrome. That is that it reads the same
forwards as backwards like “racecar”'''

def palin(word):
    if word==word[::-1]:
        return True
    return False
word = input("Provide a word and we will see if it is a palindrome: ")
print ("We see that the word \"" + word + "\" tests "
       + str(palin(word)) + " as a Palindrome.")
