def menu():
    print("What direction do you want to go?")
    print("1: North\n2: West\n3: South\n4: East\n\n")
    choice = input("Which way[N,W,S,E]:")
    if choice.isalpha()==False:
        print("Please select N,W,S, or E")
        choice= menu()
    choice = choice.upper()  
    return choice

def moveTo(location):
    print ("You are in the " + location[0] + ": " + location[1])

house = [["Bathroom",'In the bathroom, someone has dropped a bomb in this room. You may need to call Hazmat'],
         ['Kitchen','This kitchen was designed with functionality in mind, it has an island in the center of it along with standard kitchen appliances'],
         ['Dining Room',"The dining room has a large table in the center, fine china cabinette against the back wall, and clearly its owner is blind to tasteless design"],
         ['Library','The library is filled with a collection comprised of the Harry Potter series, Twilight series, and 50 Shades of Grey series. RUN AWAY ! '],
         ["Entrance/Parlor","Filled with cherry black furniture and reeks of varnish and 409"],
         ['Living Room','The living room has a recliner and a 50 inch HDTV in it.']]



location = house[4]
print (location)
direction = menu()
print (direction)
moveTo(location)

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
