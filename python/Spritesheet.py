try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# img = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png')
# width = img.get_width()
# height = img.get_height()


class Spritesheet():
    def __init__(self, img, columns, rows, radius, timer, oneshot):
        self.img = simplegui.load_image(img)
        self.columns = columns
        self.rows = rows
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.frameWidth = self.width / self.columns
        self.frameHeight = self.height / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.frameIndex = [0, 0]
        self.radius = radius
        self.clock = Clock()
        self.timer = timer
        self.done = False
        self.oneshot = oneshot

    def draw(self, canvas, position, rotation):
        #        self.img = simplegui.load_image(img)
        if not (self.done and self.oneshot):
            self.position = position
            self.rotation = rotation
            canvas.draw_image(
                self.img,  # image URL
                (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                self.frameHeight * self.frameIndex[1] + self.frameCentreY),  # center_source
                (self.frameWidth, self.frameHeight),  # width_height_source
                self.position.getP(),  # center_dest
                (self.radius * 7, self.radius * 7),  # width_height_dest
                self.rotation / (180 / math.pi)  # rotation
            )

    def update(self, canvas, position, rotation):
        if not (self.done and self.oneshot):
            self.clock.tick()
            if self.clock.transition(self.timer):
                self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns
                if self.frameIndex[0] == 0:
                    self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows
                    if self.frameIndex[1] == 0 and self.oneshot:
                        self.done = True
            self.draw(canvas, position, rotation)


class Clock():
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frameDuration):
        return self.time % frameDuration == 0
