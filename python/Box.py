try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Line import Line
from Vector import Vector

class Box:

    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        self.points = [self.pos, Vector(self.pos.x + self.width, self.pos.y), Vector(self.pos.x + self.width, self.pos.y + self.height), Vector(self.pos.x, self.pos.y + self.height)]
        
        self.lines = [ Line(self.points[i], self.points[(i + 1) % len(self.points)])
                        for i in range(len(self.points)) ] 
    def draw(self, canvas):
        for line in self.lines:
            line.draw(canvas)

    def isColliding(self, playerPos, playerRadius):
        for line in self.lines:
            if (line.distanceTo(playerPos) < line.thickness + playerRadius and line.covers(playerPos)):
                return line.normal

        return None
