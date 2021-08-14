import tkinter
'''
# Place Geometry Manager
# its another geometry manager for the tkinter but it take the absolute position for atleast one window.we need to know
# the screen size before working with it.

# Grid Geometry Manager
# in this we place the widget in the grid. Grid is defined by rows and columns .it can be of any size of rows x columns.
# widgets can be placed in the grid rows/column and it can shown according to that. These grid rows and column will not
# be shown on the UI directly but we need to virtually know and defined in the code.Butwe should make a layout on rough
# before creating the grid code . it makes our code writing more easy
'''

window = tkinter.Tk()
window.title('grid window')
window.geometry('720x520-10-200')
label = tkinter.Label(window, text='Tkinter Grid GUI', relief='sunken', borderwidth=2)
label.grid(row=0, column=0)
'''
grid = configure = config = grid_configure  ## config and configure might not work with rows and column directly ##
bbox = grid_bbox = Misc.grid_bbox   ## be aware of the Misc. ones it might not work directly here and below one ##
columnconfigure = grid_columnconfigure = Misc.grid_columnconfigure  
# grid(row=int, column=int) it defined the widget inside the grid at certain row and column. it draw or print the widget
# graphic inside the grid position.but if same row,column printed with another widget then it will overwritten the. but
# is same widget and same location then it will overlap on it already printed widgets. Also repeated widget with
# different column row will print the last one written not the earlier one.canvas.grid(row=0, column=1)
# canvas.grid(row=0, column=2) canvas.grid(row=0, column=3). so third one will print
'''
left_frame = tkinter.Frame(window)  # Frame(window,relief='sunken', borderwidth=2)
left_frame.grid_configure(row=1, column=1)
canvas = tkinter.Canvas(left_frame, relief='solid', borderwidth=1)
canvas.grid(row=1, column=0)

# Frame == It group the widget according to the position it defined in geometry manager
right_frame = tkinter.Frame(window)
right_frame.grid(row=1, column=2, sticky='n')
'''
# Buttons can be written inside the canvas/widget if written at same level and may overlap according to that widget size
# sticky property: it property of grid which is similar to anchor of pack. it take the compass positions like n,s,e,w
# button1 = tkinter.Button(text="button1")
# button2 = tkinter.Button(text="button2")
# button3 = tkinter.Button(text="button3")
'''
button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.grid(row=1, column=0)  # button1.grid(row=0, column=1) button1.grid(row=0, column=0)
button2.grid(row=2, column=0)  # button2.grid(row=1, column=1)
button3.grid(row=3, column=0)  # button3.grid(row=1, column=0)

# configure the columns & rows
# this is the way by which we can provide the width to the column row. weight property of the method will be defined the
# width. 1 is enough to separate or size the width. But better to not use thw row one because it change the like buttons
# (column_number, weight=int)
# weight option will need if we want our sticky property to run properly inside the widgets line
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=2)

# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.grid_rowconfigure(2, weight=1)

left_frame.config(relief='solid', borderwidth=1)  # this is used to give the left_frame more borderline and its outline
right_frame.config(relief='solid', borderwidth=1)  # right frame also get the shape/outline according to relief defined

left_frame.grid(sticky='ns')  # this will or change the outline according to position similar to anchor or fill
right_frame.grid(sticky='news')  # it work similar to fill or anchor here.fll because of it grid position

right_frame.columnconfigure(0, weight=1)  # width will give the rightframe more width size without it sticky wont affect
button2.config(relief='groove', borderwidth=4)  # flat, groove, raised, ridge  # it will give button two more appearance
button2.grid(sticky='ew')  # it will make or resize it to
# button2.columnconfigure(0, weight=2)

window.mainloop()

########################################################################################################################
import tkinter
import os
window = tkinter.Tk()

window.title("Grid Demo")
window.geometry('640x480-8-200')
window['padx'] = 20
label = tkinter.Label(window,text='Tkinter Grid Demo', font=('Times','10','bold'))
label.grid(row=0, column=0, columnspan=3)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=3)
window.rowconfigure(4, weight=3)
# The purpose of a listbox widget is to display a set of lines of text. Generally they are intended to allow the user to
# select one or more items from a list. All the lines of text use the same font.it allow user to select the options from
# the list of the data inside a canvas type view.
fileList = tkinter.Listbox(window)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken',selectmode=tkinter.EXTENDED)
for zone in os.listdir('C:\\Windows\\System32'): # '/Windows/System32'
    fileList.insert(tkinter.END, zone)
'''
# Scrollbar widget > A number of widgets, such as listboxes and canvases, can act like sliding windows into a larger
# virtual area. You can connect scrollbar widgets to them to give the user a way to slide the view around relative to
# the contents. Here's a screen shot of an entry widget with an associated scrollbar widget:
# here orient can be used to place the scrollbar in screen in x axis or y axis but command makes the real difference
# here because with vertical orientation we need to define the method as yview because it allow the scroll to
# rotate/move the screen in the direction it specify. with vertical if xview defined then when scrolling it  move data
# inside the canvas in the x axis view not in y axis

# this command act as connector b/w the listbox/canvas widget.yview/xview with the scrollbar widget and scrollbar>cv/lb
# below yscrollcommand and xscrollcommand of listbox/canvas widget connect to scrollbar.set method
# The connection goes both ways. The canvas's xscrollcommand option has to be connected to the horizontal scrollbar's 
# set method, and the scrollbar's command option has to be connected to the canvas's .xview method. The vertical 
# scrollbar and canvas must have the same mutual connection. If dont use the .set method one step then it do not alter 
# the behaviour for user but it does not move the scroll bar as needed. it juts move the listbox data but bar wil stick to
#  extreme top/left

# The sticky options on the .grid() method calls for the scrollbars force them to stretch just enough to fit the 
# corresponding dimension of the canvas. 
'''
y_list_Scroll = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=fileList.yview)
y_list_Scroll.grid(row=1, column=1, sticky='nws', rowspan=2)

