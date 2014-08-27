def menu():
    print("*********************\nQ to quit\nL to see current Location\nWhat direction do you want to go?")
    print("1: North\n2: West\n3: South\n4: East\n\n")
    choice = input("Which way[N,W,S,E]:")
    if choice.isalpha()==False:
        print("Please select N,W,S, or E")
        choice= menu()
    choice = choice.upper()
    print('*********************\n')
    return choice

def moveTo(house,location,direction):
    if direction=='N':
        if location[0]=='Entrance/Parlor':
            location = house[1]
        elif location[0]=='Library':
            location = house[0]
        elif location[0]=='Living Room':
            location=house[2]
        elif location[0]=='Bathroom':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Kitchen':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Dining Room':
            print('The windows are locked, there is no escape!!!\n\n')
        return location
            
    elif direction =='E':
        if location[0]=='Entrance/Parlor':
            location = house[5]
        elif location[0]=='Library':
            location = house[4]
        elif location[0]=='Living Room':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Bathroom':
            location = house[1]
        elif location[0]=='Kitchen':
            location = house[2]
        elif location[0]=='Dining Room':
            print('The windows are locked, there is no escape!!!\n\n')
        return location
            
    elif direction=='S':
        if location[0]=='Entrance/Parlor':
            print('The frontdoor is locked.Once you enter this house, there is no escape!!!\n\n')
        elif location[0]=='Library':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Living Room':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Bathroom':
            location = house[3]
        elif location[0]=='Kitchen':
            location = house[4]
        elif location[0]=='Dining Room':
            location=house[5]
        return location
        
    else:
        if location[0]=='Entrance/Parlor':
            location = house[3]
        elif location[0]=='Library':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Living Room':
            location = house[4]
        elif location[0]=='Bathroom':
            print('The windows are locked, there is no escape!!!\n\n')
        elif location[0]=='Kitchen':
            location = house[0]
        elif location[0]=='Dining Room':
            location = house[1]
        return location

house = [["Bathroom",'In the bathroom, someone has dropped a bomb in this room. You may need to call Hazmat'],
         ['Kitchen','This kitchen was designed with functionality in mind, it has an island in the center of it along with standard kitchen appliances'],
         ['Dining Room',"The dining room has a large table in the center, fine china cabinette against the back wall, and clearly its owner is blind to tasteless design"],
         ['Library','The library is filled with a collection comprised of the Harry Potter series, Twilight series, and 50 Shades of Grey series. RUN AWAY ! '],
         ["Entrance/Parlor","Filled with cherry black furniture and reeks of varnish and 409"],
         ['Living Room','The living room has a recliner and a 50 inch HDTV in it.']]

location = house[4]
print ("You are currently in the " + location[0] + ": " + location[1]+ '\n\n')
while True:

    
    direction = menu()
    if direction=='Q':
        break
    elif direction=='L':
        print ("\n\n\nYou are currently in the " + location[0] + ": " + location[1]+ '\n\n')        
    location = moveTo(house,location,direction)
    

'''
______________________________
|        |         |          |
|                             |
|    0   |     1   |       2  |
|___  ___|___  ____|____  ____|
|        |         |          |
|        |         |          | 
|    3         4         5    |
|________|___  ____|__________|
'''
