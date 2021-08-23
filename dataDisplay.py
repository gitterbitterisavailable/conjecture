import tkinter as tk
import conjecture
from turtle import *
from tkinter.constants import E, NW, S,W

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("VR-1")
        
    

    def create_widgets(self):
        #resetall pen widget
        self.restall = tk.Button(self)
        self.restall["text"] = "reset drawing"
        self.restall["command"] = self.resetALLturd
        self.restall.grid(row =2,sticky=W,ipadx=10,ipady=5)

        self.resetTurtle = tk.Button(self)
        self.resetTurtle["text"] = "reset to redraw \n (will auto draw input number)"
        self.resetTurtle["command"] = self.resetTurd
        self.resetTurtle.grid(row = 2,ipadx=10,ipady=5)


        #quit widget
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy,bd=5)
        self.quit.grid(row=1,sticky=W)

    #___________________________
 #input widget

        self.userinput = tk.Entry(self,bd=10)
        self.userinput["text"]="Input Number(hit return)"

        # Create the application variable.
       


        self.userinput.bind('<Key-Return>',self.listen)
        self.userinput.grid(sticky=S)

        self.contents = tk.StringVar()
        self.contentsInt = tk.IntVar() 
        # Set it to some value.
        self.contents.set("enterTOstart")
     
        # Tell the entry widget to watch this variable.
        self.userinput["textvariable"] = self.contents      
        
        
        


 #turtleCanvas widget
     
        canvaswid = 1000 
        canvashi = 1000 
        fac = tk.Canvas(self,width=canvaswid,height=canvashi)
        fac.grid(stick=E)
        self.turd = RawTurtle(fac)
        self.turd.right(0)
        self.turd.pen(pensize=5) 
        

    def listen(self,event):
        c = int(self.contents.get())
        d = list(conjecture.collatz(c))

        print(d[0])
        self.turd.pendown()

        for element in d:
            self.turd.right(element)
            self.turd.fd(element)

            # if element == len(d):
            #     self.turd.penup()
            #     self.turd.setpos(0,0) 
            #     self.turd.heading()   
        


           

    #__________________________
    
        # reset functions
    def resetALLturd(self):
        currentAngle = float(self.turd.heading())
        print("reset starting")
        self.turd.penup()
        self.turd.setpos(0,0)
        self.turd.right(currentAngle)
        self.turd.clear()
        


    def resetTurd(self):
        currentAngle = float(self.turd.heading())
        print("reset2 starting")
        self.turd.penup()
        self.turd.setpos(0,0)
        self.turd.right(currentAngle)
        #redraw process
        c = int(self.contents.get())
        d = list(conjecture.collatz(c))

        print(d[0])
        self.turd.pendown()

        for element in d:
            self.turd.right(element)
            self.turd.fd(element)  
        
        
         



       

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()
