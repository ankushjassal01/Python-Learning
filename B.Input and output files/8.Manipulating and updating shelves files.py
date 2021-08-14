import shelve
# we need to ensure that there is no extra curly braces or extra comma in the dict values.

# with shelve.open('ShelfTest') as fruit:
# fruit['orange'].append('very tangy') # it wont work if we write the keys as fruit['orange']=['orange', 'citrus fruit']

fruit = shelve.open('ShelfTest')

fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
print(fruit["grape"])
fruit["lime"] = "great with tequila"
# del fruit['13']
# del fruit['14']
# del fruit['pears']
# del fruit['12']
# del fruit['a small, sweet fruit growing in bunches']

# don't use the str direct concatenation with values if they don't have the str datatype. use .format or f method.
for snack in fruit.items():
    print(snack)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    # get method will give the value if its present otherwise default value
    # description=fruit.get(dict_key,"we don't have key"+dict_key)
    # print(description)
    if dict_key in fruit:
        description = fruit[dict_key]
        print(description)
    else:
        print("We don't have a " + dict_key)

# to order the set of keys. Dict/shelves file will give the unordered keys as output
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])  # ordered keys and there values

for v in fruit.values():
    print(v)

print(fruit.values())  # give this value ValuesView(<shelve.DbfilenameShelf object at 0x000000000134DFD0>)

# with the items method of keys
for key, values in fruit.items():
    if len(key) > 6:
        del fruit[key]
    else:
        print(key, ':', values)

print(fruit.items())  # this will give no values instead it will give the value below
#                     # ItemsView(<shelve.DbfilenameShelf object at 0x000000000134DFD0>)


fruit.close()

########################################################################################################################
blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]
# we are creating the file with new keys and there values from the above list variables.
# writeback is
# without writeback we might able to append/remove the values like list objects.Because shelves have no way to know that
# that these list have changed because these list was saved in memory and we have assigned. We appended the values to
# list which are saved in memory.without writeback there will be no trigger for the shelve file to write data in the
# file
# NOTE: Writeback have disadvantage of higher memory usage and with that hight time for processing according to the data
# it going to update. So better perform the temp_list one strategy because its easy and take less memory
# also writeback wont update anything until file closed or used the sync() method

# there is a sync() method which used with writeback. Sync itself caused all entries in  the cache to be written to disk
# but it also clear the cache out as well.sync is called automatically when file close but we also use it
# anywhere/anytime we want to force the data file to be updated. like below when we called sync() it cleared the cache
# and when we appended the item to key it didnt updated because there is no file in cache hence no file data updated

with shelve.open('recipes', writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"]  = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup
    for items in recipes:
        print(items, recipes[items])
    print('=' * 110)
    # we can append the data in the file if the values of keys are written in list like above.
    # we can do the indexing item assignment for list here as list objects are mutable.

# NOTE: we aware of running that file again with same append method because it will add that value again to the file.
# we might not able to append the file if we written the list directly to the dict like below:
# fruit['orange'] = ['orange', 'citrus fruit']
# fruit['orange'].append('very tangy') this wont work like this. we have to assign the list object to dict key .
# if list need to be append or change.

# one way of doing appending without writeback is assigning key value to temp list and then append and then reassign the
# temp to key in file. Like below
    temp_list  = recipes['pasta']
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    temp_list = recipes['blt']
    temp_list.append("butter")
    recipes["blt"] = temp_list

    recipes["blt"].append("butter")
    recipes["pasta"].remove("tomato")
    recipes["pasta"].append("tomato")
    for items in recipes:
        print(items, recipes[items])
    print('=' * 110)
    recipes['soup'] = soup
    recipes.sync()  # here the retrieved disk detail was removed from cache and below didnt updated the object
    #               # so better to not use sync method as it can cause issue.
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
print(blt, pasta)  # appending items to file data list wont update the original list detail like here.
########################################################################################################################
books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]['soup'])
# print(books["recipes"]["scrambled eggs"])
#
# print(books["maintenance"]["loose"])
books.close()


books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]},  # due to comma we made the tuple not dict so the recipes key have
#                                                   # the tuple values so direct calling of dict keys inside dict wont
#                                                   # work like this print(books["recipes"]['soup']) because we havnt
#                                                   # specified the index position before calling the inside values of
#                                                   # tuple.
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"][0][1])  # this is wright way to call the dict soup inside tuple
# print(books["recipes"][0][1])  # this wont work because we are have dict inside index 0 position error :KeyError: 1
# print(books["recipes"]["scrambled eggs"])
#
# print(books["maintenance"]["loose"])
books.close()
