import pygame
from settings import *
pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load('image/backgr_1.jpg')
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

class Face(pygame.sprite.Sprite):
    def __init__(self):
        super(Face, self).__init__()

        self.image = pygame.image.load('image/bl_face.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112


class Mouth(pygame.sprite.Sprite):
    def __init__(self):
        super(Mouth, self).__init__()
        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112
    # Mouthes = {'1': ('image/Mouth_monc.png', HEIGHT, 100, 120),
    #            '2': ('image/Mouth_AC.png', HEIGHT, 100, 120),
    #            '3': ('image/Mouth_kerry.png', HEIGHT, 100, 120),
    #            '4': ('image/Mouth_SHK.png', HEIGHT, 100, 120)}
    #
    # def __init__(self):
    #     super(Mouth, self).__init__()
    #     self.image = pygame.image.load(the_way)
    #     self.rect = self.image.get_rect()
    #     self.rect.bottom = rect_bottom
    #     self.rect.top = rect_top
    #     self.rect.left = rect_left

    def create_m(the_way, rect_bottom, rect_top, rect_left):
        return self

    def speak(self):
        pass

    def eat(self):
        pass

class Mouth_AC(Mouth):
    def __init__(self):
        super(Mouth_AC, self).__init__()

        self.image = pygame.image.load('image/Mouth_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 200
        self.rect.left = 112

class Mouth_kerry(Mouth):
    def __init__(self):
        super(Mouth_kerry, self).__init__()

        self.image = pygame.image.load('image/Mouth_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

class Mouth_monc(Mouth):
    def __init__(self):
        super(Mouth_monc, self).__init__()

        self.image = pygame.image.load('image/Mouth_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

class Mouth_SHK(Mouth):
    def __init__(self):
        super(Mouth_SHK, self).__init__()

        self.image = pygame.image.load('image/Mouth_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112


class Nose(pygame.sprite.Sprite):
    def __init__(self):
        super(Nose, self).__init__()

        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

    def smell(self):
        pass

class Nose_AC(Nose):
    def __init__(self):
        super(Nose_AC, self).__init__()

        self.image = pygame.image.load('image/Nose_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 112
        self.rect.left = 112

class Nose_monc(Nose):
    def __init__(self):
        super(Nose_monc, self).__init__()

        self.image = pygame.image.load('image/Nose_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

class Nose_SHK(Nose):
    def __init__(self):
        super(Nose_SHK, self).__init__()

        self.image = pygame.image.load('image/Nose_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 90

class Nose_kerry(Nose):
    def __init__(self):
        super(Nose_kerry, self).__init__()

        self.image = pygame.image.load('image/Nose_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112


class Eyes(pygame.sprite.Sprite):
    def __init__(self):
        super(Eyes, self).__init__()

        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 95
        self.rect.left = 95

    def close(self):
        pass

class Eyes_monc(Eyes):
    def __init__(self):
        super(Eyes_monc, self).__init__()

        self.image = pygame.image.load('image/Eyes_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 95
        self.rect.left = 95

class Eyes_SHK(Eyes):
    def __init__(self):
        super(Eyes_SHK, self).__init__()

        self.image = pygame.image.load('image/Eyes_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 95
        self.rect.left = 92

class Eyes_AC(Eyes):
    def __init__(self):
        super(Eyes_AC, self).__init__()

        self.image = pygame.image.load('image/Eyes_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 112
        self.rect.left = 98

class Eyes_kerry(Eyes):
    def __init__(self):
        super(Eyes_kerry, self).__init__()

        self.image = pygame.image.load('image/Eyes_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 120
        self.rect.left = 112


class EBrows(pygame.sprite.Sprite):
    def __init__(self):
        super(EBrows, self).__init__()

        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 140

    def emo(self):
        pass

class EBrows_monc(EBrows):
    def __init__(self):
        super(EBrows_monc, self).__init__()

        self.image = pygame.image.load('image/EBrows_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 140

class EBrows_AC(EBrows):
    def __init__(self):
        super(EBrows_AC, self).__init__()

        self.image = pygame.image.load('image/EBrows_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 20
        self.rect.left = 270

class EBrows_SHK(EBrows):
    def __init__(self):
        super(EBrows_SHK, self).__init__()

        self.image = pygame.image.load('image/EBrows_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 92

class EBrows_kerry(EBrows):
    def __init__(self):
        super(EBrows_kerry, self).__init__()

        self.image = pygame.image.load('image/EBrows_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 120

class Ears(pygame.sprite.Sprite):
    def __init__(self):
        super(Ears, self).__init__()

        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 120
        self.rect.left = 112

class Ears_monc(Ears):
    def __init__(self):
        super(Ears_monc, self).__init__()

        self.image = pygame.image.load('image/Ears_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 120
        self.rect.left = 112

class Ears_SHK(Ears):
    def __init__(self):
        super(Ears_SHK, self).__init__()

        self.image = pygame.image.load('image/Ears_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112

class Ears_AC(Ears):
    def __init__(self):
        super(Ears_AC, self).__init__()

        self.image = pygame.image.load('image/Ears_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 120
        self.rect.left = 105

class Ears_kerry(Ears):
    def __init__(self):
        super(Ears_kerry, self).__init__()

        self.image = pygame.image.load('image/Ears_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 120
        self.rect.left = 112


class Hair(pygame.sprite.Sprite):
    def __init__(self):
        super(Hair, self).__init__()

        self.image = pygame.image.load('image/bl.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 50
        self.rect.left = 97


class Hair_monc(Hair):
    def __init__(self):
        super(Hair_monc, self).__init__()

        self.image = pygame.image.load('image/Hair_monc.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 45
        self.rect.left = 95

class Hair_AC(Hair):
    def __init__(self):
        super(Hair_AC, self).__init__()

        self.image = pygame.image.load('image/Hair_AC.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 70
        self.rect.left = 112

class Hair_SHK(Hair):
    def __init__(self):
        super(Hair_SHK, self).__init__()

        self.image = pygame.image.load('image/Hair_SHK.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 70
        self.rect.left = 97

class Hair_kerry(Hair):
    def __init__(self):
        super(Hair_kerry, self).__init__()

        self.image = pygame.image.load('image/Hair_kerry.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.top = 100
        self.rect.left = 112
