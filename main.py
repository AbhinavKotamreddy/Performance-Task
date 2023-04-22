import pygame
from pygame import mixer
from pygame.locals import *
import random
from random import randint
import time

# mixer.init()
pygame.init()

#define fps
clock = pygame.time.Clock()
fps = 60

#define screen size
screen_width = 840
screen_height = 450
bullets = []
font = pygame.font.Font('freesansbold.ttf', 24)
font2 = pygame.font.Font('freesansbold.ttf', 15)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong But You Have A Gun')

#create Paddle Class
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

	#Define Function to display scores
	def displayScore(self, text, score, x, y, color):
		text = font.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x,y)
		screen.blit(text, textRect)
	#define function to display who wons
	def displayWin(self, text, x, y, color):
		text = font.render(text, True, color)
		textRect = text.get_rect()
		textRect.center = (x,y)
		screen.blit(text, textRect)

	def update(self):
		#set movement speed
		speed = 10
		#get controls for player 1
		key = pygame.key.get_pressed()
		if key[pygame.K_w] and self.team == 1:
			self.y = self.y - speed
		if key[pygame.K_s] and self.team == 1:
			self.y = self.y + speed
		if key[pygame.K_SPACE] and time.time() - self.time > 0.7 and self.team == 1:
			bullets.append(Bullet(self.x, self.y, self.team))
			self.time = time.time()
		#get controls for player 2
		if key[pygame.K_UP] and self.team == 2:
			self.y = self.y - speed
		if key[pygame.K_DOWN] and self.team ==2:
			self.y = self.y + speed
		if key[pygame.K_LEFT] and time.time() - self.time > 0.7 and self.team == 2:
			bullets.append(Bullet(self.x, self.y, self.team))
			self.time = time.time()
		#set boundaries for players movement
		if self.y > 410:
			self.y = 410
		if self.y < 40:
			self.y = 40
		#center players 	
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
        self.surf.fill((230,120,120))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
	# make bullets affect ball
    def update(self, ball):
        if self.x<0 or self.x > screen_width:
            return 1
        if self.team == 1:
             self.x = self.x + self.speed
        if self.team == 2:
             self.x = self.x - self.speed
        self.rect.center = (self.x, self.y)
        screen.blit(self.surf,self.rect)
        if self.y + 10 >= ball.y and self.y - 10 <= ball.y and self.x - 10 <= ball.x and self.x + 10 >= ball.x:
            bullets.remove(self)
            ball.velocityX*=-1
#Create ball class			
class Ball:
	def __init__(self,x, y):
		self.x = x
		self.y = y
		self.velocityX = randint(2,3)
		if random.randint(0, 1) == 0:
			self.velocityX *= -1
		self.velocityY = randint(2,3)
		if random.randint(0, 1) == 0:
			self.velocityY *= -1
		self.surf = pygame.Surface((10,10))
		self.surf.fill((255,255, 255))
		self.rect = self.surf.get_rect()
	
	def update(self, paddle, paddle2):
		global paddleScore, paddle2Score
		#make scores increment
		if self.x>= 840:
			paddleScore+=1
			self.x = 420
			self.y = 225
			self.velocityX = randint(2,3)
			if random.randint(0, 1) == 0:
				self.velocityX *= -1
			self.velocityY = randint(2,3)
			if random.randint(0, 1) == 0:
				self.velocityY *= -1
		if self.x<= 0:
			paddle2Score+=1
			self.x = 420
			self.y = 225
			self.velocityX = randint(2,3)
			if random.randint(0, 1) == 0:
				self.velocityX *= -1
			self.velocityY = randint(2,3)
			if random.randint(0, 1) == 0:
				self.velocityY *= -1
		#give ball collisions with paddle
		if self.y>= 450:
			self.velocityY *= -1
		if self.y<= 0:
			self.velocityY *=-1
		self.x += self.velocityX
		self.y += self.velocityY
		if self.y + 35 >= paddle.y and self.y - 35 <= paddle.y and self.x - 10 <= paddle.x and self.x + 10 >= paddle.x:
			self.velocityX *= -1.2	
		if self.y + 35 >= paddle2.y and self.y - 35 <= paddle2.y and self.x - 10 <= paddle2.x and self.x + 10 >= paddle2.x:
			self.velocityX *= -1.2
		self.rect.center = (self.x, self.y)
		screen.blit(self.surf,self.rect)
		
		
#create players and ball
paddle = Paddle(50, 225, 1)
paddle2 = Paddle(800, 225, 2)
ball = Ball(420,225)
paddleScore = 0
paddle2Score = 0
gameover = False
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
	#display scores in corners of screen
	if gameover == False:
		paddle.update()
		paddle2.update()
		ball.update(paddle, paddle2)
		paddle.displayScore("", paddleScore, 35, 20, (255,255,255))
		paddle2.displayScore("", paddle2Score, screen_width - 25, 20, (255,255,255))
	#create win splash screen
	if paddleScore >= 5:
		paddle.displayWin("PLAYER 1 WINS", 420, 200, (255,255,255))
		gameover = True
	if paddle2Score >= 5:
		paddle.displayWin("PLAYER 2 WINS", 420, 200, (255,255,255))
		gameover = True
	#remove bullets when bullets come into contact with ball
	for bullet in bullets:
		if bullet.update(ball): 
			bullets.remove(bullet)
	pygame.display.update()
	pygame.display.flip()
	clock.tick(fps)

pygame.quit()