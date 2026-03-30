import random
import pygame as pg
import sys
import pygame.draw

# Initialize pygame
pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("DESMOS")
clock = pg.time.Clock()

toScreen = lambda p: (int(WIDTH / 2 + p[0] * 50)-WIDTH/4, int(HEIGHT / 2 - p[1] * 50)+HEIGHT/2.5)

vx = [0, 5, 10]
vy = [0, 10, 0]

R = lambda: random.randint(0, 2)

vert = [(vx[i], vy[i]) for i in range(3)]

a = lambda p, v: [(p[0] + v[0]) / 2, (p[1] + v[1]) / 2]

N = range(1, 200)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]: running = False

    point = [0.0, 0.0]
    for _ in N:
        point = a(point, vert[R()])
        pg.draw.circle(screen, (255, 255, 255), toScreen(point), 1)

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()