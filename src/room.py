# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
# we need a way to connect the directional input to the directional keys and link in the adv.py
    def room_direction(self, input):
        if input == 'n':
            return self.n_to
        elif input == 's':
            return self.s_to
        elif input == 'e':
            return self.e_to
        elif input == 'w':
            return self.w_to
        else:
            return None