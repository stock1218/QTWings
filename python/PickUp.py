try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Weapon import Weapon
from PowerUp import PowerUp
from random import randrange

class PickUp:

    def tick(self):
        """Add a random type of pickup (PowerUp, Weapon(Gun, Bomb)) to pickups[] and reset the timer to a different interval"""
        type = random.choice(['PowerUp', 'Weapon'])	
	
        if(self.pickUps.length > self.maxPickUps):
            self.pickUps.pop(0)

        if(type == 'PowerUp'):
            self.pickUps.append(PowerUp())
        elif (type == 'Weapon'):
            self.pickUps.append(Weapon())


    def __init__(self, min=9000, max=200000):
        """Construct the PickUp"""
        self.pickUps = []
        self.maxPickUps = 5
        self.timer = simplegui.create_timer(randrange(min, max), self.tick)
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

