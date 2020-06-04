import tkinter as tk
import threading
import random
from threading import Thread
import time

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
        tk.Canvas.create_line(self,50,0,50,530,fill='white',width=10)
        tk.Canvas.create_line(self,550,0,550,530,fill='white',width=10)
        tk.Canvas.create_line(self,300,0,300,530,fill='white',width=10,dash=255)

        #class calls#
        car1 = Car()      #Instance Class Car
        car1.create_main_car(self)

        """K = Highway()
        K.create_highway(self)"""

        #Move the principal car
        def move_main_car():
            car1.create_main_car(self)
            circle_thread = Thread(target=car1.move_up)
            circle_thread.daemon = True
            circle_thread.start()

        #Buttons#
        tk.Button(self, text="Iniciar", font=("fixedsys", "15"), bg="yellow", command=move_main_car).place(x=10,y=565)


#Class  Car#
class Car():
    def __init__(self):
        self.x= 320
        self.y= 330
        self.x1= 500
        self.y1= 500 
        self.speed= None
        self.falling = True
        
    def create_main_car(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x1,self.y1,fill="red")
    
    def move_up(self):
        while self.falling:
            
            if self.y != 0:
                self.y -= 1
                self.y1 -= 1
            else:
                self.falling = False
            time.sleep(0.02)
                


"""class Highway():
    def __init__(self):
        self.x = 300
        self.y = 300

    def create_highway(self,canvas):
        canvas.create_rectangle(self.x,self.y,200,200,fill="yellow")"""
        

if __name__ == "__main__" :
    root = CreateRoot()
    root.resizable(False,False)
    root.title("Collision Simulator")
    root.mainloop()