# x_list_Scroll = tkinter.Scrollbar(window, orient=tkinter.HORIZONTAL, command=fileList.xview)
# x_list_Scroll.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList['yscrollcommand'] = y_list_Scroll.set
# fileList['xscrollcommand'] = x_list_Scroll.set
#
# # frame for the radio buttons
optionFrame = tkinter.LabelFrame(window, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')
#
rbValue = tkinter.IntVar()
rbValue.set(1)
# # Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# for the time Label Frame with LableFrame and Spinbox widget:
# padx in LabelFrame will add the padding to the both side of the frame like left and right
# pady in LabelFrame will add the padding to the both side of the frame like up and down
time_frame = tkinter.LabelFrame(window, text="Time", padx=36, pady=10)
time_frame.grid(row=3, column=0, sticky='new')
# time spinner:
# we can make the spin  box like figure on the screen which can let us show the data which we needed, it minimize the
# use of the scroll widget.We can define the value it can have by value or from_ or to_.
hours = tkinter.Spinbox(time_frame, width=3, value=tuple(range(0, 24)))
hours.grid(row=0, column=0)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
minutes = tkinter.Spinbox(time_frame, width=3, from_=0, to_=59)
minutes.grid(row=0, column=2)
tkinter.Label(time_frame, text=':').grid(row=0, column=3)
seconds = tkinter.Spinbox(time_frame, width=3, from_=0, to_=59)
seconds.grid(row=0, column=4)

# day-month-year
month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]

date_frame = tkinter.Frame(window, width=30, height=5)
date_frame.grid(row=4, column=0, sticky='new')

day = tkinter.Label(date_frame, text='Day')
day.grid(row=0, column=0)
day_spinner = tkinter.Spinbox(date_frame, width=4, from_=1, to_=31)
day_spinner.grid(row=1, column=0)


month = tkinter.Label(date_frame, text='Month')
month.grid(row=0, column=1)
month_spinner = tkinter.Spinbox(date_frame, width=4, value=month_list)
month_spinner.grid(row=1, column=1)


year = tkinter.Label(date_frame, text='Year')
year.grid(row=0, column=2)
year_spinner = tkinter.Spinbox(date_frame, width=8, from_=2000, to_=2099)
year_spinner.grid(row=1, column=2)


# for Result Label frame with Label and Entry widget:
result = tkinter.Label(window, text='Result')
result.grid(row=2, column=2, sticky='nw')
# Entry widget will create the a small canvas which allow user to enter the value
result_box = tkinter.Entry(window)
result_box.grid(row=2, column=2, sticky='sw')
# Result_box = tkinter.Listbox(optionFrame_3, relief='sunken', borderwidth=1, width=40, height=1)
# Result_box.grid(row=0,column=0,sticky='w')


# for OK and Cancel Buttons :

ok_frame = tkinter.Frame(window)
ok_frame.grid(row=4, column=3)
button1 = tkinter.Button(ok_frame, text="OK", command=quit)
button1.grid(row=1, column=0, sticky='n')
# below we added the command by which it quit the window if we click on cancel
cancel_frame = tkinter.Frame(window)
cancel_frame.grid(row=4, column=4)
button2 = tkinter.Button(cancel_frame, text="Cancel", command=window.destroy)
button2.grid(row=1, column=0, sticky='nw')
window.mainloop()



# time frame my logic and was wrong
# box1 = tkinter.Listbox(optionFrame_2, relief='sunken', borderwidth=1,width=5,height=1)
# box2 = tkinter.Listbox(optionFrame_2, relief='sunken', borderwidth=1,width=5,height=1)
# box3 = tkinter.Listbox(optionFrame_2, relief='sunken', borderwidth=1,width=5,height=1)
# box1.grid(row=0, column=1, sticky='nw')
# box2.grid(row=0, column=2, sticky='nw')
# box3.grid(row=0, column=3, sticky='nw')
# box1_scroll_bar_y = tkinter.Scrollbar(optionFrame_2, orient=tkinter.VERTICAL, command=box1.yview)
# box1_scroll_bar_y.grid(row=0, column=1, sticky='e')
# box2_scroll_bar_y = tkinter.Scrollbar(optionFrame_2, orient=tkinter.VERTICAL, command=box2.yview)
# box2_scroll_bar_y.grid(row=0, column=2, sticky='e')
# box3_scroll_bar_y = tkinter.Scrollbar(optionFrame_2, orient=tkinter.VERTICAL, command=box3.yview)
# box3_scroll_bar_y.grid(row=0, column=3, sticky='e')
# box1['yscrollcommand'] = box1_scroll_bar_y.set
# box2['yscrollcommand'] = box2_scroll_bar_y.set
# box3['yscrollcommand'] = box3_scroll_bar_y.set



