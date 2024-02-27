import pygame
from tools import load_image


class Over(pygame.sprite.Sprite):
    def __init__(self, size, *group):
        super().__init__(*group)
        Over.image = load_image("Images/Game_over.png")
        self.image = Over.image
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()


def game_over(screen, size, width, group):
    while True:
        Over(size, group)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

        font = pygame.font.Font(None, 75)
        string_rendered = font.render('Press "Escape" to get back to main menu', 1, pygame.Color('white'))
        text_rect = string_rendered.get_rect()
        text_rect.topleft = (width // 2 - text_rect.width // 2, 900)
        group.draw(screen)
        screen.blit(string_rendered, text_rect)
        pygame.display.flip()
