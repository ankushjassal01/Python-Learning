"""
python standard library includes wide variety of modules and their methods. it comes up with python by default.
it also include the builtin functions/modules/methods/anything in language which we can use without explicitly any
import.it include many module like random,shelve, pickle, turtle
We can check the objects of module by dir() or by opening their .py file
"""
import random
# help function give is the all the info of the required parameter/module/function
# to get the info of the method of module then do not write the () of that method.it will give error and ask for param.
# use it like below not like help(random.randint()) or help(random.randint(1)).
# help(random.randint(1,1)) it works but give help for different thing not the required one.
# it also show all the data of that module/method and any documentation link to which we can check in web.
help(list.append)
help(random.randint)
# import pickle
# for obj in dir(random.LOG4):
#     print(obj, type(obj))
# print(random.LOG4.hex())
