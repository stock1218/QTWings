try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Weapon import Weapon
from Bomb import Bomb
from PowerUp import PowerUp
import random

class PickUp:

    def __init__(self, width, height, interval):
        """Construct the PickUp"""
        self.width = width
        self.height = height
        self.pickUps = []
        self.maxPickUps = 5
        self.timer = simplegui.create_timer(interval, self.tick)
        self.timer.start()
        self.tick()

    def tick(self):
        """Add a random type of pickup (PowerUp, Weapon(Gun, Bomb)) to pickups[] and reset the timer to a different interval"""
        if(len(self.pickUps) > self.maxPickUps):
            self.pickUps.pop(0)

        self.pickUps.append(random.choice([PowerUp(self.width, self.height), Weapon(self.width, self.height), Bomb(self.width, self.height)]))

    def setInterval(self, min, max):
        self.min = min
        self.max = max

    def getPickUps(self):
        return self.pickUps

    def getType(self, pickUp):
        return self.pickUps[self.pickUps.index(pickUp)].getType()

    def givePickUp(self, pickUp):
        """Find pickup and remove it from the list"""
        getPickUp = self.pickUps.pop(self.pickUps.index(pickUp))
        return getPickUp.getValue()
 
    def update(self):
        """would be used to update sprites"""
        pass
	
    def draw(self, canvas):
        for i in self.pickUps:
            i.draw(canvas)
