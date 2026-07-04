#imports
from classes import *


##herbs
# (healing, strength, sleep, lifeforce)

mint = Herb(
    "Mint",
    "A refreshing herb known to soothe the body and sharpen the senses.",
    (0.35, 0.15, -0.20, 0)
)

nightshade = Herb(
    "Nightshade",
    "A beautiful but infamous poisonous plant. Handle with care.",
    (-0.75, -0.20, 0.85, -1)
)

glowshroom = Herb(
    "Glowshroom",
    "A faintly luminous mushroom that thrives in damp caves.",
    (0.20, 0.10, 0.35, 0)
)

gloomberry = Herb(
    "Gloomberry",
    "Dark berries with a bitter taste. Hunters avoid eating them before a journey.",
    (-0.30, -0.10, 0.70, 0)
)

warfbloom = Herb(
    "Warfbloom",
    "A crimson flower traditionally brewed before battles.",
    (-0.10, 0.80, -0.35, 0)
)

sunleaf = Herb(
    "Sunleaf",
    "Golden leaves that seem warm even on cold mornings.",
    (0.60, 0.25, -0.40, 1)
)

moonroot = Herb(
    "Moonroot",
    "A pale root harvested only under moonlight.",
    (0.10, -0.15, 0.90, 0)
)

embermoss = Herb(
    "Ember Moss",
    "A dry moss that retains warmth for hours after sunset.",
    (-0.15, 0.45, -0.25, 0)
)


##fluids
water = Fluid("water", "The very essence of making potions", (1, 4, 1, 1), "Stew")
alcohol = Fluid("alcohol", "A common base for many", (1.35, 2.336, 1, 0.791), "Extract")


##apparatus
cauldron = Cauldron(
    "Iron Cauldron",
    "A heavy iron vessel used by alchemists.",
    {"brew", "heat"},
    {"capacity": 1000}
)


###available stuffs
ingredients = {
    "Herbs" : (mint, nightshade, glowshroom, gloomberry, warfbloom, sunleaf, moonroot, embermoss),
    "Fluids" : (water, alcohol)
}