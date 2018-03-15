from Vector import Vector
from Bullet import Bullet
from PeaShooter import PeaShooter
from Shotgun import Shotgun
from Spritesheet import Spritesheet
import math
from EMP import EMP
from ExplosiveBomb import ExplosiveBomb

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Player:
    """Object providing a representation of the player"""

    def __init__(self, width, height, initialPos):
        """Initialise a new Player object"""
        self.width = width
        self.height = height
        self.radius = 9
        self.collisionRadius = self.radius
        self.health = 3
        self.position = initialPos
        self.velocity = Vector(0, 0)
        self.rotation = 0  # Degrees rotation from initial
        self.weapon = PeaShooter(5)
        self.bomb = None
        self.powerUp = None
        self.inCollision = None
        self.stationarySprite = simplegui.load_image('https://i.imgur.com/ZUpcygF.png')
        self.forwardSpritesheet = Spritesheet("https://i.imgur.com/Kd8TC2T.png", 4, 1, self.radius, 6, False)

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

    def draw(self, canvas, kbd, inGame):
        if kbd.up and inGame:
            self.forwardSpritesheet.update(canvas, self.position, self.rotation)
        else:
            canvas.draw_image(self.stationarySprite,
                              (self.stationarySprite.get_width() / 2, self.stationarySprite.get_height() / 2),
                              (self.stationarySprite.get_width(), self.stationarySprite.get_height()),
                              self.position.getP(), (self.radius * 7, self.radius * 7),
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

    def bounce(self, normal):
        self.velocity.reflect(normal)
        #pushing the player away from whatever they are colliding with
        self.velocity.subtract(normal * (self.velocity.length() * 0.5))

    def dropBomb(self):
        self.bomb.explode(self.position)
        bomb = self.bomb.getBomb()
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
