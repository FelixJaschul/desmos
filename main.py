import pygame as pg
import sys

# Initialize pygame
pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("DESMOS")
clock = pg.time.Clock()

def polygon(*points):
    # Transform points to screen coordinates
    screen_points = []
    for p in points: screen_points.append((int(WIDTH/2 + p[0] * 50), int(HEIGHT/2 + p[1] * 50)))
    pg.draw.polygon(screen, (255, 255, 255), screen_points, 1)

S = lambda a, b: [a[0] - b[0], a[1] - b[1]] # SUB
A = lambda a, b: [a[0] + b[0], a[1] + b[1]] # ADD
M = lambda a, b: [a[0] * b, a[1] * b]       # MULT by scalar

# Primitives
L = lambda pa, pb: polygon(pa, pb)
T = lambda pa, pb, pc: polygon(pa, pb, pc)
t = lambda pos, vec1, vec2, scalar: T(M(A(vec1[0], pos), scalar), M(A(vec1[1], pos), scalar), M(A(vec1[2], pos), scalar))
q = lambda scalar, pos, vec: [t(pos, vec, vec, scalar), t(pos, [vec[3], vec[4], vec[5]], vec, scalar)]

x = -0.2  # x pos
z = -6.24 # z pos

# Init vertices for Scene
# SCENE 2
vA = [(0, 0), (0, 2), (2, 2), (0, 0), (2, 0), (2, 2)]
vB = [(0, 0), (0, 2), (-2, 3), (0, 0), (-2, -1), (-2, 3)]
vC = [(2, 0), (1.5, -1), (-2, -1), (0, 0), (-2, -1), (2, 0)]

# SCENE 1
v1 = [(-1,-1), (-1, 1), (1, 1), (-1,-1), (1, -1), (1, 1)]
v2 = [(-1,-1), (-1, 1), (1, 0.1), (-1,-1), (1, -0.1), (1, 0.1)]
v3 = [(-0.5,-0.1), (-0.5, 0.1), (1, 0.1), (-0.5,-0.1), (1, -0.1), (1, 0.1)]
v4 = [(-0.5, 0.1), (1, -1), (1, 1), (-0.5,-0.1), (-0.5, 0.1), (1, -1)]

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]: running = False
    if keys[pg.K_a]: x += 0.05
    if keys[pg.K_d]: x -= 0.05
    if keys[pg.K_w]: z -= 0.1
    if keys[pg.K_s]: z += 0.1

    s = (10 / (10 + z)) # scalar

    screen.fill((0, 0, 0))
    q(s, [0 + x, -1], vA)
    q(s, [0 + x, -1], vB)
    q(s, [0 + x, -1], vC)
    #q(s, [3 + x, 0], v1)
    #q(s, [-2 + x, 0], v2)
    #q(s, [-0.5 + x, 0], v3)
    #q(s, [1 + x, 0], v4)

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()
