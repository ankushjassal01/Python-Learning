"""
OOPs: Object Oriented Programming: Its best way to program , its consists of classes and objects. Its best way to group
the objects and put them in one class. It let the object differ from other objects.
Class: it is like a template( for created this object is like a plan for do that) from where objects can be created .
All the objects created from same class will share the same characteristics.By this we can create many instances/objects
from that class template(code/definition) and use them.
objects created from the class is called Instances. It inherit the all the characteristics from the class

These class not do much other then creating the instances. Once the instance is created we can call its variables,
functions etc and use it anywhere by .dot notation.
"""


class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


milton = Kettle('Milton', '600')
# we created the instance of class Kettle name as milton and it have its price and name. We are accessing them by the
# .notation like instance_name.its_characteristics_name
# below print will show the object address and object association/type
print(milton, type(milton))  # <__main__.Kettle object at 0x00000057A4D94FD0> <class '__main__.Kettle'>
print(milton.price)
print(milton.make)
milton.price = 699
print(milton.price, milton.make)
dummy = milton.price
print(dummy)
d = 600
milton.price = d
print(milton.price, milton.make)
Cello = Kettle("Cello", "500")
print(Cello.price, Cello.make)