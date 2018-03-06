from Vector import Vector
from Bullet import Bullet

class Player:
    """Object providing a representation of the player"""

    def __init__(self, initialPos):
        """Initialise a new Player object"""
        self.position = initialPos
        self.velocity = Vector(0, 0)
        self.rotation = 0  # Degrees rotation from initial

    def directionVector(self):
        return Vector(0, -1).rotate(self.rotation)

    def rotate(self, rot):
        self.rotation += rot

    def update(self, kbd):
        """Update the Player state (should be called by Game.update)"""
        # Turning and acceleration
        if kbd.up:
            self.velocity += self.directionVector()
        if kbd.left:
            self.rotate(-2.5)
        if kbd.right:
            self.rotate(2.5)
        # Speed limiting
        if self.velocity.length() >= 5:
            self.velocity.normalize()
            self.velocity *= 5

        # Screen wrapping
        if self.position.x > 400:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = 400
        if self.position.y > 800:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = 800

        self.position += self.velocity

        self.velocity *= 0.98

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), 9, 1, "#0000ff", "#0000ff")
        canvas.draw_line(self.position.getP(),
                         (self.position + self.directionVector() * 15).getP(),
                         4, "#0000ff")

    def fire(self):
        return Bullet(
            (self.position + self.directionVector() * 16), self.directionVector() * 5)
