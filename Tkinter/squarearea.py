from tkinter import *


def NatureNum():

    x = int(txtnum.get())

    ans.set(x*x)



z = Tk()
z.title('Area of SQUARE')
z.geometry('550x600')

ans = StringVar(z)
lbnum = Label(z, text="num")
lbnum.grid(row=0, column=0)
txtnum = Entry(z)
txtnum.grid(row=0, column=1)

btnsub = Button(z, text="SUBMIT", command=NatureNum)
btnsub.grid(row=1, column=0)

lbans = Label(z, text="NumNAture")
lbans.grid(row=2, column=0)
txtans = Entry(z,textvariable=ans, width=40)
txtans.grid(row=2, column=1)



z.mainloop()

