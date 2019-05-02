# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        

    def __str__(self):
        return f"{self.current_room}, {self.inventory}"

    def player_items(self):
        if len(self.inventory) == 0:
            print("\t nothing!!!")
        for x in self.inventory:
            print("\t" + x.name+": " + x.description)
        # only for line spacing
        print()