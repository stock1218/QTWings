from Vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Shield:
      
    def __init__(self):
        self.health = 3
        self.radius = 30
        self.duration = 10
        self.isDone = False

    def draw(self, canvas, pos):
        canvas.draw_circle(pos.getP(), self.radius, 1, 'White')
   
    def tick(self):
       print("Time Left: " + str(self.duration))
       self.duration -= 1
       if(self.duration <= 0):
           self.isDone = True

    def getRadius(self):
        return self.radius
 
    def status(self):
        return self.isDone
