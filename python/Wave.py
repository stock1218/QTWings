from Gnat import Gnat
from Vector import Vector
import random

class Wave:

    def __init__(self, width, height, wave, limit):
        self.width = width
        self.height = height
        self.wave = 0
        self.nonActiveEnemies = []
        self.enemies = []
        self.isOn = False
        self.gnatLimit = limit

    def getWave(self):
        return self.wave

    def startWave(self):
        #populate enemies and start the wave
        self.isOn = True
        totalGnats = 5 * self.wave

        for i in range(totalGnats):
            self.nonActiveEnemies.append(self.addGnat())

    def update(self, player):
        if(self.isOn):
            #check if the wave is over, then start a new one
            #also update all the enemies 
            if len(self.enemies) == 0:
                self.wave += 1
                self.startWave()

            for i in self.enemies:
                i.update(player)

            self.enemies.append

            while len(self.enemies) < self.gnatLimit and len(self.nonActiveEnemies) > 0:
                self.enemies.append(self.nonActiveEnemies.pop())

    def draw(self, canvas):
        #draw all the enemies
        for i in self.enemies:
            i.draw(canvas)

    def addGnat(self): 
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
                
        return Gnat(
            Vector(spawnX, spawnY),
            Vector(1,1),
            0.2,
            2,
            1,
            6
        )

    def getEnemies(self):
        #get the enemies so for interaction
        return self.enemies
