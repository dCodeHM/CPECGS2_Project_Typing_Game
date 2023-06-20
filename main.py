import pygame, sys                                      #to open the pygame consol/cmd
from button import Button

pygame.init()                                           #pygame initialize

width = 1500
height = 780
scrRatio = pygame.display.set_mode((width, height))        #default ration for monitors or displays
background = pygame.image.load("assets/z.png")
background =pygame.transform.scale(background, (width, height))
pygame.display.set_caption("Type it faster daddy!")     #for the name in the tkinter
icon = pygame.image.load("assets/icon.png")             #for the icon in the tkinter

pygame.display.set_icon(icon)                           #for the icon in the tkinter

def get_font(size):                                     #callout the font and specific font sie depending on the display ratio
    return pygame.font.Font("assets/smoothpixel.ttf", size)

text_font = pygame.font.Font("assets/smoothpixel.ttf", 45)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    scrRatio.blit(img, (x, y))

def speeditfaster():  #NOT YET FINISHED #this is the main game loop
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        scrRatio.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        scrRatio.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(900, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        backgroundplay = pygame.image.load("assets/pixel1.png")
        scrRatio.blit(backgroundplay, (0,0))
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(scrRatio)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        
def playMenu():             #DONE                        #callout the Play Button
    while True:
        pmenuPos = pygame.mouse.get_pos()
        scrRatio.fill("black")
        
        playbackButton = Button(image = pygame.image.load("assets/aboutbox.png"), pos=(160, 700), 
                            text_input="BACK", font=get_font(35), base_color="#d5e3e6", hovering_color="yellow")
        wordbackButton = Button(image = pygame.image.load("assets/tbox.png"), pos=(550, 450), 
                            text_input="WORD", font=get_font(35), base_color="#d5e3e6", hovering_color="red")
        phrasebackButton = Button(image = pygame.image.load("assets/tbox.png"), pos=(950, 450), 
                            text_input="PHRASE", font=get_font(35), base_color="#d5e3e6", hovering_color="red")
        
        backgroundplay = pygame.image.load("assets/great.png")
        scrRatio.blit(backgroundplay, (0,0))
        
        playmenuTextbg = get_font(100).render("Please Choose Game Type", True, "black")
        playmenuRectanglebg = playmenuTextbg.get_rect(center=(750, 250))
        playmenuText = get_font(100).render("Please Choose Game Type", True, "#4262e3")
        playmenuRectangle = playmenuText.get_rect(center=(755, 245))
        scrRatio.blit(playmenuTextbg, playmenuRectanglebg)
        scrRatio.blit(playmenuText, playmenuRectangle)
        
        wordbackButton.changeColor(pmenuPos)
        phrasebackButton.changeColor(pmenuPos)
        playbackButton.changeColor(pmenuPos)
        playbackButton.update(scrRatio)
        wordbackButton.update(scrRatio)
        phrasebackButton.update(scrRatio)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wordbackButton.checkForInput(pmenuPos):
                    speeditfaster()
                #if phrasebackButton.checkForInput(menumousePos):
                    #minigame()
                if playbackButton.checkForInput(pmenuPos):
                    main_menu()
        pygame.display.update()

def minigame():
    while True:
        mnPos = pygame.mouse.get_pos()
        scrRatio.fill("black")
        
        mnbackbutton = Button(image = pygame.image.load("assets/aboutbox.png"), pos=(160, 700), 
                            text_input="BACK", font=get_font(35), base_color="#d5e3e6", hovering_color="yellow")
        wordmnbackbutton = Button(image = pygame.image.load("assets/aboutbox.png"), pos=(550, 450), 
                            text_input="WORD", font=get_font(35), base_color="#d5e3e6", hovering_color="red")
        phrasemnbackbutton = Button(image = pygame.image.load("assets/aboutbox.png"), pos=(950, 450), 
                            text_input="PHRASE", font=get_font(35), base_color="#d5e3e6", hovering_color="red")
        
        backgroundmn = pygame.image.load("assets/pixel.png")
        scrRatio.blit(backgroundmn, (0, -50))
        
        mnText1 = get_font(100).render("Please Choose Game Type", True, "black")
        mnRectangle1 = mnText1.get_rect(center=(750,250))
        mnText2 = get_font(100).render("Please Choose Game Type", True, "#fc2845")
        mnRectangle2 = mnText2.get_rect(center=(755,245))
        mnText3 = get_font(50).render("Note: Mini-game does not have a time limit.", True, "black")
        mnRectangle3 = mnText3.get_rect(center=(750,330))
        mnText4 = get_font(50).render("Note: Mini-game does not have a time limit.", True, "#e67402")
        mnRectangle4 = mnText4.get_rect(center=(750,325))
        scrRatio.blit(mnText1, mnRectangle1)
        scrRatio.blit(mnText2, mnRectangle2)
        scrRatio.blit(mnText3, mnRectangle3)
        scrRatio.blit(mnText4, mnRectangle4)
        
        
        mnbackbutton.changeColor(mnPos)
        wordmnbackbutton.changeColor(mnPos)
        phrasemnbackbutton.changeColor(mnPos)
        mnbackbutton.update(scrRatio)
        wordmnbackbutton.update(scrRatio)
        phrasemnbackbutton.update(scrRatio)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mnbackbutton.checkForInput(mnPos):
                    main_menu()
        pygame.display.update()
        
def about():
    while True:
        aboutPos = pygame.mouse.get_pos()
        scrRatio.fill("#757001")
        
        backgroundmn = pygame.image.load("assets/pixel2.png")
        scrRatio.blit(backgroundmn, (0, 0))
        
        
        aboutbackButton = Button(image = pygame.image.load("assets/aboutbox.png"), pos=(160, 705), text_input="BACK", font=get_font(35), base_color="#d5e3e6", hovering_color="Red")
        aboutdialogBox = Button(image = pygame.image.load("assets/yellowbox.png"), pos=(750, 450), text_input="", font=get_font(35), base_color="#d5e3e6", hovering_color="Red")
        aboutbackText = Button(image = pygame.image.load("assets/adjustscroll.png"), pos=(750, 110), text_input="About the Game", font=get_font(35), base_color="#e69b00", hovering_color="Red")
        
        aboutbackButton.changeColor(aboutPos)
        aboutbackText.update(scrRatio)
        aboutdialogBox.update(scrRatio)
        aboutbackButton.update(scrRatio)
        
        draw_text("       Type it Faster Daddy is a Typing Game where", text_font, (0,0,0), 290, 320)
        draw_text("         players can type as fast as they can", text_font, (0,0,0), 290, 370)
        draw_text("     within a time limit. There will be two options", text_font, (0,0,0), 290, 420)
        draw_text("                     to choose from whether to", text_font, (0,0,0), 290, 470)
        draw_text("                 type per word or per sentence.", text_font, (0,0,0), 290, 520)
        draw_text("", text_font, (0,0,0), 290, 540)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if aboutbackButton.checkForInput(aboutPos):
                    main_menu()
        pygame.display.update()
             
def main_menu():               #DONE       
    while True:
        scrRatio.blit(background, (0,0))
        
        menumousePos = pygame.mouse.get_pos()
    
        menuText = get_font(160).render("Speed it Faster Daddy!", True, "black")
        menuRectangle = menuText.get_rect(center=(750, 145))
        menuTextbg = get_font(160).render("Speed it Faster Daddy!", True, "#eeff3d")
        menuRectanglebg = menuTextbg.get_rect(center=(745, 140))
        
        pMenuButton = Button(image = pygame.image.load("assets/tbox.png"), pos = (750, 320), text_input="PLAY", font=get_font(70), base_color= "#FAF5D5", hovering_color= "Light Green",)
        miniButton = Button(image = pygame.image.load("assets/tbox.png"), pos = (750, 440), text_input="MINI-GAME", font=get_font(50), base_color= "#FAF5D5", hovering_color= "Light Blue")
        aboutButton = Button(image = pygame.image.load("assets/tbox.png"), pos = (750, 560), text_input="ABOUT", font=get_font(50), base_color= "#FAF5D5", hovering_color= "Yellow")
        quitButton = Button(image = pygame.image.load("assets/tbox.png"), pos = (750, 680), text_input="QUIT", font=get_font(50), base_color= "#FAF5D5", hovering_color= "Red")
        
        scrRatio.blit(menuText, menuRectangle)
        scrRatio.blit(menuTextbg, menuRectanglebg)
        
        for button in [pMenuButton, miniButton, aboutButton, quitButton]:
            button.changeColor(menumousePos)
            button.update(scrRatio)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pMenuButton.checkForInput(menumousePos):
                    playMenu()
                if miniButton.checkForInput(menumousePos):
                    minigame()
                if aboutButton.checkForInput(menumousePos):
                    about()
                if quitButton.checkForInput(menumousePos):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
main_menu()


