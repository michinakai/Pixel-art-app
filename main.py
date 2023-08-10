from utils import *
from colours import *

#Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.SRCALPHA)

#Custom window icon
icon = pygame.image.load('riceprite-icon.png')
pygame.display.set_caption("Riceprite")
pygame.display.set_icon(icon)

canvas = pygame.Surface((PIXEL_SIZE * COLS, PIXEL_SIZE * ROWS), pygame.SRCALPHA)
canvas_color = canvas.fill(WHITE)
canvas_w = canvas.get_width()
canvas_h = canvas.get_height()
canvas_pos = (canvas_x, canvas_y) = (50, 30)

half_w = canvas_w / 2
half_h = canvas_h / 2

bg_canvas = pygame.Surface((2,2))

def canvas_bg():
    pygame.draw.rect(WIN, BLACK, pygame.Rect((canvas_x - 3), (canvas_y - 3), (canvas_w + 6), (canvas_h + 6)), 3)

    for x in range(bg_canvas.get_width()):
        for y in range(bg_canvas.get_height()):
            bg_canvas.set_at([x, y], CANVAS_CLR_1 if (x + y) % 2 == 0 else CANVAS_CLR_2)
    WIN.blit(pygame.transform.scale(bg_canvas, (canvas_w, canvas_h)), (canvas_x, canvas_y))

    
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid        

def draw_grid(canvas, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(canvas, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

#If the draw grid line setting is set to true draw grid line
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(canvas, BLACK, (0, i * PIXEL_SIZE), (canvas_w, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(canvas, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, canvas_h - TOOLBAR_HEIGHT))

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    # draw_background
    canvas_bg()
    win.blit(canvas, (canvas_x, canvas_y))
    draw_grid(canvas, grid)

    for button in buttons:
        button.draw(win)
    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = (y - canvas_y)  // PIXEL_SIZE
    col = (x - canvas_x) // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

button_y = HEIGHT - TOOLBAR_HEIGHT/2 -25
buttons = [
    Button(500, button_y, 50, 50, TRANSPARENCY, "Eraser", WHITE),
    Button(450, button_y, 50, 50, brush_color, "Brush", WHITE)
]


def clr_buttons():
    button_pos_x = 50
    colours = 0
    for i in range(palette_w):
        buttons.append(Button(button_pos_x, button_y, 25, 50, palette[colours]))
        button_pos_x = button_pos_x + 20
        colours = colours + 1

clr_buttons()

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, TRANSPARENCY)

#main loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            
        
            if pos > canvas_pos and tool == brush:
                try:
                    row, col = get_row_col_from_pos(pos)
                    grid[row][col] = brush_color                     
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                        
                        brush_color = button.color
                        break

                        
            if pos > canvas_pos and tool == eraser:            
                try:
                    row, col = get_row_col_from_pos(pos)
                    grid[row][col] = ERASER_CLR
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                      
                        break            
    draw(WIN, grid, buttons)


pygame.quit()