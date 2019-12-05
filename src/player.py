# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

# version 1
#     def move(self, direction):
#         room = self.current_room.room_direction(direction)
#         #print('player.py', direction)
#         if room is not None:
#             self.current_room = room
#             # print('player.py room', room.name)
#             # print('player.py direction', direction)
#         else:
#             print('the way is blocked')
