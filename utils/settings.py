import pygame
pygame.init()
pygame.font.init()

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GREY = (127, 127, 127)


FPS = 60 

#size of window
WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True



def getfont(size):
    return pygame.font.SysFont("Minecraft", size)