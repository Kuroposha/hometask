import pygame, sys
from pygame.locals import *
from settings import *
from game_objects import *
from menu import *

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE,0,32)

pygame.display.set_caption("Face Mader");

bgColor = (GRAY)


backgroun = Background()
face = Face()
mouth = Mouth()
nose = Nose()
eyes = Eyes()
e_brows = EBrows()
ears = Ears()
hair = Hair()
menu = Menu()
i = 0
mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mouthes = [Mouth_AC(), Mouth_SHK(), Mouth_monc(), Mouth_kerry()]
                mouth = mouthes[i]
                i += 1
                if i == 4:
                    i = 0
            elif event.key == pygame.K_2:
                noses = [Nose_AC(), Nose_SHK(), Nose_monc(), Nose_kerry()]
                nose = noses[i]
                i += 1
                if i == 4:
                    i = 0
            elif event.key == pygame.K_3:
                eyeses = [Eyes_AC(), Eyes_SHK(), Eyes_monc(), Eyes_kerry()]
                eyes = eyeses[i]
                i += 1
                if i == 4:
                    i = 0
            elif event.key == pygame.K_4:
                e_browses = [EBrows_AC(), EBrows_SHK(), EBrows_monc(), EBrows_kerry()]
                e_brows = e_browses[i]
                i += 1
                if i == 4:
                    i = 0
            elif event.key == pygame.K_5:
                earses = [Ears_AC(), Ears_SHK(), Ears_monc(), Ears_kerry()]
                ears = earses[i]
                i += 1
                if i == 4:
                    i = 0
            elif event.key == pygame.K_6:
                haires = [Hair_AC(), Hair_SHK(), Hair_monc(), Hair_kerry()]
                hair = haires[i]
                i += 1
                if i == 4:
                    i = 0
            # if event.type == MOUSEBUTTONDOWN:
            #     ears.rect.top = 130
            #     ears.rect.left = 112
            #
            # if event.type == MOUSEBUTTONUP:
            #     ears.rect.top = 110
            #     ears.rect.left = 112
    screen.fill(bgColor)

    screen.blit(backgroun.image, backgroun.rect)
    screen.blit(face.image, face.rect)
    # game.menu()
    screen.blit(mouth.image, mouth.rect)
    screen.blit(nose.image, nose.rect)
    screen.blit(eyes.image, eyes.rect)
    screen.blit(e_brows.image, e_brows.rect)
    screen.blit(ears.image, ears.rect)
    screen.blit(hair.image, hair.rect)
    Menu.draw_menu(screen)
    # for key in Mouth().Mouthes:
    #     value = value
    # Mouth.create_m(Mouth().Mouthes)

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
