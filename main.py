from utils import *
from PIL import Image
import keyboard
import os
import math

#Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 
                              pygame.RESIZABLE | pygame.SRCALPHA)

#Custom window icon
icon = pygame.image.load('riceprite-icon.png')
pygame.display.set_caption("Riceprite")
pygame.display.set_icon(icon)

#Canvas variables
canvas = pygame.Surface((PIXEL_SIZE * COLS, PIXEL_SIZE * ROWS), pygame.SRCALPHA)
canvas_color = canvas.fill(WHITE)
canvas_w = canvas.get_width()
canvas_h = canvas.get_height()
(canvas_x, canvas_y) = (50, 50)

half_w = canvas_w / 2
half_h = canvas_h / 2

bg_canvas = pygame.Surface((2,2))

#Creates different coloured squares for background of the canvas
def canvas_bg():
    pygame.draw.rect(WIN, BLACK, pygame.Rect((canvas_x - 3), (canvas_y - 3), 
                                             (canvas_w + 6), (canvas_h + 6)), 3)

    for x in range(bg_canvas.get_width()):
        for y in range(bg_canvas.get_height()):
            bg_canvas.set_at([x, y], CANVAS_CLR_1 if (x + y) % 2 == 0 
                             else CANVAS_CLR_2)
    WIN.blit(pygame.transform.scale(bg_canvas, (canvas_w, canvas_h)), 
             (canvas_x, canvas_y))

#initiates grid   
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid        

#draws the grid
def draw_grid(canvas, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(canvas, pixel, 
                    (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

#If the draw grid line setting is set to true draw grid line
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(canvas, BLACK, (0, i * PIXEL_SIZE), 
                             (canvas_w, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(canvas, BLACK, (i * PIXEL_SIZE, 0), 
                             (i * PIXEL_SIZE, canvas_h - TOOLBAR_HEIGHT))

#Function to render everything
def draw(win, grid, buttons):
    x = brush_size
    text_font = font(15)

    win.fill(BG_COLOR)
    canvas_bg()
    win.blit(canvas, (canvas_x, canvas_y))
    draw_grid(canvas, grid)
    brush_size_text = text_font.render(f'Brush size: {x}', True, WHITE)
    win.blit(brush_size_text, (160, 600))

    for button in buttons:
        button.draw(win)
    pygame.display.update()

#Gets the pixel that needs ti be filled 
def get_row_col_from_pos(pos):
    x, y = pos
    row = (y - canvas_x)  // PIXEL_SIZE
    col = (x - canvas_y) // PIXEL_SIZE

    if row >= ROWS or col >= COLS:
        raise IndexError

    return row, col

#List to contain the buttons
buttons = [
    Button(48, canvas_h + 60, 50, 50, TRANSPARENCY, "eraser.png"),
    Button(98, canvas_h + 60, 50, 50, brush_color,"brush.png")
]

#A loop which goes through the imported colour palette and make buttons
def draw_colour_button():
    button_pos_x = canvas_w + 60
    button_pos_y = 46
    colours = 0
    colour_palette_width = int((palette_w // 8))

    for i in range(colour_palette_width):
        for i in range(8):
            buttons.append(Button(button_pos_x, button_pos_y, 30, 30, 
                                  palette[colours]))
            button_pos_x = button_pos_x + 29
            if colours < (palette_w - 1):
                colours = colours + 1
        button_pos_x = canvas_w + 60
        button_pos_y = button_pos_y + 29

    #Draws the remaining colours if colour palette is not divisible by 8    
    extra_row = 0

    if palette_w % 8 != 0:
        extra_row = 1

    if extra_row == 1:
        button_pos_x = canvas_w + 60
        for i in range(palette_w - (colour_palette_width * 8)):
            buttons.append(Button(button_pos_x, button_pos_y, 30, 30, 
                                  palette[colours]))
            button_pos_x = button_pos_x + 29
            if colours < (palette_w - 1):
                colours = colours + 1
    
#Keyboard shortcut to switch tools
def hotkey():
    global tool
    global brush_size
    if keyboard.is_pressed('e') and tool == brush:
        tool = eraser
    if keyboard.is_pressed('b') and tool == eraser:
        tool = brush

#Draws the lines or erases based on brush size
def brushsize():
    row, col = get_row_col_from_pos(pos)
    
    #brush sizes
    if brush_size == 1 and tool == brush:
        grid[row][col] = brush_color
    
    if brush_size == 2 and tool == brush:
        grid[row][col] = brush_color
        grid[row-1][col] = brush_color
        grid[row][col-1] = brush_color
        grid[row-1][col-1] = brush_color

    if brush_size == 3 and tool == brush:
        grid[row][col] = brush_color
        grid[row-1][col] = brush_color
        grid[row][col-1] = brush_color
        grid[row+1][col] = brush_color
        grid[row][col+1] = brush_color

    #eraser sizes
    if brush_size == 1 and tool == eraser:
        grid[row][col] = eraser_color
    
    if brush_size == 2 and tool == eraser:
        grid[row][col] = eraser_color
        grid[row-1][col] = eraser_color
        grid[row][col-1] = eraser_color
        grid[row-1][col-1] = eraser_color

    if brush_size == 3 and tool == eraser:
        grid[row][col] = eraser_color
        grid[row-1][col] = eraser_color
        grid[row][col-1] = eraser_color
        grid[row+1][col] = eraser_color
        grid[row][col+1] = eraser_color

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, TRANSPARENCY)

colour_list()
draw_colour_button()

#main loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Make the brush size only increase or decrease by 1 when releasing the 
        # key and set boundary for brush sizes
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_EQUALS and brush_size < 3:
                    brush_size = brush_size + 1
                    
                if event.key == pygame.K_MINUS and brush_size > 1:
                    brush_size = brush_size - 1

        #Run this if mouse is clicked
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            #Only draw if on the canvas, if not, check if a button was pressed
            if pos[0] > canvas_x and pos[1] > canvas_y and tool == brush:
                try:
                    brushsize()                
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                        
                        #Keeps the brushes previous colour
                        if button.img == "brush.png":
                            brush_color = previous_brush_color
                        else:
                            previous_brush_color = brush_color
                            brush_color = button.color

                        #Switches tools if eraser button is pressed
                        if button.img == "eraser.png":
                            tool = eraser
                        break

            #Only erase if on the canvas, if not, check if a button was pressed            
            if pos[0] > canvas_x and pos[1] > canvas_y and tool == eraser:            
                try:
                    brushsize()
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                        
                        #Switches tools if brush button is pressed
                        if button.img == "brush.png":
                            tool = brush
                      
                        break           
    draw(WIN, grid, buttons)
    hotkey()
    
    


pygame.quit()