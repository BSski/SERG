##########################################################
############- ARROW_LEFT: ADD 100 HERBIVORES -############
############- ARROW_RIGHT: ADD 25 CARNIVORES -############
######- ARROW_DOWN: SHOW HISTORY OF AMOUNTS CHART -#######
#######- ARROW_UP: HIDE HISTORY OF AMOUNTS CHART -########
##########################################################

# 16 possibile speeds with counter max 120:
#     1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.



# if reset clicked, make a new file
# zwęż okna cech tak, żeby mieściły się oznaczenia osi, zmniejsz 2*i do i
# zwiększ ilość zbieranych próbek cech ze 100 do 162
# dodaj guziki po prawej wszędzie i pokombinuj z tym
# dodaj pauze/start na spacje

############################################################################################################

# Imports.
import pygame
import random
from grid import grid
from positions import *
from datetime import datetime
# Create data file.
report = open(str(datetime.now())[:13] + "." + str(datetime.now())[14:16] + "." + str(datetime.now())[17:19]
              + ".txt", "w")
# Initialize the game engine.
pygame.init()
# Set fonts.
font  = pygame.font.SysFont("liberationmono", 13)
font2 = pygame.font.SysFont("liberationmono", 12)
font3 = pygame.font.SysFont("liberationmono", 11)
font4 = pygame.font.SysFont("humorsans", 70)
font5 = pygame.font.SysFont("liberationmono", 12)
font6 = pygame.font.SysFont("liberationmono", 14)
font7 = pygame.font.SysFont("liberationmono", 18)
# Define colors.
colors_list_red = [
[(255, 173, 153), (255, 153, 128), (255, 133, 102), (255, 112, 77), (255, 92, 51), (255, 71, 26), (255, 51, 0), (230, 46, 0)],            # RED 1
[(255, 194, 153), (255, 179, 128), (255, 163, 102), (255, 148, 77), (255, 133, 51), (255, 117, 26), (255, 102, 0), (230, 92, 0)],         # RED 2
[(255, 153, 153), (255, 128, 128), (255, 102, 102), (255, 77, 77), (255, 51, 51), (255, 26, 26), (255, 0, 0), (230, 0, 0)],               # RED 3
[(255, 153, 187), (255, 128, 170), (255, 102, 153), (255, 77, 136), (255, 51, 119), (255, 26, 102), (255, 0, 85), (230, 0, 76)],          # RED 4
[(255, 173, 153), (255, 153, 128), (255, 133, 102), (255, 112, 77), (255, 92, 51), (255, 71, 26), (255, 51, 0), (230, 46, 0)],            # RED 1
[(255, 194, 153), (255, 179, 128), (255, 163, 102), (255, 148, 77), (255, 133, 51), (255, 117, 26), (255, 102, 0), (230, 92, 0)],         # RED 2
[(255, 153, 153), (255, 128, 128), (255, 102, 102), (255, 77, 77), (255, 51, 51), (255, 26, 26), (255, 0, 0), (230, 0, 0)],               # RED 3
[(255, 153, 187), (255, 128, 170), (255, 102, 153), (255, 77, 136), (255, 51, 119), (255, 26, 102), (255, 0, 85), (230, 0, 76)]           # RED 4
]
colors_list_green = [
[(77, 255, 136), (51, 255, 119), (26, 255, 102), (0, 255, 85), (0, 230, 77), (0, 204, 68), (0, 179, 60), (0, 153, 51), (0, 128, 43)],     # GREEN 1
[(77, 255, 77), (51, 255, 51), (26, 255, 26), (0, 255, 0), (0, 230, 0), (0, 204, 0), (0, 179, 0), (0, 153, 0), (0, 128, 0)],              # GREEN 2
[(51, 255, 153), (26, 255, 140), (0, 255, 128), (0, 230, 115), (0, 204, 102), (0, 179, 89), (0, 153, 77), (0, 128, 64)],                  # GREEN 3
[(51, 255, 204), (26, 255, 198), (0, 255, 191), (0, 230, 172), (0, 204, 153), (0, 179, 134), (0, 153, 115), (0, 128, 96)],                # GREEN 4
[(77, 255, 136), (51, 255, 119), (26, 255, 102), (0, 255, 85), (0, 230, 77), (0, 204, 68), (0, 179, 60), (0, 153, 51), (0, 128, 43)],     # GREEN 1
[(77, 255, 77), (51, 255, 51), (26, 255, 26), (0, 255, 0), (0, 230, 0), (0, 204, 0), (0, 179, 0), (0, 153, 0), (0, 128, 0)],              # GREEN 2
[(51, 255, 153), (26, 255, 140), (0, 255, 128), (0, 230, 115), (0, 204, 102), (0, 179, 89), (0, 153, 77), (0, 128, 64)],                  # GREEN 3
[(51, 255, 204), (26, 255, 198), (0, 255, 191), (0, 230, 172), (0, 204, 153), (0, 179, 134), (0, 153, 115), (0, 128, 96)]                 # GREEN 4
]
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GRAY        = ( 210, 210, 210)
LIGHTGRAY   = ( 239, 239, 239)
MIDDLEGRAY  = ( 180, 180, 180)
DARKGRAY    = ( 130, 130, 130)
DARKERGRAY  = (  45,  45,  45)
FORESTGREEN = (  34, 139,  34)
DARKRED     = ( 178,  34,  34)
DARKBLUE    = (   0,   0, 139)
GREEN       = (  51, 153,  51)
BLUE        = (   0, 102, 204)
RED         = ( 202,   0,   0)
# Load images.
PLUS_UP = pygame.image.load("sprites/PLUS_UP.png")
PLUS_DOWN = pygame.image.load("sprites/PLUS_DOWN.png")
MINUS_UP = pygame.image.load("sprites/MINUS_UP.png")
MINUS_DOWN = pygame.image.load("sprites/MINUS_DOWN.png")
RESET_UP = pygame.image.load("sprites/RESET_UP.png")
RESET_DOWN = pygame.image.load("sprites/RESET_DOWN.png")
START_UP = pygame.image.load("sprites/START_UP.png")
START_DOWN = pygame.image.load("sprites/START_DOWN.png")
PAUSE_UP = pygame.image.load("sprites/PAUSE_UP.png")
PAUSE_DOWN = pygame.image.load("sprites/PAUSE_DOWN.png")

############################################################################################################

# Set size of the screen and create it.
size = (855, 583)
pygame.display.set_caption("SERG")
screen = pygame.display.set_mode(size)
serg_icon = pygame.image.load('sprites/serg.png')
pygame.display.set_icon(serg_icon)

############################################################################################################

# Define variables and lists.
animation = "|/-\\"
DNA = ["SPEED", "BOWEL_LENGTH", "FAT_LIMIT", "LEGS_LENGTH"]
counter = 0
counter_prev = counter
big_counter = 0
big_counter_prev = big_counter
reset = 0
pause = 1
reset_counter = 12
chosen_cycles_per_second = 2
counter_for_fps = 0
total_cycles_counter = 0

herbs = []
herbivores = []
carnivores = []

cycles_per_sec_list = [30, 60, 90, 120, 150, 180, 240, 300, 360, 450, 600, 720, 900, 1200]
cycles_per_sec_dividers_list = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40]

herbivores_amount_list = []
carnivores_amount_list = []
herbivores_total_amount_list = []
carnivores_total_amount_list = []

herbs_amount_list = []
herbivores_mean_speed_list = []
herbivores_mean_bowel_length_list = []
herbivores_mean_fat_limit_list = []
herbivores_mean_legs_length_list = []

carnivores_mean_speed_list = []
carnivores_mean_bowel_length_list = []
carnivores_mean_fat_limit_list = []
carnivores_mean_legs_length_list = []

btn_start_clicked = 0
btn_pause_clicked = 0
btn_reset_clicked = 0

btn_tempo_plus_clicked = 0
btn_tempo_minus_clicked = 0

btn_cps_plus_clicked = 0
btn_cps_minus_clicked = 0

btn_mutation_plus_clicked = 0
btn_mutation_minus_clicked = 0

btn_herbs_starting_amount_plus_clicked = 0
btn_herbs_starting_amount_minus_clicked = 0

btn_herbs_energy_plus_clicked = 0
btn_herbs_energy_minus_clicked = 0

btn_herbs_amount_per_spawn_plus_clicked = 0
btn_herbs_amount_per_spawn_minus_clicked = 0

btn_herbs_spawn_rate_plus_clicked = 0
btn_herbs_spawn_rate_minus_clicked = 0

btn_herbivores_starting_amount_plus_clicked = 0
btn_herbivores_starting_amount_minus_clicked = 0

btn_herbivores_spawn_energy_plus_clicked = 0
btn_herbivores_spawn_energy_minus_clicked = 0

btn_herbivores_breed_level_plus_clicked = 0
btn_herbivores_breed_level_minus_clicked = 0

btn_herbivores_movement_cost_plus_clicked = 0
btn_herbivores_movement_cost_minus_clicked = 0

btn_carnivores_starting_amount_plus_clicked = 0
btn_carnivores_starting_amount_minus_clicked = 0

btn_carnivores_spawn_energy_plus_clicked = 0
btn_carnivores_spawn_energy_minus_clicked = 0

btn_carnivores_breed_level_plus_clicked = 0
btn_carnivores_breed_level_minus_clicked = 0

btn_carnivores_movement_cost_plus_clicked = 0
btn_carnivores_movement_cost_minus_clicked = 0

bigger_screen = 0

############################################################################################################

# Settings.
# Main loop's cycles per second, between 0-14.
cycles_per_sec = cycles_per_sec_list[chosen_cycles_per_second]

tempo = 0.28                        # between 0.01 and 0.99

