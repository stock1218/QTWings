import math
from Vector import Vector
class Enemy:
    """A basic representation of an enemy which directly pursues the player"""

    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius):
        self.position = initialPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = 0
        self.velocityLimit = velocityLimit
        self.health = health
        self.radius = radius

    def update(self, player):

        if self.velocity.length() >= self.velocityLimit:
            self.velocity.normalize()
            self.velocity *= self.velocityLimit

        self.position += self.velocity

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "#ff0000", "#ff0000")

    def hit(self, other):
        d = (self.position - other.position).length()
        return d <= self.radius * 6 + other.radius

    def seekObject(self, obj):
        toObj = obj.position - self.position
        self.velocity += toObj.normalize() * self.acceleration
