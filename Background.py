import pygame

from tools import load_image


class Background(pygame.sprite.Sprite):

    def __init__(self, size, *group):
        super().__init__(*group)
        Background.image = load_image("Images/background.png")
        self.image = Background.image
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        self.rect = (self.image.get_rect())
