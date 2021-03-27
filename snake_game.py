import sys, pygame
from pygame.locals import *
from pygame import gfxdraw
import random
import time


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 25
GRID_COORD_MARGIN_SIZE = 0

window = (800,600)
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode(window)
pygame.display.set_caption('Jogo da cobra fodase')

background = pygame.Surface(window)
size=25

class Snake:
    x = 400
    y = 300
    lastX = x
    lastY = y
    size=size
    tail = []
    speed=size
    dirX=0
    dirY=0
    dead=False

    def __init__(self, screen, background):
        screen.blit(background, (self.x, self.y))
        self.rect = pygame.rect.Rect((self.x,self.y,self.size,self.size))
    

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not self.dirX == self.speed:
            self.dirX = -self.speed
            self.dirY = 0
        if key[pygame.K_RIGHT] and not self.dirX == -self.speed:
            self.dirX = self.speed
            self.dirY = 0
        if key[pygame.K_UP] and not self.dirY == self.speed:
            self.dirY = -self.speed
            self.dirX = 0
        if key[pygame.K_DOWN] and not self.dirY == -self.speed:
            self.dirY = self.speed
            self.dirX = 0
        return

    def move(self, foodX, foodY):
        if (self.y >= window[1]-self.size and self.dirY == self.speed) or (self.y <= 0 and self.dirY == -self.speed) or (self.x >= window[0]-self.size and self.dirX == self.speed) or (self.x <= 0 and self.dirX == -self.speed):
            self.die()
        
        self.lastX = self.x
        self.lastY = self.y
        self.x += self.dirX
        self.y += self.dirY

        self.justAdded = -1
        if self.x == foodX and self.y == foodY:
            self.justAdded = len(self.tail)
            if(len(self.tail) == 0):
                self.tail.append([self.lastX, self.lastY])
            else:
                self.tail.append(self.tail[-1:][0][:])
        
        listCopy=[]
        for i in self.tail:
            listCopy.append(i[:])
        
        for idx, item in enumerate(self.tail):
            if self.x == self.tail[idx][0] and self.y == self.tail[idx][1]:
                self.die()
            
            if idx == 0:
                self.tail[idx][0] = self.lastX
                self.tail[idx][1] = self.lastY
            elif not self.justAdded == idx:
                self.tail[idx][0] = listCopy[idx-1][0]
                self.tail[idx][1] = listCopy[idx-1][1]


    def draw(self, surface):
        self.rect = pygame.rect.Rect((self.x,self.y,self.size,self.size))
        pygame.draw.rect(screen, WHITE, self.rect)        
        for item in self.tail:
            self.rect = pygame.rect.Rect((item[0],item[1],self.size,self.size))
            pygame.draw.rect(screen, WHITE, self.rect)

    def die(self):
        self.dead = True


class Food:
    def __init__(self, screen, background, size):
        valX = window[0]-size
        valY = window[1]-size
        self.x = random.randint(1, valX/size) * size
        self.y = random.randint(1, valY/size) * size
        screen.blit(background, (self.x, self.y))
        self.rect = pygame.rect.Rect((self.x,self.y,size,size))

    def draw(self, surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def update(self, screen, background, size, snakeX, snakeY, tail):
        while (self.x == snakeX and self.y == snakeY) or any([self.x, self.y] == x for x in tail):
            valX = window[0]-size
            valY = window[1]-size
            self.x = random.randint(1, valX/size) * size
            self.y = random.randint(1, valY/size) * size
            self.rect = pygame.rect.Rect((self.x,self.y,size,size))

snake = Snake(screen=screen, background=background)
food = Food(screen=screen, background=background, size=snake.size)

while not snake.dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(BLACK)
    food.draw(surface=screen)
    snake.draw(screen)
    snake.handle_keys()
    snake.move(foodX=food.x, foodY=food.y)
    if not snake.justAdded == -1:
        food.update(screen=screen, background=background, size=snake.size, snakeX=snake.x, snakeY=snake.y, tail=snake.tail)
        
    pygame.display.update()

    for i in range(10):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_UP] or key[pygame.K_DOWN]:
            snake.handle_keys()
        time.sleep(.008)


sys.exit()