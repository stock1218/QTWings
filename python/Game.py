from Player import Player
from Keyboard import Keyboard
from Vector import Vector
from Enemy import Enemy
from HUD import HUD
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

WIDTH = 1600
HEIGHT = 1200

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
        self.wave = 10
        self.bullets = []
        self.enemies = []

        for i in range(5):
            self.enemies.append(Enemy(
                Vector(randrange(0, 400), randrange(0, 800)),
                Vector(1, 1),
                0.2,
                2,
                1,
                6
            ))

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
                self.bullets.remove(bullet)
                continue
            for enemy in self.enemies:
                if (enemy.position - bullet.position).length() < bullet.radius + enemy.radius:
                    print("HIT")
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    break

        for enemy in self.enemies:
            enemy.update(self.player)

    def draw(self, canvas):
        self.update()
        self.player.draw(canvas)
        for bullet in self.bullets:
            bullet.draw(canvas)

        for enemy in self.enemies:
            enemy.draw(canvas)

        self.hud.draw(canvas, self.wave)

    def start(self):
        self.frame.start()


if __name__ == "__main__":
    game = Game()
    game.start()
