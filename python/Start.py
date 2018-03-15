try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Game import Game

WIDTH = 900
HEIGHT = 600

''' 
states:
    0 = Title
    1 = Game
    2 = GameOver
'''
state = 0
textColor = 'Red'
highScore = 0

frame = simplegui.create_frame("QTWings", WIDTH, HEIGHT)
game = Game(WIDTH, HEIGHT, frame)
button = None

def drawTitle(canvas):
    global highScore
    title = "QT Wings"
    titleSize = 40

    subtitle = "Click the button to start a game"
    subtitleSize = 20

    highScoreText = "High Score: " + str(highScore)
    highScoreTextSize = 20

    margin = frame.get_canvas_textwidth(title, titleSize)/2 
    canvas.draw_text(title, (WIDTH/2 - margin, HEIGHT/2), titleSize, textColor)
    
    margin = frame.get_canvas_textwidth(subtitle, subtitleSize)/2 
    canvas.draw_text(subtitle, (WIDTH/2 - margin, HEIGHT/2 + 40), subtitleSize, textColor)

    margin = frame.get_canvas_textwidth(highScoreText, highScoreTextSize)/2
    canvas.draw_text(highScoreText, (WIDTH/2 - margin, HEIGHT/2 + 80), highScoreTextSize, textColor)
    
def drawGame(frame, canvas):
    global state, highScore
    game.draw(canvas, True)
    if (not game.inGame):
        #change state to game over
        state = 2    
        button.set_text("Return to Title")
        if game.getScore() > highScore:
            highScore = game.getScore()

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
    global state, WIDTH, HEIGHT, frame, game, button

    #start a new game
    if state == 0:
        game = Game(WIDTH, HEIGHT, frame)
        button.set_text("End Game")
        state = 1
    
    else:
        button.set_text("Start Game")
        state = 0


button = frame.add_button("Start Game", changeState)
frame.set_draw_handler(draw)
frame.start()