mutation_chance = 1                 # between 0 and 99, percents

herbs_spawn_rate = 3                # higher is faster.
herbs_amount_per_spawn = 5          #
herbs_energy = 4000                 #

herbs_starting_amount = 400         # suggested 200-1000
herbivores_starting_amount = 150    # suggested 50-200
carnivores_starting_amount = 30     # suggested 15-75

herbivores_spawn_energy = 2200      # suggested 1000-3000
carnivores_spawn_energy = 1800      # suggested 1000-3500

herbivores_breed_level = 3000       # suggested 2500-4500
carnivores_breed_level = 3000       # suggested 2000-4500

herbivores_movement_cost = 10       # suggested 10-80 (has big impact)
carnivores_movement_cost = 100      # suggested 10-80 (has big impact)

############################################################################################################

# DNA coding.
speed_dict = {
-5: 120,
-4: 60,
-3: 40,
-2: 30,
-1: 24,
0: 20,
1: 12,
2: 10,
3: 8,
4: 6,
5: 4,
6: 2,
7: 1
}
speed_cost_dict = {
0: 1.000,
1: 1.003,
2: 1.006,
3: 1.009,
4: 1.012,
5: 1.015,
6: 1.018,
7: 1.021
}
bowel_length_dict = {
0: 0.6,
1: 0.65,
2: 0.7,
3: 0.75,
4: 0.8,
5: 0.85,
6: 0.9,
7: 0.95
}
bowel_length_dict_cost = {
0: 1.00,
1: 1.01,
2: 1.02,
3: 1.03,
4: 1.04,
5: 1.05,
6: 1.06,
7: 1.07
}
fat_limit_dict = {
0: 4100,
1: 4300,
2: 4500,
3: 4700,
4: 4900,
5: 5100,
6: 5300,
7: 5500
}
fat_limit_cost_dict = {
0: 1.000,
1: 1.007,
2: 1.014,
3: 1.021,
4: 1.028,
5: 1.035,
6: 1.042,
7: 1.049
}
legs_length_dict = {
0: 1.00,
1: 0.98,
2: 0.96,
3: 0.94,
4: 0.92,
5: 0.90,
6: 0.88,
7: 0.86
}
legs_length_cost_dict = {
0: 1.000,
1: 1.007,
2: 1.014,
3: 1.021,
4: 1.028,
5: 1.035,
6: 1.042,
7: 1.049
}
############################################################################################################
# Function drawing the main parts of the interface.
def draw_window(colors_list_green, colors_list_red, herbs, herbivores, carnivores, cycles_per_sec,
                tempo, herbs_spawn_rate, herbs_amount_per_spawn, herbs_energy, herbs_starting_amount,
                herbivores_starting_amount, carnivores_starting_amount, herbivores_spawn_energy,
                carnivores_spawn_energy, herbivores_breed_level, carnivores_breed_level,
                herbivores_movement_cost, carnivores_movement_cost, mutation_chance,
                btn_start_clicked, btn_pause_clicked, btn_reset_clicked,
                btn_tempo_plus_clicked, btn_tempo_minus_clicked, btn_cps_plus_clicked,
                btn_cps_minus_clicked):

    # Logo.
    logo = font4.render("SERG", True, (80, 80, 80))
    screen.blit(logo, (39, 18))
    signature = font3.render("bsski 2020", True, (200, 200, 200))
    screen.blit(signature, (70, 60))

    # Drawing grid.
    square = 10
    square_width = square
    square_height = square
    y = -square_height + 10
    for i in range(0, 43):
        y += square_height
        x = -square_width + 213
        for j in range(0, 43):
            x += square_width
            pygame.draw.rect(screen, GRAY, [x, y, square_width-1, square_height-1])

    # Charts backgrounds.
    pygame.draw.rect(screen, WHITE, [29, 124, 162, 300])
    pygame.draw.rect(screen, WHITE, [25, 452, 162, 105])
    pygame.draw.rect(screen, WHITE, [242, 452, 162, 105])
    pygame.draw.rect(screen, WHITE, [459, 452, 162, 105])
    pygame.draw.rect(screen, WHITE, [676, 452, 162, 105])
    if bigger_screen == 1:
        pygame.draw.rect(screen, WHITE, [37, 595, 801, 191])
    # Main interface lines.
    pygame.draw.line(screen, GRAY, (12, 12), (12, 436), 1)
    pygame.draw.line(screen, GRAY, (198, 12), (198, 436), 1)
    pygame.draw.line(screen, GRAY, (656, 12), (656, 436), 1)
    pygame.draw.line(screen, GRAY, (842, 12), (842, 436), 1)
    # Amounts chart.
    pygame.draw.line(screen, GRAY, (28, 423), (189, 423), 1)
    pygame.draw.line(screen, GRAY, (28, 413), (189, 413), 1)
    pygame.draw.line(screen, GRAY, (28, 403), (189, 403), 1)
    pygame.draw.line(screen, GRAY, (28, 393), (189, 393), 1)
    pygame.draw.line(screen, GRAY, (28, 383), (189, 383), 1)
    pygame.draw.line(screen, GRAY, (28, 373), (189, 373), 1)
    pygame.draw.line(screen, GRAY, (28, 363), (189, 363), 1)
    pygame.draw.line(screen, GRAY, (28, 353), (189, 353), 1)
    pygame.draw.line(screen, GRAY, (28, 343), (189, 343), 1)
    pygame.draw.line(screen, GRAY, (28, 333), (189, 333), 1)
    pygame.draw.line(screen, GRAY, (28, 323), (189, 323), 1)
    pygame.draw.line(screen, GRAY, (28, 313), (189, 313), 1)
    pygame.draw.line(screen, GRAY, (28, 303), (189, 303), 1)
    pygame.draw.line(screen, GRAY, (28, 293), (189, 293), 1)
    pygame.draw.line(screen, GRAY, (28, 283), (189, 283), 1)
    pygame.draw.line(screen, GRAY, (28, 273), (189, 273), 1)
    pygame.draw.line(screen, GRAY, (28, 263), (189, 263), 1)
    pygame.draw.line(screen, GRAY, (28, 253), (189, 253), 1)
    pygame.draw.line(screen, GRAY, (28, 243), (189, 243), 1)
    pygame.draw.line(screen, GRAY, (28, 233), (189, 233), 1)
    pygame.draw.line(screen, DARKRED, (28, 223), (189, 223), 1)
    pygame.draw.line(screen, GRAY, (28, 213), (189, 213), 1)
    pygame.draw.line(screen, GRAY, (28, 203), (189, 203), 1)
    pygame.draw.line(screen, GRAY, (28, 193), (189, 193), 1)
    pygame.draw.line(screen, GRAY, (28, 183), (189, 183), 1)
    pygame.draw.line(screen, GRAY, (28, 173), (189, 173), 1)
    pygame.draw.line(screen, GRAY, (28, 163), (189, 163), 1)
    pygame.draw.line(screen, GRAY, (28, 153), (189, 153), 1)
    pygame.draw.line(screen, GRAY, (28, 143), (189, 143), 1)
    pygame.draw.line(screen, GRAY, (28, 133), (189, 133), 1)
    pygame.draw.line(screen, GRAY, (28, 123), (189, 123), 1)
    pygame.draw.line(screen, DARKGRAY, (28, 424), (28, 122), 1)
    pygame.draw.line(screen, DARKGRAY, (28, 424), (189, 424), 1)
    pygame.draw.line(screen, DARKGRAY, (28, 122), (189, 122), 1)
    pygame.draw.line(screen, DARKGRAY, (190, 424), (190, 122), 1)
    text_to_blit = font5.render("0", True, (50, 50, 50))
    screen.blit(text_to_blit, (18, 417))
    text_to_blit = font5.render(".1", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 397))
    text_to_blit = font5.render(".2", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 377))
    text_to_blit = font5.render(".3", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 357))
    text_to_blit = font5.render(".4", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 337))
    text_to_blit = font5.render(".5", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 317))
    text_to_blit = font5.render(".6", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 297))
    text_to_blit = font5.render(".7", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 277))
    text_to_blit = font5.render(".8", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 257))
    text_to_blit = font5.render(".9", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 237))
    text_to_blit = font5.render("1", True, (50, 50, 50))
    screen.blit(text_to_blit, (17, 217))
    text_to_blit = font5.render(".1", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 197))
    text_to_blit = font5.render(".2", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 177))
    text_to_blit = font5.render(".3", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 157))
    text_to_blit = font5.render(".4", True, (50, 50, 50))
    screen.blit(text_to_blit, (12, 137))
    text_to_blit = font5.render("k", True, (50, 50, 50))
    screen.blit(text_to_blit, (18, 117))

    # All amount history chart.
    if bigger_screen == 1:
        pygame.draw.line(screen, GRAY, (37, 785), (837, 785), 1)
        pygame.draw.line(screen, GRAY, (37, 775), (837, 775), 1)
        pygame.draw.line(screen, GRAY, (37, 765), (837, 765), 1)
        pygame.draw.line(screen, GRAY, (37, 755), (837, 755), 1)
        pygame.draw.line(screen, GRAY, (37, 745), (837, 745), 1)
        pygame.draw.line(screen, GRAY, (37, 735), (837, 735), 1)
        pygame.draw.line(screen, GRAY, (37, 725), (837, 725), 1)
        pygame.draw.line(screen, GRAY, (37, 715), (837, 715), 1)
        pygame.draw.line(screen, GRAY, (37, 705), (837, 705), 1)
        pygame.draw.line(screen, GRAY, (37, 695), (837, 695), 1)
        pygame.draw.line(screen, GRAY, (37, 685), (837, 685), 1)
        pygame.draw.line(screen, GRAY, (37, 675), (837, 675), 1)
        pygame.draw.line(screen, GRAY, (37, 665), (837, 665), 1)
        pygame.draw.line(screen, GRAY, (37, 655), (837, 655), 1)
        pygame.draw.line(screen, GRAY, (37, 645), (837, 645), 1)
        pygame.draw.line(screen, GRAY, (37, 635), (837, 635), 1)
        pygame.draw.line(screen, GRAY, (37, 625), (837, 625), 1)
        pygame.draw.line(screen, GRAY, (37, 615), (837, 615), 1)
        pygame.draw.line(screen, GRAY, (37, 605), (837, 605), 1)
        pygame.draw.line(screen, GRAY, (37, 595), (837, 595), 1)
        pygame.draw.line(screen, DARKGRAY, (36, 786), (36, 594), 1)
        pygame.draw.line(screen, DARKGRAY, (36, 786), (837, 786), 1)
        pygame.draw.line(screen, DARKGRAY, (36, 594), (837, 594), 1)
        pygame.draw.line(screen, DARKGRAY, (838, 786), (838, 594), 1)
    # Speed chart.
    pygame.draw.line(screen, GRAY, (25, 557), (186, 557), 1)
    pygame.draw.line(screen, GRAY, (25, 542), (186, 542), 1)
    pygame.draw.line(screen, GRAY, (25, 527), (186, 527), 1)
    pygame.draw.line(screen, GRAY, (25, 512), (186, 512), 1)
    pygame.draw.line(screen, GRAY, (25, 497), (186, 497), 1)
    pygame.draw.line(screen, GRAY, (25, 482), (186, 482), 1)
    pygame.draw.line(screen, GRAY, (25, 467), (186, 467), 1)
    pygame.draw.line(screen, GRAY, (25, 452), (186, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (24, 558), (24, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (24, 558), (186, 558), 1)
    pygame.draw.line(screen, DARKGRAY, (24, 451), (186, 451), 1)
    pygame.draw.line(screen, DARKGRAY, (187, 451), (187, 558), 1)
    text_to_blit = font5.render("0", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 552))
    text_to_blit = font5.render("1", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 537))
    text_to_blit = font5.render("2", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 522))
    text_to_blit = font5.render("3", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 507))
    text_to_blit = font5.render("4", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 492))
    text_to_blit = font5.render("5", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 477))
    text_to_blit = font5.render("6", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 462))
    text_to_blit = font5.render("7", True, (50, 50, 50))
    screen.blit(text_to_blit, (16, 447))
    # Bowel length chart.
    pygame.draw.line(screen, GRAY, (242, 557), (403, 557), 1)
    pygame.draw.line(screen, GRAY, (242, 542), (403, 542), 1)
    pygame.draw.line(screen, GRAY, (242, 527), (403, 527), 1)
    pygame.draw.line(screen, GRAY, (242, 512), (403, 512), 1)
    pygame.draw.line(screen, GRAY, (242, 497), (403, 497), 1)
    pygame.draw.line(screen, GRAY, (242, 482), (403, 482), 1)
    pygame.draw.line(screen, GRAY, (242, 467), (403, 467), 1)
    pygame.draw.line(screen, GRAY, (242, 452), (403, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (241, 558), (241, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (241, 558), (403, 558), 1)
    pygame.draw.line(screen, DARKGRAY, (241, 451), (403, 451), 1)
    pygame.draw.line(screen, DARKGRAY, (404, 451), (404, 558), 1)
    text_to_blit = font5.render("0", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 552))
    text_to_blit = font5.render("1", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 537))
    text_to_blit = font5.render("2", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 522))
    text_to_blit = font5.render("3", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 507))
    text_to_blit = font5.render("4", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 492))
    text_to_blit = font5.render("5", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 477))
    text_to_blit = font5.render("6", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 462))
    text_to_blit = font5.render("7", True, (50, 50, 50))
    screen.blit(text_to_blit, (233, 447))
    # Fat limit chart.
    pygame.draw.line(screen, GRAY, (459, 557), (620, 557), 1)
    pygame.draw.line(screen, GRAY, (459, 542), (620, 542), 1)
    pygame.draw.line(screen, GRAY, (459, 527), (620, 527), 1)
    pygame.draw.line(screen, GRAY, (459, 512), (620, 512), 1)
    pygame.draw.line(screen, GRAY, (459, 497), (620, 497), 1)
    pygame.draw.line(screen, GRAY, (459, 482), (620, 482), 1)
    pygame.draw.line(screen, GRAY, (459, 467), (620, 467), 1)
    pygame.draw.line(screen, GRAY, (459, 452), (620, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (458, 558), (458, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (458, 558), (620, 558), 1)
    pygame.draw.line(screen, DARKGRAY, (458, 451), (620, 451), 1)
    pygame.draw.line(screen, DARKGRAY, (621, 451), (621, 558), 1)
    text_to_blit = font5.render("0", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 552))
    text_to_blit = font5.render("1", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 537))
    text_to_blit = font5.render("2", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 522))
    text_to_blit = font5.render("3", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 507))
    text_to_blit = font5.render("4", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 492))
    text_to_blit = font5.render("5", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 477))
    text_to_blit = font5.render("6", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 462))
    text_to_blit = font5.render("7", True, (50, 50, 50))
    screen.blit(text_to_blit, (450, 447))
    # Legs length chart.
    pygame.draw.line(screen, GRAY, (676, 557), (837, 557), 1)
    pygame.draw.line(screen, GRAY, (676, 542), (837, 542), 1)
    pygame.draw.line(screen, GRAY, (676, 527), (837, 527), 1)
    pygame.draw.line(screen, GRAY, (676, 512), (837, 512), 1)
    pygame.draw.line(screen, GRAY, (676, 497), (837, 497), 1)
    pygame.draw.line(screen, GRAY, (676, 482), (837, 482), 1)
    pygame.draw.line(screen, GRAY, (676, 467), (837, 467), 1)
    pygame.draw.line(screen, GRAY, (676, 452), (837, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (675, 558), (675, 452), 1)
    pygame.draw.line(screen, DARKGRAY, (675, 558), (837, 558), 1)
    pygame.draw.line(screen, DARKGRAY, (675, 451), (837, 451), 1)
    pygame.draw.line(screen, DARKGRAY, (838, 451), (838, 558), 1)
    text_to_blit = font5.render("0", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 552))
    text_to_blit = font5.render("1", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 537))
    text_to_blit = font5.render("2", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 522))
    text_to_blit = font5.render("3", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 507))
    text_to_blit = font5.render("4", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 492))
    text_to_blit = font5.render("5", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 477))
    text_to_blit = font5.render("6", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 462))
    text_to_blit = font5.render("7", True, (50, 50, 50))
    screen.blit(text_to_blit, (667, 447))

    # Herbs icon.
    pygame.draw.circle(screen, FORESTGREEN, [711, 22], 3, 0)
    # Herbivores icon.
    pygame.draw.rect(screen, colors_list_green[7][7], [684 , 33, 9, 9])
    pygame.draw.rect(screen, DARKERGRAY, [684-1, 33-1, 11, 11], 1)
    # Carnivores icon.
    pygame.draw.rect(screen, colors_list_red[7][7], [684, 48, 9, 9])
    pygame.draw.rect(screen, DARKERGRAY, [684-1, 48-1, 11, 11], 1)

    # Settings text.
    text_to_blit = font6.render(("HERBS: " + str(len(herbs))), True, (50, 50, 50))
    screen.blit(text_to_blit, (717, 15))
    text_to_blit = font6.render(("HERBIVORES: " + str(len(herbivores))), True, (50, 50, 50))
    screen.blit(text_to_blit, (697, 30))
    text_to_blit = font6.render(("CARNIVORES: " + str(len(carnivores))), True, (50, 50, 50))
    screen.blit(text_to_blit, (697, 45))

    text_to_blit = font5.render("SETTINGS", True, (50, 50, 50))
    screen.blit(text_to_blit, (661, 69))
    text_to_blit = font2.render(("Cycles per sec: " + str(cycles_per_sec)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 85))
    text_to_blit = font2.render(("Tempo: " + str("{:.2f}".format(tempo))), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 105))
    text_to_blit = font2.render(("Mutation %: " + str(mutation_chance)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 125))

    text_to_blit = font5.render("HERBS", True, (50, 50, 50))
    screen.blit(text_to_blit, (662, 149))
    text_to_blit = font2.render(("Start. amount: " + str(herbs_starting_amount)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 165))
    text_to_blit = font2.render(("Energy: " + str(herbs_energy)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 185))
    text_to_blit = font2.render(("Per spawn: " + str(herbs_amount_per_spawn)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 205))
    text_to_blit = font2.render(("Spawn rate: " + str(herbs_spawn_rate)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 225))

    text_to_blit = font5.render("HERBIVORES", True, (50, 50, 50))
    screen.blit(text_to_blit, (662, 249))
    text_to_blit = font2.render(("Start. amount: " + str(herbivores_starting_amount)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 265))
    text_to_blit = font2.render(("Spawn energy: " + str(herbivores_spawn_energy)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 285))
    text_to_blit = font2.render(("Breed. level: " + str(herbivores_breed_level)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 305))
    text_to_blit = font2.render(("Movement cost: " + str(herbivores_movement_cost)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 325))

    text_to_blit = font5.render("CARNIVORES", True, (50, 50, 50))
    screen.blit(text_to_blit, (662, 349))
    text_to_blit = font2.render(("Start. amount: " + str(carnivores_starting_amount)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 365))
    text_to_blit = font2.render(("Spawn energy: " + str(carnivores_spawn_energy)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 385))
    text_to_blit = font2.render(("Breed. level: " + str(carnivores_breed_level)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 405))
    text_to_blit = font2.render(("Movement cost: " + str(carnivores_movement_cost)), True, (50, 50, 50))
    screen.blit(text_to_blit, (664, 425))

    text_to_blit = font2.render("AMOUNT", True, (50, 50, 50))
    screen.blit(text_to_blit, (85, 427))
    text_to_blit = font2.render("SPEED", True, (50, 50, 50))
    screen.blit(text_to_blit, (85, 559))
    text_to_blit = font2.render("BOWEL LENGTH", True, (50, 50, 50))
    screen.blit(text_to_blit, (278, 559))
    text_to_blit = font2.render("FAT LIMIT", True, (50, 50, 50))
    screen.blit(text_to_blit, (505, 559))
    text_to_blit = font2.render("LEGS LENGTH", True, (50, 50, 50))
    screen.blit(text_to_blit, (718, 559))

    # Start button.
    if btn_start_clicked == 1:
        screen.blit(START_DOWN, [36, 86])
    else:
        screen.blit(START_UP, [36, 86])

    # Pause button.
    if btn_pause_clicked == 1:
        screen.blit(PAUSE_DOWN, [85, 86])
    else:
        screen.blit(PAUSE_UP, [85, 86])

    # Reset button.
    if btn_reset_clicked == 1:
        screen.blit(RESET_DOWN, [134, 86])
    else:
        screen.blit(RESET_UP, [134, 86])

    # Cps plus button.
    if btn_cps_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 85])
    else:
        screen.blit(PLUS_UP, [826, 85])
    # Cps minus button.
    if btn_cps_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 85])
    else:
        screen.blit(MINUS_UP, [811, 85])

    # Tempo plus button.
    if btn_tempo_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 105])
    else:
        screen.blit(PLUS_UP, [826, 105])
    # Tempo minus button.
    if btn_tempo_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 105])
    else:
        screen.blit(MINUS_UP, [811, 105])

    # Mutation plus button.
    if btn_mutation_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 125])
    else:
        screen.blit(PLUS_UP, [826, 125])
    # Mutation minus button.
    if btn_mutation_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 125])
    else:
        screen.blit(MINUS_UP, [811, 125])

    # Herbs starting amount plus button.
    if btn_herbs_starting_amount_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 165])
    else:
        screen.blit(PLUS_UP, [826, 165])
    # Herbs starting amount minus button.
    if btn_herbs_starting_amount_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 165])
    else:
        screen.blit(MINUS_UP, [811, 165])

    # Herbs energy plus button.
    if btn_herbs_energy_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 185])
    else:
        screen.blit(PLUS_UP, [826, 185])
    # Herbs energy minus button.
    if btn_herbs_energy_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 185])
    else:
        screen.blit(MINUS_UP, [811, 185])

    # Herbs amount per spawn plus button.
    if btn_herbs_amount_per_spawn_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 205])
    else:
        screen.blit(PLUS_UP, [826, 205])
    # Herbs amount per spawn minus button.
    if btn_herbs_amount_per_spawn_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 205])
    else:
        screen.blit(MINUS_UP, [811, 205])

    # Herbs spawn rate plus button.
    if btn_herbs_spawn_rate_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 225])
    else:
        screen.blit(PLUS_UP, [826, 225])
    # Herbs spawn rate minus button.
    if btn_herbs_spawn_rate_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 225])
    else:
        screen.blit(MINUS_UP, [811, 225])

    # Herbivores starting amount plus button.
    if btn_herbivores_starting_amount_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 265])
    else:
        screen.blit(PLUS_UP, [826, 265])
    # Herbivores starting amount minus button.
    if btn_herbivores_starting_amount_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 265])
    else:
        screen.blit(MINUS_UP, [811, 265])

    # Herbivores spawn energy plus button.
    if btn_herbivores_spawn_energy_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 285])
    else:
        screen.blit(PLUS_UP, [826, 285])
    # Herbivores spawn energy minus button.
    if btn_herbivores_spawn_energy_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 285])
    else:
        screen.blit(MINUS_UP, [811, 285])

    # Herbivores breeding level plus button.
    if btn_herbivores_breed_level_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 305])
    else:
        screen.blit(PLUS_UP, [826, 305])
    # Herbivores breeding level minus button.
    if btn_herbivores_breed_level_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 305])
    else:
        screen.blit(MINUS_UP, [811, 305])

    # Herbivores movement cost plus button.
    if btn_herbivores_movement_cost_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 325])
    else:
        screen.blit(PLUS_UP, [826, 325])
    # Herbivores movement cost minus button.
    if btn_herbivores_movement_cost_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 325])
    else:
        screen.blit(MINUS_UP, [811, 325])

    # Carnivores starting amount plus button.
    if btn_carnivores_starting_amount_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 365])
    else:
        screen.blit(PLUS_UP, [826, 365])
    # Carnivores starting amount minus button.
    if btn_carnivores_starting_amount_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 365])
    else:
        screen.blit(MINUS_UP, [811, 365])

    # Carnivores spawning energy plus button.
    if btn_carnivores_spawn_energy_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 385])
    else:
        screen.blit(PLUS_UP, [826, 385])
    # Carnivores spawning energy minus button.
    if btn_carnivores_spawn_energy_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 385])
    else:
        screen.blit(MINUS_UP, [811, 385])

    # Carnivores breeding level plus button.
    if btn_carnivores_breed_level_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 405])
    else:
        screen.blit(PLUS_UP, [826, 405])
    # Carnivores breeding level minus button.
    if btn_carnivores_breed_level_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 405])
    else:
        screen.blit(MINUS_UP, [811, 405])

    # Carnivores movement cost plus button.
    if btn_carnivores_movement_cost_plus_clicked == 1:
        screen.blit(PLUS_DOWN, [826, 425])
    else:
        screen.blit(PLUS_UP, [826, 425])
    # Carnivores movement cost minus button.
    if btn_carnivores_movement_cost_minus_clicked == 1:
        screen.blit(MINUS_DOWN, [811, 425])
    else:
        screen.blit(MINUS_UP, [811, 425])

        # If bigger_screen flag == 1 (the window becomes taller), draw
        # a chart of total history of mean amounts of herbivores and carnivores.
    if bigger_screen == 1:
        x_herbi = 36
        for i in range(0, len(herbivores_total_amount_list)):
            if len(herbivores_total_amount_list) > 800:
                if i % (int(len(herbivores_total_amount_list) / 800) + 1) == 0:
                    x_herbi += 1
                    pygame.draw.rect(screen, colors_list_green[2][3],
                                     [x_herbi,
                                     780 - int(herbivores_total_amount_list[i] / 4),
                                     2, 2])
            else:
                pygame.draw.rect(screen, colors_list_green[2][3],
                                 [37 + i,
                                 780 - int(herbivores_total_amount_list[i] / 4),
                                 2, 2])
            x_carni = 36
        for i in range(0, len(carnivores_total_amount_list)):
            if len(carnivores_total_amount_list) > 800:
                if i % (int(len(carnivores_total_amount_list) / 800) + 1) == 0:
                    x_carni += 1
                    pygame.draw.rect(screen, colors_list_red[2][3],
                                     [x_carni,
                                     780 - int(carnivores_total_amount_list[i] / 4),
                                     2, 2])
            else:
                pygame.draw.rect(screen, colors_list_red[2][3],
                                 [37 + i,
                                 780 - int(carnivores_total_amount_list[i] / 4),
                                 2, 2])
        # Drawing charts.
    # Amount of herbivores and carnivores charts.
    for i in range(0, len(herbivores_amount_list)):
        pygame.draw.rect(screen, colors_list_green[2][3],
                         [29 + i, 422 - int(herbivores_amount_list[i] / 5), 2, 2])
    for i in range(0, len(carnivores_amount_list)):
        pygame.draw.rect(screen, colors_list_red[2][3],
                         [29 + i, 422 - int(carnivores_amount_list[i] / 5), 2, 2])
    # Drawing charts.
    # Mean value of herbivores traits charts.
    for i in range(0, len(herbivores_mean_speed_list)):
        pygame.draw.rect(screen, colors_list_green[4][3],
                         [25 + i, 556 - int(herbivores_mean_speed_list[i] * 12), 2, 2])
    for i in range(0, len(herbivores_mean_bowel_length_list)):
        pygame.draw.rect(screen, colors_list_green[4][3],
                         [242 + i, 556 - int(herbivores_mean_bowel_length_list[i] * 12), 2, 2])
    for i in range(0, len(herbivores_mean_fat_limit_list)):
        pygame.draw.rect(screen, colors_list_green[4][3],
                         [459 + i, 556 - int(herbivores_mean_fat_limit_list[i] * 12), 2, 2])
    for i in range(0, len(herbivores_mean_legs_length_list)):
        pygame.draw.rect(screen, colors_list_green[4][3],
                         [676 + i, 556 - int(herbivores_mean_legs_length_list[i] * 12), 2, 2])
    # Drawing charts.
    # Mean value of herbivores traits charts.
    for i in range(0, len(carnivores_mean_speed_list)):
        pygame.draw.rect(screen, colors_list_red[4][3],
                         [25 + i, 556 - int(carnivores_mean_speed_list[i] * 12), 2, 2])
    for i in range(0, len(carnivores_mean_bowel_length_list)):
        pygame.draw.rect(screen, colors_list_red[4][3],
                         [242 + i, 556 - int(carnivores_mean_bowel_length_list[i] * 12), 2, 2])
    for i in range(0, len(carnivores_mean_fat_limit_list)):
        pygame.draw.rect(screen, colors_list_red[4][3],
                         [459 + i, 556 - int(carnivores_mean_fat_limit_list[i] * 12), 2, 2])
    for i in range(0, len(carnivores_mean_legs_length_list)):
        pygame.draw.rect(screen, colors_list_red[4][3],
                         [676 + i, 556 - int(carnivores_mean_legs_length_list[i] * 12), 2, 2])

