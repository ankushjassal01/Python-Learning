""" modules
# modules are the method/functions which are written in a separate .py file and its all objects can be used in separate
# file/programs which we intend to write. Module are predefined or manually defined by us to import/retrieve and use.
# when they are written they are intend to make impact at that time without using them initially like sorted() its not
# of much use until used with objects.
# ######################################################################################################################
# IMPORT/FROM MODULE IMPORT
# we can also do import like below if we want to use or utilise only few methods or objects from the module.
# this way we dont need to prefix the methods with the module name like turtle.forward
# this way we can import things which we actually need
# NOTE: only drawback is that we cannot use the other method of module which are not defined in import like circle() or
# turtle.circle .Also With this way we cannot assign the prefix of module in script/code
# but we can do this import * /import* this way we can  utilise any method of module.
# import * can cause when we try to print some variable which also name as method of that module  like below
# done = "Well done, you have finished your drawing"
# forward(150)
# right(250)
# done()
# print(done)  # it give error because if done() to avoid this we can do below
# done = "Well done, you have finished your drawing"
# print(done)
# NOTE: WE CAN DO IMPORT MODULE ALSO WITH FROM MODULE IMPORT.IT ALLOWS THE METHODS RUN WHICH ARE NOT DEFINED IN FROM ONE
# from module import module_1,module_2
# import turtle
# or
# import turtle
# from module import module_1,module_2 ... Any ways is possible
# not like this from module import *,module_1 or from module import module_1,*
# or from module import module_1 * this will give error """

from turtle import forward, right  #
"""import
# Import is a way to retrieve the file/separate .py file or any module which we have written or pre defined within the
# python. Its easy to use but NOTE: CAN SHOULD TRY TO INITIALISE THEM AT BEGINNING. IT SHOULD WRITTEN AT TOP OF THE FILE
# BUT CAN BE WRITTEN BELOW TOO.ALWAYS WRITTEN AT TOP NOT NECESSARY.
# done = "Well done, you have finished your drawing"
# for i in done:
#     print(done.split())
# import turtle
# turtle.forward(150)"""

import turtle
# import time  # to control the screen/display timing
forward(100)
right(270)
forward(200)
turtle.circle(50)
right(207)
forward(223.6)
# done()    # instead of time.sleep we can use this method. it make screen pop remain until we close the popup screen
turtle.circle(57)  # both one will not run if done() or turtle.done() was written earlier it.to run that either we need
turtle.done()      # to remove done() or include this in above one. else it will give error for .circle one method
# time.sleep(2)  # let the screen freeze/stay/visible for second defined in it.
########################################################################################################################