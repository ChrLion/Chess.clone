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


class Pawn(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White Pawn.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black Pawn.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.moved = False

    def draw(self):
        screen.blit(self.image, self.pos)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        print(self.rect)

    def move(self):
        print("moved")
        self.moved = True


class Knight(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White Knight.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black Knight.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self, ):
        screen.blit(self.image, self.pos)


class Bishop(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White Bishop.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black Bishop.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self, ):
        screen.blit(self.image, self.pos)


class Rook(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White Rook.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black Rook.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self, ):
        screen.blit(self.image, self.pos)


class Queen(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White Queen.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black Queen.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self, ):
        screen.blit(self.image, self.pos)


class King(py.sprite.Sprite):
    def __init__(self, pos, white):
        super().__init__()
        if white:
            self.image = py.image.load(r'sprites\pieces\White King.png')
        else:
            self.image = py.image.load(r'sprites\pieces\Black King.png')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        screen.blit(self.image, self.pos)


def draw_pieces(draw_list):
    for piece in draw_list:
        piece.draw()


# Variables
one = 600
two = 520
three = 440
four = 360
five = 280
six = 200
seven = 120
eight = 40
h = 600
g = 520
f = 440
e = 360
d = 280
c = 200
b = 120
a = 40
a_to_h = [40, 120, 200, 280, 360, 440, 520, 600]
one_to_eight = [600, 520, 440, 360, 280, 200, 120, 40]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (184, 140, 100)
BEIGE = (255, 233, 197)

py.init()
Board = Board()
white_pawn_list = [Pawn((a_to_h[num], one_to_eight[1]), True) for num in range(8)]
black_pawn_list = [Pawn((a_to_h[num], one_to_eight[6]), False) for num in range(8)]
white_piece_list = [Knight((a_to_h[1], one_to_eight[0]), True), Knight((a_to_h[6], one_to_eight[0]), True), Rook((a_to_h[0], one_to_eight[0]), True), Rook((a_to_h[7], one_to_eight[0]), True), Bishop((a_to_h[2], one_to_eight[0]), True), Bishop((a_to_h[5], one_to_eight[0]), True), Queen((a_to_h[3], one_to_eight[0]), True), King((a_to_h[4], one_to_eight[0]), True)]
white_piece_list += white_pawn_list
black_piece_list = [Knight((a_to_h[1], one_to_eight[7]), False), Knight((a_to_h[6], one_to_eight[7]), False), Rook((a_to_h[0], one_to_eight[7]), False), Rook((a_to_h[7], one_to_eight[7]), False), Bishop((a_to_h[2], one_to_eight[7]), False), Bishop((a_to_h[5], one_to_eight[7]), False), Queen((a_to_h[3], one_to_eight[7]), False), King((a_to_h[4], one_to_eight[7]), False)]
black_piece_list += black_pawn_list
white_rect_list = []
for piece in white_piece_list:
    white_rect_list.append(piece.rect)
print(white_rect_list)
piece_list = white_piece_list + black_piece_list

print(white_pawn_list)

# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = py.display.set_mode(size)

py.display.set_caption("Chess")

# Loop until the user clicks the close button.
draw_highlight = False
piece_clicked = -1

# Used to manage how fast the screen updates
clock = py.time.Clock()

# while True:
#    for event in py.event.get():
#        if event.type == py.QUIT:
#            quit()


# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
        if event.type == py.MOUSEBUTTONDOWN:
            clicked_at = py.mouse.get_pos()
            piece_clicked = py.rect.Rect.collidelist(py.rect.Rect(clicked_at[0], clicked_at[1], 1, 1), white_rect_list)
            if piece_clicked != -1:
                print("test")
                if draw_highlight:
                    draw_highlight = False
                else:
                    draw_highlight = True

    screen.fill(WHITE)
    Board.draw_board()
    draw_pieces(piece_list)
    if draw_highlight:
        py.draw.rect(screen, (255, 0, 0), white_rect_list[piece_clicked], 5, 1)

    py.display.flip()

    clock.tick(30)
