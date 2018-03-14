import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Mine:
    def __init__(self, width, height, position, velocity):
        self.width = width
        self.height = height
        self.position = position
        self.velocity = velocity
        self.radius = 3
        self.damage = 1
        self.inCollision = None
        self.bounces = 0
        self.exploded = False
        self.timeToExplode = random.randrange(1000, 5000)
        self.timer = simplegui.create_timer(1000, self.getMillis())
        self.millis = 0

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), 10, 1, "Orange", "Orange")

    def getMillis(self):
        self.millis += 1

    def checkExplode(self):
        if self.timer.getMillis >= self.timeToExplode:
            self.explode()


    def explode(self, pos):
        self.pos = pos

    def finish(self):
        self.exploded = True

    def update(self):
        self.position += self.velocity

    def getPos(self):
        return self.position

    def getRadius(self):
        return self.radius

    def getDamage(self):
        return self.damage

    def getType(self):
        return 'Mine'

    def isColliding(self, enemy):
        return (enemy.getPos() - self.position).length() <= self.radius + enemy.getRadius()

    def outOfBounds(self):
        return (self.position.x < 0) or (self.position.x > self.width) or (self.position.y < 0) or (self.position.y > self.height)

    def shouldRemove(self):
        return self.radius <= 0