############################################################################################################

# Class creating herbs.
class Herb:
    def __init__(self, coord_x, coord_y, index, energy):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.energy = energy

    def draw(self):
        pygame.draw.circle(screen, FORESTGREEN, [(grid[self.coord_y][self.coord_x][0])+4,
                                                 (grid[self.coord_y][self.coord_x][1])+4], 3, 0)
        '''
         You can unhash this line for fancier look of the herbs.
         It is also possible to experiment a bit
         with /2, 0/ and /2/ parts to get different effects. '''
         # pygame.draw.circle(screen, GRAY, [(grid[self.coord_y][self.coord_x][0])+4,
                                            # (grid[self.coord_y][self.coord_x][1])+4], 2)

    def get_energy(self):
        return self.energy

    def get_coords(self):
        return self.coord_x, self.coord_y

    def got_eaten(self):
        herbs_pos[self.coord_y][self.coord_x] = []
        del herbs[self.index]
        for i in range(self.index, len(herbs)):
            herbs[i].index -= 1


# Class creating animals.
class animal:
    def __init__(self, coord_x, coord_y, index, dna):
        pass

    def get_index(self):
        return self.index

    def get_dna(self):
        return self.dna

    def get_state(self):
        if self.energy > 0: return 1 #alive
        if self.energy < 1: return 0 #dead

    def get_energy(self):
        return self.energy

    def set_energy(self, new_energy):
        self.energy = new_energy

    def get_coords(self):
        return (self.coord_x, self.coord_y)


