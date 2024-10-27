# not sure if this or resources really need to be a class
# if so then i'll make a class for a text display thing
class Survivors():
    def __init__(self):
        self.survivors = 0
    
    def update(self, delta):
        if delta < 0:
            self.survivors += delta