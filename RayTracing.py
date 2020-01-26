"""
This program tries to simulate the lightrays that come from a torch in a room.
"""

import tkinter


# * creation of the window
root = tkinter.Tk()
root.title("Ray tracing")

canvasSize = 600
c = tkinter.Canvas(root, width=canvasSize, heigh=canvasSize)
c.configure(bg="white")
c.pack()


# ! this list collects all the rectangles that are created
listOfRect = []
class Rectangle(object):
    
    # * this initiates the variables of the rectangle, it gives each vertex a value
    def __init__(self, x1, y1, x2, y2, colour="grey"):
        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

        self.colour = colour

        # top and bottom lines
        Line(x1, y1, x2, y1)
        Line(x1, y2, x2, y2)

        #left and right lines
        Line(x1, y1, x1, y2)
        Line(x2,y1, x2, y2)

        #creates the rectangle
        self.shape = c.create_rectangle(x1, y1, x2, y2, fill=colour)

        #adds it to the list
        listOfRect.append(self)
    
    def updateRec(self):
        c.delete(self.shape)
        self.shape = c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.colour)


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
                try:
                    gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                except:
                    gradient = 999999999999999
                cornerY = gradient * canvasSize- gradient*vertex[0] + vertex[1]
                cornerX = canvasSize
                coordsPoly.append((cornerX, cornerY))

            else:
                try:
                    gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                except:
                    gradient = 999999999999999
                cornerY = gradient * 0- gradient*vertex[0] + vertex[1]
                cornerX = 0
                coordsPoly.append((cornerX, cornerY))
        

        if coordsPoly[2][0] == 0 and coordsPoly[3][0] == canvasSize and mouseY <= self.coords[1][1]:
            coordsPoly.insert(3, (0,canvasSize))
            coordsPoly.insert(4, (canvasSize,canvasSize))
            
        if coordsPoly[2][0] == 0 and coordsPoly[3][0] == canvasSize and mouseY >= self.coords[1][1]:
            coordsPoly.insert(3, (0,0))
            coordsPoly.insert(4, (canvasSize,0))

        self.shadow = c.create_polygon(coordsPoly)




#creates a grey rectangle

rectTOP = Rectangle(100, 100, 500, 150)
rectLEFT = Rectangle(100, 200, 150, 500)
rectRIGHT = Rectangle(450, 200, 500, 500)
rectMID = Rectangle(250, 250, 350, 350)
rectMIDBOT = Rectangle(275, 500, 325, 600)

endSquare = c.create_rectangle(40, 540, 60, 560, fill="white", outline="white", activefill="green")




# * this function gets the coordinates of the mouse and sends those coordinates to the function placeLines
def motion(event):
    update(event.x, event.y)
root.bind('<Motion>', motion)


def update(mouseX, mouseY):
    for line in listOfLines:
        line.createShadow(mouseX, mouseY)
    for rect in listOfRect:
        rect.updateRec()


# * start program
root.mainloop()