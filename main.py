# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, assets, json
from icecream import ic
pygame.display.set_caption('HoL')
pygame.init()

WIN = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))
font = pygame.font.Font(None, 36)

# ----------------------------------------------------------------------------------------------------------------------
# classes and functions
def draw_window(stage: str, text_name: str, seconds: int) -> None: # TODO implementació per usar els segons
    WIN.blit(stage, (0, 0))
    render_images()

    if stage == assets.NAME_STAGE:
        render_text(f"Escribe tu nickname:", assets.BLACK, ((assets.WIDTH) //3, (assets.HEIGHT) //3))
        render_text(f"{text_name}", assets.BLACK, ((assets.WIDTH) //3, (assets.HEIGHT + 100) //3))

    elif stage == assets.TUTORIAL_STAGE:

        render_text(f"", assets.BLACK, (0, 0))


    elif stage == assets.PLAY_STAGE:
        render_text(f"{seconds} s", assets.BLACK, (0, 100))

    pygame.display.update()


def render_text(text: str, color: tuple[int], z: tuple[int]) -> None:
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, z)



def render_images() -> None:
    # WIN.blit(assets.CARDCLUBS6, (assets.CARD_X, assets.CARD_Y))
    ...


# This method checks in which state of the game you are, in the name stage, in the tutorial stage or in the game stage; so it doesn't have to execute the ones that doesnt interest you
def update_stage(stage: str, text_name: str) -> str:
    new_stage: str = stage
    new_text_name: str = text_name
    for event in pygame.event.get():
        if stage == assets.NAME_STAGE:
            if event.type == pygame.QUIT:
                pygame.quit()
                return new_stage, new_text_name

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_stage: str = assets.TUTORIAL_STAGE
                    return new_stage, new_text_name

                elif event.key == pygame.K_BACKSPACE:
                    new_text_name: str = new_text_name[:-1]

                else:
                    for key in range(pygame.K_a, pygame.K_z + 1):
                        if event.key == key:
                            key_name = pygame.key.name(key)
                            new_text_name += key_name

        elif stage == assets.TUTORIAL_STAGE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_stage: str = assets.PLAY_STAGE
                    return new_stage, new_text_name

    return new_stage, new_text_name


def update_name(stage: str, event, text_name: str) -> str:
    new_text_name: str = text_name
    new_stage: str = stage

    if stage == assets.NAME_STAGE:
        if event.type == pygame.KEYDOWN: #FIXME no entra
            if event.key == pygame.K_BACKSPACE:
                new_text_name: str = new_text_name[:-1]
                return new_text_name

            else:
                for key in range(pygame.K_a, pygame.K_z + 1):
                    if event.key == key:
                        key_name = pygame.key.name(key)
                        new_text_name += key_name

    return new_text_name, new_stage


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
    start_time: float = pygame.time.get_ticks()
    run: bool = True
    stage: int = assets.NAME_STAGE
    text_name: str = ""

    while run:
        current_time: int = pygame.time.get_ticks()
        seconds: float = (current_time - start_time) / 1000
        seconds: str = "{:.0f}".format(seconds) # formatea seconds a no tener decimales
        clock.tick(assets.FPS)

        stage, text_name = update_stage(stage, text_name)

        draw_window(stage, text_name, seconds)

    pygame.quit()

if __name__ == '__main__':
    main()

