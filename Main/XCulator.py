import tkinter
from tkinter import *


root =Tk()
root.title("XCulator - Calculator for Windows")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")
photo = PhotoImage(file=r"C:\Users\sarth\Downloads\XCulator\XCulatorAppIcon.png")
root.wm_iconphoto(False, photo)

eqn = ""

def show(value):
    global eqn
    eqn+=value
    label_result.config(text=eqn)

def clear():
    global eqn
    eqn = ""
    label_result.config(text=eqn)

def calc():
    global eqn
    result =""
    if eqn != "":
        try :
            result= eval(eqn)
        except:
            result = "Syntax Error"
            eqn =""
    label_result.config(text=result)
        

label_result = Label(root,width=25, height=2,text="",font=("arial",30),anchor="w")
label_result.pack()

Button(root,text="C",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#973131", command= lambda:clear()).place(x=10,y=100)
Button(root,text="÷",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2c4e80", command= lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2c4e80", command= lambda:show("%")).place(x=290,y=100)
Button(root,text="X",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2c4e80", command= lambda:show("*")).place(x=430,y=100)

Button(root,text="7",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("9")).place(x=290,y=200)
Button(root,text="-",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2c4e80", command= lambda:show("-")).place(x=430,y=200)

Button(root,text="4",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2c4e80", command= lambda:show("+")).place(x=430,y=300)

Button(root,text="1",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("3")).place(x=290,y=400)
Button(root,text="=",width=5, height=3,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#ff8f00",command= lambda:calc()).place(x=430,y=400)

Button(root,text="0",width=5,height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("0")).place(x=10,y=500)
Button(root,text="00",width=5, height=1,font=("arial",30),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show("00")).place(x=150,y=500)
Button(root,text=".",width=5, height=1,font=("arial",30,"bold"),bd=1, fg= "#fff",bg="#2a2d36", command= lambda:show(".")).place(x=290,y=500)

root.mainloop()