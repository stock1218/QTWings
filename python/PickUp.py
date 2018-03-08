try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Weapon import Weapon
from PowerUp import PowerUp
import random

class PickUp:

    def tick(self):
        """Add a random type of pickup (PowerUp, Weapon(Gun, Bomb)) to pickups[] and reset the timer to a different interval"""
        type = random.choice(['PowerUp', 'Weapon'])	
	
        if(len(self.pickUps) > self.maxPickUps):
            self.pickUps.pop(0)

        if(type == 'PowerUp'):
            self.pickUps.append(PowerUp(self.width, self.height))
        elif (type == 'Weapon'):
            self.pickUps.append(Weapon(self.width, self.height))


    def __init__(self, width, height, min=9000, max=200000):
        """Construct the PickUp"""
        self.width = width
        self.height = height
        self.pickUps = []
        self.maxPickUps = 5
        self.timer = simplegui.create_timer(random.randrange(min, max), self.tick)
        self.timer.start()

    def setInterval(self, min, max):
        self.min = min
        self.max = max


    def pickedUp(self, pickUp):
        """Find pickup and remove it from the list"""
        self.pickUps.pop(pickUp.index)
 
    def update(self):
        """would be used to update sprites"""
        pass

	
    def draw(self, canvas):
        for i in self.pickUps:
            i.draw(canvas)

