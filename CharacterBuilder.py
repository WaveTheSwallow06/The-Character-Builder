import pygame

def main():
	pygame.init()
	pygame.display.set_caption("The Character Builder")
	screen = pygame.display.set_mode((1778,876))
	running = True
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
	screen.blit(background, (0, 0))
	logo = pygame.image.load('text\eye.png')
	start = pygame.image.load('text\Start.png')
	lilac = pygame.image.load('Picture\head.png')
	screen.blit(logo, (613, 220))
	screen.blit(start,(613, 330))
	DLC = pygame.image.load('Picture\BlueDLC.png')
	while running:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					screen.blit(background, (0, 0))
					screen.blit(lilac,(1300, 300))
				if event.key == pygame.K_LEFT:
					screen.blit(DLC,(1300, 300))
				if event.key == pygame.K_RIGHT:
					pygame.display.flip()
					screen.blit(lilac,(1300, 300))
					
				
				
if __name__=="__main__":
	main()