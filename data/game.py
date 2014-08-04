__author__ = 'lizardfingers'

import pygame, actors, sys, score

pygame.init()


windowWidth = 800
windowHeight = 1000

screen = pygame.display.set_mode((windowWidth, windowHeight))

WHITE = (255,255,255)

clock = pygame.time.Clock()

caption = 'Moody Blues'
pygame.display.set_caption(caption)

def run():
    actors.reset()
    player = actors.Player()
    scoreKeeper = score.Score()
    while player.isAlive:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        actors.update(pygame.key.get_pressed(), player)
        scoreKeeper.update()
        actors.draw(screen)
        scoreKeeper.draw(screen)
        pygame.display.flip()
    else:
        run()