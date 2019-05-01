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
current_player = Player("Player1", room['outside'])

# Function that attempts to move the player via the direction they typed
def move_player(move, current_room):
    if move == "n" and current_room.n_to != "":
        room = current_room.n_to
    elif move == "s" and current_room.s_to != "":
        room = current_room.s_to
    elif move == "e" and current_room.e_to != "":
        room = current_room.e_to
    elif move == "w" and current_room.w_to != "":
        room = current_room.w_to
    else:
        print("\n\nThere is nowhere to go in that direction!")
        return current_room
    return room
    


# Write a loop that:
while True:
    # * Prints the current room name
    print(current_player.current_room.name)
    
    # * Prints the current description (the textwrap module might be useful here).
    print(current_player.current_room.description)
    # * Waits for user input and decides what to do.
    move = input("\n Please enter a cardinal direction. (Ex: North) \n Or a q to quit the game. >>").lower()[0]        
    # If the user enters "q", quit the game.
    if move == "q":
        print(" Thanks for playing!")
        break    
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    current_player.current_room = move_player(move, current_player.current_room)
    print("\n")
   