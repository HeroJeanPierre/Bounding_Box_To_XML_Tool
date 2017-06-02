from time import sleep
import tkinter as tk
from PIL import ImageTk, Image


class Bounding_Tool:


    def __init__(self):
        # Set up variables
        self.top = tk.Tk()
        self.top.title('Bounding Box Tool')
        self.imageFile = '/home/julien/Pictures/Chair/0001.jpg'
        # self.top.resizable(0,0)
        # #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        raw_img = Image.open(self.imageFile)
        # # Create Image with height
        self.img = ImageTk.PhotoImage(raw_img)
        self.width, self.height = raw_img.size
        # # Set the frame to be the same size as the image being tested
        self.top.geometry('{}x{}'.format(self.width, self.height))
        print('Width and Height: {}x{}'.format(self.width, self.height))
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(self.top, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
                
                
        for i in range(100):
            sleep(1)  # Need this to slow the changes down
            self.top.geometry('{}x{}'.format(self.width, self.height))
            print('Width and Height: {}x{}'.format(self.width, self.height))
            self.x = self.top.winfo_pointerx()
            self.y = self.top.winfo_pointery()
            self.abs_coord_x = self.top.winfo_pointerx() - self.top.winfo_rootx()
            self.abs_coord_y = self.top.winfo_pointery() - self.top.winfo_rooty()
            print('x: {}, y: {}, xAbs: {}, yAbs: {}'.format(self.x, self.y, self.abs_coord_x, self.abs_coord_y))
            self.top.update_idletasks()
        #frame = tk.Frame(self.top, width=100, height=100)
        #frame.bind("<Key>", key)
        frame.pack()

        def key(event):
            print("pressed", repr(event.char))
        #Start the GUI
        self.top.mainloop()







if __name__ == '__main__':

    B = Bounding_Tool()
    B.loop()
