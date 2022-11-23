import time

import pygame as py
import random
import sys

import pygame.font


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


action = False
startimg = py.image.load("sprites/Button/Start-Button-Vector-PNG.png")
multiim = py.image.load("sprites/Button/button (1).png")
soloim = py.image.load("sprites/Button/button.png")
backimg = py.image.load("sprites/Button/button (2).png")

class Button():
    def __init__(self, x, y, image, scale,text=''):
        width = image.get_width()
        height = image.get_height()
        self.image = py.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        pos = py.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                global action
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))





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
white_piece_list = [Knight((a_to_h[1], one_to_eight[0]), True), Knight((a_to_h[6], one_to_eight[0]), True),
                    Rook((a_to_h[0], one_to_eight[0]), True), Rook((a_to_h[7], one_to_eight[0]), True),
                    Bishop((a_to_h[2], one_to_eight[0]), True), Bishop((a_to_h[5], one_to_eight[0]), True),
                    Queen((a_to_h[3], one_to_eight[0]), True), King((a_to_h[4], one_to_eight[0]), True)]
white_piece_list += white_pawn_list
black_piece_list = [Knight((a_to_h[1], one_to_eight[7]), False), Knight((a_to_h[6], one_to_eight[7]), False),
                    Rook((a_to_h[0], one_to_eight[7]), False), Rook((a_to_h[7], one_to_eight[7]), False),
                    Bishop((a_to_h[2], one_to_eight[7]), False), Bishop((a_to_h[5], one_to_eight[7]), False),
                    Queen((a_to_h[3], one_to_eight[7]), False), King((a_to_h[4], one_to_eight[7]), False)]
black_piece_list += black_pawn_list
white_rect_list = []
for piece in white_piece_list:
    white_rect_list.append(piece.rect)
print(white_rect_list)
piece_list = white_piece_list + black_piece_list

print(white_pawn_list)

start_button = Button(320, 500, startimg, 0.5)
Multibutton = Button(60,440, multiim ,2)
solobutton = Button(560,440, soloim,2)
backbut = Button(10,10,backimg,1)


# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = py.display.set_mode(size)

py.display.set_caption("Chess")

# Loop until the user clicks the close button.
done = False
draw_highlight = False
# Used to manage how fast the screen updates
clock = py.time.Clock()
input_rect = pygame.Rect(200,300,140,75)
base_font = py.font.Font(None,80)
user_Name =""
textfont = pygame.font.SysFont("monospace",80)
menu = True

#_______________menu___________
run = True
while run:


    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_Name = user_Name[:-1]
            elif len(user_Name) < 18:
                user_Name += event.unicode
    screen.fill(BROWN)


    Name = textfont.render("Name",1,(BLACK))
    screen.blit(Name,(0,300))


    start_button.draw()

    pygame.draw.rect(screen,WHITE,input_rect,2)

    text_surface = base_font.render(user_Name, True,BLACK )
    input_rect.w = text_surface.get_width() + 10
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    py.display.flip()
    if len(user_Name) > 0:
        if action == True:
            run = False
            action = False
            time.sleep(0.2)


# ______________Game mode selction___________
run = True
while run == True:
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
    screen.fill(BROWN)



    Multibutton.draw()
    if action == True:
        run = False

    solobutton.draw()
    if action == True:
        run = False



    action = False


    py.display.flip()



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