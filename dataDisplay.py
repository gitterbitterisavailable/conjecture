import tkinter as tk
import conjecture
from tkinter.constants import E, NW, S

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("VR-1")
        
    

    def create_widgets(self):
        #hi widget
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Collatz Conjecture\nVisual Representation\n(confirm input not really)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(sticky=E,ipadx=10,ipady=5)

        #quit widget
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy,bd=10)
        self.quit.grid(sticky=NW)

#___________________________
 #input widget

        self.userinput = tk.Entry(self,bd=10)
        self.userinput["text"]="Input Number(hit return)"

        # Create the application variable.
       


        self.userinput.bind('<Key-Return>',self.listen)
        self.userinput.grid(sticky=S)

        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("press enter to confirm entry")
        # Tell the entry widget to watch this variable.
        self.userinput["textvariable"] = self.contents      

    def listen(self,event):
        c = int(self.contents.get())
        d = list(conjecture.collatz(c))
        
        print(d[0])
        
        


#__________________________

        # hi function
    def say_hi(self):
        print("hi")

 

       

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()
