import math
from Vector import Vector
class Gnat:
    """A basic representation of an enemy which directly pursues the player"""

    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius):
        self.position = initialPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = 0
        self.velocityLimit = velocityLimit
        self.health = health
        self.radius = radius
        self.damageDealt = 1
        self.inCollision = None

    def update(self, player):

        toPlayer = player.getPos() - self.position
        
        self.velocity += toPlayer.normalize() * self.acceleration

        if self.velocity.length() >= self.velocityLimit:
            self.velocity.normalize()
            self.velocity *= self.velocityLimit

        self.position += self.velocity

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "#ff0000", "#ff0000")

    def damage(self, damage):
        self.health -= damage

    def getHealth(self):
        return self.health   
 
    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.position
  
    #Bounce but for other enemies 
    def moveAway(self, pos):
        normal = (pos - self.position).normalize()
        self.bounce(normal)
 
    def bounce(self, normal):
        self.velocity.reflect(normal)
        #This pushes the enemy away from whatever they are colliding with
        self.velocity.subtract(normal * self.velocity.length() * 2)
