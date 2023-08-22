import pygame
import keyboard
from utils.colours import palette
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

CANVAS_CLR_1 = (129, 128, 128)
CANVAS_CLR_2 = (194, 192, 192)


#tools
brush = palette[0]
brush_color = brush
previous_brush_color = brush_color
eraser_color = TRANSPARENCY
eraser = eraser_color
tool = brush

brush_size = 1

FPS = 250 

#size of window
WIDTH, HEIGHT = 830, 900


#canvas settings
ROWS = COLS = 32

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = 16

BG_COLOR = GREY

DRAW_GRID_LINES = False

#Button images
brush_img = pygame.image.load('brush.png')
eraser_img = pygame.image.load('eraser.png')


def font(size):
    return pygame.font.SysFont("Minecraft", size)