############################################################################################################

# Class creating carnivores.
class Carnivore(animal):
    def __init__(self, coord_x, coord_y, index, dna):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.energy = carnivores_spawn_energy
        self.index = index
        self.dna = dna
        self.color = 0
        self.speed = speed_dict[int(dna[0])]
        self.bowel_length = bowel_length_dict[int(dna[1])]
        self.fat_limit = fat_limit_dict[int(dna[2])]
        self.legs_length = legs_length_dict[int(dna[3])]
        self.forbidden_move = random.choice(("e", "w", "s", "n"))
        self.possible_moves = ["e", "w", "s", "n"]

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > carnivores_breed_level:
            return "breeding"
        else:
            return "eating"

    def breeding(self):
        if len(carnivores_pos[self.coord_y][self.coord_x]) > 1:
            for i in carnivores:
                if (self.coord_x, self.coord_y) == i.get_coords():
                    if i.get_intention() == "breeding":
                        if i != carnivores[self.get_index()]:
                            self.energy = int(self.energy / 2)
                            i.set_energy(int(i.get_energy()/2))
                            born_carnivore(i.get_coords()[0], i.get_coords()[1], self.get_dna(),
                                           i.get_dna())
                        break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == "breeding":
            self.breeding()
        else:
            self.eat()

    def carni_starved(self):
        # Remove one "1" from list's (carnivores_pos) cell of this tile.
        carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]
        # Create a herb on the tile the animal died on.
        create_herb_on_field(herbs_energy, self.coord_x, self.coord_y)
        del carnivores[self.index]
        # Change all indexes of the still living carnivores by -1,
        # because all objects in the list that were after current
        # object moved to the left after its removal.
        for i in range(self.index, len(carnivores)):
            carnivores[i].index -= 1

    def draw(self):
        if self.get_energy() < carnivores_breed_level:
            pygame.draw.rect(screen, colors_list_red[self.color][3],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        else:
            pygame.draw.rect(screen, colors_list_red[self.color][7],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border.
        pygame.draw.rect(screen, DARKERGRAY,
                         [grid[self.coord_y][self.coord_x][0]-1,
                          grid[self.coord_y][self.coord_x][1]-1, 11, 11], 1)

    def move(self):
        if int(counter_prev) != int(counter):
            if int(counter) % self.speed == 0:
                carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]

                self.energy -=   carnivores_movement_cost \
                               * self.legs_length \
                               * speed_cost_dict[int(self.dna[0])] \
                               * bowel_length_dict_cost[int(self.dna[1])] \
                               * fat_limit_cost_dict[int(self.dna[2])] \
                               * legs_length_cost_dict[int(self.dna[3])]

                if not (self.coord_x == 0  or
                        self.coord_x == 42 or
                        self.coord_y == 0  or
                        self.coord_y == 42):
                        # If all conditions satisfied:
                    self.possible_moves.remove(self.forbidden_move)
                    move = random.choice(self.possible_moves)
                    if move == "e":
                        self.coord_x += 1
                        self.forbidden_move = "w"
                    elif move == "w":
                        self.coord_x -= 1
                        self.forbidden_move = "e"
                    elif move == "s":
                        self.coord_y += 1
                        self.forbidden_move = "n"
                    elif move == "n":
                        self.coord_y -= 1
                        self.forbidden_move = "s"
                else:
                    if self.coord_x == 0:
                        self.coord_x += 1
                        self.forbidden_move = "w"
                    elif self.coord_x == 42:
                        self.coord_x -= 1
                        self.forbidden_move = "e"
                    elif self.coord_y == 0:
                        self.coord_y += 1
                        self.forbidden_move = "n"
                    elif self.coord_y == 42:
                        self.coord_y -= 1
                        self.forbidden_move = "s"
                self.possible_moves = ["e", "w", "s", "n"]
                carnivores_pos[self.coord_y][self.coord_x].append(1)

    def eat(self):
        if len(herbivores_pos[self.coord_y][self.coord_x]) > 0:
            for i in herbivores:
                if self.coord_x == i.get_coords()[0] and self.coord_y == i.get_coords()[1]:
                    self.energy += i.get_energy() * self.bowel_length
                    i.got_eaten()
                    break


############################################################################################################

# Class creating herbivores.
class Herbivore(animal):
    def __init__(self, coord_x, coord_y, index, dna):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.energy = herbivores_spawn_energy
        self.index = index
        self.dna = dna
        self.color = 0
        self.speed = speed_dict[int(dna[0])]
        self.bowel_length = bowel_length_dict[int(dna[1])]
        self.fat_limit = fat_limit_dict[int(dna[2])]
        self.legs_length = legs_length_dict[int(dna[3])]
        self.forbidden_move = random.choice(("e", "w", "s", "n"))
        self.possible_moves = ["e", "w", "s", "n"]

    def get_intention(self): # 1 - breeding, 0 - food.
        if self.energy > herbivores_breed_level:
            return "breeding"
        else:
            return "eating"

    def breeding(self):
        if len(herbivores_pos[self.coord_y][self.coord_x]) > 1:
            for i in herbivores:
                if (self.coord_x, self.coord_y) == i.get_coords():
                    if i.get_intention() == "breeding":
                        if i != herbivores[self.get_index()]:
                            self.energy = int(self.energy / 2)
                            i.set_energy(int(i.get_energy()/2))
                            born_herbivore(i.get_coords()[0], i.get_coords()[1], self.get_dna(),
                                           i.get_dna())
                        break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == "breeding":
            self.breeding()
        else:
            self.eat()

    def herbi_starved(self):
        # Remove one "1" from list's (herbivores_pos) cell of this tile.
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        # Create a herb on the tile the animal died on.
        create_herb_on_field(herbs_energy, self.coord_x, self.coord_y)
        del herbivores[self.index]
        # Change all indexes of the still living carnivores by -1,
        # because all objects in the list that were after current
        # object moved to the left after its removal.
        for i in range(self.index, len(herbivores)):
            herbivores[i].index -= 1

    def draw(self):
        if self.get_energy() < herbivores_breed_level:
            pygame.draw.rect(screen, colors_list_green[self.color][3],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        else:
            pygame.draw.rect(screen, colors_list_green[self.color][7],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border.
        pygame.draw.rect(screen, DARKERGRAY,
                         [grid[self.coord_y][self.coord_x][0]-1,
                          grid[self.coord_y][self.coord_x][1]-1, 11, 11], 1)

    def move(self):
        if int(counter_prev) != int(counter):
            if int(counter) % self.speed == 0:
                herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]

                self.energy -=   herbivores_movement_cost \
                               * self.legs_length \
                               * speed_cost_dict[int(self.dna[0])] \
                               * bowel_length_dict_cost[int(self.dna[1])] \
                               * fat_limit_cost_dict[int(self.dna[2])] \
                               * legs_length_cost_dict[int(self.dna[3])]

                if not (self.coord_x == 0  or
                        self.coord_x == 42 or
                        self.coord_y == 0  or
                        self.coord_y == 42):
                        # If all conditions satisfied:
                    self.possible_moves.remove(self.forbidden_move)
                    move = random.choice(self.possible_moves)
                    if move == "e":
                        self.coord_x += 1
                        self.forbidden_move = "w"
                    elif move == "w":
                        self.coord_x -= 1
                        self.forbidden_move = "e"
                    elif move == "s":
                        self.coord_y += 1
                        self.forbidden_move = "n"
                    elif move == "n":
                        self.coord_y -= 1
                        self.forbidden_move = "s"
                else:
                    if self.coord_x == 0:
                        self.coord_x += 1
                        self.forbidden_move = "w"
                    elif self.coord_x == 42:
                        self.coord_x -= 1
                        self.forbidden_move = "e"
                    elif self.coord_y == 0:
                        self.coord_y += 1
                        self.forbidden_move = "n"
                    elif self.coord_y == 42:
                        self.coord_y -= 1
                        self.forbidden_move = "s"
                self.possible_moves = ["e", "w", "s", "n"]
                herbivores_pos[self.coord_y][self.coord_x].append(1)

    def eat(self):
        if len(herbs_pos[self.coord_y][self.coord_x]) > 0:
            for i in herbs:
                if self.coord_x == i.get_coords()[0] and self.coord_y == i.get_coords()[1]:
                    self.energy += i.get_energy() * self.bowel_length
                    i.got_eaten()
                    break

    def got_eaten(self):
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        del herbivores[self.index]
        for i in range(self.index, len(herbivores)):
            herbivores[i].index -= 1


############################################################################################################

# Creating a new herb - chooses random xy, checks on the herbs grid
# whether that xy is free. If it is - creates a new herb (adds 1
# to the grid, symbolising that a herb exists there, and creates
# an object on herbs list).
def create_herb(herbs_energy, herbs_amount_per_spawn):
    for i in range(0, herbs_amount_per_spawn):
        pos_y = random.randint(1, 41)
        pos_x = random.randint(1, 41)
        if len(herbs_pos[pos_y][pos_x]) == 0:
            herbs.append(Herb(pos_x, pos_y, len(herbs), herbs_energy))
            herbs_pos[pos_y][pos_x].append(1)

# Create a herb on a selected field.
def create_herb_on_field(herbs_energy, pos_x, pos_y):
    if len(herbs_pos[pos_y][pos_x]) == 0:
        herbs.append(Herb(pos_x, pos_y, len(herbs), herbs_energy))
        herbs_pos[pos_y][pos_x].append(1)

# Growing new herbs every /speed_dict[speed]/ frames
# in the amount of /herbs_amount_per_spawn/.
def grow_herbs(herbs_energy, speed):
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % speed_dict[speed] == 0:
            create_herb(herbs_energy, herbs_amount_per_spawn)

def spawn_herbs(herbs_energy, amount):
    amount_left_to_spawn = amount
    while amount_left_to_spawn != 0:
        pos_y = random.randint(1, 41)
        pos_x = random.randint(1, 41)
        if len(herbs_pos[pos_y][pos_x]) == 0:
            herbs.append(Herb(pos_x, pos_y, len(herbs), herbs_energy))
            herbs_pos[pos_y][pos_x].append(1)
            amount_left_to_spawn -= 1

############################################################################################################

# Spawn carnivore that was born.
def born_carnivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0, 99) >= mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0, 7)))
    #print("NEW CARNIVORE:", dna1, dna2, new_dna)
    carnivores.append(Carnivore(pos_x, pos_y, len(carnivores),
                                  new_dna[0]
                                + new_dna[1]
                                + new_dna[2]
                                + new_dna[3]))
    carnivores_pos[pos_y][pos_x].append(1)

