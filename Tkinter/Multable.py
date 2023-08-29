from tkinter import *

def Multab():

    x = int(txtno.get())
    strAns = ""

    for i in range (1,11):
        strAns +=  str(x) + "x" + str(i) + '=' + str(x*i) + "\n"
    txtans.insert(INSERT , strAns)

w1 =Tk()
w1.title("Table MULTIPLICATION FORM")
w1.geometry("350x600")

# ans = StringVar(w1)

lblno = Label(w1, text="num")
lblno.grid(row=0 , column=0)
txtno = Entry(w1)
txtno.grid(row=0 , column=1)

BtnSubmit = Button(w1 , text="SUBMIT" , command=Multab)
BtnSubmit.grid(row=1 , column=0)

lblans = Label(w1, text="Ans")
lblans.grid(row=2 , column=0)

txtans = Text(w1,  height=12, width=20)
txtans.grid(row=2 , column=1)

w1.mainloop()