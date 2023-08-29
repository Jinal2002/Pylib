from tkinter import  *

w1 = Tk()
w1.title("RadioButton")
w1.geometry("550x600")

def click():
    x = var.get()
    y = int(txta.get())
    z = int(txtb.get())

    if x==1:
        ans.set(y+z)

    if x==2:
        ans.set(y-z)

    if x==3:
        ans.set(y*z)

var = IntVar()
ans = StringVar(w1)

lba = Label(w1, text="a")
lba.grid(row=0, column=0)

lbb = Label(w1, text="b")
lbb.grid(row=1, column=0)

txta = Entry(w1)
txta.grid(row=0, column=1)


txtb = Entry(w1)
txtb.grid(row=1, column=1)

lbloption = Label(w1)
lbloption.grid(row=2 , column=0)

rdbn1 = Radiobutton(w1, text="+", variable=var, value=1)
rdbn1.grid(row=2, column=1)
rdbn2 = Radiobutton(w1, text="-", variable=var, value=2)
rdbn2.grid(row=2, column=2)
rdbn3 = Radiobutton(w1, text="*", variable=var, value=3)
rdbn3.grid(row=2, column=3)

btnsubmit = Button(w1, text="Submit",command=click)
btnsubmit.grid(row=3, column=0)

lblans = Label(w1, text="Ans")
lblans.grid(row=4, column=0)

txtans = Entry(w1, textvariable=ans)
txtans.grid(row=4, column=1)

w1.mainloop()