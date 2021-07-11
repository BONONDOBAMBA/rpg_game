from entities.entity import Entity

class Player(Entity):
    def __init__(self, name, hp, damage, drip):
        super().__init__(name, hp, damage)

        self.drip = drip

    def __str__(self):
        return super().__str__()[0:-1] + f" - Drip: {self.drip}>"
