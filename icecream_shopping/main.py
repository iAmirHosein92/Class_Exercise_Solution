from icecream import IceCream, Musical
from warehouse import Warehouse
from menu import Menu

#check if any data available for warehouse and stocks
warehouse = Warehouse()

menu = Menu()

turn_on = True

while turn_on:
    ice_creams_kinds = IceCream.icecream_dict.copy()

    user_input = menu.show()
    if user_input == 1 :
        warehouse.stock_report()
        print('\n')

    elif user_input == 2 :

        ice_cream_type = menu.which_type()
        name, price, weight, songs = menu.define_new_icecream(ice_cream_type)

        if name not in ice_creams_kinds:
            if ice_cream_type == 'normal':
                new_icecream = IceCream(name=name, weight=weight, price=price)
            elif ice_cream_type == 'musical' :
                new_icecream = Musical(name=name, weight=weight, price=price, songs=songs)
            ice_creams_kinds = IceCream.icecream_dict.copy()
            user_answer = menu.want_to_add_to_stock()
            if user_answer.lower() == 'yes':
                warehouse.add_to_stock(ice_creams_kinds= ice_creams_kinds,ice_cream= new_icecream.new_icecream)
            else:
                print('\nYou Can Add This IceCream From Menu Anytime You Want...\n ')
        else:
            print('This IceCream Have Already Defined Before.')


    elif user_input == 3 :
        warehouse.add_to_stock(ice_creams_kinds= ice_creams_kinds)
    elif user_input == 4 :
        warehouse.sell(ice_creams_kinds= ice_creams_kinds)
    elif user_input == 5 :
        warehouse.edit(ice_creams_kinds= ice_creams_kinds)
    elif user_input == 6:
        warehouse.save()
        turn_on = False
        break

