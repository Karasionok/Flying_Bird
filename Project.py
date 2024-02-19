import os
import sys
import pygame
import random

pygame.init()
size = 1200, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Bird')
birds = pygame.sprite.Group()
pipes = pygame.sprite.Group()
clock = pygame.time.Clock()
MOVEMENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEMENT, 10)
NEW_PIPE = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_PIPE, 5000)
FALLING = pygame.USEREVENT + 1
pygame.time.set_timer(FALLING, 10)
running = True


def main():
    Bird(birds)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOVEMENT:
                pipes.update()
            if event.type == NEW_PIPE:
                n = random.random() * 2 + 0.5
                Pipe(n, False, pipes)
                Pipe(1 / n, True, pipes)
            if event.type == FALLING:
                birds.update(False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    birds.update(jump=True)
        for sprite in pipes:
            if sprite.get_x() < -400:
                sprite.kill()

        screen.fill(pygame.Color("black"))
        birds.draw(screen)
        pipes.draw(screen)
        pygame.display.flip()
        clock.tick(1000)



    pygame.quit()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bird(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.v = 1
        Bird.image = load_image("Images/bird.png", -1)
        Bird.image = pygame.transform.scale(Bird.image, (150, 75))
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400

    def update(self, jump=False):
        if pygame.sprite.spritecollideany(self, pipes):
            running = False
        if not jump:
            self.a = 0.1
            self.v += self.a
            self.rect = self.rect.move((0, self.v))
        if jump:
            self.v = -5


class Pipe(pygame.sprite.Sprite):
    V = -1

    def __init__(self, size, turning=False, *group):
        super().__init__(*group)
        Pipe.image = load_image("Images/Pipe.png", -1)
        self.image = Pipe.image
        self.rect = self.image.get_rect()
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.image.get_width(),
                                                         self.image.get_height() * self.size))

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


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


if __name__ == '__main__':
    main()