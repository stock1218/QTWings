try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

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
        self.stunned = False
        self.timer = simplegui.create_timer(1000, self.tick)
        self.sprite = simplegui.load_image("https://i.imgur.com/DfeRGaR.png")

    def update(self, player):

        toPlayer = player.getPos() - self.position
        
        if(not self.stunned):
            self.velocity += toPlayer.normalize() * self.acceleration

        if self.velocity.length() >= self.velocityLimit:
            self.velocity.normalize()
            self.velocity *= self.velocityLimit

        self.position += self.velocity

    def draw(self, canvas):
        canvas.draw_image(self.sprite, (16, 16),
                          (self.sprite.get_width(), self.sprite.get_height()),
                          self.position.getP(), (self.radius * 2, self.radius * 2))
        # canvas.draw_circle(self.position.getP(), self.radius, 1, "#ff0000", "#ff0000")

    def damage(self, damage):
        self.health -= damage

    def tick(self):
        if(self.stunTime == 0):
            self.stunned = False
            self.timer.stop()
            
        else:
            self.stunTime-= 1

    def getHealth(self):
        return self.health   
 
    def getRadius(self):
        return self.radius

    def getPos(self):
        return self.position

    def stun(self, time):
        self.stunned = True 
        print("Stunned for " + str(time))
        self.stunTime = time
        self.timer.start()
  
    #Bounce but for other enemies 
    def moveAway(self, pos):
        normal = (pos - self.position).normalize()
        self.bounce(normal)
 
    def bounce(self, normal):
        self.velocity.reflect(normal)
        #This pushes the enemy away from whatever they are colliding with
        self.velocity.subtract(normal * self.velocity.length() * 2)
