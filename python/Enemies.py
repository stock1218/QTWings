from Vector import Vector
from Enemy import Enemy

class Enemies:
    def __init__(self, player):
        self.enemies = []
        self.inCollision = set([])
        self.player = player

    def collide(self, e1, e2):
        d = e2.position - e1.position #vector from e1 to e2
        n = d.getNormalized() #Unit vector in that direction

        e1c = n * e1.velocity.dot(n) #velocity e1 in collision axis
        e2c = n * e2.velocity.dot(n) #velocity e2 in collision axis

        e1p = e1.velocity - e1c #velocity e1 perpendicular to collision axis
        e2p = e2.velocity - e2c #velocity e2 perpendicular to collision axis

        e1prime = (e2c) + e1p #new velocity e1
        e2prime = (e1c) + e2p #new velocity e2
        e1.velocity = e1prime
        e2.velocity = e2prime
    def draw(self, canvas):
        for e in self.enemies:
            e.seekObject(self.player)
        self.update()
        for enemy in self.enemies:
            enemy.update(self.player)
            enemy.draw(canvas)

    def update(self):
        for e1 in self.enemies:
            for e2 in self.enemies:
                if e1.hit(e2) and (e1.position != e2.position):
                    print("COLLISION DETECTED")
                    e1e2 = (e1, e2) in self.inCollision
                    e2e1 = (e2, e1) in self.inCollision
                    if not (e1e2 or e2e1):
                        self.collide(e1, e2)
                        self.inCollision.add((e1, e2))
                else:
                    self.inCollision.discard((e1, e2))
                    self.inCollision.discard((e2, e1))


    def removeEnemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
