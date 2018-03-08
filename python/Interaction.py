try:
        import simplegui
except:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Interaction:
    '''Responsible for collisions between objects on the screen'''

    def __init__(self, player, pickUp):
        self.player = player
        self.pickUp = pickUp 
  
    def distanceTo(self, pos1, pos2):
       return (pos1 - pos2).length()
 
    def update():
        '''check for collisions'''
        for i in PickUp.getPickUps():
            if(distanceTo(i.pos, self.player.pos) <= self.player.radius + i.radius):
                self.player.givePickUp(self.pickUp.givePickUp(i))
