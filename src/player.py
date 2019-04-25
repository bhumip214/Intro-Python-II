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

    def on_take(self, item_name):
        item = self.current_room.find_item(item_name)
        if item is not None:
            self.pickup_items(item)
            self.current_room.remove_item(item)
            print(f'{item_name} is taken')
        else:
            print('Item not found')
