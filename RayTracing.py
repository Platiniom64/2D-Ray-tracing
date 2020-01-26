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
        self.botRy = y2
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

def getRectCoords(mouseX, mouseY):

    listOfCoords = []

    for rect in listOfRect:
        if rect.topLx <= mouseX and rect.topLy <= mouseY:
            listOfCoords.append(rect.topLx, rect.topLy)

    return listOfCoords




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

    getRectCoords(mouseX, mouseY)

 
listCoords = [(listOfRect[0].botLx, listOfRect[0].botLy), (listOfRect[0].botRx, listOfRect[0].botRy), 
                 (listOfRect[2].topLx, listOfRect[2].topLy), (listOfRect[2].botLx, listOfRect[2].botLy),
                 (listOfRect[1].botRx, listOfRect[1].botRy), (listOfRect[1].topLx, listOfRect[1].topLy), (listOfRect[1].topRx, listOfRect[1].topRy)]
listCoords.sort()

# * start program
c.create_polygon(listCoords,
                 fill="white")
root.mainloop()