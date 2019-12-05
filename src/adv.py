from room import Room
from player import Player
from item import Item

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

items = {
    'axe': Item("Axe of Thror", "The legendary axe of Thror created from the 'lord Star' and crafted by the hand of the creator"),
    'torch': Item("Forever Flame Torch", "A regular looking torch that bares the last remnants of the forever flame gifted from the 'lord Star'."),
    'spear': Item('Long Spear', 'the spear weilded by the legendary warrior "RiverWind", past down to tribal leaders for centuries'),
    'flint': Item('Everlast Flint', 'Everlast flint was a gift from the priestess "Minwae", to the clan of "Last River" to bring them light in the darkness'),
    'gold' : Item('Dante\'s treasure', 'Hidden from the eyes of mortals you have now discovered the greatest treasure ever place on the "Great Rock".')
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

room['outside'].add_item(items['axe'])
room['foyer'].add_item(items['torch'])
room['overlook'].add_item(items['spear'])
room['narrow'].add_item(items['flint'])
room['treasure'].add_item(items['gold'])

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

while True:
    print(
        f"\t Room: {player.current_room.name}\n {player.current_room.description}")
    print(f'items available in this room are: {[item.name for item in player.current_room.view_room_items()]}')
    text_stuff = input('make a move?').split(' ')
    if text_stuff[0] is "q":
        print('Your are Leaving the game')
        break
    elif text_stuff[0] == 'n' or text_stuff[0] == 's' or text_stuff[0] == 'e' or text_stuff[0] == 'w':
        player.move(text_stuff[0])
    else:
        print('please enter the proper commands n, s, e, w or q for Quit ')

#------------
#Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
#------------
#Add a new type of sentence the parser can understand: two words.

#Until now, the parser could just understand one sentence form:

#verb

#such as "n" or "q".

#But now we want to add the form:

#verb object

#such as "take coins" or "drop sword".

#Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.









# # version 2
# while True:
#     print(
#         f"\t Room: {player.current_room.name}\n {player.current_room.description}")
#     user_input = input('make a move ').strip().lower().split(' ')
#     if user_input[0] == 'q':
#         print('Your are leaving the game!')
#         break
#     if user_input[0] == 'n':
#         if player.current_room.n_to is None:
#             print('Cant go that way')
#             continue
#         else:
#             player.current_room = player.current_room.n_to
#     elif user_input[0] == 's':
#         if player.current_room.s_to is None:
#             print('Cant go that way')
#             continue
#         else:
#             player.current_room = player.current_room.s_to
#     elif user_input[0] == 'e':
#         if player.current_room.e_to is None:
#             print('Cant go that way')
#             continue
#         else:
#             player.current_room = player.current_room.e_to
#     elif user_input[0] == 'w':
#         if player.current_room.w_to is None:
#             print('Cant go that way')
#             continue
#         else:
#             player.current_room = player.current_room.w_to
#     else:
#         print('please enter the proper commands n, s, e, w or q for Quit ')
