import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooterman")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60

spaceshipWidth, spaceshipHeight = 55, 40

def drawWindow():       
    WIN.fill(RED)
    WIN.blit(yellowSpaceshipImage, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()
    
    pygame.quit()


if __name__ == "__main__":
    main()