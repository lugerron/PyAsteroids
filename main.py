# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	screen    = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock     = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable  = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots     = pygame.sprite.Group()
	dt        = 0
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player    = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		
		for obj in updatable:
			obj.update(dt)
		
		for obj in asteroids:
			if obj.collision(player):
				print("Game over!")
				return
			for shot in shots:
				if shot.collision(obj):
					obj.split()
					shot.kill()

		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
