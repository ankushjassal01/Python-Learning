item_price_dict={
    'Apple':50,
    'Orange':20,
    'Grapes':20,
    'Guava':20,
    'Bananas':15
}
customer_cart=[]
final_cart=[]
total_price=0
print('choose item from the below list for your cart')
for index, (item,price) in enumerate(item_price_dict.items()):
    print('{0}. {1:<9}:price:{2:^}'. format(index+1,item, price))

user_choice=int(input())
# for first add of the items in shopping cart
if 1<=user_choice<=len(item_price_dict):
    item_list=list(item_price_dict.items()) # make the list of dict values so that its easy to use that to append in customer list
    customer_cart.append(item_list[user_choice - 1])
    for items , price in customer_cart:
        total_price += price
    print('Your Cart have item,price as {}'.format(customer_cart))
    print('Your total price is : Rs.{}'. format(total_price))
    print(customer_cart)
    print()
# condtion for further add and remove from the customer cart
while True:
    customer_cart = dict(customer_cart)
    remove_Add=input("Enter '+' to ADD | '-' to REMOVE | '=' to PROCEED TO PLACE ORDER: ")
    print()
    if remove_Add =='+': # for addition in cart
        print('choose item from the below list for your cart')
        for index, (item,price) in enumerate(item_price_dict.items()):
            # print the items again to user.code reuse.need to identify the best way to do it
            print('{0}. {1:<9}:price:{2:^}'. format(index+1,item, price))
        user_add_choice=int(input())  # to add items in the customer cart
        # condition to check the user input in range of items in store
        if 1<=user_add_choice<=len(item_price_dict):
            #used item list to check data in the customer list because user adding according to item list
            if item_list[user_add_choice - 1][0] in customer_cart.keys():
                customer_cart=list(customer_cart.items())
                # get the index value of the item in customer cart
                cart_index=customer_cart.index(item_list[user_add_choice - 1])
                # removed that item first and saved that in temp variable
                temp_remove=customer_cart.pop(cart_index)
                temp_remove=list(temp_remove) # make that temp a list as tuple cant be changed
                total_price += temp_remove[1]
                temp_remove[1] += temp_remove[1] # added price as user adding same item again
                temp_remove=tuple(temp_remove) # data type change
                # added the temp variable data back in cart at its index by insert method
                customer_cart.insert(cart_index, temp_remove)
                print('Your Cart have item,price as {}'.format(customer_cart))
                print('Your total price is : Rs.{}'. format(total_price))
                print()
            else:
                customer_cart.append(item_list[user_add_choice - 1]) # if not exist then direct add
                total_price += item_list[user_add_choice - 1][1]
                print('Your Cart have item,price as {}'.format(customer_cart))
                print('Your total price is : Rs.{}'. format(total_price))
                print()

    if remove_Add == '-':
        print(customer_cart)
        remove_item=input('Choose item you want to remove: ')
        for index, cart_item in enumerate(customer_cart):
            if remove_item.capitalize() in cart_item:
                if cart_item in item_list:
                    total_price -= cart_item[1]
                    customer_cart.remove(cart_item)
                    print('remaining item in cart is : {} '.format(customer_cart))
                    print('Your total price is : Rs.{}'. format(total_price))
                else:
                    temp_remove_1=customer_cart[index]
                    customer_cart.remove(customer_cart[index])
                    temp_remove_1=  list(temp_remove_1)
                    delete_val=item_price_dict.get(temp_remove_1[0])
                    total_price -= delete_val
                    temp_remove_1[1] -= delete_val
                    temp_remove_1 =tuple(temp_remove_1)
                    customer_cart.insert(index, temp_remove_1)
                    total_price -= temp_remove_1[1]
                    print('remaining item in cart is : {} '.format(customer_cart))
                    print('Your total price is : Rs.{}'. format(total_price))
    if remove_Add == '=':
        final_cart = customer_cart
        final_cart.append(('Total Price',total_price))
        final_cart=dict(final_cart)
        print(final_cart)
        break











    # else:
    #     print('Your choice dont have any item listed in shooping list.')
    #     print('to choose again please select item again from below list')