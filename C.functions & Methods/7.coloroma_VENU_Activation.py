# coloroma is open source package for python on any OS to help converting the ASCII keywords into required
# code Like RED ='\u001b[31m' . so without coloroma in terminal/cmd it will not give the expected effect.instead
# it will print the text surrounded by ASCII letters
# if you didnt installed the python to path variables of OS , you might not able to use it in CMD(i also dont have)
# to optimize that we need to install the package coloroma by pip install in terminal OR going to IDE structure of
# python SDK packages. (UP sign indicate the newer versions)
# here i did install using pip install "path name of file ""C:/users/iphone/colorama_lpa-0.4.4b1.0-py2.py3-none-any.whl
# to use it we need to import it in our program like import coloroma and use its methods in it to start the effect
# NOTE: MAKE SURE YOU USE EITHER UPDATED VERSION OR VERSION SAME AS IT WILL USE ON SERVERS WHERE PYTHON RUN
# IF NOT THEN CODE WILL BREAK AS IT WILL HINDER THE FUNCTIONALITY OF CODE
# ALSO USE VIRTUAL ENVIRONMENT TO RUN THE PRORGRAM
# function color coding

import colorama
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str ) -> None:
    """
    this will print the text in different color coding
    :param effect: color ASCII codes which are constants
    :param text: Text to be print
    :return: None type function as we are printing
    """

    string = '{}{}{}'.format(effect, text, RESET)
    print(string)


colorama.init()
colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()


# %% VIRTUAL ENVIRONMENT
# VIRTUAL ENV help us to separate the code from main python code. like if we update the package in virtual and
# if it have bugs or functionality not working according to the code then our code wil fail but it wont affect the
# main python specially in linux where script for OS might be written in python . so if main python path hinder then
# in linux it will lock you out of your OS. so in this case VENU is optimized to use as it will copy all the package
# from main python path and also can update or install new but it will not affect the main python path
# in your IDE you will see below paths . one is where python running and other where is your project files created
# C:\Users\iphone\anaconda3.1\python.exe     "E:\spyder learning\C.functions & Methods\more test.py"
# in window;
#C:\Users\iphone\venv\Scripts\activate
# in linux
#source /home/iphone/venu/bin/activate

# for deactivation type deactivate in the path
# C:\Users\iphone\venv\Scripts\deactivate

# it will make the cmd have venv and we will able to run the python file


# testing
# Testing is the process of finding the bug in the code

# debugging
# Is the process of working out what the bugs are and fixing them

# testing and debugging go together
# first we test the code and see if its working for all edge and corner cases and if not then
# we do debugging of code and check why its failing


# Pseudocode
# Pseudocode is the code that you write in Simplified language- usually a simple version of your native language
