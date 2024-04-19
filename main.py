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


# def render_texts(stage: str, event) -> None:
#     if stage == assets.NAME_STAGE:
#         # text_surface = font.render("text", True, assets.BLACK)
#         # WIN.blit(text_surface, (0, 0))
#         handle_name(event)

#     elif stage == assets.TUTORIAL_STAGE:
#         ...

#     elif stage == assets.PLAY_STAGE:
#         ...


def draw_window(stage: str, seconds: int) -> None:
    render_images(stage)
    # render_texts(stage)
    pygame.display.update()


def render_images(stage) -> None:
    WIN.blit(stage, (0, 0))
    WIN.blit(assets.CARDCLUBS6, (assets.CARD_X, assets.CARD_Y))


def handle_click(stage) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if stage == assets.NAME_STAGE:
                handle_name(event)

            elif stage == assets.TUTORIAL_STAGE:
                # handle_tutorial(event)
                if event.key == pygame.K_a:
                    stage: str = assets.PLAY_STAGE
                    print("a")

            elif stage == assets.PLAY_STAGE:
                ...


#FIXME no se si sa funció funciona per que no s'està cridant be, quan estigui arreglat revisar la funció
def handle_name(event) -> None:
    name_input = "hola" 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return name_input

        elif event.key == pygame.K_BACKSPACE:
            name_input = name_input[:-1] # Borra el ultimo character que se ha escrito

        else:
            name_input += event.unicode


#FIXME no actualitza el valor de stage
def handle_tutorial(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            stage: str = assets.PLAY_STAGE

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
    stage: str = assets.TUTORIAL_STAGE

    while run:
        current_time: int = pygame.time.get_ticks()
        chronometer: int = (current_time - start_time) / 1000
        clock.tick(assets.FPS)
        handle_click(stage)
        draw_window(stage, chronometer)
    pygame.quit()

if __name__ == '__main__':
    main()

