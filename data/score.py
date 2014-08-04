__author__ = 'lizardfingers'

import pygame

class Score(object):
    def __init__(self):
        self.score = 0
        self.timerLimit = 100
        self.timer = 0
        self.textSize = 80
    def update(self):
        if self.timer < self.timerLimit:
            self.timer += 1
        else:
            self.score += 1
            self.timer = 0
    def draw(self, screen):
        font=pygame.font.Font('pictures/Market_Deco.ttf',self.textSize)
        textpic=font.render(str(self.score), 1,(0,0,0))
        screen.blit(textpic, (10,10))