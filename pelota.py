import pygame
from random import randint

BLACK = (0, 0, 0)


class Pelota(pygame.sprite.Sprite):
    height = 0

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        height = height
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def getRect(self):
        return self.rect.y

    def getSize(self):
        return self.height

    def moveBall(self, ballDirX, ballDirY):
        self.rect.x += ballDirX * 5
        self.rect.y += ballDirY * 5