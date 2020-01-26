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

        self.coords = [(x1, y1), (x2, y2)]

        self.shape = c.create_line(x1, y1, x2, y2, fill="black")

        listOfLines.append(self)

    def createShadow(self, mouseX, mouseY):
        
        try:
            c.delete(self.shadow)
        except:
            pass

        coordsPoly = [self.coords[1], self.coords[0]]

        for vertex in self.coords:
            if mouseX <= vertex[0]:
                gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                cornerY = gradient * canvasSize * 2- gradient*vertex[0] + vertex[1]
                cornerX = canvasSize*2
                coordsPoly.append((cornerX, cornerY))

            else:
                gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                cornerY = gradient * (-canvasSize*2) - gradient*vertex[0] + vertex[1]
                cornerX = -canvasSize * 2
                coordsPoly.append((cornerX, cornerY))


        self.shadow = c.create_polygon(coordsPoly)






# * creation of the window
root = tkinter.Tk()
root.title("Ray tracing")

canvasSize = 600
c = tkinter.Canvas(root, width=canvasSize, heigh=canvasSize)
c.configure(bg="white")
c.pack()

#creates a grey rectangle
"""
rectTOP = Rectangle(100, 75, 500, 125)
rectLEFT = Rectangle(100, 250, 150, 500)
rectRIGHT = Rectangle(450, 250, 500, 500)
"""

Line(200, 100, 200, 300)
Line(400, 100, 400, 300)
Line(100, 300, 400, 500)

# * this function gets the coordinates of the mouse and sends those coordinates to the function placeLines
def motion(event):
    update(event.x, event.y)
root.bind('<Motion>', motion)


def update(mouseX, mouseY):
    for line in listOfLines:
        line.createShadow(mouseX, mouseY)

"""
listCoords = [(listOfRect[0].botLx, listOfRect[0].botLy), (listOfRect[0].botRx, listOfRect[0].botRy), 
                 (listOfRect[2].topLx, listOfRect[2].topLy), (listOfRect[2].botLx, listOfRect[2].botLy),
                 (listOfRect[1].botRx, listOfRect[1].botRy), (listOfRect[1].topLx, listOfRect[1].topLy), (listOfRect[1].topRx, listOfRect[1].topRy)]
listCoords.sort()
"""
# * start program
root.mainloop()