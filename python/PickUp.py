try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from random import randrange

class PickUp:

    def tick(self):
        """Add a random type of pickup (PowerUp, Weapon(Gun, Bomb)) to pickups[] and reset the timer to a different interval"""
        pass

    def __init__(self, min=9000, max=200000):
        """Construct the PickUp"""
        self.pickUps = []
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

