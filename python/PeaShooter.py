try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Bullet import Bullet

class PeaShooter:
    def __init__(self):
        self.canFire = True
        self.fireRate = 5  # Rounds per second
        self.fireTimer = simplegui.create_timer(1000 / self.fireRate, self.resetFire)


    def fire(self, width, height, position, directionVector):
        if self.canFire:
            self.canFire = False
            self.fireTimer.start()
            return [Bullet(
                width, height, (position + directionVector() * 16), directionVector() * 8)]
        return None

    def resetFire(self):
        self.canFire = True
        self.fireTimer.stop()
