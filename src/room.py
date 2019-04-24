# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # The Room class should be extended with a list that holds the Items that are currently in that room.
        self.list = []

    # Add the ability to add items to rooms.
    def add_items(self, item):
        self.list.append(item)

    # Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
    def print_items(self):
        for i in self.list: 
            print(i.name)