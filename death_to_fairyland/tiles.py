


import time
import items, enemies
import world, actions
from player import Player

def print_pause(text):
    """prints each line with a pause,
       expects a list with each item a string"""
    for line in text:
        print(line)
        time.sleep(1)

def title_screen():
    return """
     ____  ____    __   ____  _   _    ____  _____
    (  _ \( ___)  /__\ (_  _)( )_( )  (_  _)(  _  )
     )(_) ))__)  /(__)\  )(   ) _ (     )(   )(_)(
    (____/(____)(__)(__)(__) (_) (_)   (__) (_____)
    ________    ____    .-./`) .-------.       ____     __
   |        | .'  __ `. \ .-.')|  _ _   \      \   \   /  /
   |   .----'/   '  \  \/ `-' \| ( ' )  |       \  _. /  '
   |  _|____ |___|  /  | `-'`"`|(_ o _) /        _( )_ .'
   |_( )_   |   _.-`   | .---. | (_,_).' __  ___(_ o _)'
   (_ o._)__|.'   _    | |   | |  |\ \  |  ||   |(_,_)'
   |(_,_)    |  _( )_  | |   | |  | \ `'   /|   `-'  /
   |   |     \ (_ o _) / |   | |  |  \    /  \      /
   '---'      '.(_,_).'  '---' ''-'   `'-'    `-..-'

   .---.        ____    ,---.   .--. ______
   | ,_|      .'  __ `. |    \  |  ||    _ `''.
 ,-./  )     /   '  \  \|  ,  \ |  || _ | ) _  \\
 \  '_ '`)   |___|  /  ||  |\_ \|  ||( ''_'  ) |
  > (_)  )      _.-`   ||  _( )_\  || . (_) `. |
 (  .  .-'   .'   _    || (_ o _)  ||(_    ._) '
  `-'`-'|___ |  _( )_  ||  (_,_)\  ||  (_.\.' /
   |        \\\\ (_ o _) /|  |    |  ||       .'
   `--------` '.(_,_).' '--'    '--''-----'`

    A stupid text based adventure game. You've been warned.
"""

def game_over():
    return """
    ___    __    __  __  ____    _____  _  _  ____  ____
   / __)  /__\  (  \/  )( ___)  (  _  )( \/ )( ___)(  _ \\
  ( (_-. /(__)\  )    (  )__)    )(_)(  \  /  )__)  )   /
   \___/(__)(__)(_/\/\_)(____)  (_____)  \/  (____)(_)\_)
"""

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.intro_txt = ""
        self.room_txt = ""

    def intro_text(self):
        if self.visited == False:
            self.visited = True
            return self.intro_txt
        else:
            return "\nYou have the feeling you've been here before..."+self.room_txt

    def modify_player(self, player):
        raise NotImplementedError()

    #below added in section 3!
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.intro_txt ="""
You wake up and the sunl is too bright. You might yak.
You have a nasty hangover.
Oh well just another day in Fairyland
...at least there are no strange fairies in your bed.
        """
        self.room_txt = """
Your bedroom. Your life.
What a mess.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def intro_text(self):
        if self.visited == False:
            self.visited = True
            return self.intro_txt
        elif self.enemy.hp > 0:
            return self.intro_txt
        else:
            return "\nYou have the feeling you've been here before..."+self.room_txt

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    # added in section 3!
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class LivingRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DustBunny())

    # def intro_text(self):
        self.intro_txt = """
Your Living Room.
It is quite ordinary.
It's odd that nothing interesting is happening here...
almost like someone put it here and forgot why,
since it serves no real purpose.

...oh Wait a Dust Bunny Monster... there is a purpose.
        """
        self.room_txt = """
Your Living Room.
        """

class Bathroom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Shiv())

    # def intro_text(self):
        self.intro_txt = """
