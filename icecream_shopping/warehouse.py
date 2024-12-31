import pyinputplus as pyip
import pandas as pd
import os

CAPACITY = 200000
class Warehouse:
    def __init__(self):
        self.stock_data = {}
        self.stock= 0
        self.profit = 0
        self.check_csv()
    def check_csv(self):
        if os.path.exists('warehouse.csv'):
            self.stock_data = pd.read_csv('warehouse.csv', index_col=0).transpose().to_dict()
            for ice_cream,values in self.stock_data.items():
                self.stock += values["weight"]
            return self.stock_data
        else:
            return {}
    def stock_report(self):
        if self.stock_data == {}:
            print("You don't have any IceCreams.")
        else:
            self.stock = 0
            num = 0
            for ice_cream,values in self.stock_data.items():
                num += 1
                print(f'{num}. {ice_cream.title()}: {values["weight"]} g(s).')
                self.stock += values["weight"]
            print(f'***     Total Ice Creams: "{self.stock}" g(s)       ***')
            print(f"---     Capacity is : < {CAPACITY - self.stock} kg(s) >     ---")


    def add_to_stock(self, ice_creams_kinds, ice_cream=None):
        if ice_cream is None:
            if ice_creams_kinds == {}:
                print('You have not defined any IceCreams before.')
            else:
                user_input_kind = pyip.inputMenu(choices=list(ice_creams_kinds.keys()),
                                                 prompt='What Kind of IceCream(s) would you like to add?\n',
                                                 numbered=True, blank= False)
                user_input_quantity = pyip.inputInt(prompt="How many IceCreams would you like to add? :  ", blank=False)
                ice_cream_weight = ice_creams_kinds[user_input_kind]['weight'] * user_input_quantity

                if ice_cream_weight + self.stock > CAPACITY:
                    print("You Haven't Enough Rooms To Add These Quantity of IceCreams.")
                else:
                    self.stock += ice_cream_weight

                    if user_input_kind in self.stock_data:
                        self.stock_data[user_input_kind]['weight'] += ice_cream_weight
                    else:
                        self.stock_data[user_input_kind] = {"weight": ice_cream_weight, "price" : ice_creams_kinds[user_input_kind]['price'], "songs" : ice_creams_kinds[user_input_kind]['songs']}
                    print(
                        f'{user_input_kind} Ice Cream Now is < {self.stock_data[user_input_kind]["weight"]} g(s) > .\n')

        else:
            for icecream, values in ice_cream.items():
                if icecream not in self.stock_data:
                    user_input_quantity = pyip.inputInt(prompt="How many IceCreams would you like to add? :  ",
                                                        blank=False)
                    ice_cream_weight = values['weight'] * user_input_quantity
                    if ice_cream_weight + self.stock > CAPACITY:
                        print("You Haven't Enough Rooms To Add These Quantity of IceCreams.")
                    else:
                        self.stock_data[icecream] = {'weight': ice_cream_weight, 'price': values['price']}
                        self.stock += ice_cream_weight
                        print(f'" {icecream} " Added To Your Stocks Successfully...\n')

            print(f'Your warehouse have  < {CAPACITY - self.stock} kg(s) > rooms.\n')


    def sell(self, ice_creams_kinds):
        self.profit = 0
        if self.stock_data == {}:
            print("You don't have any IceCreams To Sell.")
        else:
            user_input_ice_cream = pyip.inputMenu(choices=list(self.stock_data.keys()), prompt='What Ice Cream(s) would you like to sell?\n', numbered= True, blank=False)
            user_input_ice_cream_quantity = pyip.inputInt(prompt="How many IceCreams would you like to sell? :  ",min= 1, blank=False)
            if user_input_ice_cream == "musical":
                user_input_ice_cream_quantity *= 2
                songs = self.stock_data[user_input_ice_cream]['songs'].split(', ')
                print(songs)
                pyip.inputMenu(choices=songs, prompt='Which Song would you like to Play?\n',numbered= True, blank=False)
            weight = ice_creams_kinds[user_input_ice_cream]['weight'] * user_input_ice_cream_quantity
            if weight > self.stock_data[user_input_ice_cream]['weight']:
                print(f"Not enough < {user_input_ice_cream} > Ice Creams.")
                print(f"You Have < {self.stock_data[user_input_ice_cream]['weight']} > g(s) Ice Creams . ")
            else:
                    self.stock_data[user_input_ice_cream]['weight'] -= weight
                    self.stock -= weight
                    self.profit  += (self.stock_data[user_input_ice_cream]['price'] * user_input_ice_cream_quantity) * 0.20
                    print(f"Price : {self.stock_data[user_input_ice_cream]['price'] * user_input_ice_cream_quantity}")
                    print(f"Your Profit : {self.profit}")
                    print(f'" {user_input_ice_cream} x {user_input_ice_cream_quantity} " Sold .\n')

    def edit(self,ice_creams_kinds):
        if self.stock_data == {}:
            print("You don't have any IceCreams To Edit.")
        else:
            user_input_ice_cream = pyip.inputMenu(choices=list(ice_creams_kinds.keys()), prompt='What Ice Cream(s) would you like to Edit?\n', numbered= True, blank=False)
            user_input_option = pyip.inputMenu(choices=list(ice_creams_kinds[user_input_ice_cream].keys()), prompt='Which Option you want to edit?\n', numbered= True, blank=False)
            print(user_input_ice_cream)
            print(user_input_option)
            if user_input_ice_cream == "musical" and user_input_option == "songs":
                    songs = ice_creams_kinds[user_input_ice_cream]['songs'].split(',')
                    input_song = pyip.inputStr(prompt= 'What Song would you like to Add?\n')
                    songs.append(f" '{input_song.title()}' ")
                    ice_creams_kinds[user_input_ice_cream]['songs'] = ','.join(songs)
            elif user_input_option == "songs":
                print("You Can't Set Music For This Kind Of Ice Cream.")

            elif user_input_option== "weight" or user_input_option == "price":
                ice_creams_kinds[user_input_ice_cream][user_input_option] = pyip.inputFloat(prompt=f'Enter New Ice Cream {user_input_option}: ', blank=False)

    def save(self):
        wh_df = pd.DataFrame.from_dict(self.stock_data)
        wh_df = wh_df.transpose()
        wh_df.to_csv('warehouse.csv', index=True)
