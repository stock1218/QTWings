from Bullet import Bullet
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange
class Shotgun:
    def __init__(self):
        self.canFire = True
        self.fireRate = 3  # Rounds per second
        self.fireTimer = simplegui.create_timer(1000 / self.fireRate, self.resetFire)


    def fire(self, width, height, position, directionVector, isGood):
        if self.canFire:
            self.canFire = False
            self.fireTimer.start()
            bullets = []
            for i in range(8):
                bullets.append(Bullet(width, height,
                    position + directionVector() * 16, directionVector().rotate(randrange(-30, 30)) * 6, True))
            return bullets
        return None

    def resetFire(self):
        self.canFire = True
        self.fireTimer.stop()
