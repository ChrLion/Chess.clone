import pygame as py
import random
import sys


class Board:
    def __init__(self):
        self.size_x = 80
        self.size_y = 80
        self.position = 40
        self.mask = 1

    def draw_board(self):
        for u in range(4):
            for i in range(4):
                py.draw.rect(screen, BEIGE,
                             [self.size_x * 2 * i + self.position, self.size_y * u * 2 + self.position, self.size_x,
                              self.size_y])
                py.draw.rect(screen, BROWN,
                             [self.size_x * 2 * i + 3 * self.position, self.size_y * u * 2 + self.position, self.size_x,
                              self.size_y])
        for u in range(4):
            for i in range(4):
                py.draw.rect(screen, BROWN,
                             [self.size_x * 2 * i + self.position, self.size_y * u * 2 + 3 * self.position, self.size_x,
                              self.size_y])
                py.draw.rect(screen, BEIGE,
                             [self.size_x * 2 * i + 3 * self.position, self.size_y * u * 2 + 3 * self.position,
                              self.size_x, self.size_y])


class WhitePawn(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White Pawn.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackPawn(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black Pawn.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class WhiteKnight(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White Knight.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackKnight(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black Knight.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class WhiteBishop(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White Bishop.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackBishop(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black Bishop.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class WhiteRook(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White Rook.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackRook(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black Rook.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class WhiteQueen(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White Queen.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackQueen(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black Queen.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class WhiteKing(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\White King.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)


class BlackKing(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = py.image.load(r'sprites\pieces\Black King.png')
        self.rect = self.image.get_rect()

    def draw(self, ):
        screen.blit(self.image, self.pos)
action = False
startimg = py.image.load("sprites/button/Start-button-icon-on-transparent-background-PNG.png")

class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = py.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        pos = py.mouse.get_pos()


        if self.rect.collidepoint(pos):
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:

             global action
             action = True



        screen.blit(self.image, (self.rect.x, self.rect.y))


# Variables
one = 40
two = 120
three = 200
four = 280
five = 360
six = 440
seven = 520
eight = 600
a = 600
b = 520
c = 440
d = 360
e = 280
f = 200
g = 120
h = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (184, 140, 100)
BEIGE = (255, 233, 197)

py.init()
Board = Board()
start_button = Button(360, 400, startimg, 0.5)
# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = py.display.set_mode(size)

py.display.set_caption("Chess")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = py.time.Clock()

run = True
while run == True:



    for event in py.event.get():
       if event.type == py.QUIT:
            quit()
    screen.fill(WHITE)
    start_button.draw()
    py.display.flip()
    clock.tick(10)
    if action == True:
        run = False


# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

    screen.fill(WHITE)
    Board.draw_board()

    py.display.flip()

    clock.tick(30)
