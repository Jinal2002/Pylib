from tkinter import * 

w1 = Tk()
w1.title("CheckBox")
w1.geometry("400x500")

def clicked():
    str= ""

    if checkvar1.get()==1:
        str = "C "
    if checkvar2.get()==1:
        str += "C++ "
    if checkvar3.get()==1:
        str += "Python "
    if checkvar4.get()==1:
        str += "Java "
        
    strAns.set(str)
    
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()

strAns = StringVar(w1)

chkbtn1 = Checkbutton(w1, text="C", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)
chkbtn1.grid(row=0, column=0)
chkbtn2 = Checkbutton(w1, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)
chkbtn2.grid(row=0, column=1)
chkbtn3 = Checkbutton(w1, text="Python", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)
chkbtn3.grid(row=0, column=2)
chkbtn4 = Checkbutton(w1, text="Java", variable=checkvar4, onvalue=1, offvalue=0, height=2, width=10)
chkbtn4.grid(row=0, column=3)

btnsubmit = Button(w1, text="Submit", command=clicked)
btnsubmit.grid(row=1, column=0)

lblans = Label(w1, text="Ans")
lblans.grid(row=2 , column=0)

txtans = Entry(w1, textvariable=strAns)
txtans.grid(row=2 , column=1)

w1.mainloop()
