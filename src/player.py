# Write a class to hold player information, e.g. what room they are in currently.


class Player:
    def __init__(self, name, starting_room=None):
        self.name = name
        self.current_room = starting_room
        # The inventory can also be a list of items "in" the player.
        self.inventory = []

    # Add capability to add Items to the player's inventory.
    def pickup_items(self, item):
        self.inventory.append(item)

    # Called when player wants to take an item from the room
    def on_take(self, item_name):
        # check your item in current room
        item = self.current_room.find_item(item_name)
        if item is not None:
            # Then allow user to add that item to his/her inventory
            self.pickup_items(item)
            # Remove the item from the current room
            self.current_room.remove_item(item)
            print(f'{item_name} is added to your inventory!')
        else:
            print('Item not found')

    # print the list of items in inventory
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("No items in your inventory")
        else:
            print("Items in your inventory:")
            for i in self.inventory:
                print(i.name)
