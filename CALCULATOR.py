from tkinter import *

def t():
    l1["text"] = float(e.get()) - float(e1.get())
def y():
    l1["text"] = float(e.get()) + float(e1.get())
def b():
    l1["text"] = float(e.get()) * float(e1.get())
def h():
    if int(e1.get())>0:
        l1["text"] = int(e.get()) / int(e1.get())
    else:
        l1["text"] = 'Делить на 0 нельзя'


root=Tk()
e=Entry()
e1=Entry()
e.pack()
e1.pack()
l1=Label(root, text="")
l1.pack()
bt=Button(root,text="-", command=t, width=5,background='red')
bt.pack(side=LEFT)
by=Button(root,text="+", command=y, width=5,background='red')
by.pack(side=LEFT)
bb=Button(root,text="*", command=b, width=5,background='red')
bb.pack(side=LEFT)
bh=Button(root,text="/", command=h, width=5,background='red')
bh.pack(side=LEFT)
root.mainloop()


