from room import Room
from player import Player
from item import Item


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

item = {
    'sword': Item("Sword", """The Hand of Goulasjh - A gold coated hilt adorned with priceless jewels and a very worn blade.""")
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

# Link items to rooms
room['foyer'].list.append(item['sword'])
room['foyer'].list.append(item['sword'])


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
    
# Function that allows a player to take or drop an item
def item_action(action, item , player):
    if action == "take" or action == "get":
        for x in player.current_room.list:
            if x.name.lower() == item.lower():
                player.inventory.append(x)
                player.current_room.list.remove(x)
                print(x.on_take())
    if action == "drop":
        for x in player.inventory:
            if x.name.lower() == item.lower():
                player.inventory.remove(x)
                player.current_room.list.append(x)
                print(x.on_drop())
    return player

# Write a loop that:
while True:
    # * Prints the current room name
    # additional empty prints a hacky way of better spacing - looking into how to do this better...
    print()
    print(current_player.current_room.name)
    print()
    # * Prints the current description (the textwrap module might be useful here).
    print(current_player.current_room.description)
    print()

    # * Prints the items that are visible to the player in the room they are in
    print("You see the following objects of interest:")
    for x in current_player.current_room.list:
        print(x)

    # * Waits for user input and decides what to do.
    cmd = input("\n Please enter a direction you'd like to explore. (Ex: North) \n\n Or you can 'take' an object in the room and add it to your inventory \n Or 'drop' one of your inventory items. \n\n Enter i to check your inventory \n Or enter q to quit the game. >>").split(" ")    
    # The below if statement checks to see if the input is one word
    if len(cmd) == 1:
        move = cmd[0].lower()
        # If the user enters "q", quit the game.
        if move[0] == "q":
            print()
            print(" Thanks for playing! \n")
            break

        # If the user enters "i", their inventory will print to the console.
        if move[0] == "i":
            print("\n The items in your inventory are:")
            current_player.player_items()

        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.        
        else:
            current_player.current_room = move_player(move[0], current_player.current_room)
            print("\n")
    
    # Checks to see if the input is 2 words
    # Then deals with inventory actions (function above - lines 70-84)
    if len(cmd) == 2:
        current_player = item_action(cmd[0], cmd[1], current_player)

   