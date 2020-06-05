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



        c1 = Car(self)
        c2 = RandomCar(self)
        #Move the principal car
        def start_animation():

            main_car = Thread(target=c1.move_main)
            main_car.daemon = True
            main_car.start()

            
            main_car1 = Thread(target=c2.create_prob)
            main_car1.daemon = True
            main_car1.start()

        #Buttons#
        tk.Button(self, text="Iniciar", font=("fixedsys", "15"), bg="yellow", command=start_animation).place(x=10,y=565)


#Class  Car#
class Car():
    def __init__(self,canvas):
        self.canvas = canvas
        self.x1,self.y1 = 320,400
        self.x01,self.y01 =450,500
        self.moving = True
        self.maincar = canvas.create_rectangle(self.x1,self.y1,self.x01,self.y01,fill="red")
    
    def move_main(self):  #  self.canvas (canvas)     #self.maincar (objeto rectagulo)
        while self.y1 > 10:
            if self.moving:
                self.canvas.move(self.maincar,0,-2)
            self.y1 -= 1
            time.sleep(0.08)

class RandomCar():
    
    def __init__(self,canvas):
        self.canvas = canvas
        self.x1,self.y1 = 200,20
        self.x01,self.y01 =300,100    
       
    def create_prob(self):
        self.prob =  random.randint(0,1)
        if self.prob == 1:
            self.car = self.canvas.create_rectangle(self.x1,self.y1,self.x01,self.y01,fill="red")
        
        
          
if __name__ == "__main__" :
    root = CreateRoot()
    root.resizable(False,False)
    root.title("Collision Simulator")
    root.mainloop()