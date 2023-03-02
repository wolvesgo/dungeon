#!/usr/bin/env python3

# TODO:
# Help text
# Make look show descriptions of items instead of bare names
# Pick up 
# If user tries to leave the room while there is a monster, it kills them, or something


# Wall codes
# 0 - O Walls
# 1 - North 
# 2 - East 
# 3 - South
# 4 - West
# 5 - North and East
# 6 - North and South
# 7 - North and West
# 8 - East and South
# 9 - East and West
# A - South and West
# B - North, East and South
# C - North, East and West
# D - North, South and West
# E - East, South and West
# F - North, East, South and West

north_doors = ['0','2','3','4','8','9','A','E']
east_doors =  ['0','1','3','4','6','7','A','D']
south_doors = ['0','1','2','4','5','7','9','C']
west_doors =  ['0','1','2','3','5','6','8','B']

walls = """
766665CCD5
9766BA3368
A366666665
CCD5711159
9460899E48
A8CA59ED8C
76878A6668
9768C75715
99718E4299
A38A668EEE
"""

walls = "".join(walls.split())

dungeon = []

for y in range(0,10):
    dungeon.append([])
    for x in range(0,10):
        dungeon[y].append({
                    "loc"  : str(x) + ":" + str(y),
                    "enemy" : None,
                    "item" : None,
                    "openings" : walls[(y * 10) + x],
                    "door": None
                })

dungeon[9][7]['enemy'] = 'goblinhermit'
dungeon[8][5]['enemy'] = 'mouthmonster'
dungeon[8][4]['enemy'] = 'mummy'
dungeon[7][3]['enemy'] = 'icestatue'
dungeon[7][0]['enemy'] = 'shadowcreature'
dungeon[4][7]['enemy'] = 'shadowcreature'
dungeon[5][7]['enemy'] = 'willowisp'
dungeon[1][4]['enemy'] = 'willowisp'
dungeon[1][7]['enemy'] = 'icestatue'
dungeon[0][8]['enemy'] = 'eyeballmonster'


dungeon[9][9]['item'] = 'bagofholding'
dungeon[7][9]['item'] = 'rustysword'
dungeon[8][5]['item'] = 'redkey'
dungeon[7][4]['iten'] = 'spellbook'
dungeon[5][2]['item'] = 'orangekey'
dungeon[5][7]['item'] = 'yellowkey'
dungeon[0][8]['item'] = 'greenkey'
dungeon[5][6]['item'] = 'magicsunglasses'
dungeon[5][9]['item'] = 'pepperspay'


dungeon[9][5]['door'] = {'color':'red', 'wall':'west'}
dungeon[3][4]['door'] = {'color':'orange', 'wall':'east'}
dungeon[3][9]['door'] = {'color':'yellow', 'wall':'north'}
dungeon[0][7]['door'] = {'color':'green', 'wall':'north'}


# print(dungeon)
# 
# def printmap(dungeon):
#     print('<table>')
#     for y in dungeon:
#         print('<tr>')
#         for x in y:
#             print('<td class="d' + x["openings"] + '"></td>')
#         print('</tr>')
#     print('</table>')
# 
# printmap(dungeon)


## Game loop


dead = False
escaped = False
items = []
current_loc = [9,9]

lookwords = ['look','examine','glance','check']
bagwords = ['bag','sack','holding','inventory']
usewords = ['use','cast','open','unlock','sword','spell','book','magic','light','glases','sunglasses','pepper','spray'] 
attackwords = ['attack','kill','smite','destroy','punch','kick','fight','throw','shoot']
movementwords = ['n','e','s','w','north','east','south','west']
collectionwords = ['pick up','get','fetch','collect','hold','grab']
helpwords = ['help'] 


