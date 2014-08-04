__author__ = 'lizardfingers'

import pygame, random

gameObjects = pygame.sprite.Group()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.windowWidth = 800
        self.windowHeight = 1000
        self.image = pygame.image.load(imagePath).convert()
        self.image.set_colorkey((100,100,100))
        self.rect = self.image.get_rect()
        self.tag = ''
        gameObjects.add(self)

class Player(GameObject):
    def __init__(self):
        GameObject.__init__(self, 'pictures/smiley.png')
        self.rect.centerx = self.windowWidth/2 #This is half the window width, but I'm too tired to do this right right now
        self.rect.y = self.windowHeight-128
        self.speed = 5
        self.isAlive = True
        self.tag = 'player'
    def update(self, keys):
        #react to player input
        if keys[pygame.K_LEFT]:
            self.move('left')
        if keys[pygame.K_RIGHT]:
            self.move('right')
        if keys[pygame.K_UP]:
            self.move('up')
        if keys[pygame.K_DOWN]:
            self.move('down')
    def move(self, direction):
        #this is a little redundant, but I think it helps readability
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

class Baddy(GameObject):
    def __init__(self):
        GameObject.__init__(self, 'pictures/baddy.png')
        self.rect.x = random.randint(0,self.windowWidth-self.rect.width)
        self.rect.y = 0-self.rect.height
        self.speed = random.randint(1,5)
        self.tag = 'badguy'
    def update(self, player):
        #move down until out of window, then kill self
        if not self.rect.y > self.windowHeight:
            self.rect.y += self.speed
        else:
            self.kill()
        #if this and the player collides, kill the player
        if(pygame.sprite.collide_rect(self, player)):
            player.isAlive = False

class Ball(GameObject):
    def __init__(self):
        GameObject.__init__(self, 'pictures/ball.png')
        self.rect.x = random.randint(0,self.windowWidth-self.rect.width)
        self.rect.y = 0-self.rect.height
        self.speed = 7
        self.tag = 'ball'
    def update(self, player):
        #move down until out of window, then kill self
        if not self.rect.y > self.windowHeight:
            self.rect.y += self.speed
        else:
            self.kill()
        #if this and the player collides, kill the player
        if(pygame.sprite.collide_rect(self, player)):
            for obj in gameObjects:
                if obj.tag == 'badguy' or obj.tag == 'ball':
                    obj.kill()
            self.kill()

class Spawner(object):
    def __init__(self):
        self.gameTimer = 0
        self.spawnTimer = 80
        self.timerCount = 0
        self.ballChance = 0.05
    def update(self):
        self.gameTimer += 1
        #make the timer shorter the longer the game goes on
        if self.timerCount < int(self.spawnTimer - self.gameTimer/100):
            self.timerCount += 1
        else:
            #when the timer equals the spawn timer, spawn a bad guy
            rand = random.random()
            if rand < self.ballChance:
                gameObjects.add(Ball())
            else:
                gameObjects.add(Baddy())
            self.timerCount = 0
    def reset(self):
        self.gameTimer = 0
        self.timerCount = 0

spawner = Spawner()

def update(keys, player):
    player.update(keys)
    for obj in gameObjects:
        if not obj == player:
            obj.update(player)
    spawner.update()

def draw(screen):
    gameObjects.draw(screen)

def reset():
    for thing in gameObjects:
        thing.kill()
    spawner.reset()
