import random
import pygame
import time
import threading
from paleta import Paleta
from pelota import Pelota

pygame.init()


class test():
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 2, 1024)

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    GREY = (220, 220, 220)

    size = (0, 0)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    w = pygame.Surface.get_width(screen)
    h = pygame.Surface.get_height(screen)

    golpePaleta = pygame.mixer.Sound('paleta.ogg')
    golpePaed = pygame.mixer.Sound('pared.ogg')
    punto = pygame.mixer.Sound('punto.ogg')

    paletaA = Paleta(RED, 10, 100)
    paletaA.rect.x = 20
    paletaA.rect.y = int(h / 2) - 50

    paletaB = Paleta(BLUE, 10, 100)
    paletaB.rect.x = w - 30
    paletaB.rect.y = int(h / 2) - 50

    pelota = Pelota(GREEN, 30, 30)
    pelota.rect.x = int(w / 2) - 15
    pelota.rect.y = int(h / 2) - 15

    ballDirX = -1
    ballDirY = -1

    pygame.display.set_caption("Pong Fer")

    lista_sprites = pygame.sprite.Group()

    lista_sprites.add(paletaA)
    lista_sprites.add(paletaB)
    lista_sprites.add(pelota)

    clock = pygame.time.Clock()

    juegoOn = True

    asd = ""

    puntosA = 0
    puntosB = 0

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.BLACK)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, player, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac, (x, y, w, h))

            if click[0] == 1 and action is not None:
                self.asd = player
                action()
        else:
            pygame.draw.rect(self.screen, ic, (x, y, w, h))

        smallText = pygame.font.Font("LLPIXEL3.ttf", 35)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (int(x + (w / 2)), int(y + (h / 2)))
        self.screen.blit(textSurf, textRect)

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit()
                        quit()

            self.screen.fill(self.WHITE)
            largeText = pygame.font.Font("LLPIXEL3.ttf", 150)
            TextSurf, TextRect = self.text_objects("Pong", largeText)
            TextRect.center = (int(self.w / 2), int((self.h / 2) / 2))
            self.screen.blit(TextSurf, TextRect)

            self.button("1 player", int(self.w / 2 - 150), 450, 300, 50, self.WHITE, "1", self.GREY,
                        self.gameLoop)
            self.button("2 player", int(self.w / 2 - 150), int(self.h / 2), 300, 50, self.WHITE, "2", self.GREY,
                        self.gameLoop)

            pygame.display.update()
            self.clock.tick(15)

    def moverPaletaB(self):
        print("Paleta", self.paletaB.rect.y)
        print("Ball", self.pelota.getRect())
        if self.pelota.getRect() - 85 < self.paletaB.rect.y < self.pelota.getRect() + 85:
            self.paletaB.moveUp(0)
            self.paletaB.moveDown(0, self.h)
        elif self.ballDirX / self.ballDirX == -1:
            if self.paletaB.rect.y > self.pelota.getRect():
                self.paletaB.moveUp(5)
            elif self.pelota.getRect() > self.paletaB.rect.y:
                self.paletaB.moveDown(5, self.h)
        elif self.ballDirX / self.ballDirX == 1:
            if self.pelota.getRect() < self.paletaB.rect.y:
                self.paletaB.moveUp(5)
            elif self.pelota.getRect() > self.paletaB.rect.y:
                self.paletaB.moveDown(5, self.h)

    def unJugador(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paletaA.moveUp(5)
        if keys[pygame.K_s]:
            self.paletaA.moveDown(5, self.h)
        self.moverPaletaB()

    def dosJugadores(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paletaA.moveUp(5)
        if keys[pygame.K_s]:
            self.paletaA.moveDown(5, self.h)
        if keys[pygame.K_UP]:
            self.paletaB.moveUp(5)
        if keys[pygame.K_DOWN]:
            self.paletaB.moveDown(5, self.h)

    def drawLines(self):
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 40), (int(self.w / 2), 80), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 120), (int(self.w / 2), 160), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 200), (int(self.w / 2), 240), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 280), (int(self.w / 2), 320), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 360), (int(self.w / 2), 400), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 440), (int(self.w / 2), 480), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 520), (int(self.w / 2), 560), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 600), (int(self.w / 2), 640), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 680), (int(self.w / 2), 720), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 760), (int(self.w / 2), 800), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 840), (int(self.w / 2), 880), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 920), (int(self.w / 2), 960), 3)
        pygame.draw.line(self.screen, self.BLACK, (int(self.w / 2), 1000), (int(self.w / 2), 1040), 3)

    def gameLoop(self):
        while self.juegoOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juegoOn = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.juegoOn = False
            self.pelota.moveBall(self.ballDirX, self.ballDirY)
            if self.asd == "1":
                self.unJugador()
            else:
                self.dosJugadores()
            self.lista_sprites.update()
            if self.pelota.rect.x >= self.w - 15:
                self.punto.play(loops=0, maxtime=0, fade_ms=0)
                self.pelota.rect.x = int(self.w / 2) - 15
                self.pelota.rect.y = int(self.h / 2) - 15
                self.ballDirX = random.randrange(2) * 2 - 1
                self.puntosA += 1
            if self.pelota.rect.x <= 0:
                self.punto.play(loops=0, maxtime=0, fade_ms=0)
                self.pelota.rect.x = int(self.w / 2) - 15
                self.pelota.rect.y = int(self.h / 2) - 15
                self.ballDirX = random.randrange(2) * 2 - 1
                self.puntosB += 1
            if self.pelota.rect.y >= self.h - 30:
                self.golpePaed.play(loops=0, maxtime=0, fade_ms=0)
                self.ballDirY = self.ballDirY * -1
            if self.pelota.rect.y <= 0:
                self.golpePaed.play(loops=0, maxtime=0, fade_ms=0)
                self.ballDirY = self.ballDirY * -1
            if pygame.sprite.collide_mask(self.pelota, self.paletaA) or pygame.sprite.collide_mask(self.pelota,
                                                                                                   self.paletaB):
                self.golpePaleta.play(loops=0, maxtime=0, fade_ms=0)
                self.ballDirX = self.ballDirX * -1

            self.screen.fill(self.WHITE)

            self.drawLines()

            self.lista_sprites.draw(self.screen)

            font = pygame.font.Font("LLPIXEL3.ttf", 100)
            text = font.render(str(self.puntosA), 1, self.BLACK)
            self.screen.blit(text, (int(self.w / 4), 50))
            text = font.render(str(self.puntosB), 1, self.BLACK)
            self.screen.blit(text, (int(self.w / 4) * 3, 50))

            pygame.display.flip()

            self.clock.tick(100)


if __name__ == "__main__":
    test().game_intro()
