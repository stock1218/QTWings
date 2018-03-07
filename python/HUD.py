try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class HUD:
    """Class responsible for displaying the HUD of the game"""

    def __init__(self, player, width, height):
        self.player = player
        self.margin = width-20
        self.height = height

    def draw(self, canvas, wave):
        for i in range(self.player.getHealth()):
            """-n is an initial offset and *n is the space between each health unit"""
            canvas.draw_circle((self.margin-(i*30), 20), 9, 1, "#0000ff", "#0000ff")

        """only supports waves 1- 9999 due to self.margin-60"""
        canvas.draw_text('WAVE: ' + str(wave), (self.margin - 60, 60), 12, 'Red')
