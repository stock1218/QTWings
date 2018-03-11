from Player import Player
from Keyboard import Keyboard
from Vector import Vector
from Gnat import Gnat
from HUD import HUD
from PickUp import PickUp
from Interaction import Interaction
from Obstacle import Obstacle
from Wave import Wave
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

WIDTH = 800
HEIGHT = 600

class Game:
    """Object responsible for the high level organisation of the game"""

    def __init__(self):
        """Constructor - Initialise game state and prepare the canvas"""
        self.player = Player(WIDTH, HEIGHT, Vector(WIDTH/2, HEIGHT/2))
        self.keyboard = Keyboard()
        self.hud = HUD(self.player, WIDTH, HEIGHT)
        self.frame = simplegui.create_frame("QTWings", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)
        self.pickUp = PickUp(WIDTH, HEIGHT, 10000)
        self.wave = Wave(WIDTH, HEIGHT, 1)
        self.obstacles = Obstacle(WIDTH, HEIGHT)
        self.explosions = []
        self.bullets = []
        self.interaction = Interaction(self.player, self.pickUp)

        #start the wave
        self.wave.startWave()

    def update(self):
        """Update the game state"""
        self.player.update(self.keyboard)
        if self.keyboard.space:
            b = self.player.fire()
            if b:
                self.bullets += b

        if self.keyboard.b:
            bomb = self.player.getBomb()
            if(bomb):
                self.explosions.append(self.player.dropBomb())

        for explosion in self.explosions:
            explosion.update()
            if explosion.shouldRemove():
               self.explosions.remove(explosion)

        for bullet in self.bullets:
            bullet.update()

        self.wave.update(self.player)
        self.pickUp.update()
        self.interaction.update(self.wave.getEnemies(), self.explosions, self.obstacles.getObstacles(), self.bullets);

    def draw(self, canvas):
        self.update()
        self.player.draw(canvas)
        for bullet in self.bullets:
            bullet.draw(canvas)

        for explosion in self.explosions:
            explosion.draw(canvas)

        self.wave.draw(canvas)
        self.pickUp.draw(canvas)
        self.obstacles.draw(canvas)
        self.hud.draw(canvas, self.wave.getWave())

    def start(self):
        self.frame.start()


if __name__ == "__main__":
    game = Game()
    game.start()
