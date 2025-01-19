import pygame
import sys
from game import Game
from colors import Colors

pygame.init()
title_font = pygame.font.SysFont("Helvetica Neue", 40)
score_surface = title_font.render("Score:", True, Colors.white)
level_surface = title_font.render("Level:", True, Colors.white)
next_surface = title_font.render("Next Block:", True, Colors.white)
end_surface = title_font.render("GAME OVER", True, Colors.white)
screen = pygame.display.set_mode((550, 620))
score_rect = pygame.Rect(320, 80, 220, 60)
level_rect = pygame.Rect(320, 220, 220, 60)
next_rect = pygame.Rect(320, 360, 220, 180)
end_rect = pygame.Rect(320, 360, 220, 180)
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
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
            if event.key == pygame.K_SPACE and not game.game_over:
                game.drop_down()
            if event.key == pygame.K_BACKSPACE and not game.game_over:
                game.reset()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
            game.update_score(0)
            tick_interval = max(100, int(500 * (0.7 ** game.level))) 
            pygame.time.set_timer(GAME_UPDATE, tick_interval)

    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    level_value_surface = title_font.render(str(game.level), True, Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (320, 20, 50, 50))
    screen.blit(level_surface, (320, 160, 50, 50))
    screen.blit(next_surface, (320, 300, 50, 50))
    if game.game_over:
        screen.blit(end_surface, (315, 550, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, level_rect, 0, 10)
    screen.blit(level_value_surface, level_value_surface.get_rect(centerx=level_rect.centerx, centery=level_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)
