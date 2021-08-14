import tkinter

cal_window_padding = 5
cal_window = tkinter.Tk()
cal_window.title('Calculator')
cal_window.geometry('240x240')
cal_window['padx'] = cal_window_padding

# created frame for whole cal window and added another button row respective frames inside it
one_frame = tkinter.Frame(cal_window)
one_frame.grid(row=0, column=0, sticky='news')

# Entry widget for calculator entries and visible to user
input_window = tkinter.Entry(one_frame, relief='groove', borderwidth=2, width=35)  # width=30
input_window.grid(row=0, column=0, columnspan=5)
input_window.rowconfigure(0, weight=2)
input_window.grid(sticky='news')

# frame for first row of buttons C and CE
row_1_frame = tkinter.Frame(one_frame)
row_1_frame.grid(row=1, column=0, columnspan=2, sticky='nw')
button_C = tkinter.Button(row_1_frame, text='C', width=5, height=1)
button_C.grid(row=0, column=0, sticky='ew')
button_CE = tkinter.Button(row_1_frame, text='CE', width=5, height=1)
button_CE.grid(row=0, column=1)

# frame for second row of buttons 7,8,9,+
row_2_frame = tkinter.Frame(one_frame)
row_2_frame.grid(row=2, column=0, columnspan=4, sticky='nw')
button_7 = tkinter.Button(row_2_frame, text='7', width=5, height=1)
button_7.grid(row=0, column=0, columnspan=1, sticky='ew')
button_8 = tkinter.Button(row_2_frame, text='8', width=5, height=1)
button_8.grid(row=0, column=1, columnspan=1, sticky='ew')
button_9 = tkinter.Button(row_2_frame, text='9', width=5, height=1)
button_9.grid(row=0, column=2, columnspan=1, sticky='ew')
button_add = tkinter.Button(row_2_frame, text='+', width=5, height=1)
button_add.grid(row=0, column=3, columnspan=1, sticky='ew')

# frame for third row of buttons 4,5,6,-
row_3_frame = tkinter.Frame(one_frame)
row_3_frame.grid(row=3, column=0, columnspan=4, sticky='nw')
button_4 = tkinter.Button(row_3_frame, text='4', width=5, height=1)
button_4.grid(row=0, column=0, columnspan=1, sticky='ew')
button_5 = tkinter.Button(row_3_frame, text='5', width=5, height=1)
button_5.grid(row=0, column=1, columnspan=1, sticky='ew')
button_6 = tkinter.Button(row_3_frame, text='6', width=5, height=1)
button_6.grid(row=0, column=2, columnspan=1, sticky='ew')
button_minus = tkinter.Button(row_3_frame, text='-', width=5, height=1)
button_minus.grid(row=0, column=3, columnspan=1, sticky='ew')

# frame for fourth row of buttons 1,2,3,*
row_4_frame = tkinter.Frame(one_frame)
row_4_frame.grid(row=4, column=0, columnspan=4, sticky='nw')
button_1 = tkinter.Button(row_4_frame, text='1', width=5, height=1)
button_1.grid(row=0, column=0, columnspan=1, sticky='ew')
button_2 = tkinter.Button(row_4_frame, text='2', width=5, height=1)
button_2.grid(row=0, column=1, columnspan=1, sticky='ew')
button_3 = tkinter.Button(row_4_frame, text='3', width=5, height=1)
button_3.grid(row=0, column=2, columnspan=1, sticky='ew')
button_multiply = tkinter.Button(row_4_frame, text='*', width=5, height=1)
button_multiply.grid(row=0, column=3, columnspan=1, sticky='ew')

# frame for the fifth rows of button which are 0,=,/
row_5_frame = tkinter.Frame(one_frame)
row_5_frame.grid(row=5, column=0, columnspan=4, sticky='nw')
button_0 = tkinter.Button(row_5_frame, text='0', width=5, height=1)
button_0.grid(row=0, column=0, sticky='ew')
tkinter.Button(row_5_frame, text=' ', width=5, height=1).grid(row=0, column=1, columnspan=1, sticky='ew')
tkinter.Button(row_5_frame, text=' ', width=5, height=1).grid(row=0, column=2, columnspan=1, sticky='ew')
button_equal = tkinter.Button(row_5_frame, text='=', width=5, height=1)
button_equal.grid(row=0, column=1, columnspan=2, sticky='ew')
button_divide = tkinter.Button(row_5_frame, text='/', width=5, height=1)
button_divide.grid(row=0, column=3, sticky='ew')

# below window.update will let the below mixsize and maxsize to be fixed and let them show its effect on the window
# not not used then nothing will show as window will be resize to the lowest pixel/size
cal_window.update()
cal_window.minsize(one_frame.winfo_width() + cal_window_padding, input_window.winfo_height() + one_frame.winfo_height())
cal_window.maxsize(one_frame.winfo_width() + cal_window_padding, input_window.winfo_height() + one_frame.winfo_height())
cal_window.mainloop()
