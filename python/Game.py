from Player import Player
from Keyboard import Keyboard
from Vector import Vector
from Enemy import Enemy
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

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
                    enemy.health -= 1
                    if enemy.health == 0:
                        self.enemies.remove(enemy)
                        print("DESTROYED")
                    self.bullets.remove(bullet)
                    break

        for enemy in self.enemies:
            enemy.update(self.player)
            for i in self.enemies:
                if (enemy.position != i.position) and (enemy.position - i.position).length() < enemy.radius * 2:
                    pass  # What to do when they collide


    def draw(self, canvas):
        self.update()
        self.player.draw(canvas)
        for bullet in self.bullets:
            bullet.draw(canvas)

        for enemy in self.enemies:
            enemy.draw(canvas)

    def start(self):
        self.frame.start()


if __name__ == "__main__":
    game = Game()
    game.start()
