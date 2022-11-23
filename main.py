import pygame as py


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


class Pawn(py.sprite.Sprite):
    def __init__(self):
        self.sprite =

#class Knight(py.sprite.Sprite):
#
#class Bishop(py.sprite.Sprite):
#
#class Rook(py.sprite.Sprite):
#
#class King(py.sprite.Sprite):
#
#class Queen(py.sprite.Sprite):


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (184, 140, 100)
BEIGE = (255, 233, 197)

py.init()
Board = Board()
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

    py.display.flip()

    clock.tick(30)
