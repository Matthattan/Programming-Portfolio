import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooterman")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5

YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT = 55, 40
RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT = 55, 40


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('GameInPython\Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('GameInPython\Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT)), 270)


spaceshipWidth, spaceshipHeight = 55, 40

def drawWindow(red, yellow):       
    WIN.fill(RED)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellowHnMnt(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # Left
            yellow.x -= VEL
    
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # Right
            yellow.x += VEL
        
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # Up
            yellow.y -= VEL
        
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: # Down
            yellow.y += VEL

def redHnMnt(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # Left
            red.x -= VEL
    
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # Right
            red.x += VEL
        
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # Up
            red.y -= VEL
        
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT: # Down
            red.y += VEL

def main():
    red = pygame.Rect(700, 300, RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellowHnMnt(keys_pressed, yellow)
        redHnMnt(keys_pressed, red)
        drawWindow(red, yellow)
    
    pygame.quit()


if __name__ == "__main__":
    main()