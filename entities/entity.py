class Entity:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return f"<Name: {self.name} - HP: {self.hp} - Damage: {self.damage}>"

    def set_hp(self, x):
        self.hp = x
