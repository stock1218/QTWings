try:
        import simplegui
except:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PickUp import PickUp
from ExplosiveBomb import ExplosiveBomb
from NailBomb import NailBomb
from EMP import EMP

class Interaction:
    '''Responsible for collisions between objects on the screen'''

    def __init__(self, player, pickUp):
        self.player = player
        self.pickUp = pickUp

    def distanceTo(self, pos1, pos2):
       return (pos1 - pos2).length()

    def update(self, enemies, explosions, obstacles, bullets):
        #check for collisions
        for i in self.pickUp.getPickUps():
            if(self.distanceTo(i.getPos(), self.player.getPos()) <= self.player.getRadius() + i.getRadius()):
                self.player.givePickUp(self.pickUp.getType(i), self.pickUp.givePickUp(i))
                print("PICKUP")

        #enemy collisions with each other and player
        for x in enemies:
            for y in enemies:
                if (x != y) and (x.getPos() - y.getPos()).length() - 3 < x.radius * 2:
                    x.moveAway(y.getPos())
                    y.moveAway(x.getPos())

            if (self.player.getPos() - x.getPos()).length() <= self.player.getCollisionRadius() + x.getRadius():
                enemies.remove(x)
                self.player.damage(x.damageDealt)
                print("PLAYER DAMAGED")

        #Rebound bullets that hit obstacles
        collision = None
        for bullet in bullets:
            for ob in obstacles:
                collision = ob.isColliding(bullet.getPos(), bullet.getRadius())
                if(collision):
                    break

            if (collision and not bullet.inCollision == ob):
                bullet.bounce(collision)
                bullet.inCollision = ob
            elif (not collision and bullet.inCollision):
                bullet.inCollision = None

        #Check for collisions with enemies and bullets
        for bullet in bullets:
            for enemy in enemies:
                if(enemy.getPos() - bullet.getPos()).length() <= bullet.getRadius() + enemy.getRadius():
                    print("HIT")
                    enemy.damage(bullet.getDamage())
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    break

        #Removing bullets out of bounds or if they have bounced more than 2 times
        for bullet in bullets:
            if bullet.outOfBounds() or bullet.bounces > 2:
                bullets.remove(bullet)

        #Check explosions
        for explosion in explosions:
            for enemy in enemies:
                if explosion.isColliding(enemy) and not explosion.exploded:
                    if type(explosion) is ExplosiveBomb or type(explosion) is NailBomb:
                        enemy.damage(explosion.getDamage())
                        print("Damaged Enemy")
                    elif type(explosion) is EMP:
                        enemy.stun(explosion.getTime())
            explosion.finish()
        
        #check for collisions with the walls and the player
        collision = None
        for ob in obstacles:
            collision = ob.isColliding(self.player.getPos(), self.player.getRadius())
            if(collision):
                break

        if (collision and not self.player.inCollision == ob):
            self.player.bounce(collision)
            self.player.inCollision = ob
        elif (not collision and self.player.inCollision):
            self.player.inCollision = None

        #check for collisions with the walls and the enemies
        for enemy in enemies:
            collision = None
            for ob in obstacles:
                collision = ob.isColliding(enemy.getPos(), enemy.getRadius())
                if(collision):
                    break

            if(collision and not enemy.inCollision == ob):
                enemy.bounce(collision)
                enemy.inCollision = ob
            elif(not collision and enemy.inCollision):
                enemy.inCollision = None

