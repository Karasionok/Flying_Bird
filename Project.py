import pygame
import random

from Background import Background
from Bird import Bird
from Borders import Border
from Pipe import Pipe
from tools import load_image

pygame.init()
size = WIDTH, HEIGHT = 1200, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Bird')
counter = 0
# groups of sprites
birds = pygame.sprite.Group()
pipes = pygame.sprite.Group()
borders = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
# timers
clock = pygame.time.Clock()
MOVEMENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEMENT, 10)
NEW_PIPE = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_PIPE, 5000)
FALLING = pygame.USEREVENT + 1
pygame.time.set_timer(FALLING, 10)
# flags
main_menu = True
running = True
game_over = True
next_level = True


def main_menu():
    pass


def gaming():
    global next_level
    global running
    global counter
    bird = Bird(pipes, birds)
    background = Background(size, backgrounds)
    Border(0, 0, size[0], 0, borders)
    Border(0, size[1], size[0], size[1], borders)

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
                if bird.update() is False:
                    print(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        for sprite in pipes:
            if sprite.get_x() < -400:
                sprite.kill()
                counter += 0.5
                if counter == 25:
                    next_level = True  # TODO summon func
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(str(int(counter)), 1, pygame.Color('black'))
        counter_rect = string_rendered.get_rect()
        counter_rect.topleft = (550, 0)

        backgrounds.draw(screen)
        birds.draw(screen)
        pipes.draw(screen)
        screen.blit(string_rendered, counter_rect)
        pygame.display.flip()
        clock.tick(500)

    screen.fill(pygame.Color("black"))
    pygame.quit()


if __name__ == '__main__':
    gaming()
