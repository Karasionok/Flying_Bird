import pygame
from summon_results import summon_results

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


class InputBox:

    def __init__(self, x, y, w, h, font_txt, text='User'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.font = font_txt
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def main_menu(screen, clock, width, font_txt, cur):
    input_box = InputBox(400, 500, 140, 32, font_txt)
    while True:
        for event in pygame.event.get():
            input_box.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False, input_box.text
                elif event.key == pygame.K_ESCAPE:
                    return True, None
                elif event.key == pygame.K_BACKSPACE:
                    summon_results(screen, cur)
        screen.fill('black')
        font = pygame.font.Font(None, 75)
        string_rendered = font.render('Press "Space" to play', 1, pygame.Color('white'))
        text_rect = string_rendered.get_rect()
        text_rect.topleft = (width // 2 - text_rect.width // 2, 900)
        screen.blit(string_rendered, text_rect)

        font = pygame.font.Font(None, 50)
        quit_rendered = font.render('Press "Escape" to exit', 1, pygame.Color('white'))
        quit_rect = quit_rendered.get_rect()
        quit_rect.topleft = (0, 0)
        screen.blit(quit_rendered, quit_rect)

        font = pygame.font.Font(None, 50)
        string_rendered = font.render('Press "Backspace" to see top list', 1, pygame.Color('white'))
        text_rect = string_rendered.get_rect()
        text_rect.topleft = (550, 100)
        screen.blit(string_rendered, text_rect)

        font = pygame.font.Font(None, 50)
        quit_rendered = font.render('Enter your name', 1, pygame.Color('white'))
        quit_rect = quit_rendered.get_rect()
        quit_rect.topleft = (400, 400)
        screen.blit(quit_rendered, quit_rect)

        input_box.update()
        input_box.draw(screen)
        pygame.display.flip()
        clock.tick(500)
