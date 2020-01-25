"""
This program tries to simulate the lightrays that come from a torch in a room.
"""

import tkinter


class Rectangle(object):
    
    # * this initiates the variables of the rectangle, it gives each vertex a value
    def __init__(self, x1, y1, x2, y2):
        # top left coordinates
        self.topLx = x1
        self.topLy = y1
        # top right coordinates
        self.topRx = x2
        self.topRy = y1

        #bottom right
        self.botRx = x2
        self.BotRy = y2
        #bottom left
        self.botLx = x1
        self.botLy = y2

        #creates the rectangle
        c.create_rectangle(x1, y1, x2, y2, outline="grey", fill="grey")


# * creation of the window
root = tkinter.Tk()
root.title("Ray tracing")

c = tkinter.Canvas(root, width=600, heigh=600)
c.configure(bg="black")
c.pack()

#creates a grey rectangle
x = Rectangle(100, 75, 500, 125)




# * start program
root.mainloop()