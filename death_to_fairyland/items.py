#http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# class Gold(Item):
#     def __init__(self, amt):
#         self.amt = amt
#         super().__init__(name="Gold",
#                          description="A round coin with {} stamped on the front.".format(str(self.amt)),
#                          value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Claws(Weapon):
    def __init__(self):
        super().__init__(name="Claws",
                         description="""Straight out of Nightmare on Elmstreet,
these are great for tickling Elmo or whatever annoying
other sacrine soaked muppets come your way!""",
                         value=10,
                         damage=15)

class Shiv(Weapon):
    def __init__(self):
        super().__init__(name="Shiv",
                         description="""A homemade shiv made out of a sharpened toothbrush.
This versitle tool is handy for covert shanking
or spontanious dental hygene!""",
                         value=1,
                         damage=5)


class Bat(Weapon):
    def __init__(self):
        super().__init__(name="Bat with a Nail",
                         description="""A Baseball Bat with a Nail in it.
Classy with an i.""",
                         value=20,
                         damage=25)

class RocketLauncer(Weapon):
    def __init__(self):
        super().__init__(name="Rocket Launcher",
                         description="""A Military Grade death machine. Awesome!""",
                         value=50,
                         damage=50)
# class Rock(Weapon):
#     def __init__(self):
#         super().__init__(name="Rock",
#                          description="A fist-sized rock, suitable for bludgeoning.",
#                          value=0,
#                          damage=5)
#
#
# class Dagger(Weapon):
#     def __init__(self):
#         super().__init__(name="Dagger",
#                          description="A small dagger with some rust. Somewhat more dangerous than a rock.",
#                          value=10,
#                          damage=10)
