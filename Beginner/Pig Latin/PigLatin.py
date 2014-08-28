#Pig Latin

word = input("Provide a word that can be made into Pig Latin: ")

print (word[1:] + word[0].lower() + "ay")
