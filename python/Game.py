from Player import Player
from Keyboard import Keyboard
from Vector import Vector
from Gnat import Gnat
from HUD import HUD
from PickUp import PickUp
from Interaction import Interaction
from Obstacle import Obstacle
from Wave import Wave
from BigGnat import BigGnat
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

class Game:
    """Object responsible for the high level organisation of the game"""

    def __init__(self, WIDTH, HEIGHT, frame):
        """Constructor - Initialise game state and prepare the canvas"""
        self.player = Player(WIDTH, HEIGHT, Vector(WIDTH/2, HEIGHT/2))
        self.keyboard = Keyboard()
        self.hud = HUD(self.player, WIDTH, HEIGHT)
        self.frame = frame
        self.frame.set_keydown_handler(self.keyboard.keyDown)
        self.frame.set_keyup_handler(self.keyboard.keyUp)
        self.pickUp = PickUp(WIDTH, HEIGHT, 10000)
        self.wave = Wave(WIDTH, HEIGHT, 1, 20)
        self.obstacles = Obstacle(WIDTH, HEIGHT)
        self.explosions = []
        self.bullets = []
        self.enemies = []
        self.interaction = Interaction(self.player, self.pickUp)

        self.bulletLimit = 30

        self.frameTimer = simplegui.create_timer(1000, self.calcFPS)
        self.fps = 0
        self.frameCount = 0

        #set inGame to true
        self.inGame = True
        
        #start the wave
        self.wave.startWave()
        
        #start the fps timer
        self.frameTimer.start()

    def update(self):
        """Update the game state"""
        self.enemies = self.wave.getEnemies()
        if(self.player.getHealth() <= 0):
            self.inGame = False

        self.player.update(self.keyboard)
        if self.keyboard.space:
            b = self.player.fire()
            if b:
                self.bullets += b

        for i in self.enemies:
            if i.getType() == 'BigGnat':
                b = i.fire(self.player)
                if b:
                    self.bullets += b

        if self.keyboard.b:
            bomb = self.player.getBomb()
            if(bomb):
                if(bomb.getType() == 'Nail'):
                    self.bullets += self.player.dropBomb()
                else:    
                    self.explosions.append(self.player.dropBomb())

        for explosion in self.explosions:
            explosion.update()
            if explosion.shouldRemove():
               self.explosions.remove(explosion)

        for bullet in self.bullets:
            bullet.update()

        self.wave.update(self.player)
        self.pickUp.update(self.inGame)
        self.interaction.update(self.enemies, self.explosions, self.obstacles.getObstacles(), self.bullets);
       
        #limiting the number of bullets 
        if(len(self.bullets) > self.bulletLimit):
            self.bullets = self.bullets[len(self.bullets) - self.bulletLimit:] 

    def draw(self, canvas, inGame):
        self.frameCount += 1

        if(inGame):
            self.update()

        self.player.draw(canvas, self.keyboard, inGame)

        for bullet in self.bullets:
            bullet.draw(canvas)

        for explosion in self.explosions:
            explosion.draw(canvas)

        self.wave.draw(canvas)
        self.pickUp.draw(canvas)
        self.obstacles.draw(canvas)
        self.hud.draw(canvas, self.wave.getWave(), self.fps)

    def calcFPS(self):
        self.fps = self.frameCount
        self.frameCount = 0

    def getScore(self):
        return self.wave.getWave()

    def start(self):
        self.frame.start()

