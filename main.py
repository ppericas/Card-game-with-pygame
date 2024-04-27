# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame, assets, random, json, csv
pygame.init()
pygame.display.set_caption('HoL')

WIN = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))
font = pygame.font.Font(None, 32)
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

    def generate_deck(self, archivo_csv):
        with open(archivo_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            id_index = 1
            for row in reader:
                name = row['name']
                path = row['path']
                suit = row['suit']
                value = int(row['value'])

                card = Card(name, path, suit, value, id_index)
                self.cards.append(card)
                id_index += 1


    def get_new_card(self) -> Card:
        self.new_card = random.choice(self.cards)
        self.new_card_id = self.new_card.id
        self.new_card_value = self.new_card.value
        self.used_cards.append(self.new_card)
        return self.new_card_id, self.new_card_value


def draw_window(stage: str, text_name: str, actual_card, points, seconds) -> None:
    WIN.blit(stage, (0, 0))
    if stage == assets.NAME_STAGE:
        render_text(f"Juegon Nuevo", assets.BLACK, ((assets.WIDTH) // 3, (assets.HEIGHT - 100) // 5))
        render_text(f"Cuando hayas acabado, pulsa intro", assets.BLACK, ((assets.WIDTH) //5, (assets.HEIGHT - 100) // 3))
        render_text(f"Escribe tu nickname:", assets.BLACK, ((assets.WIDTH) //3, (assets.HEIGHT) // 3))
        render_text(f"{text_name}", assets.BLACK, ((assets.WIDTH) // 3, (assets.HEIGHT + 100) // 3))

    elif stage == assets.PLAY_STAGE:
        render_text(f"{seconds} s", assets.BLACK, (assets.TIEMPO_X, assets.TIEMPO_Y))
        render_text(f"{text_name}", assets.BLACK, (assets.NOMBRE_JUGADOR_X, assets.NOMBRE_JUGADOR_Y))
        render_text(f"{points}", assets.BLACK, (assets.PUNTUACION_X, assets.PUNTUACION_Y))

        extracted_cards_aux = []
        top_scores_name = []
        top_scores_points = []
        top_scores_time = []

        with open('extracted_cards.json', 'r') as file:
            extracted_cards = json.load(file)

        with open('top_scores.json', 'r') as file:
            top_scores = json.load(file)

        for dic in extracted_cards:
            extracted_cards_aux.append(dic["value"])

        for dic in top_scores:
            top_scores_name.append(dic["name"])
            top_scores_points.append(dic["points"])
            top_scores_time.append(dic["time_taken"])

        i: int = 0
        j: int = 1
        for value in extracted_cards_aux:
            render_text(f"Carta {j}: {value}", assets.BLACK, (assets.CARTAS_EXTRAIDAS_X, assets.CARTAS_EXTRAIDAS_Y + i))
            i += 20
            j += 1

        a = 0
        for name, points, time_taken in zip(top_scores_name, top_scores_points, top_scores_time):
            render_text(f"{name} - {points} - {time_taken}", assets.BLACK, (assets.HALL_OF_FAME_X, assets.HALL_OF_FAME_Y + a))
            a += 20

        for a, b in assets.cards_dict.items():
            if actual_card == a:
                render_images(b, (assets.CARD_X, assets.CARD_Y))

    pygame.display.update()


def render_text(text: str, color: tuple[int], z: tuple[int]) -> None:
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, z)


def render_images(surface: str, coordinates: tuple[int]) -> None:
    WIN.blit(surface, coordinates)


def detect_collision(mouse_x, mouse_y, square) -> bool:
    if square != None:
        if square.collidepoint(mouse_x, mouse_y) == True:
            return True

        else:
            return False

    return False


# FIXME
def compare_cards(action: str, actual_card: int, new_card_value: int, points: int) -> int:
    game_over: bool = False
    actual_card_value: int = actual_card % 13
    if actual_card_value == 0:
        actual_card_value = 13

    if action == "BOTON_INFERIOR":
        if new_card_value < actual_card_value:
            points += 1

        elif new_card_value > actual_card_value:
            game_over = True

    elif action == "BOTON_SUPERIOR":
        if new_card_value > actual_card_value:
            points += 1

        elif new_card_value < actual_card_value:
            game_over = True

    return points, game_over


def update_stage(stage: str, text_name: str, deck: object, actual_card: int, points: int, seconds) -> None:
    new_text_name: str = text_name
    for event in pygame.event.get():
        if stage == assets.NAME_STAGE:
            if event.type == pygame.QUIT:
                delete_dotjson("extracted_cards")
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_stage: str = assets.PLAY_STAGE
                    return new_stage, new_text_name, actual_card, points

                elif event.key == pygame.K_BACKSPACE:
                    new_text_name: str = new_text_name[:-1]

                else:
                    for key in range(pygame.K_a, pygame.K_z + 1):
                        if event.key == key:
                            key_name = pygame.key.name(key)
                            new_text_name += key_name

        elif stage == assets.PLAY_STAGE:
            if event.type == pygame.QUIT:
                delete_dotjson("extracted_cards")
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if detect_collision(mouse_x, mouse_y, assets.BOTON_INFERIOR):
                    action = "BOTON_INFERIOR"
                    new_card_id, new_card_value = deck.get_new_card()
                    save_card_data(actual_card % 13)
                    points, game_over = compare_cards(action, actual_card, new_card_value, points)
                    actual_card = new_card_id

                    if game_over:
                        save_user_data(new_text_name, points, seconds)
                        delete_dotjson("extracted_cards")
                        new_text_name: str = ""
                        actual_card: int = 1
                        points: int = 0
                        action: str = ""
                        stage = assets.NAME_STAGE

                elif detect_collision(mouse_x, mouse_y, assets.BOTON_SUPERIOR):
                    action = "BOTON_SUPERIOR"
                    new_card_id, new_card_value = deck.get_new_card()
                    save_card_data(actual_card % 13)
                    points, game_over = compare_cards(action, actual_card, new_card_value, points)
                    actual_card = new_card_id


                    if game_over:
                        save_user_data(new_text_name, points, seconds)
                        delete_dotjson("extracted_cards")
                        new_text_name: str = ""
                        actual_card: int = 1
                        points: int = 0
                        stage = assets.NAME_STAGE
                        

                elif detect_collision(mouse_x, mouse_y, assets.JUEGO_NUEVO):
                    new_text_name: str = ""
                    actual_card: int = 1
                    points: int = 0
                    stage = assets.NAME_STAGE
                    delete_dotjson("extracted_cards")

    return stage, new_text_name, actual_card, points


def update_name(stage: str, event, text_name: str) -> str:
    if stage == assets.NAME_STAGE:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text_name: str = text_name[:-1]
                return text_name, stage

            else:
                for key in range(pygame.K_a, pygame.K_z + 1) and range(2):
                    if event.key == key:
                        key_name = pygame.key.name(key)
                        text_name += key_name

    return text_name, stage


# TODO Utilitzar funció
def save_user_data(name: str, points: int,  time_taken: int) -> None:
    top_scores: list[dict[str, int, int]] = []

    with open('top_scores.json', 'r') as file:
        top_scores = json.load(file)

    top_scores.append({'name': name, 'points': points, 'time_taken': time_taken})
    top_scores.sort(key=lambda x: x['points'])

    if len(top_scores) > 3:
        del top_scores[:1]

    with open('top_scores.json', 'w') as file:
        json.dump(top_scores[:3], file)


def save_card_data(value: str) -> None:
    extracted_cards: list[dict[str, int]] = []

    with open('extracted_cards.json', 'r') as file:
        extracted_cards = json.load(file)

    extracted_cards.append({'value': value})

    if len(extracted_cards) > 3:
        del extracted_cards[:1]

    with open('extracted_cards.json', 'w') as file:
        json.dump(extracted_cards[:3], file)


def delete_dotjson(dotjson: str) -> None:
    with open(f'{dotjson}.json', 'r') as file:
        data = json.load(file)
        del data[:3]

    with open(f'{dotjson}.json', 'w') as file:
        json.dump(data, file)


## main loop
def main() -> None:
    run: bool = True
    text_name: str = ""
    actual_card: int = 1
    points: int = 0
    seconds = 0
    stage = assets.NAME_STAGE
    deck = Deck()
    deck.generate_deck('deck.csv')

    while run:
        clock.tick(assets.FPS)
        current_time = pygame.time.get_ticks()

        if stage == assets.NAME_STAGE:
            start_time = current_time
            seconds = 0

        elif stage == assets.PLAY_STAGE:
            seconds = (current_time - start_time) // 1000

        stage, text_name, actual_card, points = update_stage(stage, text_name, deck, actual_card, points, seconds)
        draw_window(stage, text_name, actual_card, points, seconds)

    pygame.quit()


if __name__ == '__main__':
    main()

