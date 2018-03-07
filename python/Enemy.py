import math
from Vector import Vector
class Enemy:
    """A basic representation of an enemy which directly pursues the player"""

    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius):
        self.position = initialPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.health = health
        self.rotation = 0
        self.velocityLimit = velocityLimit
        self.radius = radius



    def update(self, player):
        toPlayer = player.position - self.position

        self.velocity += toPlayer.normalize() * self.acceleration

        if self.velocity.length() >= self.velocityLimit:
            self.velocity.normalize()
            self.velocity *= self.velocityLimit


        self.position += self.velocity

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "#ff0000", "#ff0000")
