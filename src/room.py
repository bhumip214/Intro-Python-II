# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # The Room class should be extended with a list that holds the Items that are currently in that room.
        self.items_list = []

    # Add the ability to add items to rooms.
    def add_item(self, item):
        self.items_list.append(item)

    # Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
    def print_items(self):
        if len(self.items_list) == 0:
            print("No items in room")
        else:
            print("Items in room:")
            for i in self.items_list:
                print(i.name)

    # look for item's name in items list and return the whole item
    def find_item(self, item_name):
        for item in self.items_list:
            if item.name == item_name:
                return item
        return None

    # remove a item from the item's list
    def remove_item(self, item):
        self.items_list.remove(item)