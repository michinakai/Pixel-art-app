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


FPS = 250 

#size of window
WIDTH, HEIGHT = 800, 900


#canvas settings
ROWS = COLS = 32

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = 16

BG_COLOR = GREY

DRAW_GRID_LINES = False



def getfont(size):
    return pygame.font.SysFont("Minecraft", size)