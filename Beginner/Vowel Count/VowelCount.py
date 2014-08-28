'''Count Vowels – Enter a string and the program counts
the number of vowels in the text. For added complexity
have it report a sum of each vowel found.'''

vowels = "aeiou"

word = input("Give me a word and I will count the vowels: ")
count = 0
i = 0
j = 0
for i in range(0,len(word)):
    for j in range(0,len(vowels)):
        if vowels[j]==word[i].lower():
            count = count +1
print (count)

