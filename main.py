##import self.Files
from lore import *
from classes import Character
from data import *
from mmgui import mmenu

##Initial stage
import time
import json
import os
data={
"Intro" : 0,
"Tuto": 0,
"Core": 0
}
path = "pg.json"
pn = None
if os.path.exists(path):
    with open(path, "r") as pgn:
        pn = json.load(pgn)
else:
    with open("pg.json", "w") as file:
        json.dump(data, file, indent=4)
    pn = data

strt = mmenu()
if strt:
    pass
