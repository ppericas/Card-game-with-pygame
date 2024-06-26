# ----------------------------------------------------------------------------------------------------------------------
import pygame, os
pygame.init()

# ----------------------------------------------------------------------------------------------------------------------
# sizes
WIDTH: int = 600
HEIGHT: int = WIDTH/2

CARD_X: int = 164
CARD_Y: int = 68
CARD_WIDTH: int = 107
CARD_HEIGHT: int = 129

JUEGO_NUEVO_X: int = 29
JUEGO_NUEVO_Y: int = 3
JUEGO_NUEVO_WIDTH: int = 124
JUEGO_NUEVO_HEIGHT: int = 58

BOTON_INFERIOR_X: int = 31
BOTON_INFERIOR_Y: int = 83
BOTON_INFERIOR_WIDTH: int = 122
BOTON_INFERIOR_HEIGHT: int = 95

BOTON_SUPERIOR_X: int = 282
BOTON_SUPERIOR_Y: int = 83
BOTON_SUPERIOR_WIDTH: int = 122
BOTON_SUPERIOR_HEIGHT: int = 95

NOMBRE_JUGADOR_X: int = 182
NOMBRE_JUGADOR_Y: int = 3

TIEMPO_X: int = 298
TIEMPO_Y: int = 31

PUNTUACION_X: int = 182
PUNTUACION_Y: int = 31

CARTAS_EXTRAIDAS_X: int = 440
CARTAS_EXTRAIDAS_Y: int = 100

HALL_OF_FAME_X: int = 440
HALL_OF_FAME_Y: int = 232

# ----------------------------------------------------------------------------------------------------------------------
# colors
WHITE: tuple[int] = (255, 255, 255)
BLACK: tuple[int] = (0, 0, 0)
LIGHT_GREY: tuple[int] = (222, 222, 222)
RED: tuple[int] = (204, 0, 0)
DARK_GREY: tuple[int] = (66, 66, 66)


# ----------------------------------------------------------------------------------------------------------------------
# images

# baraja = []
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# for suit in suits:
#     for rank in ranks:
#         card_name = f"card{suit}{rank}"
#         baraja.append(card_name)

# Lista de nombres de las imágenes de las cartas
# cards = ['cardClubsA.png', 'cardClubs2.png', 'cardClubs3.png', 'cardClubs4.png', 'cardClubs5.png', 'cardClubs6.png',
#          'cardClubs7.png', 'cardClubs8.png', 'cardClubs9.png', 'cardClubs10.png', 'cardClubsJ.png', 'cardClubsQ.png',
#          'cardClubsK.png', 'cardDiamondsA.png', 'cardDiamonds2.png', 'cardDiamonds3.png', 'cardDiamonds4.png',
#          'cardDiamonds5.png', 'cardDiamonds6.png', 'cardDiamonds7.png', 'cardDiamonds8.png', 'cardDiamonds9.png',
#          'cardDiamonds10.png', 'cardDiamondsJ.png', 'cardDiamondsQ.png', 'cardDiamondsK.png', 'cardHeartsA.png',
#          'cardHearts2.png', 'cardHearts3.png', 'cardHearts4.png', 'cardHearts5.png', 'cardHearts6.png', 'cardHearts7.png',
#          'cardHearts8.png', 'cardHearts9.png', 'cardHearts10.png', 'cardHeartsJ.png', 'cardHeartsQ.png', 'cardHeartsK.png',
#          'cardSpadesA.png', 'cardSpades2.png', 'cardSpades3.png', 'cardSpades4.png', 'cardSpades5.png', 'cardSpades6.png',
#          'cardSpades7.png', 'cardSpades8.png', 'cardSpades9.png', 'cardSpades10.png', 'cardSpadesJ.png', 'cardSpadesQ.png',
#          'cardSpadesK.png']

# Generación del código para rellenar
# for card in cards:
#     card_name_upper = card.split('.')[0].upper()  # Convierte el nombre de la imagen a mayúsculas
#     card_name_lower = card.split('.')[0].lower()  # Convierte el nombre de la imagen a minúsculas
#     print(f"{card_name_upper}_IMAGE = pygame.image.load(os.path.join('assets', '{card_name_lower}.png'))")
#     print(f"{card_name_upper} = pygame.transform.scale({card_name_upper}_IMAGE, (WIDTH, HEIGHT))")

# {NOMBRE_IMAGEN_EN_MAYUSCULAS}_IMAGE = pygame.image.load(
#     os.path.join('assets', '{nombre_imagen_en_minusculas}.png'))
# {NOMBRE_IMAGEN_EN_MAYUSCULAS} = pygame.transform.scale({NOMBRE_IMAGEN_EN_MAYUSCULAS}_IMAGE, (WIDTH, HEIGHT))

