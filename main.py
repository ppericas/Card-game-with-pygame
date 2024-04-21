# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, assets, random, json, csv
pygame.init()
pygame.display.set_caption('HoL')

WIN = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# ----------------------------------------------------------------------------------------------------------------------
# classes and functions
class Card:
    def __init__(self, name: str, path: str, value: int) -> None:
        self.name = name
        self.path = path
        self.value = value

class Hearts(Card):
    def __init__(self, name: str, path: str, value: int) -> None:
        super().__init__(name, path, value)
        self.suit = "Hearts"

class Diamonds(Card):
    def __init__(self, name: str, path: str, value: int) -> None:
        super().__init__(name, path, value)
        self.suit = "Diamonds"

class Clubs(Card):
    def __init__(self, name: str, path: str, value: int) -> None:
        super().__init__(name, path, value)
        self.suit = "Clubs"

class Spades(Card):
    def __init__(self, name: str, path: str, value: int) -> None:
        super().__init__(name, path, value)
        self.suit = "Spades"

def create_deck(csv_file):
    deck = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            image_path = row['path']
            value = int(row['value'])
            suit = row['suit']

            if suit == 'Hearts':
                card = Hearts(name, image_path, value)

            elif suit == 'Diamonds':
                card = Diamonds(name, image_path, value)

            elif suit == 'Clubs':
                card = Clubs(name, image_path, value)

            elif suit == 'Spades':
                card = Spades(name, image_path, value)

            deck.append(card)
    return deck


def draw_window(stage: str, text_name: str, action: str) -> None:
    WIN.blit(stage, (0, 0))

    if stage == assets.NAME_STAGE:
        render_text(f"Cuando hayas acabado, pulsa intro", assets.BLACK, ((assets.WIDTH) //5, (assets.HEIGHT - 100) //3))
        render_text(f"Escribe tu nickname:", assets.BLACK, ((assets.WIDTH) //3, (assets.HEIGHT) //3))
        render_text(f"{text_name}", assets.BLACK, ((assets.WIDTH) //3, (assets.HEIGHT + 100) //3))

    elif stage == assets.TUTORIAL_STAGE:
        render_images(assets.CARDBACK, (assets.CARD_X, assets.CARD_Y))

    elif stage == assets.PLAY_STAGE:
        current_time: int = pygame.time.get_ticks()
        seconds: float = current_time / 1000
        seconds: str = "{:.0f}".format(seconds) # formatea seconds a no tener decimales
        clock.tick(assets.FPS)
        render_text(f"{seconds} s", assets.BLACK, (0, 100))
        if int(seconds) >= 1:
            # TODO Part on s'implementara es condicional de si has clicat a dedins d'un quadrat de higher o lower
            
            if action == "BOTON_SUPERIOR":
                card = get_random_card()
                render_images(card, (assets.CARD_X, assets.CARD_Y))
                render_text(f"a", assets.BLACK, (0, 0))

    pygame.display.update()

def render_text(text: str, color: tuple[int], z: tuple[int]) -> None:
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, z)


def render_images(surface: str, coordinates: tuple[int]) -> None:
    WIN.blit(surface, coordinates)


def get_random_card() -> Card:
    random_card = random.choice(assets.deck)
    return random_card


def detect_collision(mouse_x, mouse_y, square):
    if square.collidepoint(mouse_x, mouse_y) == True:
        return True
    else:
        return False


# This method checks in which state of the game you are, in the name stage, in the tutorial stage or in the game stage; so it doesn't have to execute the ones that doesnt interest you
def update_stage(stage: str, text_name: str) -> str:
    new_stage: str = stage
    new_text_name: str = text_name
    action = None
    for event in pygame.event.get():
        if stage == assets.NAME_STAGE:
            if event.type == pygame.QUIT:
                pygame.quit()
                return new_stage, new_text_name, action

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_stage: str = assets.TUTORIAL_STAGE
                    return new_stage, new_text_name, action

                elif event.key == pygame.K_BACKSPACE:
                    new_text_name: str = new_text_name[:-1]

                else:
                    for key in range(pygame.K_a, pygame.K_z + 1):
                        if event.key == key:
                            key_name = pygame.key.name(key)
                            new_text_name += key_name

        elif stage == assets.TUTORIAL_STAGE:
            if event.type == pygame.QUIT:
                pygame.quit()
                return new_stage, new_text_name, action

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_stage: str = assets.PLAY_STAGE
                    return new_stage, new_text_name, action

        elif stage == assets.PLAY_STAGE:

            if event.type == pygame.QUIT:
                pygame.quit()
                return new_stage, new_text_name

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    ...

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if detect_collision(mouse_x, mouse_y, assets.BOTON_INFERIOR) == True:
                    action = "BOTON_SUPERIOR"

                elif detect_collision(mouse_x, mouse_y, assets.BOTON_SUPERIOR) == True:
                    action = "BOTON_SUPERIOR"

                elif detect_collision(mouse_x, mouse_y, assets.JUEGO_NUEVO) == True:
                    action = "JUEGO_NUEVO"

    return new_stage, new_text_name, action


def update_name(stage: str, event, text_name: str) -> str:
    new_text_name: str = text_name
    new_stage: str = stage

    if stage == assets.NAME_STAGE:
        if event.type == pygame.KEYDOWN:
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
    run: bool = True
    deck = create_deck('deck.csv')
    stage: int = assets.NAME_STAGE
    text_name: str = ""

    while run:
        clock.tick(assets.FPS)
        stage, text_name, action = update_stage(stage, text_name)
        draw_window(stage, text_name, action)

    pygame.quit()

if __name__ == '__main__':
    main()

