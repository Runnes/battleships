import pygame
import sys
import gamemodes

def play_again_pygame():
    pygame.init() # initializing the constructor
    res = (1920, 1080) # screen resolution
    screen = pygame.display.set_mode(res) # opens up a window
    color = (255, 255, 255)# white color
    color_light = (170, 170, 170)# light shade of the button
    color_dark = (100, 100, 100) # dark shade of the button
    width = screen.get_width()
    battleship_1 = pygame.image.load('battleshipjpg.jpg')


    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 50)# defining a font
    text = smallfont.render('quit', True, color)

    while True:

        x1=width/6
        y1=height/6
        x2=width/6 + 140
        y2=height/6 + 40

        x1_2 = width - width/6
        x2_2 = width - width/6 + 140
        y1_2= height - height/6
        y2_2 = height - height/6 + 40

        #print(x1, x2, y1, y2)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN: # checks if a mouse is clicked
                if x1_2 - x1_2/6 <= mouse[0] <= x1_2 - x1_2/6+300 and y1_2-y1_2/6 <= mouse[1] <= y1_2-y1_2/6+100:                    # if the mouse is clicked on the button
                    pygame.quit()
                    sys.exit()  # pygame quit wywalalo jakis maly blad


                    # pygame.quit() #  the game is terminated
                    # sys.exit() # pygame quit wywalalo jakis maly blad
                if x1_2 / 6 <= mouse[0] <= x1_2 / 6 + 300 and y1_2 - y1_2 / 6 <= mouse[1] <= y1_2 - y1_2 / 6 + 100:  # if the mouse is clicked on the button
                    pygame.quit()  # the game is terminated
                    gamemodes.main()

        screen.fill((107, 107, 107))
        mouse = pygame.mouse.get_pos()

        #if mouse is hovered on a button it changes to lighter shade
        #nie ma zadnego rectangla - on rysuje rectangla pierwszego jesli mouse jest na tym polu w pygame.draw, jak nie jest to rysuje z else

        # if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y1:
        #     pygame.draw.rect(screen, color_light, [x1, y1, 140, 40])
        #     pygame.draw.rect(screen,(0,0,0),[10,20,30,40])
        #
        # else:
        #     pygame.draw.rect(screen, color_dark, [x1, y1, 140, 40])
        #pygame.draw.rect(screen,(0,0,0),[x1,x2,300,100])

        pygame.draw.rect(screen,(0,255,0),pygame.Rect(x1_2/6,y1_2-y1_2/6,300,100))
        pygame.draw.rect(screen,(0,255,0),[x1_2-x1_2/6,y1_2-y1_2/6,300,100])
        screen.blit(smallfont.render('Play', True, (0,0,0)),(x1_2/6+100,y1_2-y1_2/6+30))
        screen.blit(smallfont.render("Exit",True,(0,0,0)),(x1_2-x1_2/6+100,y1_2-y1_2/6+30))
        screen.blit(smallfont.render("Developed by ", True, color),(width-350,height-150))
        screen.blit(smallfont.render("Karol Workowski", True, color),(width-350,height-50))
        pygame.display.set_caption('Battleships')
        screen.blit(battleship_1,(width/3,0))
        #battleship_1 = pygame.transform.scale(screen, (1920, 1080))
        pygame.display.update()



play_again_pygame()



def battleships_pygame():
    pygame.init() # initializing the constructor
    res = (1920, 1080) # screen resolution
    screen = pygame.display.set_mode(res) # opens up a window
    color = (255, 255, 255)# white color
    color_light = (170, 170, 170)# light shade of the button
    color_dark = (100, 100, 100) # dark shade of the button
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 50)# defining a font

