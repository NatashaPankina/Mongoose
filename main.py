import pygame
import sys
import sqlite3
from io import BytesIO
import time
from tkinter import *
from PIL import Image, ImageTk

bd = sqlite3.connect("mangoose2.db")
cur = bd.cursor()
f = 0
k = 0
images = cur.execute(
    'select image, name from other_images where name in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)').fetchall()
images2 = cur.execute('select image, name from other_images where name in (13, 14, 15, 16, 17)').fetchall()
timee = 0
SCREEN = -1

res = cur.execute("""SELECT image FROM life""").fetchall()
lifes_name = [BytesIO(i[0]) for i in res]
res = cur.execute("""SELECT image FROM trap_num""").fetchall()
trap_num = [BytesIO(i[0]) for i in res]

Key_chest = cur.execute("""SELECT image FROM other_images WHERE name = 'key_chest'""").fetchone()[0]
Key_hatch = cur.execute("""SELECT image FROM other_images WHERE name = 'key_hatch'""").fetchone()[0]
Axe = cur.execute("""SELECT image FROM other_images WHERE name = 'axe'""").fetchone()[0]
Hatch = cur.execute("""SELECT image FROM other_images WHERE name = 'hatch'""").fetchone()[0]
Chest = cur.execute("""SELECT image FROM other_images WHERE name = 'chest'""").fetchone()[0]
Trap = cur.execute("""SELECT image FROM other_images WHERE name = 'trap'""").fetchone()[0]
No_trap = cur.execute("""SELECT image FROM other_images WHERE name = 'no_trap'""").fetchone()[0]
Begin = cur.execute("""SELECT image FROM other_images WHERE name = 'begin'""").fetchone()[0]
invent_box = cur.execute("""SELECT image FROM other_images WHERE name = 'invent_box'""").fetchone()[0]
white = cur.execute("""SELECT image FROM other_images WHERE name = 'white'""").fetchone()[0]
black = cur.execute("""SELECT image FROM other_images WHERE name = 'black'""").fetchone()[0]
walls1 = cur.execute("""SELECT walls FROM levels WHERE number = 1""").fetchone()[0]
walls2 = cur.execute("""SELECT walls FROM levels WHERE number = 2""").fetchone()[0]
walls3 = cur.execute("""SELECT walls FROM levels WHERE number = 3""").fetchone()[0]
floor1 = cur.execute("""SELECT floor FROM levels WHERE number = 1""").fetchone()[0]
floor2 = cur.execute("""SELECT floor FROM levels WHERE number = 2""").fetchone()[0]
floor3 = cur.execute("""SELECT floor FROM levels WHERE number = 3""").fetchone()[0]


def final_and_splash(text):
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.resizable(width=False, height=False)
    root.overrideredirect(1)
    w = 800
    h = 550
    root.geometry(f"{w}x{h}+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 2}")
    imagee = ImageTk.PhotoImage(Image.open(BytesIO(images[0][0])))
    can = Canvas(root, width=800, height=550)
    can.create_image(400, 275, image=imagee)
    can.create_text(375, 275, text=text, fill='white', justify='center', font='"Segoe Print" 26')
    can.pack()
    root.after(1, root.destroy)
    root.mainloop()


