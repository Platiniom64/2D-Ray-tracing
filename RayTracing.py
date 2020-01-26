"""
This program tries to simulate the lightrays that come from a torch in a room.
"""

import tkinter


# * creation of the window
root = tkinter.Tk()
root.title("Ray tracing")

canvasSize = 700
c = tkinter.Canvas(root, width=canvasSize, heigh=canvasSize)
c.configure(bg="white")
c.pack()


# ! this list collects all the rectangles that are created
listOfRect = []
class Rectangle(object):
    
    # * this initiates the variables of the rectangle, it gives each vertex a value
    def __init__(self, x1, y1, x2, y2, colour="grey"):
        #these variables are stored for the next funciton, to update the recangle
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

        #creates the rectangle to be visible, otherwise there are only four lines
        self.shape = c.create_rectangle(x1, y1, x2, y2, fill=colour)

        #adds it to the list
        listOfRect.append(self)
    
    def updateRec(self):
        #first we remove the previous rectangle
        c.delete(self.shape)
        #then we replace it on top of the shadows
        self.shape = c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.colour)


# ! this list collects all the lines that are created
listOfLines = []
class Line(object):
    def __init__(self, x1, y1, x2, y2):
        # we first store the variables from the innit function
        self.coords = [(x1, y1), (x2, y2)]

        # we then create the line at those coordinates
        self.shape = c.create_line(x1, y1, x2, y2, fill="black")
        # we also create its shadow sothat when we update the shadow the entity exists
        self.shadow = c.create_line(-10,-10,-10,-10)

        listOfLines.append(self)

    def createShadow(self, mouseX, mouseY):
        #we first delete the shadow we created (that wasn't displayed on the screen if it is the first time)
        c.delete(self.shadow)
        
        # we begin by adding the two woordinates to the list of coordinates for the polynomial
        coordsPoly = [self.coords[1], self.coords[0]]

        #for each coordinate of the line, we create a coordinate that extends to the end of the window
        for vertex in self.coords:
            if mouseX < vertex[0]:
                gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                cornerY = gradient * canvasSize- gradient*vertex[0] + vertex[1]
                cornerX = canvasSize
                coordsPoly.append((cornerX, cornerY))

            elif mouseX > vertex[0]:
                gradient = (vertex[1] - mouseY)/(vertex[0] - mouseX)
                cornerY = gradient * 0- gradient*vertex[0] + vertex[1]
                cornerX = 0
                coordsPoly.append((cornerX, cornerY))

            else:
                if mouseX < self.coords[0][0] or mouseX < self.coords[1][0]:
                    if mouseY > self.coords[0][1]:
                        coordsPoly.append((mouseX, 0))
                        coordsPoly.append((canvasSize, 0))
                    else:
                        coordsPoly.append((mouseX, canvasSize))
                        coordsPoly.append((canvasSize, canvasSize))
                        

                elif mouseX > self.coords[0][0] or mouseX > self.coords[1][0]:
                    if mouseY > self.coords[0][1]:
                        coordsPoly.append((0, 0))
                        coordsPoly.append((mouseX, 0))
                    else:
                        coordsPoly.append((0, canvasSize))
                        coordsPoly.append((mouseX, canvasSize))
                
                else:
                    if mouseY > self.coords[0][1]:
                        coordsPoly.append((mouseX, 0))
                    else:
                        coordsPoly.append((mouseX, canvasSize))

                        

        # * this expands the polygon as when the line is horizontal, the shape ends on each side so these funtions extend those sothat the cover the hole window
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
"""
Hline = Line(100, 300, 500, 300)
Vline = Line(300, 100, 300, 500)
"""


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