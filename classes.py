from dataclasses import dataclass, field
from enum import Enum
import math

# ==========================
# Effect Definitions
# ==========================

class HerbEffect(Enum):
    HEALING = "healing"
    STRENGTH = "strength"
    SLEEP = "sleep"
    LIFEFORCE = "lifeforce"


class FluidEffect(Enum):
    ETA = "eta"
    C = "C"
    GRADE = "grade"
    RHO = "rho"


# ==========================
# Base Ingredient
# ==========================

@dataclass
class Ingredient:
    name: str
    description: str
    vectors: tuple

    EFFECT_NAMES = ()

    def __post_init__(self):
        if len(self.vectors) != len(self.EFFECT_NAMES):
            raise ValueError(
                f"{self.name}: expected {len(self.EFFECT_NAMES)} vector values."
            )

    @property
    def effects(self):
        return dict(zip(self.EFFECT_NAMES, self.vectors))

    def __repr__(self):
        return f"{self.name.upper()}\n\t{self.description}\n"


# ==========================
# Ingredient Types
# ==========================

class Herb(Ingredient):
    EFFECT_NAMES = tuple(e.value for e in HerbEffect)

@dataclass
class Fluid(Ingredient):
    EFFECT_NAMES = tuple(e.value for e in FluidEffect)
    suffix: str = "Fluid"

# ==========================
# Apparatus
# ==========================

@dataclass
class Apparatus:
    name: str
    description: str

    tags: set[str] = field(default_factory=set)
    stats: dict[str, float] = field(default_factory=dict)

    def __repr__(self):
        return (
            f"{self.name}\n"
            f"\t{self.description}\n"
            f"\nTags: {self.tags}\n"
            f"\tStats: \n{self.stats}"
        )

@dataclass
class Cauldron(Apparatus):

    herbs: list = field(default_factory=list)
    fluid: Fluid | None = None
    amount_ml: float = 0
    potion = None
    effstack = []

    def add(self, herb, char):
        
        pass

    def fill(self, fluid, amount, char):
        """
        Parameters
        ----------
        amount : float
            fraction of cauldron to fill from 0.0 to 1.0.
        """
        pass

    def brew(self):
        pass

    def get(self, char):
        pass

    def empty(self):
        pass


# ==========================
# Player
# ==========================

@dataclass
class Character:
    name: str = "Player"
    species: str = "Human"
    inventory: dict = field(default_factory=dict)

    selected = None

    def add(self, item, amount=1):
        self.inventory[item.name] = self.inventory.get(item.name, 0) + amount

    def remove(self, item, amount=1):
        if item.name not in self.inventory:
            return False
        
        if self.inventory[item.name] < amount:
            return False

        self.inventory[item.name] -= amount

        if self.inventory[item.name] <= 0:
            del self.inventory[item.name]

        return True

    def has(self, item):
        return item.name in self.inventory

    def show_inventory(self):
        print(f"\n=== {self.name}'s Inventory ===")

        if not self.inventory:
            print("Inventory Empty.")
            return

        print("\nItem                 Qty")
        print("-" * 24)

        for item, qty in self.inventory.items():
            print(f"{item:<20} {qty}")

    def select(self, item):
        if not self.has(item):
            return False

        self.selected = item
        return True

    def clear_selection(self):
        self.selected = None
    
    def __repr__(self):
        return f"{self.name} ({self.species})"
    

# ==========================
# Potions
# ==========================

#funcs for Potions
def potname(ing, fl):
    return f"{ing.name.capitalize()} {fl.suffix.capitalize()}"

def unit(vec):
    mag = math.sqrt(sum(x*x for x in vec))

    if mag == 0:
        return tuple(0 for _ in vec)

    return tuple(x / mag for x in vec)

def dirv(vec, index):
    return tuple(
        value
        for i, value in enumerate(vec)
        if i != index
    )

def simmilarity(a,b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")
    ua = unit(a)
    ub = unit(b)
    return sum(
        x*y
        for x, y in zip(ua, ub)
    )

def resAdd(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")
    out = []
    resConst = 2
    for i in range(len(a)):
        aval = a[i]
        bval = b[i]

        adir = dirv(a, i)
        bdir = dirv(b, i)

        res = simmilarity(adir, bdir)
        scale = ((res + 1) / 2) ** resConst

        rsult = (aval + bval)*scale
        out.append(rsult)
    Out =[]
    for j in out:
        Out.append(round(j, 3))
    return tuple(Out)




#---------------------------


@dataclass
class Potion:
    name: str
    description: str

    effects: dict[str, float]


