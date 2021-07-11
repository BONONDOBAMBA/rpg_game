from entities.entity import Entity

class Enemy(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)