# Spawn a new carnivore.
def spawn_carnivore(amount):
    amount_left_to_spawn = amount
    while amount_left_to_spawn != 0:
        pos_y = random.randint(1, 41)
        pos_x = random.randint(1, 41)
        if len(carnivores_pos[pos_y][pos_x]) < 1:
            carnivores.append(Carnivore(pos_x, pos_y, len(carnivores),
                                          str(random.randint(0, 7))
                                        + str(random.randint(0, 7))
                                        + str(random.randint(0, 7))
                                        + str(random.randint(0, 7))))
            carnivores_pos[pos_y][pos_x].append(1)
            amount_left_to_spawn -= 1

# Spawn herbivore that was born.
def born_herbivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0, 99) >= mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0, 7)))
    #print("NEW HERBIVORE:", dna1, dna2, new_dna)
    herbivores.append(Herbivore(pos_x, pos_y, len(herbivores),
                                  new_dna[0]
                                + new_dna[1]
                                + new_dna[2]
                                + new_dna[3]))
    herbivores_pos[pos_y][pos_x].append(1)

# Spawn a new herbivore.
def spawn_herbivore(amount):
    amount_left_to_spawn = amount
    while amount_left_to_spawn != 0:
        pos_y = random.randint(1, 41)
        pos_x = random.randint(1, 41)
        if len(herbivores_pos[pos_y][pos_x]) < 1:
            herbivores.append(Herbivore(pos_x, pos_y, len(herbivores),
                                          str(random.randint(0, 7))
                                        + str(random.randint(0, 7))
                                        + str(random.randint(0, 7))
                                        + str(random.randint(0, 7))))
            herbivores_pos[pos_y][pos_x].append(1)
            amount_left_to_spawn -= 1

