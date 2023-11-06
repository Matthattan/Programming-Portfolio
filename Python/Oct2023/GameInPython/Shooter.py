import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooterman")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255,)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

bulletHitSound = pygame.mixer.Sound(os.path.join('Python-Portfolio/Python/Oct2023/GameInPython/Assets', 'Grenade+1.mp3'))
bulletFireSound = pygame.mixer.Sound(os.path.join('Python-Portfolio/Python/Oct2023/GameInPython/Assets', 'Gun+Silencer.mp3'))

healthFont = pygame.font.SysFont('papyrus', 40)
WinnerFont = pygame.font.SysFont('jokerman', 100)

FPS = 60
VEL = 5
BLT_VEL = 7
MAX_BLT = 5

YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT = 55, 40
RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT = 55, 40

yellowHit = pygame.USEREVENT + 1
redHit = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Python-Portfolio/Python/Oct2023/GameInPython\Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Python-Portfolio/Python/Oct2023/GameInPython\Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Python-Portfolio/Python/Oct2023/GameInPython\Assets', 'space.png')), (WIDTH, HEIGHT))

spaceshipWidth, spaceshipHeight = 55, 40

def drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth):       
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, WHITE, BORDER)

    redHealthText = healthFont.render(f"Health: {redHealth}", 1, WHITE)
    yellowHealthText = healthFont.render(f"Health: {yellowHealth}", 1, WHITE)

    WIN.blit(redHealthText, (WIDTH - redHealthText.get_width() - 10, 10))
    WIN.blit(yellowHealthText, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in redBullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellowBullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

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

def handleBullets(yellowBullets, redBullets, yellow, red):
    for bullet in yellowBullets:
        bullet.x += BLT_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redHit))
            yellowBullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellowBullets.remove(bullet)
    
    for bullet in redBullets:
        bullet.x -= BLT_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellowHit))
            redBullets.remove(bullet)
        elif bullet.x < 0:
            redBullets.remove(bullet)

def drawWinner(text):
    draw_text = WinnerFont.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))

    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, RSPACESHIP_WIDTH, RSPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, YSPACESHIP_WIDTH, YSPACESHIP_HEIGHT)

    yellowBullets = []
    redBullets = []

    redHealth = 1
    yellowHealth = 1

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and len(yellowBullets) < MAX_BLT:
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellowBullets.append(bullet)
                    bulletFireSound.play()
                
                if event.key == pygame.K_p and len(redBullets) < MAX_BLT:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    redBullets.append(bullet)
                    bulletFireSound.play()

            if event.type == redHit:
                redHealth -= 1
                bulletHitSound.play()
            
            if event.type == yellowHit:
                yellowHealth -= 1
                bulletHitSound.play()

        winnerText = ""

        drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth)

        if redHealth <= 0:
            winnerText = "Yellow Wins!"

        if yellowHealth <= 0:
            winnerText = "Red Wins!"

        if winnerText != "":
            drawWinner(winnerText)
            break

        keys_pressed = pygame.key.get_pressed()
        yellowHnMnt(keys_pressed, yellow)
        redHnMnt(keys_pressed, red)
        handleBullets(yellowBullets, redBullets, yellow, red)

    main()

if __name__ == "__main__":
    main()