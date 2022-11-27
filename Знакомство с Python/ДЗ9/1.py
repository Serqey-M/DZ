import pygame
import random


def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[0][i] == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win


pygame.init()
window = pygame.display.set_mode((300, 300))
screen = pygame.Surface((300, 300))
pygame.display.set_caption('крестики-нолики')
screen.fill((255, 255, 255))
field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
minloop = True
game_over = False
while minloop:
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 3)
    window.blit(screen, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            minloop = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1]//100][pos[0]//100] == '':
                field[pos[1]//100][pos[0]//100] = 'X'
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != '':
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = 'O'
            player_win = get_win_check(field, 'X')
            ai_win = get_win_check(field, 'O')
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption('Вы победили')
                else:
                    pygame.display.set_caption('Компьютер победил')
            elif field[0].count('X')+field[0].count('O')+field[1].count('X')+field[1].count('O')+field[2].count('X')+field[2].count('O') == 8:
                game_over = True
                pygame.display.set_caption('Ничья')
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'O':
                pygame.draw.line(screen, (255, 0, 0),
                                 (j*100+5, i*100+5), (j*100+95, i*100+95), 3)
                pygame.draw.line(screen, (255, 0, 0),
                                 (j*100+95, i*100+5), (j*100+5, i*100+95), 3)
            elif field[i][j] == 'X':
                pygame.draw.line(screen, (0, 0, 255),
                                 (j*100+5, i*100+5), (j*100+95, i*100+95), 3)
                pygame.draw.line(screen, (0, 0, 255),
                                 (j*100+95, i*100+5), (j*100+5, i*100+95), 3)
