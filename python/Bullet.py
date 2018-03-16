class Bullet:
    def __init__(self, width, height, position, velocity, isGood):
        self.width = width
        self.height = height
        self.position = position
        self.velocity = velocity
        self.radius = 3
        self.damage = 1
        self.inCollision = None
        self.bounces = 0
        self.isGood = isGood

    def draw(self, canvas):
        if(self.isGood):
            canvas.draw_circle(self.position.getP(), self.radius, 1, "#00ff00", "#00ff00")
        else:
            canvas.draw_circle(self.position.getP(), self.radius, 1, 'Red', 'Red')

    def update(self):
        self.position += self.velocity

    def bounce(self, normal):
        self.velocity.reflect(normal)
        self.bounces += 1

    def getPos(self):
        return self.position

    def getRadius(self):
        return self.radius

    def getDamage(self):
        return self.damage

    def getType(self):
        return 'bullet'

    def isColliding(self, obj):
        return (obj.getPos() - self.position).length() <= self.radius + obj.getRadius()

    def outOfBounds(self):
        return (self.position.x < 0) or (self.position.x > self.width) or (self.position.y < 0) or (self.position.y > self.height)