############################################################################################################

# Add starting herbs, herbivores and carnivores.
spawn_herbs(herbs_energy, herbs_starting_amount)
spawn_herbivore(herbivores_starting_amount)
spawn_carnivore(carnivores_starting_amount)

# Set the main loop to not done and initialize a clock.
done = False
clock = pygame.time.Clock()

# ================================================================================================ #
# ################################################################################################ #
# ##------------------------------------- Main Program Loop ------------------------------------## #
# ################################################################################################ #
# ================================================================================================ #


while not done:
    # ################################# #
    # ##------ Main Event loop ------## #
    # ################################# #

    # Catching events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # "If keyboard button clicked:".
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Add 50 herbivores.
                spawn_herbivore(50)
            if event.key == pygame.K_RIGHT:
                # Add 20 carnivores.
                spawn_carnivore(20)
            if event.key == pygame.K_UP:
                screen = pygame.display.set_mode((855, 583))
                bigger_screen = 0
            if event.key == pygame.K_DOWN:
                screen = pygame.display.set_mode((855, 810))
                bigger_screen = 1

        # "If mouse button clicked:".
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Start button clicked.
            if pygame.mouse.get_pos()[0] >= 36  and \
               pygame.mouse.get_pos()[0] <= 75  and \
               pygame.mouse.get_pos()[1] >= 86  and \
               pygame.mouse.get_pos()[1] <= 106:
                   # If all conditions satisfied:
                   pause = 0
                   btn_start_clicked = 1

            # Pause button clicked.
            if pygame.mouse.get_pos()[0] >= 85  and \
               pygame.mouse.get_pos()[0] <= 124 and \
               pygame.mouse.get_pos()[1] >= 86  and \
               pygame.mouse.get_pos()[1] <= 106:
                   # If all conditions satisfied:
                   # start = tempo
                   pause = 1
                   btn_pause_clicked = 1

            # Reset button clicked.
            if pygame.mouse.get_pos()[0] >= 136 and \
               pygame.mouse.get_pos()[0] <= 175 and \
               pygame.mouse.get_pos()[1] >= 86  and \
               pygame.mouse.get_pos()[1] <= 106:
                   # If all conditions satisfied:
                   reset = 1
                   btn_reset_clicked = 1

            # Cycles Per Second plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 85  and \
               pygame.mouse.get_pos()[1] <= 98:
                   # If all conditions satisfied:
                   chosen_cycles_per_second += 1
                   if chosen_cycles_per_second > 13:
                       chosen_cycles_per_second = 13
                   btn_cps_plus_clicked = 1
            # Cycles Per Second minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 85  and \
               pygame.mouse.get_pos()[1] <= 98:
                   # If all conditions satisfied:
                   chosen_cycles_per_second -= 1
                   if chosen_cycles_per_second < 0:
                       chosen_cycles_per_second = 0
                   btn_cps_minus_clicked = 1

            # Tempo plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 105 and \
               pygame.mouse.get_pos()[1] <= 118:
                   # If all conditions satisfied:
                   tempo += 0.09
                   # If /tempo/ > 1, set it to 1. Makes '1' a min value.
                   if tempo > 1.00: tempo = 1.00
                   btn_tempo_plus_clicked = 1
            # Tempo minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 105 and \
               pygame.mouse.get_pos()[1] <= 118:
                   # If all conditions satisfied:
                   tempo -= 0.09
                   # If /tempo/ < 0.01, set it to 0.01. Makes '0.01' a min value.
                   if tempo < 0.01: tempo = 0.01
                   btn_tempo_minus_clicked = 1

            # Mutation plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 125 and \
               pygame.mouse.get_pos()[1] <= 138:
                   # If all conditions satisfied:
                   mutation_chance += 1
                   if mutation_chance > 100:
                       mutation_chance = 100
                   btn_mutation_plus_clicked = 1
            # Mutation minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 125 and \
               pygame.mouse.get_pos()[1] <= 138:
                   # If all conditions satisfied:
                   mutation_chance -= 1
                   if mutation_chance < 0:
                       mutation_chance = 0
                   btn_mutation_minus_clicked = 1

            # Herbs starting amount plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 165 and \
               pygame.mouse.get_pos()[1] <= 178:
                   # If all conditions satisfied:
                   herbs_starting_amount += 50
                   if herbs_starting_amount > 1000:
                       herbs_starting_amount = 1000
                   btn_herbs_starting_amount_plus_clicked = 1
            # Herbs starting amount minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 165 and \
               pygame.mouse.get_pos()[1] <= 178:
                   # If all conditions satisfied:
                   herbs_starting_amount -= 50
                   if herbs_starting_amount < 0:
                       herbs_starting_amount = 0
                   btn_herbs_starting_amount_minus_clicked = 1

            # Herbs energy plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 185 and \
               pygame.mouse.get_pos()[1] <= 198:
                   # If all conditions satisfied:
                   herbs_energy += 50
                   if herbs_energy > 5500:
                       herbs_energy = 5500
                   btn_herbs_energy_plus_clicked = 1
            # Herbs energy minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 185 and \
               pygame.mouse.get_pos()[1] <= 198:
                   # If all conditions satisfied:
                   herbs_energy -= 50
                   if herbs_energy < 0:
                       herbs_energy = 0
                   btn_herbs_energy_minus_clicked = 1

            # Herbs amount per spawn plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 205 and \
               pygame.mouse.get_pos()[1] <= 218:
                   # If all conditions satisfied:
                   herbs_amount_per_spawn += 1
                   if herbs_amount_per_spawn > 100:
                       herbs_amount_per_spawn = 100
                   btn_herbs_amount_per_spawn_plus_clicked = 1
            # Herbs amount per spawn minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 205 and \
               pygame.mouse.get_pos()[1] <= 218:
                   # If all conditions satisfied:
                   herbs_amount_per_spawn -= 1
                   if herbs_amount_per_spawn < 0:
                       herbs_amount_per_spawn = 0
                   btn_herbs_amount_per_spawn_minus_clicked = 1

            # Herbs spawn rate plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 225 and \
               pygame.mouse.get_pos()[1] <= 238:
                   # If all conditions satisfied:
                   herbs_spawn_rate += 1
                   if herbs_spawn_rate > 7:
                       herbs_spawn_rate = 7
                   btn_herbs_spawn_rate_plus_clicked = 1
            # Herbs spawn rate minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 225 and \
               pygame.mouse.get_pos()[1] <= 238:
                   # If all conditions satisfied:
                   herbs_spawn_rate -= 1
                   if herbs_spawn_rate < 0:
                       herbs_spawn_rate = 0
                   btn_herbs_spawn_rate_minus_clicked = 1

            # Herbivores starting amount plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 265 and \
               pygame.mouse.get_pos()[1] <= 278:
                   # If all conditions satisfied:
                   herbivores_starting_amount += 20
                   if herbivores_starting_amount > 800:
                       herbivores_starting_amount = 800
                   btn_herbivores_starting_amount_plus_clicked = 1
            # Herbivores starting amount minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 265 and \
               pygame.mouse.get_pos()[1] <= 278:
                   # If all conditions satisfied:
                   herbivores_starting_amount -= 20
                   if herbivores_starting_amount < 0:
                       herbivores_starting_amount = 0
                   btn_herbivores_starting_amount_minus_clicked = 1

            # Herbivores spawn energy plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 285 and \
               pygame.mouse.get_pos()[1] <= 298:
                   # If all conditions satisfied:
                   herbivores_spawn_energy += 50
                   if herbivores_spawn_energy > 5500:
                       herbivores_spawn_energy = 5500
                   btn_herbivores_spawn_energy_plus_clicked = 1
            # Herbivores spawn energy minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 285 and \
               pygame.mouse.get_pos()[1] <= 298:
                   # If all conditions satisfied:
                   herbivores_spawn_energy -= 50
                   if herbivores_spawn_energy < 0:
                       herbivores_spawn_energy = 0
                   btn_herbivores_spawn_energy_minus_clicked = 1

            # Herbivores breeding level plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 305 and \
               pygame.mouse.get_pos()[1] <= 318:
                   # If all conditions satisfied:
                   herbivores_breed_level += 50
                   if herbivores_breed_level > 5500:
                       herbivores_breed_level = 5500
                   btn_herbivores_breed_level_plus_clicked = 1
            # Herbivores breeding level minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 305 and \
               pygame.mouse.get_pos()[1] <= 318:
                   # If all conditions satisfied:
                   herbivores_breed_level -= 50
                   if herbivores_breed_level < 0:
                       herbivores_breed_level = 0
                   btn_herbivores_breed_level_minus_clicked = 1

            # Herbivores movement cost plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 325 and \
               pygame.mouse.get_pos()[1] <= 338:
                   # If all conditions satisfied:
                   herbivores_movement_cost += 5
                   if herbivores_movement_cost > 200:
                       herbivores_movement_cost = 200
                   btn_herbivores_movement_cost_plus_clicked = 1
            # Herbivores movement cost minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 325 and \
               pygame.mouse.get_pos()[1] <= 338:
                   # If all conditions satisfied:
                   herbivores_movement_cost -= 5
                   if herbivores_movement_cost < 0:
                       herbivores_movement_cost = 0
                   btn_herbivores_movement_cost_minus_clicked = 1

            # Carnivores starting amount plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 365 and \
               pygame.mouse.get_pos()[1] <= 378:
                   # If all conditions satisfied:
                   carnivores_starting_amount += 5
                   if carnivores_starting_amount > 300:
                       carnivores_starting_amount = 300
                   btn_carnivores_starting_amount_plus_clicked = 1
            # Carnivores starting amount minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 365 and \
               pygame.mouse.get_pos()[1] <= 378:
                   # If all conditions satisfied:
                   carnivores_starting_amount -= 5
                   if carnivores_starting_amount < 0:
                       carnivores_starting_amount = 0
                   btn_carnivores_starting_amount_minus_clicked = 1

            # Carnivores spawning energy plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 385 and \
               pygame.mouse.get_pos()[1] <= 398:
                   # If all conditions satisfied:
                   carnivores_spawn_energy += 50
                   if carnivores_spawn_energy > 5500:
                       carnivores_spawn_energy = 5500
                   btn_carnivores_spawn_energy_plus_clicked = 1
            # Carnivores spawning energy minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 385 and \
               pygame.mouse.get_pos()[1] <= 398:
                   # If all conditions satisfied:
                   carnivores_spawn_energy -= 50
                   if carnivores_spawn_energy < 0:
                       carnivores_spawn_energy = 0
                   btn_carnivores_spawn_energy_minus_clicked = 1

            # Carnivores breeding level plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 405 and \
               pygame.mouse.get_pos()[1] <= 418:
                   # If all conditions satisfied:
                   carnivores_breed_level += 50
                   if carnivores_breed_level > 5500:
                       carnivores_breed_level = 5500
                   btn_carnivores_breed_level_plus_clicked = 1
            # Carnivores breeding level minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 405 and \
               pygame.mouse.get_pos()[1] <= 418:
                   # If all conditions satisfied:
                   carnivores_breed_level -= 50
                   if carnivores_breed_level < 0:
                       carnivores_breed_level = 0
                   btn_carnivores_breed_level_minus_clicked = 1

            # Carnivores movement cost plus button clicked.
            if pygame.mouse.get_pos()[0] >= 826 and \
               pygame.mouse.get_pos()[0] <= 839 and \
               pygame.mouse.get_pos()[1] >= 425 and \
               pygame.mouse.get_pos()[1] <= 438:
                   # If all conditions satisfied:
                   carnivores_movement_cost += 10
                   if carnivores_movement_cost > 500:
                       carnivores_movement_cost = 500
                   btn_carnivores_movement_cost_plus_clicked = 1
            # Carnivores movement cost minus button clicked.
            if pygame.mouse.get_pos()[0] >= 811 and \
               pygame.mouse.get_pos()[0] <= 824 and \
               pygame.mouse.get_pos()[1] >= 425 and \
               pygame.mouse.get_pos()[1] <= 438:
                   # If all conditions satisfied:
                   carnivores_movement_cost -= 10
                   if carnivores_movement_cost < 0:
                       carnivores_movement_cost = 0
                   btn_carnivores_movement_cost_minus_clicked = 1

        # "If mouse button unclicked:".
        if event.type == pygame.MOUSEBUTTONUP:
                   btn_start_clicked = 0
                   btn_pause_clicked = 0
                   btn_reset_clicked = 0
                   btn_tempo_plus_clicked = 0
                   btn_tempo_minus_clicked = 0
                   btn_cps_plus_clicked = 0
                   btn_cps_minus_clicked = 0
                   btn_mutation_plus_clicked = 0
                   btn_mutation_minus_clicked = 0
                   btn_herbs_starting_amount_plus_clicked = 0
                   btn_herbs_starting_amount_minus_clicked = 0
                   btn_herbs_energy_plus_clicked = 0
                   btn_herbs_energy_minus_clicked = 0
                   btn_herbs_amount_per_spawn_plus_clicked = 0
                   btn_herbs_amount_per_spawn_minus_clicked = 0
                   btn_herbs_spawn_rate_plus_clicked = 0
                   btn_herbs_spawn_rate_minus_clicked = 0
                   btn_herbivores_starting_amount_plus_clicked = 0
                   btn_herbivores_starting_amount_minus_clicked = 0
                   btn_herbivores_spawn_energy_plus_clicked = 0
                   btn_herbivores_spawn_energy_minus_clicked = 0
                   btn_herbivores_breed_level_plus_clicked = 0
                   btn_herbivores_breed_level_minus_clicked = 0
                   btn_herbivores_movement_cost_plus_clicked = 0
                   btn_herbivores_movement_cost_minus_clicked = 0
                   btn_carnivores_starting_amount_plus_clicked = 0
                   btn_carnivores_starting_amount_minus_clicked = 0
                   btn_carnivores_spawn_energy_plus_clicked = 0
                   btn_carnivores_spawn_energy_minus_clicked = 0
                   btn_carnivores_breed_level_plus_clicked = 0
                   btn_carnivores_breed_level_minus_clicked = 0
                   btn_carnivores_movement_cost_plus_clicked = 0
                   btn_carnivores_movement_cost_minus_clicked = 0

    # Set CPS.
    cycles_per_sec = cycles_per_sec_list[chosen_cycles_per_second]
    clock.tick(cycles_per_sec)
    # Increase /counter/ with a step of a size of /tempo/ every frame,
    # if simulation isn't paused. If /counter/ is bigger than 120,
    # reset it, and increase /big_counter/ by 1.
    counter_prev = counter
    #print("pre :",big_counter)
    #print("pre PREV:",big_counter_prev)
    big_counter_prev = big_counter
    #print("post :",big_counter)
    #print("post PREV :",big_counter_prev)
    if not pause:
        counter += tempo
    if int(counter) >= 120:
        big_counter += 1
        counter = 0

    # Increase /counter_for_fps/ by 1.
    # If /counter_for_fps/ is bigger than 120,
    # reset it.
    counter_for_fps += 1
    if counter_for_fps == 120:
        counter_for_fps = 0

    # ################################# #
    # ##- Game Logic / Drawing Code -## #
    # ################################# #

    # Draw interface.
    if counter_for_fps % cycles_per_sec_dividers_list[chosen_cycles_per_second] == 0:
       # If condition is satisfied:
        screen.fill(LIGHTGRAY)
        draw_window(colors_list_green, colors_list_red, herbs, herbivores, carnivores,
                    cycles_per_sec, tempo, herbs_spawn_rate, herbs_amount_per_spawn, herbs_energy,
                    herbs_starting_amount, herbivores_starting_amount, carnivores_starting_amount,
                    herbivores_spawn_energy, carnivores_spawn_energy, herbivores_breed_level,
                    carnivores_breed_level, herbivores_movement_cost, carnivores_movement_cost,
                    mutation_chance, btn_start_clicked, btn_pause_clicked, btn_reset_clicked,
                    btn_tempo_plus_clicked, btn_tempo_minus_clicked, btn_cps_plus_clicked,
                    btn_cps_minus_clicked)
        # Animation to prevent Windows from hanging the window when paused.
        # Also useful in approximating lag.
        text_to_blit = font7.render(animation[0], True, (50, 50, 50))
        screen.blit(text_to_blit, (837, 561))
        animation = animation + animation[0]
        animation = animation[1:]

    # Spawn herbs every /speed_dict[herbs_spawn_rate]/ frames.
    grow_herbs(herbs_energy, herbs_spawn_rate)

    # Draw herbs.
    if counter_for_fps % cycles_per_sec_dividers_list[chosen_cycles_per_second] == 0:
        for i in herbs:
            i.draw()

    # Check if any carnivore died out of starvation,
    # then either breed or eat, then move.
    for i in herbivores:
        if i.get_state() == 0:
            i.herbi_starved()
    if not pause:
        for i in herbivores:
            i.action()
    for i in herbivores:
        if counter_for_fps % cycles_per_sec_dividers_list[chosen_cycles_per_second] == 0:
            i.draw()
        i.move()

    # Check if any carnivore died out of starvation,
    # then either breed or eat, then move.
    for i in carnivores:
        if i.get_state() == 0:
            i.carni_starved()
    if not pause:
        for i in carnivores:
            i.action()
    for i in carnivores:
        if counter_for_fps % cycles_per_sec_dividers_list[chosen_cycles_per_second] == 0:
            i.draw()
        i.move()

    # Reseting the simulation.
    if reset == 1:
        if reset_counter > 0:
            for i in herbs:
                i.got_eaten()
            for i in herbivores:
                i.set_energy(0)
            for i in carnivores:
                i.set_energy(0)
        reset_counter -= 1
        if reset_counter == 0:
            big_counter = 0
            report = open(str(datetime.now())[:13] + "." + str(datetime.now())[14:16] + "." + str(datetime.now())[17:19]
                          + ".txt", "w")
            spawn_herbs(herbs_energy, herbs_starting_amount)
            spawn_herbivore(herbivores_starting_amount)
            spawn_carnivore(carnivores_starting_amount)
            herbivores_amount_list = []
            carnivores_amount_list = []
            herbivores_total_amount_list = []
            carnivores_total_amount_list = []
            herbs_amount_list = []
            herbivores_mean_speed_list = []
            herbivores_mean_bowel_length_list = []
            herbivores_mean_fat_limit_list = []
            herbivores_mean_legs_length_list = []
            carnivores_mean_speed_list = []
            carnivores_mean_bowel_length_list = []
            carnivores_mean_fat_limit_list = []
            carnivores_mean_legs_length_list = []
            reset = 0
            reset_counter = 12
            total_cycles_counter = 0

    # Displaying info and updating mean values lists.
    if not int(counter_prev) == int(counter):
        if int(counter) % 20 == 0:
            # Updating lists with actual mean values of amounts and traits.
            if len(herbivores_amount_list) > 160:
                herbivores_amount_list = herbivores_amount_list[1:]
            herbivores_amount_list.append(len(herbivores))
            herbivores_total_amount_list.append(len(herbivores))

            if len(carnivores_amount_list) > 160:
                carnivores_amount_list = carnivores_amount_list[1:]
            carnivores_amount_list.append(len(carnivores))
            carnivores_total_amount_list.append(len(carnivores))

            if len(herbivores_mean_speed_list) > 160:
                herbivores_mean_speed_list = herbivores_mean_speed_list[1:]
            local_sum = 0
            for i in herbivores:
                local_sum += int(i.dna[0])
            if not len(herbivores) == 0:
                herbivores_mean_speed = local_sum / len(herbivores)
                herbivores_mean_speed_list.append(herbivores_mean_speed)
            else:
                herbivores_mean_speed_list = herbivores_mean_speed_list[1:]

            if len(herbivores_mean_bowel_length_list) > 160:
                herbivores_mean_bowel_length_list = herbivores_mean_bowel_length_list[1:]
            local_sum = 0
            for i in herbivores:
                local_sum += int(i.dna[1])
            if not len(herbivores) == 0:
                herbivores_mean_bowel_length = local_sum / len(herbivores)
                herbivores_mean_bowel_length_list.append(herbivores_mean_bowel_length)
            else:
                herbivores_mean_bowel_length_list = herbivores_mean_bowel_length_list[1:]

            if len(herbivores_mean_fat_limit_list) > 160:
                herbivores_mean_fat_limit_list = herbivores_mean_fat_limit_list[1:]
            local_sum = 0
            for i in herbivores:
                local_sum += int(i.dna[2])
            if not len(herbivores) == 0:
                herbivores_mean_fat_limit = local_sum / len(herbivores)
                herbivores_mean_fat_limit_list.append(herbivores_mean_fat_limit)
            else:
                herbivores_mean_fat_limit_list = herbivores_mean_fat_limit_list[1:]

            if len(herbivores_mean_legs_length_list) > 160:
                herbivores_mean_legs_length_list = herbivores_mean_legs_length_list[1:]
            local_sum = 0
            for i in herbivores:
                local_sum += int(i.dna[3])
            if not len(herbivores) == 0:
                herbivores_mean_legs_length = local_sum / len(herbivores)
                herbivores_mean_legs_length_list.append(herbivores_mean_legs_length)
            else:
                herbivores_mean_legs_length_list = herbivores_mean_legs_length_list[1:]

            if len(carnivores_mean_speed_list) > 160:
                carnivores_mean_speed_list = carnivores_mean_speed_list[1:]
            local_sum = 0
            for i in carnivores:
                local_sum += int(i.dna[0])
            if not len(carnivores) == 0:
                carnivores_mean_speed = local_sum / len(carnivores)
                carnivores_mean_speed_list.append(carnivores_mean_speed)
            else:
                carnivores_mean_speed_list = carnivores_mean_speed_list[1:]

            if len(carnivores_mean_bowel_length_list) > 160:
                carnivores_mean_bowel_length_list = carnivores_mean_bowel_length_list[1:]
            local_sum = 0
            for i in carnivores:
                local_sum += int(i.dna[1])
            if not len(carnivores) == 0:
                carnivores_mean_bowel_length = local_sum / len(carnivores)
                carnivores_mean_bowel_length_list.append(carnivores_mean_bowel_length)
            else:
                carnivores_mean_bowel_length_list = carnivores_mean_bowel_length_list[1:]

            if len(carnivores_mean_fat_limit_list) > 160:
                carnivores_mean_fat_limit_list = carnivores_mean_fat_limit_list[1:]
            local_sum = 0
            for i in carnivores:
                local_sum += int(i.dna[2])
            if not len(carnivores) == 0:
                carnivores_mean_fat_limit = local_sum / len(carnivores)
                carnivores_mean_fat_limit_list.append(carnivores_mean_fat_limit)
            else:
                carnivores_mean_fat_limit_list = carnivores_mean_fat_limit_list[1:]

            if len(carnivores_mean_legs_length_list) > 160:
                carnivores_mean_legs_length_list = carnivores_mean_legs_length_list[1:]
            local_sum = 0
            for i in carnivores:
                local_sum += int(i.dna[3])
            if not len(carnivores) == 0:
                carnivores_mean_legs_length = local_sum / len(carnivores)
                carnivores_mean_legs_length_list.append(carnivores_mean_legs_length)
            else:
                carnivores_mean_legs_length_list = carnivores_mean_legs_length_list[1:]

            if big_counter_prev != big_counter:
                if big_counter % 1 == 0:
                    if not pause:
                        print("")
                        print("---")
                        print("---")
                        print("Cycles since start:", total_cycles_counter)
                        print("---")
                        print("---")
                        print("")
                        report.write(  str(datetime.now().time())                  + ";"
                                     + str(big_counter)                            + ";"
                                     + str(total_cycles_counter)                   + ";"
                                     + str(len(herbs))                             + ";"
                                     + str(len(herbivores))                        + ";"
                                     + str(len(carnivores))                        + ";"
                                     + str(round(herbivores_mean_speed, 4))        + ";"
                                     + str(round(herbivores_mean_bowel_length, 4)) + ";"
                                     + str(round(herbivores_mean_fat_limit, 4))    + ";"
                                     + str(round(herbivores_mean_legs_length, 4))  + ";"
                                     + str(round(carnivores_mean_speed, 4))        + ";"
                                     + str(round(carnivores_mean_bowel_length, 4)) + ";"
                                     + str(round(carnivores_mean_fat_limit, 4))    + ";"
                                     + str(round(carnivores_mean_legs_length, 4))  + ";"
                                     + "\r\n")
                        report.flush()

    # Increase total cycles number by 1.
    if not pause:
        total_cycles_counter += 1

    # ################################# #
    # ##----- Update The Screen -----## #
    # ################################# #

    pygame.display.flip()
