# Introduction
This adventure game is based off the post (need link) at the lets talk data blog. With the exception of minor tweaks to get the code working properly, I have not altered this code from the original post. Since I am working through this project as a developmental exercise I plan to catalog my progress in this README file. As such expect to see a breakout of things I understand and do not understand below:

## Items
The items.py file is fairly straightforward and a solid example of how to develop a class with multiple subclasses. This is perhaps the most easily comprehensible section of the code.

## Enemies
The enemies.py file creates the Enemy class which is then instantiated into the enemies the player will encounter in the game, including a GiantSpider and Snake. The enemies are then instantiated on an as needed basis corresponding to the rooms in which they inhabit (see tiles.py).

## Player
The player.py file creates the Player class. This class is supported by a number of key functions that enable gameplay. including
- is_alive: a basic bool function also shared by enemies
- inventory: the inventory is created as a list, there is also a function to display the inventory via print_inventory
- move: this updates the location and plays the intro_text for a tile
    - each direction has an associated function which updates the game coordinates (this aligns closely with \_world which uses location as the dictionary key)
- attack: this selects a weapon (best available) and allows the user to attack an enemy
    - isinstance is used here to ignore the non-objects stored in inventory
    - this fcn allows the Player to modify the enemy hp, recall that modify_player in the tiles class allows the enemy to change the player hp
- **do_action is explained at the end under the game section
- flee is not explained**

## Actions
The actions.py file contains a class and subclasses used to generate the text that will be displayed to the player during game play. This is very helpful because it also assigns hotkeys to the various commands, creating an extremely helpful prompt for the user.

The attribute "method" is used to assign the command required to perform an action using the "do_action" function in the Player class.

These classes essentially allow us to map the human readable prompts and inputs back to the underlying functions. In my mind this is the distinguishing difference between just plugging in python commands and having a game interface.

## Tiles
The tiles.py file demonstrates another example of classes linked to subclasses. Here the MapTile class is refined into generic types of rooms i.e. EnemyRoom and LootRoom before being used to create specific rooms that will be implemented in the game (i.e. GiantSpiderRoom, Find5GoldRoom).

It is easy to imagine that the types of map tiles could be expanded into PuzzleRoom or TrapRoom.

The tiles provide the basic functionality of the game allowing for:
- intro_text: which describes a room
- modify_player: which allows updates to the player character
    - updating the player inventory (when picking up loot)
    - changng the player hp based on an attacking enemy
- calling items (LootRoom) and enemies (EnemyRoom): when the room is instantiated it can be associated with an Item or Enemy

As a convienance to the player the tiles also received the late addition (in section 3 or 4 of the blog post) functionality to survey what moves are available from a given room and to create the "move" list which is passed through other functions until being printed in the user display. Thus each room captures the moves available to a player at any given time and prints them to the prompt.

*note: This section only creates the framework for the rooms that will be implemented as part of the game map, this game map is described in world.py*

## World
To create the game world the author uses a spreadsheet program to create a tab delimited text file saved in resources as map.txt. This file is read into the world.py file which essentially performs the following:
- creates an x and y coordinate according to the position in the map.txt file
- assigns the x, y coordinate from map.txt to the key of a dictionary called \_world
- creates an instantiated Tile based on the room name, and assigns it to the value of the corresponding location key in the \_world dict.
- handles blank tiles by assigning None to the value
- Assigns the starting location for the game based on StartingRoom
- provides a method to easily retrieve the room object based on location (x,y)

**It is unclear if \_world is being properly returned in load_tiles, furthermore it is unclear if the starting_position is being properly updated in the load_tiles function.**

## Game
Although this is the wrapper that allows the whole game to function it is helpful to call out what this does in sequence:

**Game Initializes**
- world.load_tiles() creates the game map and instantiates all the tile instances
- Player() instantiates the player
- The files imported explicetly are:
    - world.py, player.py, items.py
    - The world.py file includes the tile objects as part of the \_world dict, this is where enemies.py and actions.py are incorporated (as part of the location)
    - **where is action.py (its sad this I'm having trouble tracing these files)**
- the starting location is also found and the intro text is printed

**Game Begins Loop**
While the player is alive and hasn't won yet the following happens in sequence:
- load room
- modify_player
- check players state (i.e. is alive and hasn't won)
- show the available_actions
    - available_actions are bound to MapTile
    - this consists of adjacent_moves & invantory
    - or in an EnemyRoom with enemy.is_alive == T attack options
    - the available_actions calls on the Actions class which provides the user interface. note that the available_actions are ultimately a list of human readable output based on the Actions class
- user enters an input
- the user input is checked against the each hotkey associated with an action
- if there is a match the action is performed via the player.do_action
    - this is performed as follows:
        - do_action takes an action.py action as an input (i.e. player.do_action(action, \*\*action.kwargs) where action = 'Move north')
        - do_action gets the action attributes by looking up the name attribute (i.e. getattr(self, action.method.__name__))
        - the method attribute is a player command (i.e. Player.move_north)
        - the associated player command is executed with \*\*kwargs for inputs (I dont completely understand what the kwargs are here)
- go to the top of the loop

### Known Issues
- Everytime you enter a Find5GoldRoom you pick up 5 gold (this doesnt change state)
- The inventory doesn't stack gold
