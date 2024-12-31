from icecream import IceCream
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
        name, price, weight = menu.define_new_icecream()
        if name not in ice_creams_kinds:
            new_icecream = IceCream(name=name, weight=weight, price=price)
            ice_creams_kinds = IceCream.icecream_dict.copy()
            print(ice_creams_kinds)
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