Your Bathroom.
So dirty, so very very dirty.
You will never get laid. :(

You see a deadly looking toothbrush. A shiv in fact!
You are now armed and dangerous.
You pick up Shiv.
        """
        self.room_txt = """
The Bathroom.
Your throne room does not inspire confidence.
        """

class Garden(MapTile):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.intro_txt="""
Your Garden.
Last stop before venturing out into the world
        """
        self.room_txt="""
Your Garden. Nothing is happening here.
        """
    def modify_player(self, player):
        pass

class EnchantedForrest(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.intro_txt = """
The Enchanted Forrest, a magic place filled with wonder!
Somehow it seems... unremarkable.
        """
        self.room_txt="""
Another unremarkable part of the forrest.
        """
    def modify_player(self, player):
        pass

class GingerbreadHouse(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Witch())
        self.intro_txt = """
A Gingerbread house, lets have a look around.
You see ...things. Like umm a Witch.
The Witch is crazy pissed your not a fat child... here she comes!
        """
        self.room_txt="""
A dead Witch. She looks peaceful.
        """

class HiddenRoom(LootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,items.RocketLauncer())
        self.intro_txt = """
You Enter a Hidden Room.
There must be treasure here.
Well no treasure... But there is a BAMF Rocket Launcher in here.
Why would a Witch have this?

You pick up the Rocket Launcher.
        """
        self.room_txt="""
The room is empty, you already took the thing.
        """

class GlassLake(LootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,items.Bat())
        self.intro_txt = """
You see a Lake so still it looks like glass.
In a more sophosticated game there might be a puzzle here.
Instead there is a watery tart with a sword... no not a sword.

You pick up the Bat with a Nail in it.
        """
        self.room_txt="""
Go away you got your bat. There is nothing else to do here.
        """

class LonelyGnomePub(LootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,items.Claws())
        self.intro_txt="""
You enter the Lonely Gnome Pub.
The room is empty. I guess there are no Lonely Gnomes around here.
Oh well no drinks for you. Instead. Have. Some. Claws.

You pick up Claws.
        """
        self.room_txt="""
Truely the least interesting place in the world.
        """

class DragonLair(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Cthulu())
        self.intro_txt="""
You enter a Dark Cave, a lair one might even say.
Oh My, in front of you stands Cthulu Lord of Chaos.
You two are going to be besties...
        """
        self.room_txt="""
A dead squid monster from the Realm of Nightmares lays dead before you.
Perhaps you should do something else.
        """

class TreasureRoom(MapTile):
    def intro_text(self):
        return """
You enter a treasure room.
You have just dispached the Lord of Chaos.
Clearly only good things from here on out.

Suddenly! A whirling vortext of madness appears and sucks you in
Thats the end of the game. You Win! Feel good about it.
        """
    def modify_player(self,player):
        player.victory = True

#===============================================================================
# Old Tiles
#===============================================================================
# class EmptyCavePath(MapTile):
#     def intro_text(self):
#         return """
#         Another unremarkable part of the cave. You must forge onwards.
#         """
#
#     def modify_player(self, player):
#         #Room has no action on player
#         pass
#
# class GiantSpiderRoom(EnemyRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, enemies.GiantSpider())
#
#     def intro_text(self):
#         if self.enemy.is_alive():
#             return """
#             A giant spider jumps down from its web in front of you!
#             """
#         else:
#             return """
#             The corpse of a dead spider rots on the ground.
#             """
#
# class FindDaggerRoom(LootRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, items.Dagger())
#
#     def intro_text(self):
#         return """
#         Your notice something shiny in the corner.
#         It's a dagger! You pick it up.
#         """
#
# # added in section 4!
# class LeaveCaveRoom(MapTile):
#     def intro_text(self):
#         return """
#         You see a bright light in the distance...
#         ... it grows as you get closer! It's sunlight!
#
#
#         Victory is yours!
#         """
#
#     def modify_player(self, player):
#         player.victory = True
#
# # jb added -- seems like an oversight on the website
# class Find5GoldRoom(LootRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, items.Gold(5))
#
#     def intro_text(self):
#         return """
#         You notice 5 gold on the ground. You pick it up.
#         """
# # jb added -- seems like an oversight on the website
# class SnakePitRoom(EnemyRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, enemies.Snake())
#
#     def intro_text(self):
#         if self.enemy.is_alive():
#             return """
#             It appears you have entered a snake pit!
#             """
#         else:
#             return """
#             The snakes are dead, you prevail.
#             """
