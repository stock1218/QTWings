from Vector import Vector
from Bullet import Bullet
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Player:
    """Object providing a representation of the player"""

    def __init__(self, width, height,initialPos):
        """Initialise a new Player object"""
        self.width = width
        self.height = height
        self.health = 5
        self.position = initialPos
        self.velocity = Vector(0, 0)
        self.rotation = 0  # Degrees rotation from initial
        self.canFire = True
        self.fireRate = 3 #rounds per second
        self.fireTimer = simplegui.create_timer(1000 / self.fireRate, self.resetFire)

    def directionVector(self):
        return Vector(0, -1).rotate(self.rotation)

    def rotate(self, rot):
        self.rotation += rot

    def update(self, kbd):
        """Update the Player state (should be called by Game.update)"""
        # Turning and acceleration
        if kbd.up:
            self.velocity += self.directionVector() * 0.3
        if kbd.left:
            self.rotate(-2.5)
        if kbd.right:
            self.rotate(2.5)
        # Speed limiting
        if self.velocity.length() >= 5:
            self.velocity.normalize()
            self.velocity *= 5

        # Screen wrapping
        if self.position.x > self.width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = self.width
        if self.position.y > self.height:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = self.height

        self.position += self.velocity

        self.velocity *= 0.98

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), 9, 1, "#0000ff", "#0000ff")
        canvas.draw_line(self.position.getP(),
                         (self.position + self.directionVector() * 15).getP(),
                         4, "#0000ff")

    def fire(self):
        if self.canFire:
            self.canFire = False
            self.fireTimer.start()
            return Bullet(
                (self.position + self.directionVector() * 16), self.directionVector() * 8)
        return None

    def resetFire(self):
        self.canFire = True
        self.fireTimer.stop()

    def getHealth(self):
        return self.health
