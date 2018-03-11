class Bullet:
    def __init__(self, width, height, position, velocity):
        self.width = width
        self.height = height
        self.position = position
        self.velocity = velocity
        self.radius = 3
        self.damage = 1
        self.inCollision = False

    def draw(self, canvas):
        canvas.draw_circle(self.position.getP(), self.radius, 1, "#00ff00", "#00ff00")

    def update(self):
        self.position += self.velocity

    def bounce(self, normal):
        self.velocity.reflect(normal)

    def getPos(self):
        return self.position

    def getRadius(self):
        return self.radius

    def getDamage(self):
        return self.damage

    def outOfBounds(self):
        return (self.position.x < 0) or (self.position.x > self.width) or (self.position.y < 0) or (self.position.y > self.height)
