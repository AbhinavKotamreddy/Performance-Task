import pygame
from pygame import mixer
from pygame.locals import *
import random
from random import randint
import time


# pygame.mixer.pre_init(44100, -16, 2, 512)
# mixer.init()
pygame.init()

#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 840
screen_height = 450
bullets = []

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Totally Regular Normal Standard Typical Common Ordinary Traditional Simple Conventional Natural Commonplace Pong')

class Paddle():
	def __init__(self,x, y,team):
		self.surf=pygame.Surface((10,60))
		self.surf.fill((255,255,255))	
		self.x = x
		self.y = y
		self.team = team
		self.time = time.time()
		self.rect = self.surf.get_rect()
		self.rect.center = (self.x, self.y)



	def update(self):
		#set movement speed
		speed = 10
		


		#get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_w] and self.team == 1:
			self.y = self.y - speed
		if key[pygame.K_s] and self.team == 1:
			self.y = self.y + speed
		if key[pygame.K_d] and self.team == 1:
			self.x = self.x + speed
		if key[pygame.K_a] and self.team == 1:
			self.x = self.x - speed
		#record current time
		#shoot
		if key[pygame.K_SPACE] and time.time() - self.time > 0.3 and self.team == 1:
			bullets.append(Bullet(self.x, self.y, self.team))
			self.time = time.time()
		if key[pygame.K_UP] and self.team == 2:
			self.y = self.y - speed
		if key[pygame.K_DOWN] and self.team ==2:
			self.y = self.y + speed
		if self.y > 410:
			self.y = 410
		if self.y < 40:
			self.y = 40
		if key[pygame.K_LEFT] and time.time() - self.time > 0.3 and self.team == 2:
			bullets.append(Bullet(self.x, self.y, self.team))
			self.time = time.time()
        #update mask
		self.rect.center = (self.x, self.y)
		screen.blit(self.surf,self.rect)
#Create bullet class
class Bullet:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.speed = 3
        self.surf = pygame.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        if self.x<0 or self.x > screen_width:
            return 1
        if self.team == 1:
             self.x = self.x + self.speed
        if self.team == 2:
             self.x = self.x - self.speed
        self.rect.center = (self.x, self.y)
        screen.blit(self.surf,self.rect)
class Ball:
	def __init__(self,x, y):
		self.x = x
		self.y = y
		self.velocity = [5,5]
		#self.velocity = [randint(4,8),randint(-8,8)]
		self.surf = pygame.Surface((10,10))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect()
	def update(self):
		if ball.rect.x>= 840:
			ball.velocity[0] *= -1
		if ball.rect.x<= 0:
			ball.velocity[0] += -1
		if ball.rect.y>= 450:
			ball.velocity[1] *= -1
		if ball.rect.y<= 0:
			ball.velocity[1] *=-1
		#self.rect.x += self.velocity[0]
		#self.rect.y += self.velocity[1]
		self.rect.center = (self.x, self.y)
		screen.blit(self.surf,self.rect)
	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8,8)



	
		
			
#create player
paddle = Paddle(50, 225, 1)
paddle2 = Paddle(800, 225, 2)
ball = Ball(420,225)
run = True
while run:

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				run =False
	"""if ball.rect.x>= 840:
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x<= 0:
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y>= 450:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y<= 0:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.x == paddle.rect.x and ball.rect.y == paddle.rect.y:
		ball.velocity[0]=-ball.velocity[0]
		"""
	screen.fill((0, 0, 0))
	paddle.update()
	paddle2.update()
	ball.update()
	for bullet in bullets:
		if bullet.update(): 
			bullets.remove(bullet)
	pygame.display.update()
	pygame.display.flip()
	clock.tick(fps)

pygame.quit()
