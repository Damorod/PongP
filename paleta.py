import pygame

BLACK = (0, 0, 0)


class Paleta(pygame.sprite.Sprite):
    height = 0
    def __init__(self, color, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        height = height
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels, tam):
        self.rect.y += pixels
        if self.rect.y > tam - 100:
            self.rect.y = tam - 100

    def getHeight(self):
        return self.height

