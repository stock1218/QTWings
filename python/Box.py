try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Box:

    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.draw_polygon([self.pos.getP(), (self.pos.x + self.width, self.pos.y), (self.pos.x + self.width, self.pos.y + self.height), (self.pos.x, self.pos.y + self.height)], 1, 'Blue', 'White')
