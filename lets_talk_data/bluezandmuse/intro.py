'''after reading through the lets talk data example then looking over the bluezandmuse website I'm uncertain if there is any merit to trying to implement this approach to a text based adventure. It appears somewhat cumbersome, but then again may have some merits.

For now though I don't really like it.'''

# write your description text
sections = [
(
"""You are at the front of your friends house. Your friends house is to the North. The driveway is to the South""", "Front of Friend's House"), #0
(
"""You are in your friends house. The kitchen is to the East, the living room to the West.""", "Friend's House") #1
]

# create enumerated python-readable text
sec = {}
for indexed in enumerate(sections):
    index = indexed[0]
    long_name = indexed[1][1] #description
    short_name = ''
    for C in long_name:
        if C in ' /': #spaces and slashes to dashes
            short_name += '-'
        elif not C in ".'": # dont use periods and approstrophies
            short_name += C.lower()
    sec[short_name] = index

# make the direction dictionary
# NOTE: there are many more on the website!
dirs = {'north':0, 'n':0,
        'south':1, 's':1,
        'west':2, 'w':2,
        'east':3, 'e':3}