PLAY_STAGE_IMAGE = pygame.image.load(
    os.path.join('assets', 'play_stage.png'))
PLAY_STAGE = pygame.transform.scale(PLAY_STAGE_IMAGE, (WIDTH, HEIGHT))

NAME_STAGE_IMAGE = pygame.image.load(
    os.path.join('assets', 'name_stage.png'))
NAME_STAGE= pygame.transform.scale(NAME_STAGE_IMAGE, (WIDTH, HEIGHT))

CARDBACK_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardback.png'))
CARDBACK = pygame.transform.scale(CARDBACK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBSA_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubsa.png'))
CARDCLUBSA = pygame.transform.scale(CARDCLUBSA_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS2_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs2.png'))
CARDCLUBS2 = pygame.transform.scale(CARDCLUBS2_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS3_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs3.png'))
CARDCLUBS3 = pygame.transform.scale(CARDCLUBS3_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS4_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs4.png'))
CARDCLUBS4 = pygame.transform.scale(CARDCLUBS4_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS5_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs5.png'))
CARDCLUBS5 = pygame.transform.scale(CARDCLUBS5_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS6_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs6.png'))
CARDCLUBS6 = pygame.transform.scale(CARDCLUBS6_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS7_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs7.png'))
CARDCLUBS7 = pygame.transform.scale(CARDCLUBS7_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS8_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs8.png'))
CARDCLUBS8 = pygame.transform.scale(CARDCLUBS8_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS9_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs9.png'))
CARDCLUBS9 = pygame.transform.scale(CARDCLUBS9_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBS10_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubs10.png'))
CARDCLUBS10 = pygame.transform.scale(CARDCLUBS10_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBSJ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubsj.png'))
CARDCLUBSJ = pygame.transform.scale(CARDCLUBSJ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBSQ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubsq.png'))
CARDCLUBSQ = pygame.transform.scale(CARDCLUBSQ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDCLUBSK_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardclubsk.png'))
CARDCLUBSK = pygame.transform.scale(CARDCLUBSK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDSA_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamondsa.png'))
CARDDIAMONDSA = pygame.transform.scale(CARDDIAMONDSA_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS2_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds2.png'))
CARDDIAMONDS2 = pygame.transform.scale(CARDDIAMONDS2_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS3_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds3.png'))
CARDDIAMONDS3 = pygame.transform.scale(CARDDIAMONDS3_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS4_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds4.png'))
CARDDIAMONDS4 = pygame.transform.scale(CARDDIAMONDS4_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS5_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds5.png'))
CARDDIAMONDS5 = pygame.transform.scale(CARDDIAMONDS5_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS6_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds6.png'))
CARDDIAMONDS6 = pygame.transform.scale(CARDDIAMONDS6_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS7_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds7.png'))
CARDDIAMONDS7 = pygame.transform.scale(CARDDIAMONDS7_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS8_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds8.png'))
CARDDIAMONDS8 = pygame.transform.scale(CARDDIAMONDS8_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS9_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds9.png'))
CARDDIAMONDS9 = pygame.transform.scale(CARDDIAMONDS9_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDS10_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamonds10.png'))
CARDDIAMONDS10 = pygame.transform.scale(CARDDIAMONDS10_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDSJ_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamondsj.png'))
CARDDIAMONDSJ = pygame.transform.scale(CARDDIAMONDSJ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDSQ_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamondsq.png'))
CARDDIAMONDSQ = pygame.transform.scale(CARDDIAMONDSQ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDDIAMONDSK_IMAGE = pygame.image.load(
    os.path.join('assets', 'carddiamondsk.png'))
CARDDIAMONDSK = pygame.transform.scale(CARDDIAMONDSK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTSA_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardheartsa.png'))
CARDHEARTSA = pygame.transform.scale(CARDHEARTSA_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS2_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts2.png'))
CARDHEARTS2 = pygame.transform.scale(CARDHEARTS2_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS3_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts3.png'))
CARDHEARTS3 = pygame.transform.scale(CARDHEARTS3_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS4_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts4.png'))
CARDHEARTS4 = pygame.transform.scale(CARDHEARTS4_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS5_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts5.png'))
CARDHEARTS5 = pygame.transform.scale(CARDHEARTS5_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS6_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts6.png'))
CARDHEARTS6 = pygame.transform.scale(CARDHEARTS6_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS7_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts7.png'))
CARDHEARTS7 = pygame.transform.scale(CARDHEARTS7_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS8_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts8.png'))
CARDHEARTS8 = pygame.transform.scale(CARDHEARTS8_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS9_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts9.png'))
CARDHEARTS9 = pygame.transform.scale(CARDHEARTS9_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTS10_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardhearts10.png'))
CARDHEARTS10 = pygame.transform.scale(CARDHEARTS10_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTSJ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardheartsj.png'))
CARDHEARTSJ = pygame.transform.scale(CARDHEARTSJ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTSQ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardheartsq.png'))
CARDHEARTSQ = pygame.transform.scale(CARDHEARTSQ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDHEARTSK_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardheartsk.png'))
CARDHEARTSK = pygame.transform.scale(CARDHEARTSK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADESA_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspadesa.png'))
CARDSPADESA = pygame.transform.scale(CARDSPADESA_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES2_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades2.png'))
CARDSPADES2 = pygame.transform.scale(CARDSPADES2_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES3_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades3.png'))
CARDSPADES3 = pygame.transform.scale(CARDSPADES3_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES4_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades4.png'))
CARDSPADES4 = pygame.transform.scale(CARDSPADES4_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES5_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades5.png'))
CARDSPADES5 = pygame.transform.scale(CARDSPADES5_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES6_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades6.png'))
CARDSPADES6 = pygame.transform.scale(CARDSPADES6_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES7_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades7.png'))
CARDSPADES7 = pygame.transform.scale(CARDSPADES7_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES8_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades8.png'))
CARDSPADES8 = pygame.transform.scale(CARDSPADES8_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES9_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades9.png'))
CARDSPADES9 = pygame.transform.scale(CARDSPADES9_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADES10_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspades10.png'))
CARDSPADES10 = pygame.transform.scale(CARDSPADES10_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADESJ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspadesj.png'))
CARDSPADESJ = pygame.transform.scale(CARDSPADESJ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADESQ_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspadesq.png'))
CARDSPADESQ = pygame.transform.scale(CARDSPADESQ_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

CARDSPADESK_IMAGE = pygame.image.load(
    os.path.join('assets', 'cardspadesk.png'))
CARDSPADESK = pygame.transform.scale(CARDSPADESK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))


# ----------------------------------------------------------------------------------------------------------------------
# cards
cards_list: list[str] = [
    CARDCLUBSA, CARDCLUBS2, CARDCLUBS3, CARDCLUBS4, CARDCLUBS5, CARDCLUBS6, CARDCLUBS7, CARDCLUBS8, CARDCLUBS9, CARDCLUBS10, CARDCLUBSJ, CARDCLUBSQ, CARDCLUBSK,
    CARDDIAMONDSA, CARDDIAMONDS2, CARDDIAMONDS3, CARDDIAMONDS4, CARDDIAMONDS5, CARDDIAMONDS6, CARDDIAMONDS7, CARDDIAMONDS8, CARDDIAMONDS9, CARDDIAMONDS10, CARDDIAMONDSJ, CARDDIAMONDSQ, CARDDIAMONDSK,
    CARDHEARTSA, CARDHEARTS2, CARDHEARTS3, CARDHEARTS4, CARDHEARTS5, CARDHEARTS6, CARDHEARTS7, CARDHEARTS8, CARDHEARTS9, CARDHEARTS10, CARDHEARTSJ, CARDHEARTSQ, CARDHEARTSK,
    CARDSPADESA, CARDSPADES2, CARDSPADES3, CARDSPADES4, CARDSPADES5, CARDSPADES6, CARDSPADES7, CARDSPADES8, CARDSPADES9, CARDSPADES10, CARDSPADESJ, CARDSPADESQ, CARDSPADESK
    ]

cards_dict = {}
for index, card_image in enumerate(cards_list, start=1):
    cards_dict[index] = card_image

JUEGO_NUEVO = pygame.Rect(JUEGO_NUEVO_X, JUEGO_NUEVO_Y, JUEGO_NUEVO_WIDTH, JUEGO_NUEVO_HEIGHT)
BOTON_INFERIOR = pygame.Rect(BOTON_INFERIOR_X, BOTON_INFERIOR_Y, BOTON_INFERIOR_WIDTH, BOTON_INFERIOR_HEIGHT)
BOTON_SUPERIOR = pygame.Rect(BOTON_SUPERIOR_X, BOTON_SUPERIOR_Y, BOTON_SUPERIOR_WIDTH, BOTON_SUPERIOR_HEIGHT)

# NOMBRE_JUGADOR = pygame.Rect(NOMBRE_JUGADOR_X, NOMBRE_JUGADOR_Y, NOMBRE_JUGADOR_WIDTH, NOMBRE_JUGADOR_HEIGHT)

# ----------------------------------------------------------------------------------------------------------------------
# others
FPS: int = 60

