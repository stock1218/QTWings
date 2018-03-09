from Player import Player
from Keyboard import Keyboard
from Vector import Vector
from Gnat import Gnat
from HUD import HUD
from PickUp import PickUp
from Interaction import Interaction

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
        self.player = Player(WIDTH, HEIGHT, Vector(200, 400))
        self.keyboard = Keyboard()
        self.hud = HUD(self.player, WIDTH, HEIGHT)
        self.frame = simplegui.create_frame("QTWings", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)
        self.pickUp = PickUp(WIDTH, HEIGHT, 10000)
        self.wave = 1
        self.bullets = []
        self.enemies = []

        for i in range(5):
            self.enemies.append(Gnat(
                Vector(randrange(0, 400), randrange(0, 800)),
                Vector(1, 1),
                0.2,
                2,
                1,
                6
            ))
        self.interaction = Interaction(self.player, self.pickUp, self.enemies)

    def update(self):
        """Update the game state"""
        self.player.update(self.keyboard)
        if self.keyboard.space:
            b = self.player.fire()
            if b:
                self.bullets += b

        for bullet in self.bullets:
            bullet.update()
            if bullet.outOfBounds():
                self.bullets.remove(bullet)
                continue
            for enemy in self.enemies:
                if (enemy.position - bullet.position).length() < bullet.radius + enemy.radius:
                    print("HIT")
                    enemy.health -= 1
                    if enemy.health == 0:
                        self.enemies.remove(enemy)
                        print("DESTROYED")
                    self.bullets.remove(bullet)
                    break

        for enemy in self.enemies:
            enemy.update(self.player)

        self.pickUp.update()
        self.interaction.update();

    def draw(self, canvas):
        self.update()
        self.player.draw(canvas)
        for bullet in self.bullets:
            bullet.draw(canvas)

        for enemy in self.enemies:
            enemy.draw(canvas)

        self.hud.draw(canvas, self.wave)
        self.pickUp.draw(canvas)

    def start(self):
        self.frame.start()


if __name__ == "__main__":
    game = Game()
    game.start()
