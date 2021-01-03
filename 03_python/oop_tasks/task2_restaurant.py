# Menu class that inherits from dictionary allowing for easier updating and initialising of menu
class Menu(dict):
    def __init__(self, menu_items):
        for food, price in menu_items.items():
            self.update({food: price})
    
    
    def __str__(self):
        print("\n\n***\nHere's the menu:")

        # prints menu items in nice format with price formatting and capitalisation
        for food, price in self.items():
            print("{}, Price: £{:,.2f}".format(food.title(), price))

        return "Hope you enjoy your visit\n***"


# Order class that inherits from list allowing for easier appending functionality
class Order(list):
    def __init__(self):
        self.make_order()


    def make_order(self):
        # checks for all existing menus and prints to customer
        allowed_menus = [k for k, v in globals().items() if isinstance(v, Menu)]
        
        print("\n***\nPossible Menus:\n")
        for menu in allowed_menus:
            print(menu.strip("menu").replace('_', ' ').title())
        
        # asks for customer option of menu and double checks that it's a valid choice
        self.menu_option = input("\nWhich menu will you be ordering from?\n").lower().replace(' ', '_') + "_menu"
        assert self.menu_option in allowed_menus

        self.menu = [v for k, v in globals().items() if k == self.menu_option][0]
        print(self.menu)
        
        # asks how many items they'd like to order  and which items they'd like
        num_items = int(input("\nHow many items would you like?\n"))
        for i in range(num_items):
            item = input("\nWhat would you like?\n")
            assert item in self.menu.keys()
            self.append(item)    

        # prints back order to customer
        print(f"This is your order {self}. That'll cost {self.order_total()}")


    def what_is_my_order(self):
        print(self)
        
    # calculates order total
    def order_total(self):
        total = 0
        for order_item in self:
            total += [price for food, price in self.menu.items() if food == order_item][0]
        
        return total


if __name__ == "__main__":
    japanese_items = {"sushi": 9, "ramen": 5, "katsu curry": 6}
    lunch_items = {"katsu curry": 5, "onigiri": 2}
    
    japan_menu = Menu(japanese_items)
    japan_lunch_menu = Menu(lunch_items)
    japan_menu["ramune"] = 3
    
    leo_order = Order()
    leo_order.what_is_my_order()
    leo_order.order_total()