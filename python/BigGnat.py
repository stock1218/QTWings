from Gnat import Gnat
from PeaShooter import PeaShooter
from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class BigGnat(Gnat):
    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius=15):
        self.position = initialPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = 0
        self.velocityLimit = velocityLimit
        self.inCollision = None
        self.damageDealt = 1
        self.stunned = False
        self.health = health
        self.radius = radius
        self.weapon = PeaShooter(30)
        self.timer = simplegui.create_timer(1000, self.tick)
        self.sprite = simplegui.load_image("https://i.imgur.com/DfeRGaR.png")

    def directionVector(self, player):
        toPlayer = player.getPos() - self.position
        toPlayer.normalize()
        return toPlayer.rotate(self.rotation)

    def update(self, player):

        toPlayer = player.getPos() - self.position

        if (not self.stunned):
            self.velocity += toPlayer.normalize() * self.acceleration

        if self.velocity.length() >= self.velocityLimit:
            self.velocity.normalize()
            self.velocity *= self.velocityLimit

        self.position += self.velocity

    def fire(self, player):
        return self.weapon.fire(900, 600, self.position, lambda: self.directionVector(player))

    def getType(self):
        return 'BigGnat'
