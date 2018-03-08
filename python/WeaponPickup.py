##from Weapon import Weapon
from random import randrange
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class WeaponPickup():
    def __init__(self, x, y, min=9000, max=200000):
        """Construct the PickUp"""
        self.x = x
        self.y = y
##        self.payload =
        self.timer = simplegui.create_timer(randrange(min, max), self.tick)
        self.timer.start()
        self.pickedUp = False

    def pickUp(self):
        self.pickedUp = True

    def isPickedUp(self):
        return self.pickedUp
