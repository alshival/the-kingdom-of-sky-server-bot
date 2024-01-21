import os
import re
import discord

map_dir = 'public/maps/'

SkyRealms ={
    "isle": "Isle of Dawn",
    "prairie": "Daylight Prairie",
    "forest": "Hidden Forest",
    "valley": "Valley of Triumph",
    "wasteland": "Golden Wasteland",
    "vault": "Vault of Knowledge",
  }

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
    response = ''
    if (map is None) and (spirit is None):
        class Map:
            def __init__(self):
                self.value = 'map_art'
    
        # Creating an instance of the Map class
        map = Map()
        response = f"""
This function provides information about {SkyRealms[realm]}.
**Map Options** 
* Map Art: Rerturns the map art shown below.
* Map Pics: Returns maps designed by the Sky Infographics Database.
**Spirit Options**
* Trees: Returns the Spirit Cosmetic/Spell Trees for the realm.
* <Spirit>: Returns an infographic on a specific spirit's location.
"""
        file = [filename for filename in os.listdir(map_dir) if re.search(f"{realm}\.art\.webp", filename)][0]
        return [[discord.File(map_dir + file, filename=f"{realm}.art.webp")],response]
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
    return [files_to_send,response]