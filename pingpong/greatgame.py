import pygame
import sys
import random
import math
import copy

size = [700,500]

WHITE = [0xFF, 0xFF, 0xFF]
RED = [255, 0, 0]
BLACK = [0, 0, 0]
BLUE = [0, 0, 255]

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping pong!")

draw_objects = []
tiles = []

clock = pygame.time.Clock()

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

        self.color = [255,255,255]
        
    def draw(self, screen):
        print("draw")

class Ball(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.size = 10
 
    def draw(self, screen):
        self.x += self.speed_x
        self.y += self.speed_y
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )

class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 100
        self.height = 20
        self.line_width = 1
        self.fill_color = BLUE

    def draw(self, screen):
        self.x += self.speed_x
        self.size = [0,0, self.width, self.height]
        surface = pygame.Surface((self.width,self.height))
        surface.fill(self.fill_color)
        pygame.draw.rect(surface, self.color, self.size,self.line_width)
        screen.blit(surface, (self.x, self.y))

#create the ball
theBall = Ball(random.randrange(0, size[0]), 120)

draw_objects.append(theBall)

#create tiles
for i in range(0,2):
    y = i * 20
    for j in range(0,7):
        x = j * 100
        tiles.append([x,y])

tiles_start = copy.deepcopy(tiles)

print("tiles: %s" % len(tiles))

paddle = Paddle(20, size[1]-40)
paddle.width = 140
draw_objects.append(paddle)

draw_ob_start = draw_objects

def restart():
    global tiles
    global draw_objects
    draw_objects = draw_ob_start
    theBall.x = random.randrange(0, size[0])
    theBall.y = 120
    tiles = copy.deepcopy(tiles_start)
    theBall.speed_x = 0
    theBall.speed_y = 0

def ball_hits_paddle():
    if theBall.y >= paddle.y \
       and theBall.x >= paddle.x \
       and theBall.x <= paddle.x + paddle.width / 3:
        theBall.speed_x -= 2
        theBall.speed_y *= -1
    if theBall.y >= paddle.y \
       and theBall.x >= paddle.x + paddle.width / 3  \
       and theBall.x <= paddle.x + 2 * paddle.width / 3: 
        theBall.speed_y *= -1   
    if theBall.y >= paddle.y \
       and theBall.x >= paddle.x + 2 * paddle.width / 3  \
       and theBall.x <= paddle.x + paddle.width:
        theBall.speed_x += 2
        theBall.speed_y *= -1

def ball_hits_tile():
    for k in range(0, len(tiles)):
        if theBall.x >= tiles[k][0] \
           and theBall.x <= tiles[k][0] + 100 \
           and theBall.y < tiles[k][1] + 20:
            del tiles[k]
            theBall.speed_y *= -1
            break

def update():
    global tiles
    global draw_objects
    if theBall.x >= size[0] or theBall.x <= 0:
        theBall.speed_x *= -1
    if theBall.y >= size[1]:
        restart()
    if theBall.y <= 0:
        theBall.speed_y *= -1
        
    ball_hits_paddle()

    ball_hits_tile()
    
    #restart game when all tiles are cleared
    if len(tiles) == 0:
        draw_objects = []
            

def draw():
    screen.fill(BLACK)
    if len(draw_objects) > 0:
        for ob in draw_objects:
            ob.draw(screen)
    else:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("You win! Press space key to restart.",True,WHITE)
        screen.blit(text, [250, 250])
    for tile_coord in tiles:
        tile = Paddle(tile_coord[0], tile_coord[1])
        tile.fill_color = RED
        tile.draw(screen)

    if paddle.x <= 0 or paddle.x + paddle.width >= size[0]:
        paddle.speed_x = 0
        
    pygame.display.flip()
    clock.tick(60)
    
gameOn = True
while gameOn:
    update()
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameOn = False
        if event.type == pygame.KEYDOWN:
            if theBall.speed_x == 0 and theBall.speed_y == 0:
                theBall.speed_x = -6
                theBall.speed_y = 6
            if event.key == pygame.K_LEFT:
                paddle.speed_x = -10
                
            if event.key == pygame.K_RIGHT:
                paddle.speed_x = 10
                
            if event.key == pygame.K_SPACE:
                restart()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle.speed_x = 0
            if event.key == pygame.K_RIGHT:
                paddle.speed_x = 0


    
