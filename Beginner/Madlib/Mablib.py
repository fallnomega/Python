#Converted Summer Son’s Mad Libs  from JavaScript to Python

randomName = input('Random name (ex. Ryan) :')
name = input('Your name (ex. why do you need an example of your name?) :')
disgustingObject = input('A disgusting object, plural (ex. bugs [sorry, entomologists]) :') 
pluralNoun = input('Noun, plural (ex. pencils) :')
pluralNoun2 = input('Noun, plural (ex. pens) :')
adject1 = input('Adjective (ex. wonderful) :')
adject2 = input('Adjective (ex. weird) :')
adject3 = input('Adjective (ex. angry) :')
animal = input('Type of animal, singular (ex. wallaby) :')
singularNoun1 = input('Noun, singular (ex. book) :')
pastVerb1 = input('Verb, past tense (ex. poked) :')
presVerb = input('Verb, present tense (ex. eat) :')
pastVerb2 = input('Verb, past tense (ex. found) :')
occupation = input('Type of occupation (ex. janitor) :')
adject4 = input('Adjective (ex. happy) :')
properNoun = input("Proper noun, restaurant (ex. Papa John's) :") 
pastVerb3 = input('Verb, past tense (ex. wrote) :')
singularNoun2 = input('Noun, singular (ex. computer) :')
superlative = input('Superlative (ex. worst) :')




print('To: ' + str(randomName) + "@email.com")
print('From: ' + str(name) + '@email.com')
print('Subject: Can\'t make work today')
print('\nHi,')
print('''\nI\'ve come down with a bad case of the ''' + str(disgustingObject) + '''.I\'ve been
throwing up ''' + str(pluralNoun) + ''' all day and keep forgetting what ''' + str(pluralNoun2) +''' are. My
hands are '''+str(adject1) + ''' as a result, and my hair is '''+ str(adject2) +'''. Yesterday, I
was bitten by my neighbor\'s  ''' + str(animal) + '''. I tried to fight it with my ''' + str(singularNoun1) +''',
but it ''' + str(pastVerb1) + ''' and proceeded to furiously ''' +  str(presVerb) + '''. I ''' + str(pastVerb2) + '''
 and called for help, but only a ''' + str(occupation) + ''' came to my aid. He was ''' + str(adject4) +
'''. I finally reached my phone and dialed 911, but for some reason it
redirected me to ''' + str(properNoun) + '''! It was a lost cause. I ''' + str(pastVerb3) + ''' all the
way back home, where I found solace in my ''' + str(singularNoun2) + '''. I\'m sorry to say,
but I won\'t make it into work today. Hopefully you will understand.''')

print('\nSincerely,\n Your ' + str(superlative) + ' employee')
