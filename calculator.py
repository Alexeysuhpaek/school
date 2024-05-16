
from tkinter import *
root = Tk()
entry_field = Entry(root, width=50, borderwidth=6)
entry_field.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

def click_hadler(event=None):
    assert type (event) == int
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(event))







button_1 = Button(root, text='1' , padx=50, pady=20, command=lambda: click_hadler(1))
button_2 = Button(root, text='2' , padx=50, pady=20, command=lambda: click_hadler(2))
button_3 = Button(root, text='3' , padx=50, pady=20, command=lambda: click_hadler(3))
button_4 = Button(root, text='4' , padx=50, pady=20, command=lambda: click_hadler(4))
button_5 = Button(root, text='5' , padx=50, pady=20, command=lambda: click_hadler(5))
button_6 = Button(root, text='6' , padx=50, pady=20, command=lambda: click_hadler(6))
button_7 = Button(root, text='7' , padx=50, pady=20, command=lambda: click_hadler(7))
button_8 = Button(root, text='8' , padx=50, pady=20, command=lambda: click_hadler(8))
button_9 = Button(root, text='9' , padx=50, pady=20, command=lambda: click_hadler(9))
button_0 = Button(root, text='0' , padx=50, pady=20, command=lambda: click_hadler(0))

def clear_event():
    entry_field.delete(0, END)


tmp = None
def sum_event ():
    global tmp
    if not tmp:
        tmp = entry_field.get()
        entry_field.delete(0, END)
    else:
        current = entry_field.get()
        entry_field.delete(0, END)
        entry_field.insert(0, int(current) + int(tmp))
        tmp = None

button_add = Button(root, text='+', padx=49, pady=20, command=sum_event)
button_clear = Button(root, text='Clear', padx=50, pady=20, command= clear_event)
button_equal = Button(root, text='=', padx=50, pady=20)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2,  column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2, sticky='we')
button_equal.grid(row=5, column=1, columnspan=2, sticky='we')
button_add.grid(row=5, column=0,)




root.mainloop()