def text(intro_text, num, coord, center=True, x=None, color='white', font='Vernada'):
    font = pygame.font.SysFont(font, num)
    text_coord = coord
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(color))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        if center:
            intro_rect.centerx = screen.get_width() // 2
        if x is not None:
            intro_rect.centerx = x
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def win():
    try:
        global k
        im_0 = cur.execute("""SELECT image FROM other_images WHERE name = bib'""").fetchone()[0]
        k = min(im.get_height(), im.get_width()) / minn_side
        im = pygame.image.load(BytesIO(im_0))
        image = pygame.transform.scale(im, (im.get_width() / (im.get_height() / minn_side), minn_side))
        rect = image.get_rect()
        rect.centerx = screen.get_width() // 2
        n = 0
        while True:
            if n == 0:
                screen.fill((0, 0, 0))
                intro_text = ['Я дошёл до конца. Это было очень странное место. Порой,',
                              'повернувшись, я оказывался в совершенно в другом месте.',
                              'Но я не сдавался.']
                text(intro_text, 50, 150)
            elif n == 1:
                screen.blit(image, rect)
                intro_text = ['В конце пути я нашёл библиотеку. Множество интересной информации.',
                              'Я всё расшифровал. Все наконец-то поверили мне. Я выиграл!']
                text(intro_text, 35, screen.get_height() - 150)
            elif n == 3:
                SCREEN = 1
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    n += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    running = False
                    return
            pygame.display.flip()
    except Exception as d:
        print(d)


