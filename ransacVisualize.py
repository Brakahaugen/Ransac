import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


finish = False
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

clock = pygame.time.Clock()

def draw_circles():

    for i in range(0, len(table_x)):
        pygame.draw.circle(screen, BLUE, (int(table_x[i]+offset_x+WIDTH/2), int(table_y[i]+offset_y+HEIGHT/2)), 2)

        
f = open('dataset1.txt')
table_x = []
table_y = []

for l in f:
    row = l.split()
    table_x.append(float(row[0]))
    table_y.append(float(row[1]))

print(max(table_x))
print(max(table_y))
print(min(table_x))
print(min(table_y))

offset_x = ((abs(min(table_x)) + abs(max(table_x)))/2)
offset_y = ((abs(min(table_y)) + abs(max(table_y)))/2)
print(offset_x)
print(offset_y)

#model
r = 0
x = 0
y = 0

#n – minimum number of data points required to estimate model parameters
n = 10

#k – maximum number of iterations allowed in the algorithm
k = 100

#t – threshold value to determine data points that are fit well by model 
t = 100

#d – number of close data points required to assert that a model fits well to data


while not finish:

	screen.fill(BACKGROUND_COLOR)

	text = "Score:"

	draw_circles()

	#pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(10)

	pygame.display.update()