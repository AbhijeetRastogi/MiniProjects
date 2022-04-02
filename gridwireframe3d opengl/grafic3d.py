import random
from tkinter.tix import MAIN
from unicodedata import name

from pip import main

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = list(list())

X = 2
Y = 2

X += 1
Y += 1

for y in range(Y):
    for x in range(X):
            vertices.append((x, y, random.random()))

edges = list(list())


for y in range(Y-1):
    for x in range(X-1):
        edges.append((x+X*y, X+x+X*y))
        edges.append((X+x+X*y, x+1+X*y ))
        edges.append((x+1+X*y, x+X*y ))
        edges.append((x+1+X*y, X+x+X*y))
        edges.append((X+x+X*y, X+x+1+X*y ))
        edges.append((X+x+1+X*y, x+1+X*y ))
    

surfaces = list(list())
for x in range(round((X-1)*(Y-1)/2)):
    surfaces.append((x, x+1, x+2))

color = (
    (0.071, 0.792, 0.0),
    (0.07, 0.8, 0.83),
    (0.88, 0.086, 0.90),
    (0.7, 0.8, 0.1),
    (0.98, 0.586, 0.186),
    (0.07, 0.08, 0.83),
)


def cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x +=1
        for point in surface:
            glColor3fv(color[x])
            glVertex3fv(vertices[point])
    glEnd()
    glBegin(GL_LINES)

    for edge in edges:
        for point in edge:
            glVertex3fv(vertices[point])

    glEnd()

if __name__ == "__main__":
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslate(-0.5, -0.5, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(0.1, 0, 0)
                if event.key == pygame.K_d:
                    glTranslatef(-0.1, 0, 0)
                if event.key == pygame.K_w:
                    glTranslatef(0, 0, 0.1)
                if event.key == pygame.K_s:
                    glTranslatef(0, 0, -0.1)
                if event.key == pygame.K_q:
                    glTranslatef(0, -0.1, 0)
                if event.key == pygame.K_e:
                    glTranslatef(0, 0.1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 4:
                    glTranslatef(0, 0, 0.1)
                if event.button == 5:
                    glTranslatef(0, 0, -0.1)

        glRotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)
