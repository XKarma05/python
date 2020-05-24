import pygame
from random import randrange
import time
import msvcrt

white = (255, 255, 255)
red = (213, 50, 80)
blue = (50, 153, 213)

wH = 400
wW = 600

pygame.init()

fen = pygame.display.set_mode((wW, wH))
pygame.display.set_caption('ca c\'est mon snake')

snake_block = 10

font = pygame.font.SysFont("comicsansms", 20)

def score(points):
    pygame.draw.rect(fen, white, (0, 0, 200, 25))
    value = font.render("Your Score: " + str(points), True, red)
    fen.blit(value, (10, 0))

def serpent(snake):
    for coords in snake:
        pygame.draw.rect(fen, blue, (coords[0]*10, coords[1]*10, snake_block, snake_block))

def food():
    x, y = randrange(60), randrange(40)
    pygame.draw.rect(fen, red,  (x*10+2, y*10+2, 6, 6))
    return x, y

def jeu():
    fen.fill(white)

    snake = []
    x0, y0 = 30, 20
    dx, dy = 0, 0
    snake.append((x0, y0))

    score(0)

    snakeL = 1
    grandir = False
    flip = True

    serpent(snake)
    foodx, foody = food()
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    dy = -1
                    flip = True
                if (event.key == pygame.K_DOWN):
                    dy = 1
                    flip = True
                if (event.key == pygame.K_LEFT):
                    dx = -1
                    flip = False
                if (event.key == pygame.K_RIGHT):
                    dx = 1
                    flip = False

            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()

        time.sleep(0.1)

        if(flip == True):
            y0 += dy
        else:
            x0 += dx

        if(x0 < 0 or x0 > wW/10 or y0 < 0 or y0 > wH/10):
            running = False

        for part in snake[:-1]:
            if(part == (x0, y0)):
                running = False

        if(x0 == foodx and y0 == foody):
            score(snakeL)
            snakeL += 1
            foodx, foody = food()
            pygame.display.flip()
            grandir = True


        if(grandir == False):
            pygame.draw.rect(fen, white, (snake[0][0]*10, snake[0][1]*10, 10, 10))
            del snake[0]
        else:
            grandir = False


        snake.append((x0, y0))
        serpent(snake)

        pygame.display.flip()

    rejouer = font.render("Appuyez sur r pour rejouer ou sur q pour quitter", True, red)
    fen.blit(rejouer, (wW // 6, wH // 3))
    pygame.display.flip()

def main():
    jeu()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    jeu()
                if event.key == pygame.K_a:
                    pygame.quit()
                    exit()

main()
