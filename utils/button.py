from .settings import *



class Button:
    def __init__(self, x, y, width, height, color,img = None, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.img = img
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        button_rect = pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(
            win, BLACK, (self.x, self.y, self.width, self.height), 2)
        
        if self.text:
            button_font = font(11)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width /
                                    2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))
        if self.img:
            img_surface = pygame.image.load(self.img)
            win.blit(img_surface, (self.x + self.width /
                                    2 - img_surface.get_width()/2, self.y + self.height/2 - img_surface.get_height()/2))
        
        
    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True