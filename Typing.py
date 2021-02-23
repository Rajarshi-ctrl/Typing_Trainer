from tkinter import *
import time
from tkinter.messagebox import showinfo

def start():
    a = var.get()
    time.sleep(2)
    time.sleep(a*60)
    b = txt.count(" ")
    c = (b+1)/a
 #   d = len(txt)
  #  e = d/a
 #   print(f"Your typing speed is : {c} wpm")
  #  print("       And        ")
   # print(f"Your typing speed is : {e} letter per minute")
    showinfo("Typing speed", f"Your typing speed is: {c}wpm")


if __name__ == "__main__":

    root = Tk()
    root.geometry("966x584")
    root.maxsize(966, 584)
    root.minsize(966, 584)
    root.title("| Typing Trainer |")
    root.iconphoto(False, PhotoImage(file='typ.png'))

    var = IntVar()

    Label(text="Welcome to this Typing trainer..", bg="grey", fg="black", padx=8, pady=2, font=("lucida",18,"bold"), relief=GROOVE, borderwidth=3).pack(side=TOP, fill=X)

    txt = Text(root, bg="white",font=(None,13), borderwidth=4)
    txt.pack(fill=X)


    f1 = Frame(root, borderwidth=5)
    Button(f1, fg="black", bg="grey", borderwidth=3, text="START", font=(None,12,"bold"), command=start).pack(side=RIGHT)
    

    Label(f1, text="Select Time : ", font=(None,10,"bold")).pack(side=LEFT)
    
    Radiobutton(f1, text="1 minute", variable=var, value=1).pack(side=LEFT)
    Radiobutton(f1, text="2 minute", variable=var, value=2).pack(side=LEFT)
    Radiobutton(f1, text="5 minute", variable=var, value=5).pack(side=LEFT)
    Radiobutton(f1, text="10 minute", variable=var, value=10).pack(side=LEFT)
    Radiobutton(f1, text="15 minute", variable=var, value=15).pack(side=LEFT)

    f1.pack(fill=X)

    Label(root, text="Thanks for using this Typing trainer.... Have a good day !", bg="grey", fg="black", font=(None,10,"bold"), padx=14, pady=4, relief=RIDGE, borderwidth=5).pack(fill=X)

    root.mainloop()
