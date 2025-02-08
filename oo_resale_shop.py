class ResaleShop:

    # construct shop object
    def __init__(self):
        self.inventory = []

    # buy a computer, add it to inventory
    def buy_comp(self, item: "Computer"):  
        print(f"Buying {item.title}...")
        self.inventory.append(item)
        print("Successfully added to inventory.")

    # sell a computer, check if you have it, if so remove from inventory
    def sell_comp(self, item: "Computer"):
        print(f"Selling {item.title}...")
        if item in self.inventory:
            self.inventory.remove(item)
            print("Successfully removed from inventory.")
        else:
            print("Item not found in inventory.")

    # display inventory unless it is empty
    def display_inventory(self):
        print("Checking inventory...")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for comp in self.inventory:
                comp.display_computer()
