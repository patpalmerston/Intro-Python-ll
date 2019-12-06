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
    'axe': Item("axe", "The legendary axe of Thror created from the 'lord Star' and crafted by the hand of the creator"),
    'torch': Item("torch", "A regular looking torch that bares the last remnants of the forever flame gifted from the 'lord Star'."),
    'spear': Item('spear', 'the spear weilded by the legendary warrior "RiverWind", past down to tribal leaders for centuries'),
    'flint': Item('flint', 'Everlast flint was a gift from the priestess "Minwae", to the clan of "Last River" to bring them light in the darkness'),
    'gold': Item('gold', 'Hidden from the eyes of mortals you have now discovered the greatest treasure ever place on the "Great Rock".')
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

# create room items
room['outside'].add_item(items['axe'])
room['outside'].add_item(items['spear'])
room['outside'].add_item(items['torch'])
room['foyer'].add_item(items['torch'])
room['foyer'].add_item(items['axe'])
room['foyer'].add_item(items['spear'])
room['overlook'].add_item(items['spear'])
room['overlook'].add_item(items['axe'])
room['overlook'].add_item(items['torch'])
room['narrow'].add_item(items['flint'])
room['narrow'].add_item(items['axe'])
room['narrow'].add_item(items['spear'])
room['treasure'].add_item(items['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Name?'), room['outside'])

# version 1

while True:
    print(
        f"\t Room: {player.current_room.name}\n {player.current_room.description}")
    print(
        f'items available in this room are: {[item.name for item in player.current_room.view_room_items()]}')

    cmd = input('make a move? ').strip().lower().split(" ")

    current_items = {
        item.name: item for item in player.current_room.view_room_items()}

    player_items = {item.name for item in player.view_inventory()}
    # print('current_items', [current_items])

    if cmd[0] == "q":
        print('Your are Leaving the game')
        break
    elif cmd[0] == 'n' or cmd[0] == 's' or cmd[0] == 'e' or cmd[0] == 'w':
        player.move(cmd[0])

    elif cmd[0] == 'i':
        print(f'items in inventory: {player_items}')

    elif len(cmd) == 2:
        verb = cmd[0]
        item_name = cmd[1]

        if verb == "take" or verb == "get":
            # print('verb', verb)
            # print('item_name', item_name)
            if item_name not in current_items:
                print("Item does not exist in this room!")
                continue
            else:
                player.current_room.remove_item(current_items[item_name])
                player.grab_item(current_items[item_name])
                current_items[item_name].on_take()
        elif verb == 'drop':
            if item_name not in current_items:
                player.current_room.add_item(current_items[item_name])
                player.drop_item(current_items[item_name])
                current_items[item_name].on_drop()
            else:
                print('Well this is embarrasing, you dont have an ' + item_name)
                continue

    else:
        print('please enter the proper commands "n", "s", "e", "w", "i" for Inventory, "q" for Quit ')


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
