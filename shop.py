# ==========================
# Imports
# ==========================

from dataclasses import dataclass, field

# ==========================
# Shop
# ==========================

@dataclass
class Shop:

    name: str = "Village Shop"

    stock: dict = field(default_factory=dict)

    # ----------------------
    # Display
    # ----------------------

    def show(self):
        """Displays the current stock."""
        pass

    # ----------------------
    # Buying
    # ----------------------

    def buy(self, char, item, amount=1):
        """Player buys an item."""
        pass

    # ----------------------
    # Selling
    # ----------------------

    def sell(self, char, item, amount=1):
        """Player sells an item."""
        pass

    # ----------------------
    # Stock Management
    # ----------------------

    def add_stock(self, item, amount, price):
        """Adds an item to the shop."""
        pass

    def remove_stock(self, item, amount):
        """Removes stock."""
        pass

    def has_stock(self, item, amount=1):
        """Checks availability."""
        pass

    # ----------------------
    # Future
    # ----------------------

    def restock(self):
        """Daily restock."""
        pass

    def generate_daily_stock(self):
        """Procedural stock generation."""
        pass

    def update_prices(self):
        """Dynamic pricing."""
        pass