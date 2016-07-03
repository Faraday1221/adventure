import world
from tiles import title_screen, game_over
from player import Player
# import time
#
# def print_pause(text):
#     """prints each line with a pause,
#        expects a list with each item a string"""
#     for line in text:
#         print(line)
#         time.sleep(2)

def play():
    print(title_screen())
    input("Press Any Key to Start: ")
    world.load_tiles()
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    # print_pause(room.intro_text()) # trying this instead of above
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    print(game_over())


if __name__ == "__main__":
    play()
