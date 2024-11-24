import pygame
import sys
from game import Game

pygame.init()
dark_blue = (44,44,127)
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()                    
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_r and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_SPACE and game.game_over == False:
                game.drop_down()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()


    screen.fill(dark_blue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)