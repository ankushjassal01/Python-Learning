import tkinter

'''
IT allow us to create GUI program.its created in tcl which is scripting language. it sent the tcl code to tcl
interpreter which is Embedded in python.
Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.
Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under Tk.

Widgets are positioned with one of the geometry managers Place, Pack
or Grid. These managers can be called with methods place, pack, grid
available in every Widget.

Actions are bound to events by resources (e.g. keyword argument
command) or with the method bind.

Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

Its documentation is not well maintained.
its some methods. not all included, some may be classes ( which are written with pascal cases (Abc))
ACTIVE ; ALL ; ANCHOR ; ARC ; BASELINE ; BEVEL ; BOTH ; BOTTOM ; BROWSE ; BUTT ; BaseWidget ; BitmapImage ; BooleanVar ;
 Button ; CASCADE ; CENTER ; CHAR ; CHECKBUTTON ; CHORD ; COMMAND ; CURRENT ; CallWrapper ; Canvas ; Checkbutton ; 
 DISABLED ; DOTBOX ; DoubleVar ; E ; END ; EW ; EXCEPTION ; EXTENDED ; Entry ; Event ; FALSE ; FIRST ; FLAT ; Frame ; 
 GROOVE ; Grid ; HIDDEN ; HORIZONTAL ; INSERT ; INSIDE ; Image ; IntVar ; LAST ; LEFT ; Label ; LabelFrame ; Listbox ; 
 MITER ; MOVETO ; MULTIPLE ; Menu ; Menubutton ; Message ; Misc ; N ; NE ; NO ; NONE ; NORMAL ; NS ; NSEW ; NUMERIC ; 
 NW ; NoDefaultRoot ; OFF ; ON ; OUTSIDE ; OptionMenu ; PAGES ; PIESLICE ; PROJECTING ; Pack ; PanedWindow ; PhotoImage 
 ; Place ; RADIOBUTTON ; RAISED ; READABLE ; RIDGE ; RIGHT ; ROUND ; Radiobutton ; S ; SCROLL ; SE ; SEL ; SEL_FIRST ; 
 SEL_LAST ; SEPARATOR ; SINGLE ; SOLID ; SUNKEN ; SW ; Scale ; Scrollbar ; Spinbox ; StringVar ; TOP ; TRUE ; Tcl ; 
 TclError ; TclVersion ; Text ; Tk ; TkVersion ; Toplevel ; UNDERLINE ; UNITS ; VERTICAL ; Variable ; W ; WORD ; 
 WRITABLE ; Widget ; Wm ; X ; XView ; Y ; YES ; YView ; constants ; getboolean ; getdouble ; getint ; image_names ; 
 image_types ; mainloop ; re ; sys ; wantobjects ; 


python 2 dont have same import as python 3 it have import as Tkinter rather then tkinter
So to counter this we can use this :
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
tkinter._test()

# mainWindow = tkinter.Tk()
# 
# mainWindow.title("Hello World")
# mainWindow.geometry('640x480+8+400')
# mainWindow.mainloop()

'''
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()  # its just a test window to check if its working
mainWindow = tkinter.Tk()  # this is root window. everything must be placed within or one of child window.

mainWindow.title('title')  # its module to print the title name of the UI
mainWindow.geometry(
    '640x480+200-200')  # size of the pop UI. It can either take 2 args or 4 like 640x480 or 640x480-8+400
#                                     # rest two define the pixel. 'x' between resolution is normal string x. so dont
#                                     # use *;; + & - in between the last two args. +8+400 means  8 pixel left and 400
#                                     # down to the screen but at same height. and -8-400 8 pixel right and 400 pixel up
#                                     # more the size it will go away from left or right according to pixel size

# tkinter.label(master_window,text='the value we want to print')  it print the value where we want our geometry manager
# to print on window .it take some about of space from the window and at there nothing can be printed.below with pack
# geometry we are printing the text on window sides like left or right bottom top
# Label is also a class and it contain many func , run below:
# for i in dir(tkinter.Label()):
#     if i[0] !='_':
#         print(i, end=' ; ')
# label = tkinter.Label(mainWindow, text="Hello World").pack(side='top') it can be written like this too.
label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# Canvas is a wdget . It used to display the graphics and it is represent as class in tkinter . it have many methods
# but below we are using it without it. here we used the relief and border_width resource of it and it values .Relief
# can have these values but not empty :flat, groove, raised, ridge, solid, or sunken
# if we used the fill keyword in pack then for it value as tkinter.Y it will work for left and right and tkinter.X will
# work with top and bottom and fill the canvas window to the window size in x axis and y axis.IF want fill to work on
# each sides and it axis then we need to use the to Expand param and set it value to True. But if the the sides worked
# with respective axis used with expand then it will give output as opposite side like side =left and axis is Y and
# expand is true then output will be of Top/bottom Y axis with expand similar with other respective sides
# canvas.pack(side='top', fill=tkinter.X, expand=True) or canvas.pack(side='bottom', fill=tkinter.X, expand=True)
# canvas.pack(side='left', fill=tkinter.Y, expand=True) or canvas.pack(side='right', fill=tkinter.Y, expand=True)
# but with fill as BOTH it work similar like X and Y respective side but if we used the expand but if we used it then it
# will fill the widget to whole window no matter which side used canvas.pack(side='left',fill=tkinter.BOTH,expand=True)
canvas = tkinter.Canvas(relief='raised', borderwidth=10)
canvas.pack(side='left', anchor='n')
#############################################################
# button are already bordered object in the tkinter. it can be used in pack geometry with the
# respective_button_object.pack(side='')
# Frame() > Frame it used to divide the window objects in different location like here we used left frame for widgets
# and left frame for button . Here we need to notice one thing  with button we used anchor in the left frame so when it
# used then pack() anchor position will not work it will be override by the left frame anchor
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='s', expand=True)
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# anchor keyword inside pack will place the button/widget object on the window according to its value. like  n,s,w,e
# represent as north south west east. If anchor not used then button/widget will be placed according to its side defined
#  in pack() .anchor side will changed the behaviour of button/widget position according to side and to the extreme
# positions like ;left then extreme left but if canvas is left then it wont do that . if top/bottom then only horizontal
#  positions of anchor will displace the button/widget position, if left/right then only vertical ones
button1.pack(side='top', anchor='s')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='w')

# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)

mainWindow.mainloop()  # give the control of the above written UI code to Tcl/tk back. It handle the all the event GUI
#                      # need in order to function.
########################################################################################################################
# Geometry manager
# Everything in tkinter is Window and objects are placed in  hierarchy.
# Geometry Manager have three type: Pack manager , Grid Manager
# everything must be placed within root or in one of child window.Not every window have childern but every window
# except root must have master window
# widgets : canvas,
