from math import *
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
def ground():
	glBegin(GL_QUADS)
	glColor3f(1,0,0)
	glVertex3f(-100,0,-100)
	glVertex3f(-100,0,100)
	glVertex3f(100,0,100)
	glVertex3f(100,0,-100)
	glEnd()
def pyramid(x,y,z):
	glPushMatrix()
	glTranslatef(x,y,z)
	glBegin(GL_QUADS)
	glColor3f(1,0,0)
	glVertex3f(-1,-0.1,-1)
	glVertex3f(1,-0.1,-1)
	glVertex3f(1,-0.1,1)
	glVertex3f(-1,-0.1,1)
	glEnd()
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,1)
	glVertex3f(0,1,0)
	glColor3f(0,1,0)
	glVertex3f(-1,-0.1,-1)
	glVertex3f(1,-0.1,-1)
	glVertex3f(1,-0.1,1)
	glVertex3f(-1,-0.1,1)
	glVertex3f(-1,-0.1,-1)
	glEnd()
	glPopMatrix()
def main():
	px = 0.1 
	y = 2
	z = -4
	pygame.init()
	pygame.key.set_repeat(300,100)
	display = (600,600)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
	glMatrixMode(GL_PROJECTION)
	gluPerspective(45,(display[0]/display[1]),0.5,50)	
	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_DEPTH_TEST);
	
	
	phi = 0
	while True:
		glLoadIdentity()
		gluLookAt(
		px,y,z,
		0,y-1,50,
		0,1,0
		)	
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key ==pygame.K_UP:
					y+=0.1
					print y
				if event.key == pygame.K_DOWN:
					y-=0.1
					print y
				if event.key ==pygame.K_LEFT:
					px+=0.1
					print px
				if event.key == pygame.K_RIGHT:
					px-=0.1
					print px
				if event.key ==pygame.K_HOME:
					glTranslatef(0,0,0.1)
				if event.key == pygame.K_END:
					glTranslatef(0,0,-0.1)
				if event.key==pygame.K_PAGEUP:
					z+=0.1
				if event.key==pygame.K_PAGEDOWN:
					z-=0.1
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		ground()
		pyramid(0,0,0)
		glPushMatrix()
		glTranslatef(-5,0,0)
		for x in range(5):
			glTranslatef(0,0,5)
			pyramid(0,0,0)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(5,0,0)
		for x in range(5):
			glTranslatef(0,0,5)
			pyramid(0,0,0)
		glPopMatrix()
		
		pygame.display.flip()
		pygame.time.wait(40)
main()	
	