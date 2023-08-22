from utils import *
import keyboard

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
(canvas_x, canvas_y) = (50, 30)

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
    x = brush_size
    text_font = font(15)

    win.fill(BG_COLOR)
    # draw_background
    canvas_bg()
    win.blit(canvas, (canvas_x, canvas_y))
    draw_grid(canvas, grid)
    brush_size_text = text_font.render(f'Brush size: {x}', True, WHITE)
    win.blit(brush_size_text, (450, 800))


    for button in buttons:
        button.draw(win)
    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = (y - canvas_y)  // PIXEL_SIZE
    col = (x - canvas_x) // PIXEL_SIZE

    if row >= ROWS or col >= COLS or row <= canvas_y or col <= canvas_x:
        raise IndexError

    return row, col

button_y = HEIGHT - TOOLBAR_HEIGHT/2 -25
buttons = [
    Button(5, 30, 50, 50, TRANSPARENCY, "Eraser", WHITE),
    Button(5, 80, 50, 50, brush_color, "Brush", WHITE)
]


def colour_buttons():
    button_pos_x = 570
    button_pos_y = 28
    colours = 0
    colour_palette_width = int(palette_w / 8)
    for i in range(colour_palette_width):
        for i in range(8):
            buttons.append(Button(button_pos_x, button_pos_y, 30, 30, palette[colours]))
            button_pos_x = button_pos_x + 29
            colours = colours + 1
        button_pos_x = 570
        button_pos_y = button_pos_y + 29

def hotkey():
    global tool
    global brush_size
    if keyboard.is_pressed('e') and tool == brush:
        tool = eraser
    if keyboard.is_pressed('b') and tool == eraser:
        tool = brush

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

colour_buttons()

#main loop
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_EQUALS and brush_size < 3:
                    brush_size = brush_size + 1
                if event.key == pygame.K_MINUS and brush_size > 1:
                    brush_size = brush_size - 1

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
        
            if pos[0] > canvas_x and pos[1] > canvas_y and tool == brush:
                try:
                    brushsize()                
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue

                        if button.text == "Brush":
                            brush_color = previous_brush_color
                        else:
                            previous_brush_color = brush_color
                            brush_color = button.color

                        if button.text == "Eraser":
                            tool = eraser
                        break

                        
            if pos[0] > canvas_x and pos[1] > canvas_y and tool == eraser:            
                try:
                    brushsize()
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue

                        if button.text == "Brush":
                            tool = brush
                      
                        break           
    draw(WIN, grid, buttons)
    hotkey()
    


pygame.quit()