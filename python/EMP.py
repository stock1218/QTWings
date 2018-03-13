try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class EMP:

    def __init__(self):
        self.time = 5
        self.radius = 100
        self.pos = None
        self.exploded = False

    def explode(self, pos):
        self.pos = pos

    def update(self):
        #update sprites
        self.radius -= 1

    def finish(self):
        self.exploded = True

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, 'White')

    def hasExploded(self):
        return self.exploded

    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.pos

    def getTime(self):
        return self.time

    def getType(self):
        return 'EMP'

    def getBomb(self):
        return self

    def isColliding(self, enemy):
        return (self.pos - enemy.getPos()).length() <= enemy.getRadius() + self.radius

    def shouldRemove(self):
        return self.radius <= 0
