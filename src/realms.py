import os
import re
import discord

map_dir = 'public/maps/'

def get_map_art(realm):
    maps = os.listdir(map_dir)
    map_matches = [filename for filename in maps if re.search(f"{realm}.*art.*", filename)]
    return [discord.File(map_dir + x, filename=x) for x in map_matches]

def get_map(realm):
    maps = os.listdir(map_dir)
    map_matches = [filename for filename in maps if re.search(f"{realm}(?!.*art).*", filename)]
    return [discord.File(map_dir + x, filename=x) for x in map_matches]

regular_spirit_dir = 'public/spirits/'

def get_spirit_trees(realm):
    spirits = os.listdir(regular_spirit_dir)
    map_matches = [filename for filename in spirits if re.search(f"{realm}.*trees.*", filename)]
    return [discord.File(regular_spirit_dir + x, filename=x) for x in map_matches]

def spirit_info(spirit):
    spirits = os.listdir(regular_spirit_dir)
    map_matches = [filename for filename in spirits if re.search(f".*{spirit}.*", filename)]
    return [discord.File(regular_spirit_dir + x, filename=x) for x in map_matches]

def get_files_to_send(realm,map,spirit):
    files_to_send = []
    if map:
        if map.value == 'map_art':
            files_to_send += get_map_art(realm)
        elif map.value == 'map_pic':
            files_to_send += get_map(realm)
    if spirit:
        if spirit.value=="trees":
            files_to_send += get_spirit_trees(realm)
        elif spirit.value:
            files_to_send += spirit_info(spirit.value)
    return files_to_send