import pygame
import sys
import random
pygame.init()
w = 800
h = 600
RED = (255,0,0)
BLUE = (0,0,255)
SPEED = 10
player_size = 50
player_pos = [w/2, h - 2 * player_size]
rand_col = (random.randint(1, 255), random.randint(1,255), random.randint(1,255))
screen = pygame.display.set_mode((w,h))
score = 0
food_size = 45
rand_pos = [random.randint(0,800 - food_size), 0]

pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
game_over = False
pygame.draw.rect(screen, rand_col, (rand_pos[0], rand_pos[1] ,food_size, food_size))

def detect_collision(player_pos, rand_pos):
  p_x = player_pos[0]
  p_y = player_pos[1]

  r_x = rand_pos[0]
  r_y = rand_pos[1]
  if r_x >= p_x and r_x < p_x + player_size or p_x >= r_x and p_x < r_x + food_size:
    if r_y >= p_y and r_y < p_y + player_size or p_y >= r_y and p_y < r_y:
      return True
  return False

while not game_over:
  rand_col = (random.randint(1, 255), random.randint(1,255), random.randint(1,255))
  rand_pos = [random.randint(0,800 - food_size), 0]
  for event in pygame.event.get():
    if event. type == pygame.quit:
      sys.quit
    if event.type == pygame.KEYDOWN:
      x = player_pos[0]
      y = player_pos[1]
      if event.key == pygame. K_LEFT:
        x -= player_size
      elif event.key == pygame. K_RIGHT:
        x += player_size
      if x >= 800:
        x = 800 - player_size
        game_over = True
        break
      elif x < 0:
        x = 0
        game_over = True
      player_pos = [x,y]
      if detect_collision(player_pos,rand_pos):
        score += 1
  screen.fill((0,0,0))

  pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1],player_size, player_size))
  if rand_pos[1] <= h and rand_pos[1]:
    rand_pos[0] += SPEED
  pygame.draw.rect(screen, rand_col, (rand_pos[0], rand_pos[1] ,food_size, food_size))
  pygame.display.update()