from Player import Player
from Keyboard import Keyboard
from Vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Game:
    """Object responsible for the high level organisation of the game"""

    def __init__(self):
        """Constructor - Initialise game state and prepare the canvas"""
        self.player = Player(Vector(200, 400))
        self.keyboard = Keyboard()
        self.frame = simplegui.create_frame("QTWings", 400, 800)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)
        self.bullets = []
    def update(self):
        """Update the game state"""
        self.player.update(self.keyboard)
        if self.keyboard.space:
            b = self.player.fire()
            if b:
                self.bullets.append(b)

        for bullet in self.bullets:
            bullet.update()
            if bullet.outOfBounds():
                del bullet

    def draw(self, canvas):
        self.update()
        self.player.draw(canvas)
        for bullet in self.bullets:
            bullet.draw(canvas)
    def start(self):
        self.frame.start()


if __name__ == "__main__":
    game = Game()
    game.start()
