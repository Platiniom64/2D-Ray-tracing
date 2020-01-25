"""
This program tries to simulate the lightrays that come from a torch in a room.
"""

import tkinter

# ! this list collects all the rectangles that are created
listOfRect = []
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

        #adds it to the list
        listOfRect.append(self)

# ! this list collects all the lines that are created
listOfLines = []
class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2

        self.x2 = x2
        self.y2 = y2

        self.shape = c.create_line(x1, y1, x2, y2, fill="white")

        listOfLines.append(self)


# * creation of the window
root = tkinter.Tk()
root.title("Ray tracing")

c = tkinter.Canvas(root, width=600, heigh=600)
c.configure(bg="black")
c.pack()

#creates a grey rectangle
rectTOP = Rectangle(100, 75, 500, 125)
rectLEFT = Rectangle(100, 250, 150, 500)
rectRIGHT = Rectangle(450, 250, 500, 500)


# * this function gets the coordinates of the mouse and sends those coordinates to the function placeLines
def motion(event):
    placeLines(event.x, event.y)
root.bind('<Motion>', motion)


def placeLines(mouseX, mouseY):


    for line in listOfLines:
        c.delete(line.shape)
        listOfLines.remove(line)

    
    for rectangle in listOfRect:
        Line(mouseX, mouseY, rectangle.topLx, rectangle.topLy)


# * start program
root.mainloop()