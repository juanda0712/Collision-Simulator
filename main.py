import tkinter as tk

class Simulator:
    #Inputs: Parent windows
    #Outputs:
    #Restrictions: None
    def __init__(self, master):                                                 #Constructor method
        self.master = master
        master.title("Collision Simulator")

        splashCanvas = tk.Canvas(master,height=600,width=600)
        splashCanvas.pack()
        
    def swithCanvas(self):
        print("Greetings!")

root = tk.Tk()
interface = Simulator(root)
root.mainloop()