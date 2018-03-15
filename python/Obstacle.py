try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Box import Box
from Vector import Vector
from random import randrange


class Obstacle:

    def __init__(self, width, height):
        self.obstacles = []
        for i in range(10):
            size = randrange(50,70)
            self.obstacles.append(Box(
                Vector(randrange(0, width), randrange(0, height)), 
                size,
                size))
        self.sprite = simplegui.load_image("https://i.imgur.com/JWaXkha.png")

    def getObstacles(self):
        return self.obstacles

    def draw(self, canvas):
        for i in self.obstacles:
            # canvas.draw_polygon(i.points, i.thickness, 'White', 'White')
            canvas.draw_image(self.sprite, (self.sprite.get_width() / 2, self.sprite.get_height() / 2),
                              (self.sprite.get_width(), self.sprite.get_height()),
                              ((i.points[1][0] - ((i.points[1][0] - i.points[0][0]) / 2),
                                (i.points[3][1] - ((i.points[3][1] - i.points[0][1]) / 2)))),
                              ((i.points[1][0] - i.points[0][0] + 1), (i.points[3][1] - i.points[0][1] + 1)))

            #i.draw(canvas)
