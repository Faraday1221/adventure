class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class DustBunny(Enemy):
    def __init__(self):
        super().__init__(name="Dust Bunny", hp=5, damage=1)

class Witch(Enemy):
    def __init__(self):
        super().__init__(name="Witch", hp=40, damage=15)

class Cthulu(Enemy):
    def __init__(self):
        super().__init__(name="Cthulu", hp=100, damage=25)


# class GiantSpider(Enemy):
#     def __init__(self):
#         super().__init__(name="Giant Spider", hp=10, damage=2)
#
# class Ogre(Enemy):
#     def __init__(self):
#         super().__init__(name="Ogre", hp=30, damage=15)
#
# # jb added -- seems like an oversite on the website
# class Snake(Enemy):
#     def __init__(self):
#         super().__init__(name="Snake", hp=5, damage=10)
