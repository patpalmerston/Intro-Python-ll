

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print("Congrats you now have the " + self.name)

    def on_drop(self):
        print("Dam this thing! I am dropping the " + self.name)
