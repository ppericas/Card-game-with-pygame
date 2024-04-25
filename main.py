# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, assets, random, json, csv
pygame.init()
pygame.display.set_caption('HoL')
from icecream import ic

WIN = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# ----------------------------------------------------------------------------------------------------------------------
# classes and function
# HACK Ho he fet sense utilitzar classes heredades per que trob que no aportaria res
class Card:
    def __init__(self, name, path, suit, value, id):
        self.name = name
        self.path = path
        self.suit = suit
        self.value = value
        self.id = id


class Deck:
    def __init__(self):
        self.images = []
        self.cards = []
        self.used_cards = []
        self.posible_cards: str = []


    def generate_deck(self, archivo_csv):
        try:
            with open(archivo_csv, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                id_index = 1
                for row in reader:
                    name = row['name']
                    if name in self.posible_cards:
                        continue

                    self.posible_cards.append(name)
                    path = row['path']
                    suit = row['suit']
                    value = int(row['value'])

                    card = Card(name, path, suit, value, id_index)
                    self.cards.append(card)
                    # print(f"{name}, {path}, {suit}, {value}, {id_index}")
                    id_index += 1

        except FileNotFoundError:
            print(f"Error: El archivo '{archivo_csv}' no fue encontrado.")

        except Exception as e:
            print(f"Error inesperado al procesar el archivo CSV: {e}")


    def get_random_card(self) -> Card:
        self.random_card = random.choice(self.cards)
        self.used_cards.append(self.random_card)
        return self.random_card

    def update_used_cards(self):
        ...

    def get_id(self):
        return id

def draw_window(stage: str, text_name: str, action: str, deck) -> None:
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

        if action == "BOTON_SUPERIOR":
            random_card = deck.get_random_card()
            actual_card = random_card.id
            for i, j in assets.cards_dict.items():
                ic(actual_card, i)
                if actual_card == i:
                    ic("a")
                    render_images(j, (assets.CARD_X, assets.CARD_Y))

                


        elif action == "BOTON_INFERIOR":
            ...
        elif action == "":
            ...

    pygame.display.update()


def render_text(text: str, color: tuple[int], z: tuple[int]) -> None:
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, z)


def render_images(surface: str, coordinates: tuple[int]) -> None:
    WIN.blit(surface, coordinates)


def detect_collision(mouse_x, mouse_y, square):
    if square.collidepoint(mouse_x, mouse_y) == True:
        return True
    else:
        return False


# This method checks in which state of the game you are, in the name stage, in the tutorial stage or in the game stage; so it doesn't have to execute the ones that doesnt interest you
def update_stage(stage: str, text_name: str, action, deck) -> str:
    new_stage: str = stage
    new_text_name: str = text_name
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
                for key in range(pygame.K_a, pygame.K_z + 1) and range(2):
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
    text_name: str = ""
    action = None
    stage: int = assets.NAME_STAGE
    # card = assets.CARDBACK
    deck = Deck()
    deck.generate_deck('deck.csv')

    while run:
        clock.tick(assets.FPS)
        stage, text_name, action = update_stage(stage, text_name, action, deck)
        draw_window(stage, text_name, action, deck)

    pygame.quit()

if __name__ == '__main__':
    main()