while(not dead and not escaped): 

    # Let user type something
    # Check what user typed
    # Maybe do an action
    # Print the appropriate answer

    # Taking input from the user
    # Taking input from the user
    action = input("> ").lower().split()

    # Look
    if ( len( set(action) & set(lookwords) ) > 0 ):
        current_room = dungeon[ current_loc[0] ][ current_loc[1] ]

        # current_room['enemy'] == None
        # current_room['item']
        # current_room['openings']
        # current_room['door']


        doors = []

        if ( current_room['openings'] in north_doors ):
            doors.append('North')
        if ( current_room['openings'] in east_doors ):
            doors.append('East')
        if ( current_room['openings'] in south_doors ):
            doors.append('South')
        if ( current_room['openings'] in west_doors ):
            doors.append('West')

        print("You are in a twisty maze. The stone walls make you feel trapped.")

        print("It looks like there are doors to the " + ", ".join(doors))

        if ( current_room['door'] != None ):
            print("The " + current_room['door']['wall'].capitalize() + " door is closed. The " + current_room['door']['color'] + " door has a big lock on it")

        if ( current_room['enemy'] != None ): 
            print("As you look around, you see a " + current_room['enemy'] + " in the corner. It stares at you hungrily.")
       
        if ( current_room['item'] != None ):
            print("There is a(n) " + current_room['item'] + " discarded in the corner. Yolo, it could be usefull..")

    # Bag
    elif ( len( set(action) & set(bagwords) ) > 0 ):
        print("Looking at inventory")

        if not items:
            print("No items")

        else:
            # Print something about the items you have
            # itmes = ["bagofholding","rustysword","spellbook"]
            print("So far, you have these in your vaguely bag saped item:")
            
            for item in items:
                if item != "bagofholding": 
                    print(" * " + item)

    # Use, Cast, Attack, Open, Unlock
    elif ( len( set(action) & set(usewords) ) > 0 ): 
        print("Doing use words code")

    # North, East, South, West
    elif ( len( set(action) & set(movementwords) ) > 0 ):

        current_room = dungeon[ current_loc[0] ][ current_loc[1] ]

        if ( "north" in action or "n" in action ): 

            if (current_room['openings'] in north_doors ): 

                if current_room['door'] != None and current_room['door']['wall'] == 'north':
                    # handle a locked door
                    print("Is it a novelty to smash you head into something othe then wood? If you look up, you'll see a" + current_room['door']['color'] + "door!")
                else:
                    print("Going north")
                    current_loc[0] = current_loc[0] - 1
                    
            else:
                print("That looks like a wall. It's not going to work")




        elif ( "east" in action  or "e" in action ):
            if (current_room['openings'] in east_doors ): 

                if current_room['door'] != None and current_room['door']['wall'] == 'east':
                    # handle a locked door
                    print("Is it a novelty to smash you head into something othe then wood? If you look up, you'll see a" + current_room['door']['color'] + "door!")
                else: 
                    print("Going east")
                    current_loc[1] = current_loc[1] +1
            else:
                print("Your head probably hurts.")

        elif ( "south" in action or "s" in action ): 
            if (current_room['openings'] in south_doors ): 

                if current_room['door'] != None and current_room['door']['wall'] == 'south':
                    # handle a locked door
                    print("Is it a novelty to smash you head into something othe then wood? If you look up, you'll see a" + current_room['door']['color'] + "door!")
                else:
                    print("Going south")
                    current_loc[0] = current_loc[0] + 1
            else:
                print("Those are bricks. Try annother direction.")

        elif ( "west" in action  or "w" in action ):
            if (current_room['openings'] in west_doors ): 
                if current_room['door'] != None and current_room['door']['wall'] == 'west':
                    # handle a locked door
                    print("Is it a novelty to smash you head into something othe then wood? If you look up, you'll see a" + current_room['door']['color'] + "door!")
                else:
                    print("Going west")
                    current_loc[1] = current_loc[1] - 1
            else:
                print("My head hurts after seeing that")
        else:
            print("I can't go there. I don't know where it is")

        current_room = dungeon[ current_loc[0] ][ current_loc[1] ]
        print(current_room)

    # Attack
    elif ( len( set(action) & set(attackwords) ) > 0 ):
        print("attacking...")

    # Help
    elif ( len( set(action) & set(helpwords) ) > 0 ):
        print("helping...")

    # Grabbing
    elif ( len( set(action) & set(collectionwords) ) > 0 ):

        # current_loc = [9,9]
        # dungeon[9][9]['item'] = 'bagofholding'
        # items = []

        # 1. Use the current location to check if there is anything in the current room
        # 2. If there is something in the current room, then:
        #  20. If the user doesn't have the bagofholding, print "Gee, it'd be nice if you had a bag to put that in"
        #  2a. Print a message about grabbing the item
        #  2b. Add the item to your bag of holding (items[])
        #  2c. Remove the item from the room
        # 3. If there was nothing in the room, then print a message that there is nothing to get
        if dungeon[current_loc[0]][current_loc[1]]['item']==None:
            print("Your hand gropes open air. Try looking at your surroundings before reaching out blindly.")
        
        elif "bagofholding" not in items and dungeon[current_loc[0]][current_loc[1]]['item'] != "bagofholding":
            print("Gee, if only you had something to put your item in! Something vaguely bag shaped...?")
        
        else:
            if  dungeon[current_loc[0]][current_loc[1]]['item']=="bagofholding":
                print("You grab the vaguely bag shaped item. As you strap it on, you feel it is unnaturaly light.")
            else:
                print("You put " +  dungeon[current_loc[0]][current_loc[1]]['item'] + " in your bagofholding. You wonder how it will be of use on your journey...")
            
            items.append(dungeon[current_loc[0]][current_loc[1]]['item'])
            dungeon[current_loc[0]][current_loc[1]]['item'] = None

    
    else:
        print("I don't know what to do")



if ( dead ): 
    print("You dead")

elif( escaped ):
    print("Yay, sweet freedom! ohwait, is that annother door???")

