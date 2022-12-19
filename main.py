import pygame
import sys


class Hero(pygame.sprite.Sprite):
    image = pygame.image.load('a.png')

    # image = pygame.transform.scale(im, (im.get_width() // 2, im.get_height() // 2))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0

    def up(self):
        self.rect.y -= 1

    def down(self):
        self.rect.y += 1

    def right(self):
        self.rect.x += 1

    def left(self):
        self.rect.x -= 1

    def add_image(self):
        return self.image

    def add_rect(self):
        return self.rect


class Labyrinth(pygame.sprite.Sprite):
    image = pygame.image.load('b.png')

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Labyrinth.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def add_image(self):
        return self.image

    def add_rect(self):
        return self.rect


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill(pygame.Color('white'))
    running = True
    clock = pygame.time.Clock()
    l = Labyrinth()
    h = Hero()
    z = 0
    z1 = 0
    z2 = 0
    z3 = 0
    CONSTANT = ''
    while running:
        screen.fill(pygame.Color('white'))
        screen.blit(l.add_image(), l.add_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if not pygame.sprite.collide_mask(l, h):
                        CONSTANT = 'down'
                        if pygame.sprite.collide_mask(l, h):
                            CONSTANT = 'up'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if not pygame.sprite.collide_mask(l, h):
                        CONSTANT = 'up'
                        if pygame.sprite.collide_mask(l, h):
                            CONSTANT = 'down'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if not pygame.sprite.collide_mask(l, h):
                        CONSTANT = 'left'
                        if pygame.sprite.collide_mask(l, h):
                            CONSTANT = 'right'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if not pygame.sprite.collide_mask(l, h):
                        CONSTANT = 'right'
                        if pygame.sprite.collide_mask(l, h):
                            CONSTANT = 'left'
            elif event.type == pygame.KEYUP:
                # if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                CONSTANT = 'stop'

        if CONSTANT == 'down':
            if not pygame.sprite.collide_mask(l, h):
                h.down()
                if pygame.sprite.collide_mask(l, h):
                    h.up()
        elif CONSTANT == 'up':
            if not pygame.sprite.collide_mask(l, h):
                h.up()
                if pygame.sprite.collide_mask(l, h):
                    h.down()
        elif CONSTANT == 'left':
            if not pygame.sprite.collide_mask(l, h):
                h.left()
                if pygame.sprite.collide_mask(l, h):
                    h.right()
        elif CONSTANT == 'right':
            if not pygame.sprite.collide_mask(l, h):
                h.right()
                if pygame.sprite.collide_mask(l, h):
                    h.left()

        screen.blit(h.add_image(), h.add_rect())
        clock.tick(200)
        pygame.display.flip()
    pygame.quit()