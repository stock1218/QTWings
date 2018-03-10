try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class ExplosiveBomb:

    def __init__(self):
        self.damage = 10
        self.radius = 40
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
        canvas.draw_circle(self.pos.getP(), self.radius, 1, 'Red', 'Red')

    def hasExploded(self):
        return self.exploded

    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.pos

    def getDamage(self):
        return self.damage

    def isColliding(self, enemy):
        return (self.getPos() - enemy.getPos()).length() <= enemy.getRadius() + self.getRadius()
