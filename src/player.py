# Write a class to hold player information, e.g. what room they are in currently.


class Player:
    def __init__(self, name, starting_room=None):
        self.name = name
        self.current_room = starting_room
        # The inventory can also be a list of items "in" the player.
        self.inventory = []

    # Called when player wants to take an item from the room
    def on_take(self, item_name):
        # check your item in current room
        item = self.current_room.find_item(item_name)
        if item is not None:
            # add that item to player's inventory
            self.inventory.append(item)
            # Remove the item from the current room
            self.current_room.remove_item(item)
            print(f'{item_name} is added to your inventory!')
        else:
            print('Item not found!')

    # check for item's name in inventory and return the whole item else return none
    def check_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    # remove a item from the inventory
    def remove_item(self, item):
        self.inventory.remove(item)

    # Called when player wants to drop an item from inventory
    def on_drop(self, item_name):
        # check your item in inventory
        item = self.check_inventory(item_name)
        if item is not None:
            # Remove the item from the inventory
            self.remove_item(item)
            # add that item to room's item list
            self.current_room.add_item(item)
            print(f'{item_name} is dropped from your inventory!')
        else:
            print('Item not found!')

    # print the list of items in inventory
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("No items in your inventory")
        else:
            print("Items in your inventory:")
            for i in self.inventory:
                print(i.name)
