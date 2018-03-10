from Gnat import Gnat
from Vector import Vector
import random

class Wave:

    def __init__(self, width, height, wave):
        self.width = width
        self.height = height
        self.wave = 1
        self.enemies = []

    def getWave(self):
        return self.wave

    def startWave(self):
        #populate enemies and start the wave
        for i in range(self.wave):
            gnats = 5 * self.wave

        #add Gnats
        for g in range(gnats):

            edge = random.choice(['top', 'bottom', 'left', 'right'])

            if(edge == 'top'):
                spawnX = random.randrange(0, self.width)
                spawnY = random.randrange(-500, -100)

            elif(edge == 'bottom'):
                spawnX = random.randrange(0, self.width)
                spawnY = random.randrange(self.height + 100, self.height + 500)

            elif(edge == 'left'):
                spawnX = random.randrange(-500, -100)
                spawnY = random.randrange(0, self.width)
  
            else:
                spawnX = random.randrange(self.width + 100, self.width + 500)
                spawnY = random.randrange(0, self.width) 
                
            self.enemies.append(Gnat(
                Vector(spawnX, spawnY),
                Vector(1,1),
                0.2,
                2,
                1,
                6
            ))
            

    def update(self, player):
        #check if the wave is over, then start a new one
        #also update all the enemies 
        if len(self.enemies) == 0:
            self.wave += 1
            self.startWave()

        for i in self.enemies:
            i.update(player)

    def draw(self, canvas):
        #draw all the enemies
        for i in self.enemies:
            i.draw(canvas)

    def getEnemies(self):
        #get the enemies so for interaction
        return self.enemies
