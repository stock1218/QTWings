from Vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Shield:
      
    def __init__(self):
        self.health = 3
        self.radius = 30
        self.isDone = False

    def draw(self, canvas, pos):
        canvas.draw_circle(pos.getP(), self.radius, 1, 'rgba(0, 255, 0, 0.3)', 'rgba(0, 255, 0, 0.3)')
   
    def tick(self):
       if(self.health <= 0):
           self.isDone = True

    def getRadius(self):
        return self.radius
 
    def getStatus(self):
        return self.isDone

    def damage(self, amount):
        self.health -= amount
        print("SHIELD HEALTH: " + str(self.health))
