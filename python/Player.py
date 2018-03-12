from Vector import Vector
from Bullet import Bullet
from PeaShooter import PeaShooter
from Shotgun import Shotgun
import math
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
        self.radius = 9
        self.collisionRadius = self.radius
        self.health = 3
        self.position = initialPos
        self.velocity = Vector(0, 0)
        self.rotation = 0  # Degrees rotation from initial
        self.weapon = Shotgun()
        self.bomb = None
        self.powerUp = None
        self.spritesheet = Spritesheet("https://i.imgur.com/Kd8TC2T.png", 4, 1)

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
        if kbd.down:
            self.velocity -= self.directionVector() * 0.3
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

        #checking shield
        if(self.powerUp):
            self.powerUp.tick()
            if(self.powerUp.getStatus()):
                self.powerUp = None
                self.collisionRadius = self.radius

    def draw(self, canvas, kbd):
        if kbd.up:
            Spritesheet("https://i.imgur.com/Kd8TC2T.png", 4, 1)
        else:
            canvas.draw_image(simplegui.load_image('https://i.imgur.com/ZUpcygF.png'), (16, 15),
                              (20, 16), self.position.getP(), (self.radius * 4, self.radius * 4),
                              self.rotation / (180 / math.pi))
        #canvas.draw_circle(self.position.getP(), self.radius, 1, "#0000ff", "#0000ff")
        #canvas.draw_line(self.position.getP(),
        #                 (self.position + self.directionVector() * 15).getP(),
        #                 4, "#0000ff")

        if(self.powerUp):
            self.powerUp.draw(canvas, self.position)

    def givePickUp(self, type, pickUp):
        if(type == 'PowerUp'):
            self.powerUp = pickUp
            self.collisionRadius = pickUp.getRadius()

        elif (type == 'Weapon'):
            self.weapon = pickUp
        else:
            if(not self.bomb):
                self.bomb = pickUp

        print("PICKED UP: " + type) 

    def fire(self):
        return self.weapon.fire(self.width, self.height, self.position, self.directionVector)

    def dropBomb(self):
        self.bomb.explode(self.position)
        bomb = self.bomb
        self.bomb = None
        return bomb

    def getBomb(self):
        return self.bomb

    def getPos(self):
        return self.position

    def getRadius(self):
        return self.radius

    def getCollisionRadius(self):
        return self.collisionRadius

    def getHealth(self):
        return self.health

    def damage(self, amount):
        if(self.powerUp):
            self.powerUp.damage(amount)
        else:
            self.health -= amount
