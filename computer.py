# Import only ResaleShop from oo_resale_shop.py
from oo_resale_shop import ResaleShop  

class Computer:
    # construct a computer object with the necessary attributes
    def __init__(self, name: str, year: int, processor: str, HD: int, mem: int, OS: str, amt: int):
        self.title = f"{name} ({year})"
        self.description = name
        self.year_made = year
        self.processor_type = processor
        self.hard_drive_capacity = HD
        self.memory = mem
        self.operating_system = OS
        self.price = amt

    # update the operating system of the computer
    def update_os(self, new_os: str):
        print(f"Updating OS to {new_os}...")
        self.operating_system = new_os
        print("Done.")

    # update the price of the computer
    def update_price(self, new_price: int):
        print(f"Updating price to ${new_price}...")
        self.price = new_price
        print("Done.")

    # display the computer's attributes
    def display_computer(self):
        print(f"""
        Description: {self.description}
        Year Made: {self.year_made}
        Processor Type: {self.processor_type}
        Hard Drive Capacity: {self.hard_drive_capacity}GB
        Memory: {self.memory}GB
        Operating System: {self.operating_system}
        Price: ${self.price}
        """)


def main():
    # create a resale shop object and computer objects
    shop = ResaleShop()  
    computer1 = Computer("Macbook Pro", 2018, "Intel Core i7", 256, 16, "MacOS", 2000)
    computer2 = Computer("Dell XPS", 2020, "Intel Core i5", 512, 8, "Windows 10", 1200)
    computer3 = Computer("HP Pavilion", 2017, "AMD Ryzen 5", 1024, 16, "Windows 11", 900)

    # shop banner
    print("__________________________________________")
    print(" ")
    print("Welcome to my Computer Reseale Shop!")
    print("__________________________________________")
    print(" ")

    # buy a computer and display the inventory
    shop.buy_comp(computer1)
    shop.display_inventory()

    # update the computer's operating system and price, display attributes
    computer1.update_os("MacOS Catalina")
    computer1.update_price(1799)
    computer1.display_computer()

    # buy computers 2 and 3 and display the inventory
    shop.buy_comp(computer2)
    shop.buy_comp(computer3)
    shop.display_inventory()

    # sell computer 1 and display the inventory
    shop.sell_comp(computer1)
    shop.display_inventory()

    # update computer 3's operating system and price, display attributes
    computer3.update_os("Windows 11 Pro")
    computer3.update_price(799)
    computer3.display_computer()

    # update computer 2's operating system and price, display attributes
    computer2.update_os("Windows 11 Home")
    computer2.update_price(999)
    computer2.display_computer()

    # sell computer 3 and show final inventory
    shop.sell_comp(computer3)
    shop.display_inventory()

if __name__ == "__main__":
    main()