import pygame
import sys


class Hero(pygame.sprite.Sprite):
    image = pygame.image.load('c.png')

    # image = pygame.transform.scale(im, (im.get_width() // 2, im.get_height() // 2))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 200
        self.turn = 0

    def up(self):
        self.rect.y -= 1
        self.image = pygame.transform.rotate(self.image, 360 - self.turn)
        self.turn = 0

    def down(self):
        self.rect.y += 1
        self.image = pygame.transform.rotate(self.image, 180 - self.turn)
        self.turn = 180

    def right(self):
        self.rect.x += 1
        self.image = pygame.transform.rotate(self.image, 90 - self.turn)
        self.turn = 90

    def left(self):
        self.rect.x -= 1
        self.image = pygame.transform.rotate(self.image, 270 - self.turn)
        self.turn = 270

    def add_image(self):
        return self.image

    def add_rect(self):
        return self.rect


class Labyrinth(pygame.sprite.Sprite):
    image = pygame.image.load('walls2.png')

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Labyrinth.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def up(self):
        self.rect.y += 10

    def down(self):
        self.rect.y -= 10

    def right(self):
        self.rect.x -= 10

    def left(self):
        self.rect.x += 10

    def add_image(self):
        return self.image

    def add_rect(self):
        return self.rect


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill(pygame.Color('white'))
    running = True
    clock = pygame.time.Clock()
    l = Labyrinth()
    h = Hero()
    while running:
        screen.fill(pygame.Color('white'))
        screen.blit(l.add_image(), l.add_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if not pygame.sprite.collide_mask(l, h):
                h.right()
                l.right()
                if pygame.sprite.collide_mask(l, h):
                    h.left()
                    l.left()

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            if not pygame.sprite.collide_mask(l, h):
                h.down()
                l.down()
                if pygame.sprite.collide_mask(l, h):
                    h.up()
                    l.up()

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if not pygame.sprite.collide_mask(l, h):
                h.left()
                l.left()
                if pygame.sprite.collide_mask(l, h):
                    h.right()
                    l.right()

        if key[pygame.K_UP] or key[pygame.K_w]:
            if not pygame.sprite.collide_mask(l, h):
                h.up()
                l.up()
                if pygame.sprite.collide_mask(l, h):
                    h.down()
                    l.down()

        screen.blit(h.add_image(), h.add_rect())
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()