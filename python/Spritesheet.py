import simplegui

# img = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png')
# width = img.get_width()
# height = img.get_height()


class Spritesheet():
    def __init__(self, img, columns, rows):
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

    def draw(self, canvas):
        #        self.img = simplegui.load_image(img)

        canvas.draw_image(
            self.img,  # image URL
            (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
             self.frameHeight * self.frameIndex[1] + self.frameCentreY),  # center_source
            (self.frameWidth, self.frameHeight),  # width_height_source
            (self.frameWidth / 2, self.frameHeight / 2),  # center_dest
            (self.frameWidth, self.frameHeight)  # width_height_dest
        )

    def update(self, canvas):
        self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns
        if self.frameIndex[0] == 0:
            self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows
        self.draw(canvas)


class Clock():
    def __init__(self, time):
        self.time = time

    def tick(self):
        self.time += 1

    def transition(self, frameDuration):
        return (self.time % frameDuration == 0)
