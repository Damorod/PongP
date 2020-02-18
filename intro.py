import pygame

pygame.init()

size = (0, 0)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

WHITE = (255, 255, 255)
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode(size, pygame.FULLSCREEN)

w = pygame.Surface.get_width(gameDisplay)
h = pygame.Surface.get_height(gameDisplay)

clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (int(x + (w / 2)), int(y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()

        gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Pong", largeText)
        TextRect.center = (int(w / 2), int((h / 2) / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("1 player", 1100, 450, 100, 50, green, bright_green, )
        button("2 player", 550, 450, 100, 50, red, bright_red)

        pygame.display.update()
        clock.tick(15)


game_intro()
