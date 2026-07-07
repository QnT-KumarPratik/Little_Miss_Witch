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
    potion: Potion | None = field(default=None)
    effstack: tuple[float, float, float, float] | None = None

    def add(self, herb, char):
        if self.fluid is None:
            print("The cauldron has no brewing fluid.")
            return False

        if not isinstance(herb, Herb):
            print("Only herbs may be added.")
            return False

        if not char.remove(herb):
            print(f"{char.name} doesn't have {herb.name}.")
            return False

        self.herbs.append(herb)

        if self.effstack is None:
            self.effstack = herb.vectors
        else:
            self.effstack = resAdd(self.effstack, herb.vectors)

        print(f"Added {herb.name}.")
        return True


    def fill(self, fluid, amount, char):
        """
        Parameters
        ----------
        amount : float
            fraction of cauldron to fill from 0.0 to 1.0.
        """
        if not isinstance(fluid, Fluid):
            print("Only fluids may be poured.")
            return False

        if not (0 < amount <= 1):
            print("Amount must be between 0 and 1.")
            return False

        if self.fluid is not None:
            print("The cauldron already contains fluid.")
            return False

        if not char.remove(fluid):
            print(f"{char.name} has no {fluid.name}.")
            return False

        self.fluid = fluid
        self.amount_ml = self.stats["capacity"] * amount

        print(
            f"Filled with {self.amount_ml:.0f} mL of {fluid.name}."
        )
        return True
        
    def brew(self):
        if self.fluid is None:
            print("Nothing to brew.")
            return None

        if not self.herbs:
            print("There are no herbs inside.")
            return None
        
        assert self.effstack is not None
        herb_effects = dict(
            zip(Herb.EFFECT_NAMES, self.effstack)
            )

        self.potion = Potion(
            potname(self.herbs, self.fluid),
            f"A potion brewed using {self.fluid.suffix.lower()} and made from"
            + ", ".join(h.name for h in self.herbs),
            herb_effects
        )

        print(f"Brewed {self.potion.name}.")

        return self.potion
    

    def get(self, char):
        if self.potion is None:
            print("There is no finished potion.")
            return None

        char.add(self.potion)

        potion = self.potion

        self.empty()

        print(f"{char.name} obtained {potion.name}.")

        return potion

    def empty(self):
        self.herbs.clear()
        self.fluid = None
        self.amount_ml = 0
        self.effstack = None
        self.potion = None


# ==========================
# Player
# ==========================

@dataclass
class Character:
    name: str = "Player"
    species: str = "Human"
    inventory: dict[object, int] = field(default_factory=dict)

    selected = None
    balance = 0

    def add(self, item, amount=1):
        self.inventory[item] = self.inventory.get(item, 0) + amount

    def remove(self, item, amount=1):
        if item not in self.inventory:
            return False

        self.inventory[item] -= amount

        if self.inventory[item] <= 0:
            del self.inventory[item]
        return True

    def has(self, item):
        return item in self.inventory

    def show_inventory(self):
        print(f"\n=== {self.name}'s Inventory ===")

        if not self.inventory:
            print("Inventory Empty.")
            return

        print("\nItem                 Qty")
        print("-" * 24)

        for item, qty in self.inventory.items():
            print(f"{item.name:<20} {qty}") # type: ignore

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


