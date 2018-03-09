from Enemy import Enemy
import math
from Vector import Vector
from PeaShooter import PeaShooter
class BigGnat(Enemy):
    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius):
        self.position = initialPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = 0
        self.velocityLimit = velocityLimit
        self.health = health
        self.radius = radius
        self.weapon = PeaShooter(3)

    def fire(self):
        return self.weapon.fire(self.width, self.height, self.position, self.directionVector)

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "#ff0000", "#ff0000")

    def decrementHealth(self, decrement):
        self.health -= decrement