def splash2():
    try:
        global k, SCREEN
        im = pygame.image.load(BytesIO(images[4][0]))
        k = min(im.get_height(), im.get_width()) / minn_side
        image = pygame.transform.scale(im, (im.get_width() / (im.get_height() / minn_side), minn_side))
        rect = image.get_rect()
        rect.centerx = screen.get_width() // 2
        im2 = pygame.image.load(BytesIO(images[5][0]))
        image2 = pygame.transform.scale(im2, (im2.get_width() / (im2.get_height() / minn_side), minn_side))
        rect2 = image2.get_rect()
        rect2.centerx = screen.get_width() // 2
        n = 0
        while True:
            if n == 0:
                screen.fill((0, 0, 0))
                intro_text = ["ВНИМАНИЕ!!!", "",
                              'Для продолжения истории нажимайте пробел,',
                              'для её пропуска нажмите "q".']
                text(intro_text, 50, 150)
            elif n == 1:
                screen.fill((0, 0, 0))
                intro_text = ['Имя: Клауд',
                              'Возраст: 23',
                              'Интересы: Археология, история',
                              '',
                              '- Я с детства любил изучать прошлое, откапывать',
                              'игрушки в песочнице, рассматривать карты, читать',
                              'книги о всемирных тайнах...']
                text(intro_text, 50, 150)
            elif n == 2:
                screen.blit(image, rect)
                intro_text = ['И вот, моя страсть привела меня к Египту. Я днями и ночами впитывал в себя эти загадки.',
                              'В ходе одной экспедиции я наткнулся на что-то... странное, непривычное для этой тематики.']
                text(intro_text, 35, screen.get_height() - 150)
            elif n == 3:
                screen.fill((0, 0, 0))
                intro_text = ['Почти полностью разрушенное и утоновшее в песках построение.',
                              'Оно напоминало Храмы Луксора, но иерогливы отличались, техника постройки тоже.',
                              'Я хотел собрать людей, которые помогли бы мне исследовать это место...',
                              'Но никто мне не верил. Тогда мне пришлось принять важное решение. ',
                              'Я иду туда один.']
                text(intro_text, 45, 150)
            elif n == 4:
                screen.blit(image2, rect2)
                intro_text = ['И только мне предстоит узнать, что скрывает это место!']
                text(intro_text, 60, screen.get_height() // 2 + 50)
            elif n == 5:
                SCREEN = 1
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    n += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    SCREEN = 1
                    return
            pygame.display.flip()
    except Exception as d:
        print(d)


def button_press(but):
    but.getim2()
    pygame.display.update()
    time.sleep(0.1)
    but.getim1()
    pygame.display.update()


def menu():
    try:
        global SCREEN, k, running
        b1 = ButtonFabrika(images[7][0], images[8][0], screen.get_height() // 6 * 4, True)
        b2 = ButtonFabrika(images[9][0], images[10][0], screen.get_height() // 6 * 3, True)
        im1 = pygame.image.load(BytesIO(images[6][0]))
        image1 = pygame.transform.scale(im1, (im1.get_width() / k, im1.get_height() / k))
        im_rect = image1.get_rect()
        im_rect.centerx = screen.get_width() // 2
        while True:
            screen.fill((0, 0, 0))
            screen.blit(image1, im_rect)
            intro_text = ['Тайна затерянного храма']
            text(intro_text, 70, screen.get_height() // 6, False, screen.get_width() // 2, 'black')
            intro_text1 = ['Последнее время проведённое в игре: ',
                           str(cur.execute('select ttt from tiiime').fetchone()[0])]
            text(intro_text1, 50, screen.get_height() // 4, False, screen.get_width() // 2, 'black')
            b1.getim1()
            b2.getim1()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                    SCREEN = 0
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = b1.proverka(event.pos)
                    if result:
                        button_press(b1)
                        running = False
                        SCREEN = 0
                        pygame.quit()
                        return
                    result1 = b2.proverka(event.pos)
                    if result1:
                        button_press(b2)
                        SCREEN = 2
                        pygame.display.update()
                        return
            pygame.display.flip()
        pygame.display.update()
    except Exception as d:
        print(d)


def new_game():
    global k, SCREEN, timee, f
    f = 1
    im1 = pygame.image.load(BytesIO(images2[2][0]))
    image1 = pygame.transform.scale(im1, (im1.get_width() / k / 2, im1.get_height() / k / 2))
    im_rect = image1.get_rect()
    im_rect.y = 30
    im_rect.centerx = screen.get_width() // 3
    im2 = pygame.image.load(BytesIO(images2[3][0]))
    image2 = pygame.transform.scale(im2, (im2.get_width() / k / 2, im2.get_height() / k / 2))
    im_rect1 = image1.get_rect()
    im_rect1.y = 30
    im_rect1.centerx = screen.get_width() // 3
    im3 = pygame.image.load(BytesIO(images2[4][0]))
    image3 = pygame.transform.scale(im3, (im3.get_width() / k / 2, im3.get_height() / k / 2))
    im_rect3 = image1.get_rect()
    im_rect3.y = 30
    im_rect3.centerx = screen.get_width() // 3
    im = pygame.image.load(BytesIO(images[6][0]))
    image = pygame.transform.scale(im, (im.get_width() / k, im.get_height() / k))
    im_rect2 = image.get_rect()
    im_rect2.centerx = screen.get_width() // 2
    b1 = ButtonFabrika(images2[0][0], images2[0][0], screen.get_height() // 6 * 5, False, screen.get_width() // 6)
    b2 = ButtonFabrika(images2[1][0], images2[1][0], screen.get_height() // 6 * 5, False, screen.get_width() // 6 * 3)
    b3 = ButtonFabrika(images[9][0], images[10][0], screen.get_height() // 6 * 5, False, screen.get_width() // 6 * 4.5)
    b4 = ButtonFabrika(images2[0][0], images2[0][0], 40, False, 50)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(image, im_rect2)
        if f == 1:
            screen.blit(image1, im_rect)
        elif f == 2:
            screen.blit(image2, im_rect1)
        elif f == 3:
            screen.blit(image3, im_rect3)
        b1.getim1()
        b2.getim1()
        b3.getim1()
        b4.getim1()
        intro_text = ['Выберете персонажа :)',
                      '      _        _     ',
                      '   /     \  /     \  ',
                      '   \      \/      /  ',
                      '     \          /    ',
                      '       \      /      ',
                      '         \  /        ',
                      '          \/         ']
        text(intro_text, 55, 200, False, screen.get_width() // 6 * 4.5, 'black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                SCREEN = 0
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = b1.proverka(event.pos)
                if result:
                    button_press(b1)
                    if f != 1:
                        f -= 1
                    else:
                        f = 3
                result1 = b2.proverka(event.pos)
                if result1:
                    button_press(b2)
                    if f != 3:
                        f += 1
                    else:
                        f = 1
                result2 = b3.proverka(event.pos)
                if result2:
                    button_press(b3)
                    timee = pygame.time.get_ticks()
                    SCREEN = 3
                    return
                result3 = b4.proverka(event.pos)
                if result3:
                    button_press(b4)
                    SCREEN = 1
                    return
        pygame.display.flip()


class ButtonFabrika:
    def __init__(self, im1, im2, y, center, x=None):
        global k
        im1 = pygame.image.load(BytesIO(im1))
        im2 = pygame.image.load(BytesIO(im2))
        self.im1 = pygame.transform.scale(im1, (im1.get_width() / k, im1.get_height() / k))
        self.im2 = pygame.transform.scale(im2, (im2.get_width() / k, im2.get_height() / k))
        self.rect = self.im1.get_rect()
        self.mask = pygame.mask.from_surface(self.im1)
        self.rect.y = y
        if center:
            self.rect.centerx = screen.get_width() // 2
        if x is not None:
            self.rect.centerx = x

    def getim1(self):
        screen.blit(self.im1, self.rect)

    def getim2(self):
        screen.blit(self.im2, self.rect)

    def proverka(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False


class Hero(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        im = pygame.image.load(BytesIO(name))
        self.image = pygame.transform.scale(im, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = screen2.get_width() // 2
        self.rect.y = screen2.get_height() // 2
        self.turn = 0

    def up(self):
        self.image = pygame.transform.rotate(self.image, 360 - self.turn)
        self.turn = 0

    def down(self):
        self.image = pygame.transform.rotate(self.image, 180 - self.turn)
        self.turn = 180

    def right(self):
        self.image = pygame.transform.rotate(self.image, 270 - self.turn)
        self.turn = 270

    def left(self):
        self.image = pygame.transform.rotate(self.image, 90 - self.turn)
        self.turn = 90

    def add_image(self):
        return self.image

    def add_rect(self):
        return self.rect

    def new_image(self, n):
        self.image = n


class Labyrinth(pygame.sprite.Sprite):
    def __init__(self, walls, floors):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BytesIO(walls))
        self.image2 = pygame.image.load(BytesIO(floors))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = -4096 + screen.get_width() // 3 * 2
        self.rect.y = -4096 + screen.get_height()

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

    def add_image2(self):
        return self.image2

    def add_rect(self):
        return self.rect


class class_Key_hatch(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_Key_chest(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_Axe(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.transform.scale(pygame.image.load(BytesIO(name)), (150, 80))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_Trap(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_No_trap(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_Chest(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class class_Hatch(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class Inventory(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        # image = pygame.image.load(name)
        self.image = pygame.transform.scale(pygame.image.load(BytesIO(name)), (150, 80))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


class Check(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('white.jpg')
        # image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(image, (170, 170))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]


class class_Begin(pygame.sprite.Sprite):
    def __init__(self, name, xy, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.image.load(BytesIO(name))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xy[0]
        self.rect.y = xy[1]

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


def first():
    global l, h, protect, lifes, level, key_h, key_c, key_a, image, image2, image3, pers
    name_obj = [(Chest, (-1343, -2647)), (Hatch, (905, -1300)), (Key_chest, (41, -70)), (Begin, (613, 737))]
    trapss = [(Trap, (929, -835)), (Trap, (-1513, -2601)), (Trap, (61, -2547)), (Trap, (61, -2420)),
              (Trap, (929, -1055))]
    l = Labyrinth(walls1, floor1)
    a = cur.execute("""SELECT n1 FROM pers_traffic WHERE num = ?""", (f,)).fetchone()[0]
    h = Hero(a)
    res = cur.execute("""SELECT * FROM pers_traffic WHERE num = ?""", (f,)).fetchall()[0]
    pers = [i for i in res]
    pers = pers[2:]
    class_Key_chest(*name_obj[2], key_chest)
    class_Begin(*name_obj[3], begin)
    class_Chest(*name_obj[0], chest)
    class_Hatch(*name_obj[1], hatch)
    protect = 0
    lifes = 3
    level = 1
    key_h = False
    key_c = False
    key_a = False
    image = pygame.image.load(BytesIO(floor2))
    image2 = pygame.transform.scale(pygame.image.load(BytesIO(invent_box)), (500, 300))
    image3 = pygame.transform.scale(pygame.image.load(lifes_name[-1]), (350, 130))
    for i in trapss:
        class_Trap(*i, traps)


def second():
    global l, protect, lifes, level, key_h, key_c, key_a, image, image2, image3
    name_obj = [(Chest, (-1991, -2803)), (Hatch, (-2556, 684)), (Key_chest, (-616, 334)), (Key_hatch, (-2400, -2703)),
                (Begin, (500, 700))]
    trapss = [(Trap, (-206, -416)), (Trap, (194, -2191)), (Trap, (-2581, -1746)), (Trap, (-2016, -2566)),
              (Trap, (-1906, -2566)), (Trap, (-1796, -2566))]
    l = Labyrinth(walls2, floor2)
    class_Key_hatch(*name_obj[3], key_hatch)
    class_Key_chest(*name_obj[2], key_chest)
    class_Begin(*name_obj[4], begin)
    class_Chest(*name_obj[0], chest)
    class_Hatch(*name_obj[1], hatch)
    protect = 0
    lifes = 3
    level = 1
    key_h = False
    key_c = False
    key_a = False
    image = pygame.image.load(BytesIO(floor2))
    image2 = pygame.transform.scale(pygame.image.load(BytesIO(invent_box)), (500, 300))
    for i in trapss:
        class_Trap(*i, traps)


def third():
    global l, h, protect, lifes, level, key_h, key_c, key_a, image, image2, image3
    name_obj = [(Chest, (-939, -1837)), (Hatch, (681, -1000)), (Key_chest, (645, 669)), (Axe, (-1891, -2551)),
                (Begin, (745, 901))]
    trapss = [(Trap, (-2283, -2017)), (Trap, (-2079, -1051)), (Trap, (-1443, -1971)), (Trap, (2151, 617)),
              (Trap, (641, -1791)), (Trap, (889, -465)), (Trap, (-546, -1971))]
    l = Labyrinth(walls3, floor3)
    class_Key_chest(*name_obj[2], key_chest)
    class_Begin(*name_obj[4], begin)
    class_Axe(*name_obj[3], axe)
    class_Chest(*name_obj[0], chest)
    class_Hatch(*name_obj[1], hatch)
    protect = 0
    lifes = 3
    level = 1
    key_h = False
    key_c = False
    key_a = False
    image = pygame.image.load(BytesIO(floor3))
    image2 = pygame.transform.scale(pygame.image.load(BytesIO(invent_box)), (500, 300))
    for i in trapss:
        class_Trap(*i, traps)


def first_chest():
    Inventory(Key_hatch, (35, 85), invent)


def second_chest():
    global protect
    Inventory(trap_num[4], (286, 200), invent)
    protect = 4


def third_chest():
    Inventory(Key_hatch, (35, 85), invent)


if __name__ == '__main__':
    final_and_splash('''Дорогой пользователь!
     Спасибо за визит нашей игры :)
     Мы безумно рады, что вы решили
     поиграть именно в нашу игру.
     Хорошего вам время припровождения!''')
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    minn_side = min(screen.get_width(), screen.get_height())
    maxx_screen = max(screen.get_width(), screen.get_height())
    running = True
    clock = pygame.time.Clock()
    traps = pygame.sprite.Group()
    no_traps = pygame.sprite.Group()
    invent = pygame.sprite.Group()
    screen2 = pygame.Surface((screen.get_width() // 3 * 2, screen.get_height()))
    screen3 = pygame.Surface((500, 300))
    screen4 = pygame.Surface((350, 130))
    key_hatch = pygame.sprite.Group()
    key_chest = pygame.sprite.Group()
    axe = pygame.sprite.Group()
    chest = pygame.sprite.Group()
    hatch = pygame.sprite.Group()
    begin = pygame.sprite.Group()
    animation = 0
    splash2()
    while True:
        if SCREEN == 0:
            running = False
            break
        if SCREEN == 1:
            menu()
        if SCREEN == 2:
            new_game()
        if SCREEN == 3:
            break
    first()
    number = 0
    while running:
        screen.blit(image, (0, 0))
        screen2.blit(image, (0, 0))
        screen3.blit(image2, (0, 0))
        screen4.blit(image3, (0, 0))
        last_pos = (0, 0)
        if animation % 5:
            number = animation % 20 // 5
        h = Hero(pers[number])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = event.pos

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if not pygame.sprite.collide_mask(l, h):
                h.right()
                l.right()
                animation += 1
                for i in key_hatch:
                    i.right()
                for i in key_chest:
                    i.right()
                for i in axe:
                    i.right()
                for i in chest:
                    i.right()
                for i in hatch:
                    i.right()
                for i in traps:
                    i.right()
                for i in no_traps:
                    i.right()

                while pygame.sprite.collide_mask(l, h):
                    l.left()
                    for i in key_hatch:
                        i.left()
                    for i in key_chest:
                        i.left()
                    for i in axe:
                        i.left()
                    for i in chest:
                        i.left()
                    for i in hatch:
                        i.left()
                    for i in traps:
                        i.left()
                    for i in no_traps:
                        i.left()

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            if not pygame.sprite.collide_mask(l, h):
                h.down()
                l.down()
                animation += 1
                for i in key_hatch:
                    i.down()
                for i in key_chest:
                    i.down()
                for i in axe:
                    i.down()
                for i in chest:
                    i.down()
                for i in hatch:
                    i.down()
                for i in traps:
                    i.down()
                for i in no_traps:
                    i.down()

                while pygame.sprite.collide_mask(l, h):
                    l.up()
                    for i in key_hatch:
                        i.up()
                    for i in key_chest:
                        i.up()
                    for i in axe:
                        i.up()
                    for i in chest:
                        i.up()
                    for i in hatch:
                        i.up()
                    for i in traps:
                        i.up()
                    for i in no_traps:
                        i.up()

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            if not pygame.sprite.collide_mask(l, h):
                h.left()
                l.left()
                animation += 1
                for i in key_hatch:
                    i.left()
                for i in key_chest:
                    i.left()
                for i in axe:
                    i.left()
                for i in chest:
                    i.left()
                for i in hatch:
                    i.left()
                for i in traps:
                    i.left()
                for i in no_traps:
                    i.left()

                while pygame.sprite.collide_mask(l, h):
                    l.right()
                    for i in key_hatch:
                        i.right()
                    for i in key_chest:
                        i.right()
                    for i in axe:
                        i.right()
                    for i in chest:
                        i.right()
                    for i in hatch:
                        i.right()
                    for i in traps:
                        i.right()
                    for i in no_traps:
                        i.right()

        elif key[pygame.K_UP] or key[pygame.K_w]:
            if not pygame.sprite.collide_mask(l, h):
                h.up()
                l.up()
                animation += 1
                for i in key_hatch:
                    i.up()
                for i in key_chest:
                    i.up()
                for i in axe:
                    i.up()
                for i in chest:
                    i.up()
                for i in hatch:
                    i.up()
                for i in traps:
                    i.up()
                for i in no_traps:
                    i.up()

                while pygame.sprite.collide_mask(l, h):
                    l.down()
                    for i in key_hatch:
                        i.down()
                    for i in key_chest:
                        i.down()
                    for i in axe:
                        i.down()
                    for i in chest:
                        i.down()
                    for i in hatch:
                        i.down()
                    for i in traps:
                        i.down()
                    for i in no_traps:
                        i.down()

        for i in traps:
            new = Check((i.rect.x - 30, i.rect.y - 30))
            if new.rect.colliderect(h) and not (pygame.sprite.spritecollideany(h, traps)) \
                    and pygame.Rect(screen.get_width() // 3 * 2 + 276, screen.get_height() // 5 * 3 + 190, 240,
                                    110).collidepoint(last_pos):
                class_No_trap(No_trap, i.add_rect(), no_traps)
                traps.remove(i)
                protect -= 1
                for i in invent:
                    if i.rect.x == 286 and i.rect.y == 200:
                        i.image = pygame.image.load(trap_num[protect])


            elif pygame.sprite.spritecollideany(h, traps):
                f = pygame.sprite.spritecollideany(h, traps)
                class_No_trap(No_trap, f.add_rect(), no_traps)
                traps.remove(f)
                image3 = pygame.transform.scale(pygame.image.load(lifes_name[lifes - 1]), (350, 130))
                if lifes != 0:
                    lifes -= 1

        if lifes == 0:
            t = pygame.time.get_ticks()
            timee = t - timee
            cur.execute('''UPDATE tiiime
                        set ttt=?''', (timee,))
            bd.commit()
            running = False

        if (pygame.sprite.spritecollideany(h, chest) and pygame.Rect(screen.get_width() // 3 * 2 + 25,
                                                                     screen.get_height() // 5 * 3 + 190, 240,
                                                                     110).collidepoint(
                last_pos) and key_c and level in (1, 2)) or (
                pygame.sprite.spritecollideany(h, chest) and pygame.Rect(screen.get_width() // 3 * 2 + 286,
                                                                         screen.get_height() // 5 * 3 + 190, 240,
                                                                         110).collidepoint(
                last_pos) and key_a and level == 3):
            if level == 1:
                first_chest()
            elif level == 2:
                second_chest()
            elif level == 3:
                third_chest()

        if pygame.sprite.spritecollideany(h, hatch) and pygame.Rect(screen.get_width() // 3 * 2 + 25,
                                                                    screen.get_height() // 5 * 3 + 190, 240,
                                                                    110).collidepoint(last_pos) and key_h:
            if level == 1:
                second()
            elif level == 2:
                third()
            elif level == 3:
                t = pygame.time.get_ticks()
                timee = t - timee
                cur.execute('''UPDATE tiiime
                            set ttt=?''', (timee,))
                bd.commit()
                running = False

        if pygame.sprite.spritecollideany(h, axe):
            f = pygame.sprite.spritecollideany(h, axe)
            Inventory(Axe, (286, 85), invent)
            axe.remove(f)
            key_h = True

        if pygame.sprite.spritecollideany(h, key_chest):
            f = pygame.sprite.spritecollideany(h, key_chest)
            Inventory(Key_chest, (35, 200), invent)
            key_chest.remove(f)
            key_c = True

        if pygame.sprite.spritecollideany(h, key_hatch):
            f = pygame.sprite.spritecollideany(h, key_hatch)
            Inventory(Key_hatch, (35, 85), invent)
            key_hatch.remove(f)
            key_a = True

        screen2.blit(l.add_image2(), l.add_rect())
        key_hatch.draw(screen2)
        key_chest.draw(screen2)
        axe.draw(screen2)
        chest.draw(screen2)
        hatch.draw(screen2)
        traps.draw(screen2)
        no_traps.draw(screen2)
        invent.draw(screen3)
        screen2.blit(l.add_image(), l.add_rect())
        screen2.blit(h.add_image(), h.add_rect())
        screen2.blit(pygame.image.load(BytesIO(black)), (0, 0))
        screen4.blit(image3, (0, 0))
        screen.blit(screen2, (0, 0))
        screen.blit(screen3, (screen.get_width() // 3 * 2 + 20, screen.get_height() // 5 * 3))
        screen.blit(screen4, (screen.get_width() // 3 * 2 + 20, screen.get_height() // 5 * 3 - 150))
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
    final_and_splash('''Ещё раз спасибо за то, что
        зашёл в нашу игру :)
        Всего наилучшего, до новых встреч!''')

bd.close()