# README
This game is based on the lets talk data adventure tutorial found [here](https://github.com/phillipjohnson/text-adventure-tut) with some minor tweaks (_note: I originally found the code from the blog posts and thus have a bootleg copy of these files rather than a copy of the real repo_). I worked on this to build more familiarity with python, hopefully a somewhat interesting game is a byproduct. **Requires Python 3**

## Running the Game
Download the death_to_fairyland directory. From inside that directory run the following command at the command line (e.g. Git Bash for Windows or Terminal for OS X).

    python game.py

## Things that could be improved:
Since this is more or less an exercise in object oriented programing and not game design there are a bunch of things that could be improved in the game... some of which are listed below:


#### Puzzles
It would be cool to add some puzzles and choices to the game, especially since the combat system is very simple

#### Items
Item value is basically useless since there is no in game economy (buying, selling, trading)

#### Combat System
Combat is very simple, the best weapon is selected for the player and is based on damage only.  

#### Map
As currently implemented the map is fairly cryptic, a NSEW description might be a helpful way to make navigation more useful. Perhaps a "look around" command that describes a MapTile.

#### File Storage
YAML files might be a great way to save and store all the text in this text based adventure.
