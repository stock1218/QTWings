try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Game import Game

WIDTH = 1600
HEIGHT = 1200

'''
states:
    0 = Title
    1 = Game
    2 = GameOver
'''
state = 0
textColor = 'Red'

frame = simplegui.create_frame("QTWings", WIDTH, HEIGHT)
game = Game(WIDTH, HEIGHT, frame)

def drawTitle(canvas):

    title = "QT Wings"
    titleSize = 40
    subtitle = "Click the button to start a game"
    subtitleSize = 20
    margin = frame.get_canvas_textwidth(title, titleSize)/2 
    canvas.draw_text(title, (WIDTH/2 - margin, HEIGHT/2), titleSize, textColor)
    
    margin = frame.get_canvas_textwidth(subtitle, subtitleSize)/2 
    canvas.draw_text(subtitle, (WIDTH/2 - margin, HEIGHT/2 + 40), subtitleSize, textColor)
    
def drawGame(frame, canvas):
    game.draw(canvas, True)
    if (not game.inGame):
        changeState()    

def drawGameOver(canvas):
    game.draw(canvas, False)
    text = "Game Over"
    textSize = 40
    subtext = "Click the button to return to the title screen"
    subtextSize = 20

    margin = frame.get_canvas_textwidth(text, textSize)/2 
    canvas.draw_text(text, (WIDTH/2 - margin, HEIGHT/2), textSize, textColor)
    
    margin = frame.get_canvas_textwidth(subtext, subtextSize)/2 
    canvas.draw_text(subtext, (WIDTH/2 - margin, HEIGHT/2 + 40), subtextSize, textColor)

def draw(canvas):
    if(state == 0):
        drawTitle(canvas)
    
    elif(state == 1):
        drawGame(frame, canvas)

    elif(state == 2):
        drawGameOver(canvas)

def changeState():
    global state, WIDTH, HEIGHT, frame, game

    #start a new game
    if state == 0:
        game = Game(WIDTH, HEIGHT, frame)

    state = (state + 1) % 3 


frame.set_draw_handler(draw)
frame.add_button("Start Game", changeState)
frame.start()