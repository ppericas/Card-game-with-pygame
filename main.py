# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, os, random, json
from icecream import ic
pygame.init()


def output_to_file(text:str) -> None:
    with open('debug_log.txt', 'a') as f:
        f.write(f'{text}\n')

ic.configureOutput(prefix='Debug| ', outputFunction = output_to_file, includeContext=True)

# ----------------------------------------------------------------------------------------------------------------------
# constants
## window

pygame.display.set_caption('HoL')
WIDTH: int = 700
HEIGHT: int = 375
#FIXME segons condicions foto

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

## colors
WHITE: tuple[int] = (255, 255, 255)
BLACK: tuple[int] = (0, 0, 0)
LIGHT_GREY: tuple[int] = (222, 222, 222)
RED: tuple[int] = (204, 0, 0)
DARK_GREY: tuple[int] = (66, 66, 66)

## assets
PLAY_STAGE_IMAGE = pygame.image.load(
    os.path.join('assets', 'play_stage.png'))
PLAY_STAGE = pygame.transform.scale(PLAY_STAGE_IMAGE, (WIDTH, HEIGHT))

NAME_STAGE_IMAGE = pygame.image.load(
    os.path.join('assets', 'name_stage.png'))
NAME_STAGE= pygame.transform.scale(NAME_STAGE_IMAGE, (WIDTH, HEIGHT))

TUTORIAL_STAGE_IMAGE = pygame.image.load(
    os.path.join('assets', 'tutorial_stage.png'))
TUTORIAL_STAGE = pygame.transform.scale(TUTORIAL_STAGE_IMAGE, (WIDTH, HEIGHT))

## others
FPS: int = 60
font = pygame.font.Font(None, 36)

# ----------------------------------------------------------------------------------------------------------------------
# classes and functions
def draw_window(stage) -> None:
    WIN.fill(WHITE)
    render_images(stage)
    render_texts(stage)
    pygame.display.update()

# TODO separar en funcions petites tots els textos en una funció per cada 'etapa' del joc (posar el nom, instruccions, joc) 

def render_texts(stage: str) -> None:
    match stage:
        case "name":
            render_text("", font, BLACK, 100, 100)
            render_text("", font, BLACK, 100, 100)

        case "tutorial":
            ...

        case "play":
            ...


def render_text(text, font, color, x, y) -> None:
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, (x, y))

def render_images(stage) -> None:
    WIN.blit(stage, (0, 0))


## main loop
def main() -> None:
    clock = pygame.time.Clock()
    run = True
    stage = NAME_STAGE

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        clock.tick(FPS)
        draw_window(stage)
    pygame.quit()

if __name__ == '__main__':
    main()

