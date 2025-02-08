class ResaleShop:
    def __init__(self):
        self.inventory = []

    def buy_comp(self, item: "Computer"):  # Use "Computer" as a string to prevent circular import
        print(f"Buying {item.title}...")
        self.inventory.append(item)
        print("Successfully added to inventory.")

    def sell_comp(self, item: "Computer"):
        print(f"Selling {item.title}...")
        if item in self.inventory:
            self.inventory.remove(item)
            print("Successfully removed from inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Checking inventory...")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for comp in self.inventory:
                comp.display_computer()
