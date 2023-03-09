import pygame
from pygame import mixer
from pygame.locals import *
import random


# pygame.mixer.pre_init(44100, -16, 2, 512)
# mixer.init()
pygame.init()

#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 840
screen_height = 450

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

class Paddle():
	def __init__(self,x, y):
		self.surf=pygame.Surface((10,60))
		self.surf.fill((255,255,255))	
		self.x = x
		self.y = y
		self.last_shot = pygame.time.get_ticks()


	def update(self):
		#set movement speed
		speed = 10
		#set a cooldown variable
		cooldown = 350 #milliseconds
		game_over = 0
		


		#get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_UP] and self.y >30:
			self.y = self.y - speed
		if key[pygame.K_DOWN] and self.y < 420:
			self.y = self.y + speed
		#record current time
		time_now = pygame.time.get_ticks()
		#shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			bullet = Bullets(self.x,self.y)
			self.last_shot = time_now
        #update mask
		screen.blit(self.surf,(self.x,self.y))
		      
#Create bullet class
class Bullets():
		def __init__(self, x, y):
			self.surf=pygame.Surface((10,10))
			self.surf.fill((254,255,255))			
			self.x = x
			self.y = y
		key = pygame.key.get_pressed()
		def update(self):
			self.x += 5
			screen.blit(self.surf,(self.x,self.y))
		if key[pygame.K_SPACE]:
			self.surf=pygame.Surface((10,10))
			self.surf.fill((254,255,255))			
			self.x = x
			self.y = y

			
#create player
paddle = Paddle(50, 225)
x = Bullets(50, 225)
run = True
while run:

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				run =False
	screen.fill((0, 0, 0))
	x.update()
	paddle.update()
	pygame.display.update()
	pygame.display.flip()
	clock.tick(fps)

pygame.quit()
