import pyinputplus as pyip
from icecream import IceCream

class Menu:
    def __init__(self):
        self.name= ""
        self.price = 0
        self.weight = 0
        self.songs = None

    def show(self):
        user_input = pyip.inputMenu(choices=
                                    ["Stock Report",
                                    "Define New Icecream",
                                    "Add Icecream To Stock",
                                    "Sell Icecream",
                                    "Edit Icecream",
                                    "Exit"],
                                    numbered=True)
        if user_input == "Stock Report":
            return 1
        elif user_input == "Define New Icecream":
            return 2
        elif user_input == "Add Icecream To Stock":
            return 3
        elif user_input == "Sell Icecream":
            return 4
        elif user_input == "Edit Icecream":
            return 5
        elif user_input == "Exit":
            return 6
        else:
            print("Invalid Input")

    def which_type(self):
        which_type = pyip.inputMenu(['Normal', 'Musical'], prompt= "Which Type Would you like to add?\n", numbered=True,blank=False)
        return which_type.lower()


    def define_new_icecream(self,ice_cream_type):
        self.name = pyip.inputStr("Please Enter Icecream Kind Name: ", blank=False, )
        self.price = pyip.inputFloat("Please Enter Icecream Price: ", min=1, blank=False)
        self.weight = pyip.inputFloat("Please Enter Icecream Weight: ", min=1, blank=False)
        if ice_cream_type == "musical":
            self.songs = pyip.inputStr("Please Enter Song Name: ", blank=False, )

        return self.name, self.price, self.weight, self.songs

    def want_to_add_to_stock(self):
        user_answer = pyip.inputYesNo("Do You Want Add This IceCream To Your Stocks List Now? (Yes/No)\n", blank=False)
        return user_answer


