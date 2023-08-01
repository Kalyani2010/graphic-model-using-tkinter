import pygame
import random
import sys
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - player_size * 2]
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
def create_enemies():
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
def draw_objects(player_pos, enemy_list):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
def update_enemy_positions(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += 20
        else:
            enemy_list.pop(idx)
def collision_check(player_pos, enemy_list):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False
def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_size
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_size
    create_enemies()
    update_enemy_positions(enemy_list)
    if collision_check(player_pos, enemy_list):
        pygame.quit()
        sys.exit()
    draw_objects(player_pos, enemy_list)
    clock.tick(30)
    pygame.display.update()