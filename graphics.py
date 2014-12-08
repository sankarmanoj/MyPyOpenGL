import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices = (
	(1,-1,-1),
	(1,1,-1),
	(-1,1,-1),
	(-1,-1,-1),
	(1,-1,1),
	(1,1,1),
	(-1,-1,1),
	(-1,1,1),
	)
edges=(
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
	)
surfaces=(
(0,1,2,3),
(3,2,7,6),
(6,5,7,4),
(4,5,1,0),
(3,5,7,2),
(4,0,3,6)
)
ground_vertices = (
	(-10,-0.1,-100),
	(-10,-0.1,100),
	(10,-0.1,100),
	(10,0.1,-100)
	)
colors = (
	(1,0,0),
	(1,1,1),
	(0,0,0),
	(1,1,0),
	(1,0,1),
	(0,1,1),
	(1,0,0),
	(1,1,1),
	(0,0,0),
	(1,1,0),
	(1,0,1),
	(0,1,1)
	)
def ground():
	glBegin(GL_QUADS)
	glColor3f(0.1,0.1,0.1)
	for vertex in ground_vertices:
		glVertex3fv(vertex)
	glEnd()
def Cube():
	glBegin(GL_QUADS)
	glColor3f(0,1,0)
	x=0
	for surface in surfaces:
		x=0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])	
	glEnd()
	
def main():
	object_passed = False
	pygame.init()
	pygame.key.set_repeat(300,100)
	display = (600,600)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
	gluPerspective(45,(display[0]/display[1]),2,50)
	glTranslatef(0,0,-50)
	while not object_passed:
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key ==pygame.K_UP:
					glTranslatef(0,-0.1,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,0.1,0)
				if event.key ==pygame.K_LEFT:
					glTranslatef(0.1,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(-0.1,0,0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glTranslatef(0,0,0.2)
		pos = glGetDoublev(GL_MODELVIEW_MATRIX)
		camera_z =pos[3][2]
		camera_x=pos[3][0]
		camera_y=pos[3][1]
		if camera_z <0:
			object_passed = True
		ground()
		Cube()
		pygame.display.flip()# Change to flip
		pygame.time.wait(10)
for x in range(10):
	main() 			
		