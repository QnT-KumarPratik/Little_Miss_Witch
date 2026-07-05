##import self.Files
from lore import *
from classes import Character
from data import *

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

##Progression read
def lazyprint(text, pace=2.0):
    texts = text.split("""

""")
    for txt in texts:
        print(txt)
        time.sleep((len(txt)/(pace*26)))
        print("\n")

if not pn["Core"]:
    if not pn["Intro"]:
        print("""=================================================
        LITTLE MISS WITCH
=================================================""")
        lazyprint(Intro, 1)
        temp = input("Press enter to continue...")
        del temp
        pn["Intro"] = True
        print("\n\n\n")

    if not pn["Tuto"]:
        lazyprint(TutoInit, 0.75)
        crug = False
        chc = input("Type 'start' to begin tutorial or 'skip' to quit tutorial.")
        while not crug:
            if chc.lower() == "skip":
                crug = True
                pn["TC"] = 6
            elif chc.lower() != "start":
                chc=input("'skip' or 'start'")
            else:
                del crug
                pn["TC"]=0
                break

    