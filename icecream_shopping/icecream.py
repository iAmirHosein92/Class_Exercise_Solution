import pyinputplus as pyip
import pandas as pd
import os



class IceCream:
    if os.path.exists('ice_creams_kinds.csv'):
         icecream_dict = pd.read_csv('ice_creams_kinds.csv', index_col=0).transpose().to_dict()
    else:
        icecream_dict = {}

    def __init__(self, name, weight, price):
            self.name = name
            self.weight = weight
            self.price = price
            self.new_icecream = {}
            self.define_new_icecream()

    def define_new_icecream(self):
        self.new_icecream[self.name] = {'weight': self.weight, 'price': self.price}
        for icecream in self.new_icecream.keys():
            if icecream not in self.icecream_dict:
                IceCream.icecream_dict[self.name] = {'weight': self.weight, 'price': self.price}
                self.ic_save()
                return self.new_icecream.items()


    def ic_save(self):
        ic_df = pd.DataFrame.from_dict(IceCream.icecream_dict)
        ic_df = ic_df.transpose()
        ic_df.to_csv('ice_creams_kinds.csv', index=True)



class Musical(IceCream):
    def __init__(self, name, weight, price, songs):
        super().__init__(name, weight, price)
        self.songs = songs
        self.add_song_to_icecream()
        print(self.new_icecream)


    def add_song_to_icecream(self):
        self.new_icecream[self.name]['songs'] = self.songs
        IceCream.icecream_dict[self.name]['songs'] = self.songs
        self.ic_save()
        return self.new_icecream.items()

