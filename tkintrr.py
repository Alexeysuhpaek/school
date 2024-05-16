from tkinter import *
root = Tk()

with open('припять ночью.jpg', 'rb') as f:
    baobab = f.read()

def erunda():
    btn = Button(root, text='Жмякни на меня!', bg="purple")
    btn.grid(row=0, column=0)
    # print(baobab)
btn1 = Button(root, text='Жмякни на меня!',command=erunda)
# a = PhotoImage(file='припять ночью.jpg')
# l = Label(image=a)
btn1.grid(row=5, column=5)
# l.pack()
root.mainloop()