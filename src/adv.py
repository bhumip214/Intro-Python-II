from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = None
room['outside'].e_to = None
room['outside'].w_to = None

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None

room['overlook'].s_to = room['foyer']
room['overlook'].n_to = None
room['overlook'].e_to = None
room['overlook'].w_to = None

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = None
room['narrow'].s_to = None

room['treasure'].s_to = room['narrow']
room['treasure'].e_to = None
room['treasure'].w_to = None
room['treasure'].n_to = None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Bhumi", room['outside'])

# Write a loop that:
while True:
    # * Prints the current room name
    print(f'You are currently in {player.current_room.name}')
    player.current_room.print_items()

    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    cmd = input("Enter n, s, e, or w ->")
    print(f'You entered {cmd}')

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if cmd == "n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print("Movement into this direction is not allowed")

    if cmd == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print("Movement into this direction is not allowed")

    if cmd == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print("Movement into this direction is not allowed")

    if cmd == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print("Movement into this direction is not allowed")

    # If the user enters "q", quit the game.
    if cmd == "q":
        print("Good bye!")
        break
