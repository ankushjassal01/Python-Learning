item_price_dict = {
    'Apple': 50,
    'Orange': 20,
    'Grapes': 20,
    'Guava': 20,
    'Bananas': 15
}
cart={}
total_price=0
final_cart={}
final_check= None
print('Choose item from the below list for your cart:')
for index, (item, price) in enumerate(item_price_dict.items()):
    print('{0:<9}:Price(in Rs):{1:^}'.format(item, price))
while final_check != 'P':
    if cart == {}:
        user_choice = input('Please Type Item Name to Add it to Cart: ').capitalize()
        if user_choice in item_price_dict:
            item_count = 1
            cart[user_choice]=[item_price_dict[user_choice],{'QUANTITY(KG)':item_count}]
            total_price += item_price_dict[user_choice]
            print('-'*30)
            print("Your Cart have ITEMS/PRICE(IN RS.)/QUANTITY as: \n{}".format(cart))
            print('Your TOTAL PRICE is : Rs.{}'.format(total_price))
            print('-'*30)
        else:
            print('-'*30)
            print("""Your choice: "{}" is wrong or not in items list. please choose correctly""".format(user_choice))
            print('-'*30)
    else:
        while True:
            add_remove = input("""Enter " + " to ADD MORE ITEMS || " - "  to REMOVE ITEMS || " = " to PROCEED TO PLACE ORDER: """)
            if add_remove == '+':
                print('-'*30)
                print('choose item from the below list for your cart')
                for index, (item, price) in enumerate(item_price_dict.items()):
                    print('{0:<9}:price:{1:^}'.format(item, price))
                print('-'*30)
                add_choice = input('Please Type Item Name to ADD it to Cart: ').capitalize()
                if add_choice in cart:
                    cart[add_choice][0] += item_price_dict[add_choice]
                    cart[add_choice][1]['QUANTITY(KG)'] = cart[add_choice][0] // item_price_dict[add_choice]
                    total_price += item_price_dict[add_choice]
                    print('-'*30)
                    print("Your Cart have ITEMS/PRICE(IN RS.)/QUANTITY as: \n{}".format(cart))
                    print('Your TOTAL PRICE is : Rs.{}'.format(total_price))
                    print('-'*30)
                elif (add_choice in item_price_dict) and (add_choice not in cart):
                    item_count=1
                    cart[add_choice]=[item_price_dict[add_choice],{'QUANTITY(KG)':item_count}]
                    total_price += item_price_dict[add_choice]
                    print('-'*30)
                    print("Your Cart have ITEMS/PRICE(IN RS.)/QUANTITY as: \n{}".format(cart))
                    print('Your TOTAL PRICE is : Rs.{}'.format(total_price))
                    print('-'*30)
                else:
                    print('-'*30)
                    print("""Your choice: "{}" is wrong or not in items list. please choose correctly""".format(add_choice))
                    print('-'*30)
            if add_remove == '-':
                remove_choice = input('Please Type The Item Name you want to REMOVE from Cart: ').capitalize()
                if remove_choice in cart:
                    if cart[remove_choice][0] == item_price_dict[remove_choice]:
                        total_price -= item_price_dict[remove_choice]
                        cart.pop(remove_choice)
                        print('-'*30)
                        print("'{}' item is removed.remaining item in cart is : \n{} ".format(remove_choice,cart))
                        print('Your TOTAL PRICE is : Rs.{}'.format(total_price))
                        print('-'*30)
                    else:
                        cart[remove_choice][0] -= item_price_dict[remove_choice]
                        cart[remove_choice][1]['QUANTITY(KG)'] -= 1
                        total_price -= item_price_dict[remove_choice]
                        print('-'*30)
                        print("'{}' item is removed.remaining item in cart is : \n{} ".format(remove_choice,cart))
                        print('Your TOTAL PRICE is : Rs.{}'.format(total_price))
                        print('-'*30)
                else:
                    print('-'*30)
                    print("""Your choice: "{}" is wrong or not in items list. please choose correctly""".format(remove_choice))
                    print('-'*30)
            if add_remove == '=':
                final_cart=cart
                final_cart['Total Price']=total_price
                print('='*30)
                print('Your Cart Have Below Items')
                print(final_cart)
                print('='*30)
                final_check=input("Do you want to proceed with Billing then TYPE: \"P\" \nOR \nDo you want to ADD or REMOVE items from cart AGAIN then TYPE: \"Y\": ")
                print()
                if final_check =='P':
                    print('='*60)
                    print('You cart have below items please proced with billing method')
                    print(final_cart)
                    print('Thank You for Shopping with us')
                    print('='*60)
                    break
                elif final_check == 'Y':
                    pass


