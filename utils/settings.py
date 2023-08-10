import pygame
from colours import palette
pygame.init()
pygame.font.init()


#colours
TRANSPARENCY = (0, 0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GREY = (38 , 38, 38)

ERASER_CLR = TRANSPARENCY

CANVAS_CLR_1 = (129, 128, 128)
CANVAS_CLR_2 = (194, 192, 192)


#tools
brush = brush_color = palette[0]
eraser = ERASER_CLR
tool = brush


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