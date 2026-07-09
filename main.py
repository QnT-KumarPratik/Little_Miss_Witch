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

#webthinsies
import webbrowser

def open_link(url: str):
    """
    Opens the given URL in the default web browser.
    Includes basic validation to ensure the URL is valid.
    """
    # Basic validation
    if not isinstance(url, str) or not url.strip():
        raise ValueError("URL must be a non-empty string.")
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("URL must start with 'http://' or 'https://'.")

    try:
        # Open in a new browser tab
        opened = webbrowser.open_new_tab(url)
        if opened:
            return True
    except Exception as e:
        return f"{type(e).__name__}: {e}"


strt = mmenu()
if strt:
    pass
else:
    quit()
