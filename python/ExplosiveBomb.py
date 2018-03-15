try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Spritesheet import Spritesheet
class ExplosiveBomb:

    def __init__(self):
        self.damage = 10
        self.radius = 100
        self.pos = None
        self.exploded = False
        self.ss = None


    def explode(self, pos):
        self.pos = pos
        self.ss = Spritesheet("http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png", 9, 9, self.radius / 3.5, 2, True)

    def update(self):
        #update sprites
        self.radius -= 1

    def finish(self):
        self.exploded = True

    def draw(self, canvas):
        #canvas.draw_circle(self.pos.getP(), self.radius, 1, 'Red', 'Red')
        self.ss.update(canvas, self.pos, 0)
        self.ss.draw(canvas, self.pos, 0)

    def hasExploded(self):
        return self.exploded

    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.pos

    def getDamage(self):
        return self.damage

    def getType(self):
        return 'Explosive'

    def getBomb(self):
        return self

    def isColliding(self, enemy):
        return (self.pos - enemy.getPos()).length() <= enemy.getRadius() + self.radius

    def shouldRemove(self):
        return self.radius <= 0
