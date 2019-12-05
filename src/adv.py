from room import Room
from player import Player

# Declare all the roomss

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
player = Player(input('Name?'), room['outside'])

# Write a loop that:
#
# * Print the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# version 1

# while True:
#     print(
#         f"\t Room: {player.current_room.name}\n {player.current_room.description}")
#     text_stuff = input('make a move?').split(' ')
#     if text_stuff[0] is "q":
#         print('Your are Leaving the game')
#         break
#     elif text_stuff[0] == 'n':
#         player.move(text_stuff[0])
#     elif text_stuff[0] == 'e':
#         player.move(text_stuff[0])
#     elif text_stuff[0] == 'w':
#         player.move(text_stuff[0])
#     elif text_stuff[0] == 's':
#         player.move(text_stuff[0])
#     else:
#         print('please enter the proper commands n, s, e, w or q for Quit ')

# version 2
while True:
    print(
        f"\t Room: {player.current_room.name}\n {player.current_room.description}")
    user_input = input('make a move ').strip().lower().split(' ')
    if user_input[0] == 'q':
        print('Your are leaving the game!')
        break
    if user_input[0] == 'n':
        if player.current_room.n_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = player.current_room.n_to
    elif user_input[0] == 's':
        if player.current_room.s_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = player.current_room.s_to
    elif user_input[0] == 'e':
        if player.current_room.e_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = player.current_room.e_to
    elif user_input[0] == 'w':
        if player.current_room.w_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = player.current_room.w_to
    else:
        print('please enter the proper commands n, s, e, w or q for Quit ')
