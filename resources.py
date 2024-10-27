class Resources():
    def __init__(self):
        resources = 0
    
    def update(self, resourcesGained, lostToFlood):
        self.resources += resourcesGained
        if lostToFlood == True:
            self.resources = 0
