from Enemy import Enemy
import math
from Vector import Vector
from Gnat import Gnat
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Tank(Gnat):
    def __init__(self, initialPos, velocity, acceleration, velocityLimit, health, radius):
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
        self.weapon = []
        self.timer = simplegui.create_timer(1000, self.tick)

    def directionVector(self):
        return Vector(0, -1).rotate(self.rotation)

    def fire(self):
        return self.weapon.fire(900, 600, self.position, self.directionVector)

    def layMine(self):
        pass

    def getType(self):
        return 'Tank'

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "Yellow", "Yellow")
