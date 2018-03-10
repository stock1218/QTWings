try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

class Line:
    def __init__(self, thickness, point1, point2):
        self.pA = point1
        self.pB = point2
        self.thickness = thickness
        self.unit = (self.pB - self.pA).normalize()
        self.normal = self.unit.copy().rotateAnti()
        
    def draw(self, canvas):
        canvas.draw_line(self.pA.getP(), self.pB.getP(), self.thickness, "White")
        
    def distanceTo(self, pos):
        posToA = pos - self.pA
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()

    def covers(self, pos):
        return ((pos - self.pA).dot(self.unit) >= 0 and
                (pos - self.pB).dot(-self.unit) >= 0)
