try:
        import simplegui
except:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PickUp import PickUp

class Interaction:
    '''Responsible for collisions between objects on the screen'''

    def __init__(self, player, pickUp):
        self.player = player
        self.pickUp = pickUp 
  
    def distanceTo(self, pos1, pos2):
       return (pos1 - pos2).length()

    def update(self):
        '''check for collisions'''
        for i in self.pickUp.getPickUps():
            if(self.distanceTo(i.getPos(), self.player.getPos()) <= self.player.getRadius() + i.getRadius()):
                self.player.givePickUp(self.pickUp.givePickUp(i))
                print("PICKUP")
