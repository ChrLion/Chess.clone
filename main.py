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
                py.draw.rect(screen, BEIGE, [self.size_x*2*i+self.position, self.size_y*u*2+self.position, self.size_x, self.size_y])
                py.draw.rect(screen, BROWN, [self.size_x*2*i+3*self.position, self.size_y*u*2+self.position, self.size_x, self.size_y])
        for u in range(4):
            for i in range(4):
                py.draw.rect(screen, BROWN, [self.size_x*2*i+self.position, self.size_y*u*2+3*self.position, self.size_x, self.size_y])
                py.draw.rect(screen, BEIGE, [self.size_x*2*i+3*self.position, self.size_y*u*2+3*self.position, self.size_x, self.size_y])


class WhitePawn(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White Pawn.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)

   # def move_pawn(self, new_pos):
class BlackPawn(py.sprite.Sprite):
            def __init__(self):
                self.image = py.image.load(r'sprites\pieces\Black Pawn.png')
                self.rect = self.image.get_rect()

            def draw(self, pos):
                screen.blit(self.image, pos)
class WhiteKnight(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White Knight.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class BlackKnight(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\Black Knight.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class WhiteBishop(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White Bishop.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class BlackBishop(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\Black Bishop.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class WhiteRook(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White Rook.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class BlackRook(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\Black Rook.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class WhiteKing(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White King.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class BlackKing(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\Black King.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class WhiteQueen(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\White Queen.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)
class BlackQueen(py.sprite.Sprite):
    def __init__(self):
        self.image = py.image.load(r'sprites\pieces\Black Queen.png')
        self.rect = self.image.get_rect()

    def draw(self, pos):
        screen.blit(self.image, pos)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (184, 140, 100)
BEIGE = (255, 233, 197)

py.init()
Board = Board()
TestPawm = White_pawn()
# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = py.display.set_mode(size)

py.display.set_caption("Chess")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = py.time.Clock()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()


# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

    screen.fill(WHITE)
    Board.draw_board()
    TestPawm.draw_white_pawn((40, 120))

    py.display.flip()

    clock.tick(30)
