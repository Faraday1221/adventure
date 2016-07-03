Some things to keep in mind here:

- Basic Map modified for DTF
- Adding an "interactive" scene for each room?

Things that could be improved:
## Misc
- Giving the player provides no benefit

## Tiles
- add "scenes" to Rooms something like.
>    for i in string.split('\n'):
        print(i,'\n')
        pause(2)


## Items
- pick up items over and over again when entering rooms
    - perhaps a unique attribute?
    - perhaps a in inventory attribute check

## Fighting System
- The fighting system doesn't allow us to change weapons
    - So there is basically no point in "selecting a weapon"
    - It isn't clear how we could select a weapon, either when we pick it up or from inventory
- Weapons have no speed, that would be a cool differentiator    
