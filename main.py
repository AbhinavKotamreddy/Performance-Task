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
		self.x = x
		self.y = y
		self.image = pygame.image.load("gun1.png")
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
		rect = self.image.get_rect(center = (self.x, self.y))
		screen.blit(self.image, rect)
		      
#Create bullet class
class Bullets(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("bullet2.png")
			self.rect = self.image.get_rect()
			self.rect.center = [x, y]

bullet_group = pygame.sprite.Group()
#create player
paddle = Paddle(50, 225)


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
	bullet_group.draw(screen)
	paddle.update()
	pygame.display.update()
	pygame.display.flip()
	clock.tick(fps)

pygame.quit()
