import pygame

from tools import load_image


class Bird(pygame.sprite.Sprite):
    def __init__(self, pipes, borders, group):
        super().__init__(group)
        self.v = 1
        self.a = 0.1
        self.pipes = pipes
        self.borders = borders
        Bird.image = load_image("Images/Bird.png", -1)
        Bird.image = pygame.transform.scale(Bird.image, (100, 75))
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400

    def update(self):
        self.v += self.a
        self.rect = self.rect.move((0, self.v))
        if pygame.sprite.spritecollideany(self, self.pipes):
            return False
        elif pygame.sprite.spritecollideany(self, self.borders):
            return False

    def jump(self):
        self.v = -5
