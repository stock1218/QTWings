try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Bullet import Bullet
from Vector import Vector

class NailBomb:

    def __init__(self):
        self.pos = None
        self.exploded = False
        self.bulletCount = 30
        self.bullets = []
        self.damage = 10

    def explode(self, pos):
        facing = Vector(0, -1)
        for i in range(self.bulletCount):
            self.bullets.append(Bullet(800, 600, pos, facing * 10))
            facing.rotate(360 / self.bulletCount)

    def update(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.outOfBounds():
                self.bullets.remove(bullet)

    def finish(self):
        self.exploded = True

    def getType(self):
        return 'Nail'

    def getBomb(self):
        return self.bullets

    def draw(self, canvas):
        for bullet in self.bullets:
            bullet.draw(canvas)

    def hasExploded(self):
        return self.exploded

    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.pos

    def getDamage(self):
        return self.damage

    def isColliding(self, enemy):
        for bullet in self.bullets:
            if (enemy.position - bullet.position).length() < (bullet.radius + enemy.radius) * 4:
                self.bullets.remove(bullet)
                return True
        return False

    def shouldRemove(self):
        return not self.bullets
