import tkinter as tk
import threading
import random

class CreateRoot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.window = True
        self.switchWindow(StartPage)

    def switchWindow(self, createCanvas):
        createCanvas = createCanvas(self)
        if self.window is not True:
            self.window.destroy()
        self.window = createCanvas
        self.window.pack()
        

class StartPage(tk.Canvas):
    def __init__(self,master):
        tk.Canvas.__init__(self, master)
        tk.Canvas.config(self,height=600,width=600,bg="red")
        tk.Label(self, text="Juan Daniel Rodriguez Montero").place(x=280,y=300)
        tk.Button(self, text="Ir al simulador",
        command=lambda: master.switchWindow(Simulator)).place(x=10,y=10)

class Simulator(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master)
        tk.Canvas.config(self,bg="black",height=600,width=600)

        #highway lines#
        tk.Canvas.create_line(self,0,530,600,530,fill='white',width=4) 
        tk.Canvas.create_line(self,50,0,50,530,fill='white',width=7)
        tk.Canvas.create_line(self,550,0,550,530,fill='white',width=7)
        tk.Canvas.create_line(self,300,0,300,530,fill='white',width=7,dash=255)



if __name__ == "__main__" :
    root = CreateRoot()
    root.resizable(False,False)
    root.title("Collision Simulator")
    root.mainloop()