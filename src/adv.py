from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# I am passing the key to the dictionary
player_one = Player("Samwise the Brave", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player_action = ""

current_room = player_one.get_room()

print(f"Welcome to the adventure, {player_one.name}")

print(f"Current Room Description: {current_room.description}")

legitmate_moves = ['n', 's', 'e', 'w']

while player_action is not 'q':
 
    player_action = input(f"What do you want to do, {player_one.name}? Or press q to quit. ")
    
    if player_action in legitmate_moves:

        if player_action == 'n' and current_room.n_to != None: # Test room is real and player direction
            player_one.set_room(current_room.n_to)
            current_room = player_one.get_room()
            print(f"You are now in {player_one.get_room().get_name()}")
            print(f"Room Description: {current_room.description}")

        elif player_action == 's' and current_room.s_to != None:
            player_one.set_room(current_room.s_to)
            current_room = player_one.get_room()
            print(f"You are now in {player_one.get_room().name}")
        
        elif player_action == 'e' and current_room.e_to != None:
            player_one.set_room(current_room.e_to)
            current_room = player_one.get_room()
            print(f"You are now in {player_one.get_room().name}")

        elif player_action == 'w' and current_room.w_to != None:
            player_one.set_room(current_room.w_to)
            current_room = player_one.get_room()
            print(f"You are now in {player_one.get_room().name}")
        
        else:
            print("ERROR: You can't go there! Illegitimate move.")
    elif player_action is not 'q':
        print("Not an acceptable input command")

# Print when out of loop and player has quit the game.
print("Goodbye! Thanks for playing!")

    
  
    


