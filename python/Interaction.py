try:
        import simplegui
except:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PickUp import PickUp
from ExplosiveBomb import ExplosiveBomb
from NailBomb import NailBomb

class Interaction:
    '''Responsible for collisions between objects on the screen'''

    def __init__(self, player, pickUp, enemies):
        self.player = player
        self.pickUp = pickUp
        self.enemies = enemies

    def distanceTo(self, pos1, pos2):
       return (pos1 - pos2).length()

    def update(self, explosions):
        '''check for collisions'''
        for i in self.pickUp.getPickUps():
            if(self.distanceTo(i.getPos(), self.player.getPos()) <= self.player.getRadius() + i.getRadius()):
                self.player.givePickUp(self.pickUp.getType(i), self.pickUp.givePickUp(i))
                print("PICKUP")

        '''enemy collisions with each other and player'''
        for x in self.enemies:
            for y in self.enemies:
                if (x.position != y.position) and (x.position - y.position).length() - 3 < x.radius * 2:
                    x.position += x.position.copy().subtract(y.position).normalize()
                    y.position += y.position.copy().subtract(x.position).normalize()

            if (self.player.position - x.position).length() <= self.player.getCollisionRadius() + 1 + x.radius:
                self.enemies.remove(x)
                self.player.damage(x.damageDealt)
                print("PLAYER DAMAGED")

        #Check explosions
        for explosion in explosions:
            for enemy in self.enemies:
                if explosion.isColliding(enemy):
                    if type(explosion) is ExplosiveBomb or type(explosion) is NailBomb:
                        enemy.damage(explosion.getDamage())
            explosion.finish()
