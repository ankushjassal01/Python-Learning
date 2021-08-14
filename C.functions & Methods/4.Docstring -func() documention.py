# %% docstring
# documentation
# documenting your function and classes makes it easier for other people to use them
# without it other programmers need to read the func code line by line and understand what its doing & how to call them
# documentation helps us also read it and modify it later after long time.
# it gives us also clear understanding what we want our func intend to do
# we can write our params also and what are there types or exceptions we want it give & what will func return or print
# docstring
"""
this is called as docstring . its written inside the three double quotes.
We can write everything regarding our function inside this block
its depend upon us how long we wrote it and how much data we want want to include and how brief we want it to be
"""


# in other language docstring written before func declared but in python it written inside the func code block
# it become the attribute of function
# in python everything is object so this means func can have attributes
# to check the docstring of function then hover over the func. IDE will show the docstring of function
# or type ctrl+Q or ctrl+click(it will open the builtin.py .. mostly used for built in func)
# docstring is attribute of the function . we can chec it by below .(dot) notation
# we can type print(function_name.__doc__) to get the docstring
# if we are using the terminal only then to check the docstring we can type help(function_name) will print the docstring


def centered_text(text, width=120):  # width=120 is maring width default to 120
    """
    function to make proper width formatted banner of text data
    also it raise error when text is more the the define param width

    :param text: user text
    :param width: screen width we want to add
    :return: it do not return anything. its return type- None function. It print the data
    """
    if text == '*':
        print('*' * width)
    elif len(text) > (width - 4):
        raise ValueError('text:{} is more then defined width {}'.format(text, width))
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text('*')
centered_text('I am out of schedule here in learning')
centered_text(
    'My target for completion is dec 31 per my progress its not looking to meet even after Janurary.SO WHAT CAN I DO')
centered_text(" ")  # now it works like print() . it give blank line for us
centered_text(width=100)  # here we used keyword argument and gave only width and have text value as default
centered_text('per my progress its not looking to meet even after Janurary')
centered_text('*')

# %% Module
# what is Module
# from python documentation
# "A Module is a file containing the python definitions and statements".
# the file name is the module name with the suffix .py appended

