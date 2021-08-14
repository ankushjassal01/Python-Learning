# %% Handling Invalid Arguments

# As we seen that function usually dont give as exception so to add exception when code is not properly per
# data type or length then we can use "raise" with ValueError
def centered_text(text):
    width = 100
    if text == '*':
        print('*' * width)
    elif len(text) > (width - 4):
        # these exception raise can help us understand our code more easily and
        # we can check where our parameters are violated the data definition
        raise ValueError('text:{} is more then defined width {}'.format(text, width))
        # # width += (len(text)-width)
        # # print('**{}**'.format(text.center(width-4)))  # dynamic width condition
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text('*')
centered_text('I am out of schedule here in learning')
centered_text('My target for completion is dec 31 per my progress its not looking to meet even after Janurar. SO WHAT CAN I DO')
centered_text('per my progress its not looking to meet even after Janurary')
centered_text('*')


# %% with two argumets
# with two argumets
# below given two params which are not default
def centered_text(text, width):
    # width=text_width
    if text == '*':
        print('*' * width)
    elif len(text) > (width-4):
        raise ValueError('text:{} is more then defined width {}'.format(text,width))
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text('*',120)
centered_text('I am out of schedule here in learning', 120)
centered_text('My target for completion is dec 31 per my progress its not looking to meet even after Janurar. SO WHAT CAN I DO',120)
centered_text('per my progress its not looking to meet even after Janurary', 120)
centered_text('*',120)


# %% With Default Value

# Default VALUE IS very helpful in multiple parameters functions.
# like below . we dont have to pass the width parameter when calling the functions.this makes function calling easy.
# We do gave width if required. But if not given then default will be given to output of function
# syntax is simple.. def func(parameter_name=default value):
# do not add space b/w the paramters and value (p=1)
def centered_text(text, width=120):  # width=120 is marking width default to 120
    if text == '*':
        print('*' * width)
    elif len(text) > (width-4):
        raise ValueError('text:{} is more then defined width {}'.format(text,width))
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text(width=121,text='*')
centered_text('I am out of schedule here in learning')
centered_text('My target for completion is dec 31 per my progress its not looking to meet even after Janurar. SO WHAT CAN I DO')
centered_text(' ') # if i want to print the space the i need to specify the space text in params for this function
centered_text('per my progress its not looking to meet even after Janurary')
centered_text('*')


# %% WITH KEYWORD ARGUMENTS
# DEFAULT PARAMETERS TYPE IN PYTHON:
# functions used positional and keyword arguments parameters types  :
# Positional comes when they given in order and not default one should be given.if not given then error
# keyword came in picture when params are default if used alone in multiple param and
# only want to give the particular arguments.it given by there name
# if Keyword argument used and other param is not default then we get this kind of error:
# "" TypeError: centered_text() missing 1 required positional argument: 'text' ""
# Keyword can be used for non default too check line 61 code centered_text(width=121,text='*')
# centered_text(' ') # if i want to print the space the i need to specify the space text in params for this function
# to minimize that we can give default value to our text param too. like text=" "
# LIKE NOW WE MARKED TEXT TO DEFAULT BUT WE ONLY WANA GIVE THE WIDTH PARAM THEN WE CAN USE ""KEYWORD ARGUMENTS""
# LIKE centered_text(width=60) # giving a keyword argument only # it given by its name not by its position
# VAR-POSITIONAL and positional only & keyword only and var-keyword only
# var are parameters which start from * or **.. it must comes after positional or keywords arguments if those used
# positional only are the params which used in high level of coding in C func
# keyword only 
# variable defined after var-positional params must be keyword only  it includes var-keywords args
# sequence is :
# positional Or keyword arguments --VAR-POSITIONAL -- keyword only -- var-keyword only


def centered_text(text=" ", width=120):  # width=120 is marking width default to 120
    if text == '*':
        print('*' * width)
    elif len(text) > (width-4):
        raise ValueError('text:{} is more then defined width {}'.format(text,width))
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text('*')
centered_text('I am out of schedule here in learning')
centered_text('My target for completion is dec 31 per my progress its not looking to meet even after Janurar. SO WHAT CAN I DO')
centered_text() # now it works like print() . it give blank line for us
centered_text(width=100) # here we used keyword argument and gave only width and have text value as default
centered_text('per my progress its not looking to meet even after Janurary')
centered_text('*')