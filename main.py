# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame

pygame.init()

# ----------------------------------------------------------------------------------------------------------------------
# constants
# window

pygame.display.set_caption('HoL')
WIDTH: int = 700
HEIGHT: int = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
WHITE: list[int] = (255, 255, 255)
BLACK: list[int] = (0, 0, 0)
LIGHT_GREY: list[int] = (222, 222, 222)
DARK_GREY: list[int] = (66, 66, 66)

# others
FPS = 60

# ----------------------------------------------------------------------------------------------------------------------
# classes and functions

def draw_window():
	WIN.fill(WHITE)
	pygame.display.update()

# main loop
def main():
	clock = pygame.time.Clock()
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		clock.tick(FPS)
		draw_window()

	pygame.quit()

if __name__ == '__main__':
    main()
