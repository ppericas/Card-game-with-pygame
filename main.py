# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
pygame.init()
import assets, json
from icecream import ic
pygame.display.set_caption('HoL')

WIN = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))
font = pygame.font.Font(None, 36)

# ----------------------------------------------------------------------------------------------------------------------
# classes and functions
# TODO separar en funcions petites tots els textos en una funció per cada 'etapa' del joc (posar el nom, instruccions, joc) 
def draw_window(stage: str, seconds: int) -> None:
    handle_click(stage)
    render_texts(stage)
    render_images(stage)
    pygame.display.update()


def render_images(stage) -> None:
    WIN.blit(stage, (0, 0))
    # WIN.blit(assets.CARDCLUBS6, (0, 0))


def render_texts(stage: str) -> None:
    if stage == assets.NAME_STAGE:
        text_surface = font.render("text", True, assets.BLACK)
        WIN.blit(text_surface, (0, 0))

    elif stage == assets.TUTORIAL_STAGE:
        ...

    elif stage == assets.PLAY_STAGE:
        ...


def handle_name(event) -> None:
    name_input = "hola"
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return name_input

        elif event.key == pygame.K_BACKSPACE:
            name_input = name_input[:-1] # Borra el ultimo character que se ha escrito

        else:
            name_input += event.unicode


def handle_click(stage) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif stage == assets.NAME_STAGE:
            handle_name(event)

        elif stage == assets.TUTORIAL_STAGE:
            ...

        elif stage == assets.PLAY_STAGE:
            ...

def save_user_data(name: str, time_taken: int) -> None: # TODO usar aquesta funció
    top_scores: list[dict[str, int]] = []
    with open('top_scores.json', 'r') as file:
        top_scores = json.load(file)

    top_scores.append({'name': name, 'time_taken': time_taken})
    top_scores.sort(key=lambda x: x['time_taken']) # sort by time_taken

    with open('top_scores.json', 'w') as file:
        json.dump(top_scores[:3], file) # save only the 5 names first from top_scores

## main loop
def main() -> None:
    clock = pygame.time.Clock()
    start_time: int = pygame.time.get_ticks()
    run = True
    stage: str = assets.NAME_STAGE

    while run:
        current_time: int = pygame.time.get_ticks()
        chronometer: int = (current_time - start_time) / 1000
        clock.tick(assets.FPS)
        draw_window(stage, chronometer)
    pygame.quit()

if __name__ == '__main__':
    main()

