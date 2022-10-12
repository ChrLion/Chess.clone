import pygame as py

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

py.init()

# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = py.display.set_mode(size)

py.display.set_caption("Chess")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = py.time.Clock()

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            quit()

    screen.fill(WHITE)

    py.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)
