

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up_description(self):
        print("Congrats you now have the " + self.name)

    def drop_description(self):
        print("Dam this thing! I am dropping the " + self.name)
