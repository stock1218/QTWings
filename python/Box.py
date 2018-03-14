try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Line import Line
from Vector import Vector

class Box:

    def __init__(self, pos, width, height):
        self.thickness = 3
        self.pos = pos
        self.width = width
        self.height = height
        self.vectorPoints = [self.pos, Vector(self.pos.x + self.width, self.pos.y), Vector(self.pos.x + self.width, self.pos.y + self.height), Vector(self.pos.x, self.pos.y + self.height)]  
        self.points = [(i.getP()) for i in self.vectorPoints]
        self.lines = [ Line(self.thickness, self.vectorPoints[i], self.vectorPoints[(i + 1) % len(self.vectorPoints)])
                        for i in range(len(self.points)) ] 
    def draw(self, canvas):
        for line in self.lines:
            line.draw(canvas)

    def isColliding(self, playerPos, playerRadius):
        result = None
        for line in self.lines:
            if (line.distanceTo(playerPos) <= line.thickness + playerRadius and line.covers(playerPos)):
                return line.normal
        return None
