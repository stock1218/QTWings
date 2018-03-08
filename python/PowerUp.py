try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 
import random

class PowerUp:
    
    def __init__(self):
        """Construct PowerUp"""
        self.type = randchoice(['God Mode', 'Shield'])
        
    

    def draw(canvas):
         canvas.draw_circle((self.margin-(i*30), 20), 9, 1, 'Red', 'Red') 
