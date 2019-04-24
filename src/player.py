# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __int__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # The inventory can also be a list of items "in" the player.
        self.inventory = []
        
    # Add capability to add Items to the player's inventory. 
    def pickup_Items(self, item):
        self.inventory.append(item)
