import pygame, sys
from pygame.locals import *
from settings import *
# from main import screen
# helloText = "Hello, my little friends. My name is Prosessor Dowell. Help me find my face!"
# (x,y,fontSize) = (10,40,40)
# myFont = pygame.font.SysFont("None", fontSize)
# fontColor = (BLUE)
# fontImage = myFont.render(helloText, 0, (fontColor))

# #punkts = [(10, 10, u'Game', PINK, PURP, 0),
#           (10, 60, u'Mouth', PINK, PURP, 1),
#           (10, 110, u'Nose', PINK, PURP, 2),
#           (10, 160, u'Eyes', PINK, PURP, 3),
#           (10, 210, u'Eye Brows', PINK, PURP, 4),
#           (10, 260, u'Ears', PINK, PURP, 5),
#           (10, 310, u'Hair', PINK, PURP, 6),
#           (10, 360, u'QUIT', PINK, PURP, 7)]

class Menu(object):
    # def __init__(self, punkts = [10, 10, u'Punkt', PINK, PURP]):
    #     self.punkts = punkts
    #
    # def render(self, space, font, num_punkt):
    #     for i in self.punkts:
    #         if num_punkt == i[5]:
    #             space.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
    #         else:
    #             space.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    #
    # def menu(self):
    #     done = True
    #     font_menu = pygame.font.SysFont("None", 20)
    #     punkt = 0
    #     while done:
    #         screen.fill((0, 100, 200))
    #
    #         mp = pygame.mouse.get_pos()
    #         for i in self.punkts:
    #             if mp[0]>i[0] and mp[0]<i[0]+100 and mp[1]>i[1] and mp[1]<i[1]+40:
    #                 punkt = i[5]
    #         self.render(screen, font_menu, punkt)
    #
    #         for e in pygame.event.get():
    #             if e.type == pygame.QUIT:
    #                 sys.exit()
    #             if e.type == pygame.KEYDOWN:
    #                 if e.key == pygame.KESCAPE:
    #                     sys.exit()
    #                 if e.key == pygame.K_UP:
    #                     if punkt > 0:
    #                         punkt -= 1
    #                     # else:
    #                     #     punkt == 7
    #                 if e.key == pygame.K_DOWN:
    #                     if punkt < len(self.punkts)-1:
    #                         punkt += 1
    #                     # else:
    #                     #     punkt = 1
    #             if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
    #                 if punkt == 0:
    #                     done = False
    #                 elif punkt == 1:
    #                     pass
    #                 elif punkt == 2:
    #                     pass
    #                 elif punkt == 3:
    #                     pass
    #                 elif punkt == 4:
    #                     pass
    #                 elif punkt == 5:
    #                     pass
    #                 elif punkt == 6:
    #                     pass
    #                 else:
    #                     sys.exit()

    def draw_menu(surf):
        rect_m_size = Rect((10,10),(100,40))
        rect_n_size = Rect((10,60),(100,40))
        rect_e_size = Rect((10,110),(100,40))
        rect_b_size = Rect((10,160),(100,40))
        rect_ea_size = Rect((10,210),(100,40))
        rect_h_size = Rect((10,260),(100,40))
        rect_width = 0
        pygame.draw.rect(surf, PURP, rect_m_size, rect_width)
        pygame.draw.rect(surf, PURP, rect_n_size, rect_width)
        pygame.draw.rect(surf, PURP, rect_e_size, rect_width)
        pygame.draw.rect(surf, PURP, rect_b_size, rect_width)
        pygame.draw.rect(surf, PURP, rect_ea_size, rect_width)
        pygame.draw.rect(surf, PURP, rect_h_size, rect_width)

    # def change_mouth(self):
    #     if event.type == MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             for key in MOUTHES:
    #                 yield value
