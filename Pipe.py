import pygame

from tools import load_image


class Pipe(pygame.sprite.Sprite):
    V = -1

    def __init__(self, size, turning=False, *group):
        super().__init__(*group)
        Pipe.image = load_image("Images/Pipe.png", -1)
        self.image = Pipe.image
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.image.get_width(),
                                                         self.image.get_height() * self.size))
        self.rect = self.image.get_rect()

        if turning:
            self.image = pygame.transform.flip(self.image, 0, 1)
            self.rect.x = 1300
            self.rect.y = -100
        else:
            self.rect.x = 1300
            self.rect.y = 1100 - self.image.get_height()

    def get_x(self):
        return self.rect.x

    def update(self):
        self.rect = self.rect.move((self.V, 0))
