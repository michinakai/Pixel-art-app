from utils import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
icon = pygame.image.load('riceprite-icon.png')
pygame.display.set_caption("Riceprite")
pygame.display.set_icon(icon)

canvas = pygame.Surface((PIXEL_SIZE * COLS, PIXEL_SIZE * ROWS))
canvas_color = canvas.fill(WHITE)
canvas_w = canvas.get_width()
canvas_h = canvas.get_height()

canvas_pos = canvas_x, canvas_y = 50, 30

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



run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, WHITE)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 -25
buttons = [
    Button(10, button_y, 50, 50, RED)
]

#main game loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
  
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    break

    draw(WIN, grid, buttons)


pygame.quit()