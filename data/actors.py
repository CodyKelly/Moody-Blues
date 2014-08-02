__author__ = 'lizardfingers'

import pygame, random

baddyGroup = pygame.sprite.Group()
actors = pygame.sprite.Group()

class Actor(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.windowWidth = 800
        self.windowHeight = 600
        self.image = pygame.image.load(imagePath).convert()
        self.image.set_colorkey((100,100,100))
        self.rect = self.image.get_rect()
        actors.add(self)

class Player(Actor):
    def __init__(self):
        Actor.__init__(self, 'pictures/smiley.png')
        self.rect.centerx = self.windowWidth/2 #This is half the window width, but I'm too tired to do this right right now
        self.rect.y = self.windowHeight-128
        self.speed = 10
        self.isAlive = True
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.move('left')
        if keys[pygame.K_RIGHT]:
            self.move('right')
        if keys[pygame.K_UP]:
            self.move('up')
        if keys[pygame.K_DOWN]:
            self.move('down')
        for baddy in baddyGroup.sprites():
            if pygame.sprite.collide_rect(self, baddy):
                self.isAlive = False
    def move(self, direction):
        if direction == 'left':
            if not self.rect.left - self.speed < 0:
                self.rect.x -= self.speed
        elif direction == 'right':
            if not self.rect.right + self.speed > self.windowWidth:
                self.rect.x += self.speed
        elif direction == 'up':
            if not self.rect.top - self.speed < 0:
                self.rect.y -= self.speed
        elif direction == 'down':
            if not self.rect.bottom + self.speed > self.windowHeight:
                self.rect.y += self.speed

class Baddy(Actor):
    def __init__(self):
        Actor.__init__(self, 'pictures/baddy.png')
        baddyGroup.add(self)
        self.rect.x = random.randint(0,self.windowWidth-self.rect.width)
        self.rect.y = 0-self.rect.height
        self.speed = random.randint(1,5)
    def update(self, keys):
        if not self.rect.y > self.windowHeight:
            self.rect.y += self.speed
        else:
            self.kill()

class Spawner(object):
    def __init__(self):
        self.gameTimer = 0
        self.spawnTimer = 80
        self.timerCount = 0
    def update(self):
        self.gameTimer += 1
        if self.timerCount < int(self.spawnTimer - self.gameTimer/100):
            self.timerCount += 1
        else:
            baddyGroup.add(Baddy())
            self.timerCount = 0
    def reset(self):
        self.gameTimer = 0
        self.timerCount = 0

spawner = Spawner()

def update(keys):
    actors.update(keys)
    spawner.update()

def draw(screen):
    actors.draw(screen)

def reset():
    for a in actors:
        a.kill()
    spawner.reset()
