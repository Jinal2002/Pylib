from tkinter import  *

w1 = Tk()
w1.title("RadioButton")
w1.geometry("400x500")

def click():
    y = var.get()
    
    if y==1:
        ans.set("C")

    if y==2:
        ans.set("C++")

    if y==3:
        ans.set("Python")

var = IntVar()
ans = StringVar(w1)

lbloption = Label(w1,text='num')
lbloption.grid(row=0 , column=0)

rdbn1 = Radiobutton(w1, text="C", variable=var, value=1)
rdbn1.grid(row=0, column=1)
rdbn2 = Radiobutton(w1, text="C++", variable=var, value=2)
rdbn2.grid(row=0, column=2)
rdbn3 = Radiobutton(w1, text="Python", variable=var, value=3)
rdbn3.grid(row=0, column=3)

btnsubmit = Button(w1, text="Submit",command=click)
btnsubmit.grid(row=2, column=0)

lblans = Label(w1, text="Ans")
lblans.grid(row=3, column=0)

txtans = Entry(w1, textvariable=ans)
txtans.grid(row=3, column=1)

w1.mainloop()