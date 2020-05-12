##########################################################
#######################--- SERG ---#######################
##############- ARROW_UP: ADD ONE CARNIVORE -#############
############- ARROW_LEFT: ADD 100 HERBIVORES -############
###########- ARROW_RIGHT: ADD 100 CARNIVORES -############
###########- ESCAPE: REMOVE ALL THE OBJECTS -#############
##########################################################

# Info:
# DNA = [SPEED, BOWEL_LENGTH, FAT_LIMIT, LEGS_LENGTH ]
# 16 possibile speeds with counter max 120:  1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.

# To add: więcej cech, statystyki, the faster the costier.

# Algorytm zarządzający
# Podziel na osobne pliki

#################################################################################################################################
# Imports
import pygame
import random
from grid import grid
from positions import *
# Initialize the game engine
pygame.init()
# Set fonts
font = pygame.font.SysFont("liberationmono", 13)
font2 = pygame.font.SysFont("liberationmono", 11)
font3 = pygame.font.SysFont("liberationmono", 11)
font4 = pygame.font.SysFont("humorsans", 70)
# Define colors
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
ORANGE      = ( 255, 102,   0)
YELLOW      = ( 255, 255,   0)
GREEN       = (  51, 153,  51)
CYAN        = (   0, 255, 255)
BLUE        = (   0, 102, 204)
PURPLE      = ( 102,   0, 204)
PINK        = ( 255,   0, 255)
RED         = ( 202,   0,   0)
# Load images
plus_up=pygame.image.load("sprites/plus_up.png")
plus_down=pygame.image.load("sprites/plus_down.png")
minus_up=pygame.image.load("sprites/minus_up.png")
minus_down=pygame.image.load("sprites/minus_down.png")
reset_up=pygame.image.load("sprites/reset_up.png")
reset_down=pygame.image.load("sprites/reset_down.png")
start_up=pygame.image.load("sprites/start_up.png")
start_down=pygame.image.load("sprites/start_down.png")
pause_up=pygame.image.load("sprites/pause_up.png")
pause_down=pygame.image.load("sprites/pause_down.png")
#################################################################################################################################
# Define variables and lists
DNA = ["SPEED", "BOWEL_LENGTH", "FAT_LIMIT", "LEGS_LENGTH"]
counter = 0
counter_prev = counter
big_counter = 0
big_counter_prev = big_counter
key_up = 0
del_all = 0
button_start_clicked = 0
button_pause_clicked = 0
button_reset_clicked = 0
button_tempo_plus_clicked = 0
button_tempo_minus_clicked = 0
reset_counter = 12
pause = 1
herbs = []
herbivores = []
carnivores = []
#################################################################################################################################
# Settings
fps = 60                            # between 20-60, suggested 30.   60 might lag when under load.  [it's possible to go over 60, but it will lag a lot]
tempo = 0.22                        # between 0.01 and 0.99  [ 60 fps + 800/150/50 + tempo 0.8 and it lags. tempo 0.5 seems fine ]

herbs_spawn_rate = 7                # between 7 and -5. higher is faster.
herbs_amount_per_spawn = 5          # suggested 5-20
herbs_energy = 1000                 # suggested 300-2000

herbs_starting_amount = 400         # suggested 200-1000
herbivores_starting_amount = 150    # suggested 50-20
carnivores_starting_amount = 30     # suggested 15-75

herbivores_spawn_energy = 2900      # suggested 1000-3000
carnivores_spawn_energy = 2000      # suggested 1000-3500

herbivores_breed_level = 3000       # suggested 2500-4500
carnivores_breed_level = 3000       # suggested 2000-4500

herbivores_movement_cost = 10       # suggested 10-80 (has big impact)
carnivores_movement_cost = 80       # suggested 10-80 (has big impact)

mutation_chance = 2                 # between 0 and 99, percents
#################################################################################################################################
# DNA coding
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
legs_length_dict = {
0: 0.98,
1: 0.96,
2: 0.94,
3: 0.92,
4: 0.90,
5: 0.88,
6: 0.86,
7: 0.84
}
#################################################################################################################################
# Set size of the screen and create it
size = (775, 449)
pygame.display.set_caption("SERG")
screen = pygame.display.set_mode(size)
serg_icon = pygame.image.load('sprites/serg.png')
pygame.display.set_icon(serg_icon)
#################################################################################################################################
# Function to draw the main parts
def draw_window():
    # logo
    logo = font4.render("SERG", True, (80, 80, 80))
    screen.blit(logo, (19, 18))

    # Drawing grid
    square = 10
    square_width = square
    square_height = square
    y = -square_height + 10
    for i in range(0, 43):
        y += square_height
        x = -square_width + 172
        for j in range(0, 43):
            x += square_width
            pygame.draw.rect(screen, GRAY, [x, y, square_width-1, square_height-1])

    # Lines
    pygame.draw.line(screen, GRAY, (13, 12), (13, 436), 1)
    pygame.draw.line(screen, GRAY, (159, 12), (159, 436), 1)
    pygame.draw.line(screen, GRAY, (615, 12), (615, 436), 1)
    pygame.draw.line(screen, GRAY, (761, 12), (761, 436), 1)


    # Start button
    if button_start_clicked == 1:
        screen.blit(start_down, [23, 80])
    else:
        screen.blit(start_up, [23, 80])

    # Pause button
    if button_pause_clicked == 1:
        screen.blit(pause_down, [68, 80])
    else:
        screen.blit(pause_up, [68, 80])

    # Reset button
    if button_reset_clicked == 1:
        screen.blit(reset_down, [113, 80])
    else:
        screen.blit(reset_up, [113, 80])


    par_4 = font2.render("Settings", True, (50, 50, 50))
    screen.blit(par_4, (619, 7))
    par_4 = font2.render(("FPS: "
                          + str(fps)), True, (50, 50, 50))
    screen.blit(par_4, (622, 28))
    par_4 = font2.render(("Tempo: "
                          + str(round(tempo,2))), True, (50, 50, 50))
    screen.blit(par_4, (622, 48))
    par_4 = font2.render(("Mutation %: "
                          + str(mutation_chance)), True, (50, 50, 50))
    screen.blit(par_4, (622, 68))

    par_4 = font2.render(("HERBS: "
                          + str(len(herbs))), True, (50, 50, 50))
    screen.blit(par_4, (620, 97))
    par_4 = font2.render(("Start. amount: "
                          + str(herbs_starting_amount)), True, (50, 50, 50))
    screen.blit(par_4, (622, 117))
    par_4 = font2.render(("Energy: "
                          + str(herbs_energy)), True, (50, 50, 50))
    screen.blit(par_4, (622, 137))
    par_4 = font2.render(("Per spawn: "
                          + str(herbs_amount_per_spawn)), True, (50, 50, 50))
    screen.blit(par_4, (622, 157))
    par_4 = font2.render(("Spawn rate: "
                          + str(herbs_spawn_rate)), True, (50, 50, 50))
    screen.blit(par_4, (622, 177))

    par_4 = font2.render(("HERBIVORES: "
                          + str(len(herbivores))), True, (50, 50, 50))
    screen.blit(par_4, (620, 206))
    par_4 = font2.render(("Start. amount: "
                          + str(herbivores_starting_amount)), True, (50, 50, 50))
    screen.blit(par_4, (622, 226))
    par_4 = font2.render(("Spawn energy: "
                          + str(herbivores_spawn_energy)), True, (50, 50, 50))
    screen.blit(par_4, (622, 246))
    par_4 = font2.render(("Breeding level: "
                          + str(herbivores_breed_level)), True, (50, 50, 50))
    screen.blit(par_4, (622, 266))
    par_4 = font2.render(("Movement cost: "
                          + str(herbivores_movement_cost)), True, (50, 50, 50))
    screen.blit(par_4, (622, 286))

    par_4 = font2.render(("CARNIVORES: "
                          + str(len(carnivores))), True, (50, 50, 50))
    screen.blit(par_4, (620, 315))
    par_4 = font2.render(("Start. amount: "
                          + str(carnivores_starting_amount)), True, (50, 50, 50))
    screen.blit(par_4, (622, 335))
    par_4 = font2.render(("Spawn energy: "
                          + str(carnivores_spawn_energy)), True, (50, 50, 50))
    screen.blit(par_4, (622, 355))
    par_4 = font2.render(("Breeding level: "
                          + str(carnivores_breed_level)), True, (50, 50, 50))
    screen.blit(par_4, (622, 375))
    par_4 = font2.render(("Movement cost: "
                          + str(carnivores_movement_cost)), True, (50, 50, 50))
    screen.blit(par_4, (622, 395))

    par_4 = font2.render(("H:"
                          + str(len(herbs))), True, (50, 50, 50))
    screen.blit(par_4, (21, 135))
    par_4 = font2.render(("HV:"
                          + str(len(herbivores))), True, (50, 50, 50))
    screen.blit(par_4, (66, 135))
    par_4 = font2.render(("CV:"
                          + str(len(carnivores))), True, (50, 50, 50))
    screen.blit(par_4, (115, 135))


    # Fake buttons 1
    screen.blit(plus_up, [742, 128])
    #screen.blit(plus_down, [744, 128])
    screen.blit(minus_up, [726, 128])
    #screen.blit(minus_down, [728, 128])

    # Tempo plus button.
    if button_tempo_plus_clicked == 1:
        screen.blit(plus_down, [742, 230])
    else:
        screen.blit(plus_up, [742, 230])

    # Tempo minus button.
    if button_tempo_minus_clicked == 1:
        screen.blit(minus_down, [726, 230])
    else:
        screen.blit(minus_up, [726, 230])


    '''
    # bottom right part
    cornertext_1 = font.render("Use buttons on", True, (50, 50, 50))
    screen.blit(cornertext_1, (632, 320))
    cornertext_2 = font.render("the right side", True, (50, 50, 50))
    screen.blit(cornertext_2, (632, 340))
    cornertext_3 = font.render("of the window", True, (50, 50, 50))
    screen.blit(cornertext_3, (636, 360))
    cornertext_4 = font.render("to modify", True, (50, 50, 50))
    screen.blit(cornertext_4, (652, 380))
    cornertext_5 = font.render("the habitat.", True, (50, 50, 50))
    screen.blit(cornertext_5, (645, 400))
    '''

    signature = font3.render("bsski 2020", True, (200, 200, 200))
    screen.blit(signature, (654, 425))

#################################################################################################################################

# Class creating herbs
class Herb:
    def __init__(self, coord_x, coord_y, index, energy):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.energy = energy

    def draw(self):
        pygame.draw.circle(screen, FORESTGREEN,
                           [(grid[self.coord_y][self.coord_x][0])+4,
                            (grid[self.coord_y][self.coord_x][1])+4], 3, 0)
        # You can unhash this line for fancier look of the herbs. It is also possible to experiment a bit with /2, 0/ and /2/ parts to get interesting effects.
        pygame.draw.circle(screen, GRAY, [(grid[self.coord_y][self.coord_x][0])+4, (grid[self.coord_y][self.coord_x][1])+4], 2)

    def get_energy(self):
        return self.energy

    def get_coords(self):
        return self.coord_x, self.coord_y

    def got_eaten(self):
        herbs_pos[self.coord_y][self.coord_x] = []
        del herbs[self.index]
        for i in range(self.index, len(herbs)):
            herbs[i].index -= 1


# Class creating animals
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


#################################################################################################################################

# Class creating carnivores
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
        self.possible_moves=["e", "w", "s", "n"]

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
                            born_carnivore(i.get_coords()[0], i.get_coords()[1], self.get_dna(), i.get_dna())
                        break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == "breeding":
            self.breeding()
        else:
            self.eat()

    def carni_starved(self):
        #print("it is this long:", len(carnivores_pos[self.coord_y][self.coord_x]))
        carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]
        del carnivores[self.index]
        for i in range(self.index, len(carnivores)):
            carnivores[i].index -= 1
        # and turn into a herb

    def draw(self):
        if self.get_energy() < carnivores_breed_level:
            pygame.draw.rect(screen, colors_list_red[self.color][3],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        else:
            pygame.draw.rect(screen, colors_list_red[self.color][7],
                             [grid[self.coord_y][self.coord_x][0],
                              grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border
        pygame.draw.rect(screen, DARKERGRAY,
                         [grid[self.coord_y][self.coord_x][0]-1,
                          grid[self.coord_y][self.coord_x][1]-1, 11, 11], 1)

    def move(self):
        carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]
        if not int(counter_prev) == int(counter):
            if int(counter) % self.speed == 0:
                self.energy -= carnivores_movement_cost * self.legs_length
                if not (self.coord_x == 0 or self.coord_x == 42 or self.coord_y == 0 or self.coord_y == 42):
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


# Class creating herbivores
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
        self.possible_moves=["e", "w", "s", "n"]

    def get_intention(self): # 1 - breeding, 0 - food
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
                            born_herbivore(i.get_coords()[0], i.get_coords()[1], self.get_dna(), i.get_dna())
                        break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == "breeding":
            self.breeding()
        else:
            self.eat()

    def herbi_starved(self):
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        del herbivores[self.index]
        for i in range(self.index, len(herbivores)):
            herbivores[i].index -= 1
        # and turn into a herb

    def draw(self):
        if self.get_energy() < herbivores_breed_level:
            pygame.draw.rect(screen, colors_list_green[self.color][3],
                                [grid[self.coord_y][self.coord_x][0],
                                    grid[self.coord_y][self.coord_x][1], 9, 9])
        else:
            pygame.draw.rect(screen, colors_list_green[self.color][7],
                                [grid[self.coord_y][self.coord_x][0],
                                    grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border
        pygame.draw.rect(screen, DARKERGRAY,
                            [grid[self.coord_y][self.coord_x][0]-1,
                                grid[self.coord_y][self.coord_x][1]-1, 11, 11], 1)

    def move(self):
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        if not int(counter_prev) == int(counter):
            if int(counter) % self.speed == 0:
                self.energy -= herbivores_movement_cost * self.legs_length
                if not (self.coord_x == 0 or self.coord_x == 42
                            or self.coord_y == 0 or self.coord_y == 42):
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
                    self.energy += i.get_energy()*self.bowel_length
                    i.got_eaten()
                    break

    def got_eaten(self):
        del herbivores[self.index]
        for i in range(self.index, len(herbivores)):
            herbivores[i].index -= 1


#################################################################################################################################

# Creating a new herb - chooses random xy, checks on the herbs grid whether that xy is free. If it is - creates a new herb (adds 1 to the grid, symbolising that a herb exists there, and creates an object on herbs list).
def create_herb(herbs_energy):
    pos_y = random.randint(1, 41)
    pos_x = random.randint(1, 41)
    if len(herbs_pos[pos_y][pos_x]) == 0:
        herbs.append(Herb(pos_x, pos_y, len(herbs), herbs_energy))
        herbs_pos[pos_y][pos_x].append(1)

# Spawning herbs every /speed_dict[speed]/ frames in the amount of /herbs_amount_per_spawn/.
def spawn_herbs(speed):
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % speed_dict[speed] == 0:
            for i in range(0, herbs_amount_per_spawn):
                create_herb(herbs_energy)

#################################################################################################################################

# Spawn carnivore that was born
def born_carnivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0, 99) >= mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0, 7)))
            print("MUTATION OCCURED!", i, new_dna[i])
    print("CARNIVORE:", dna1, dna2, new_dna)
    carnivores.append(Carnivore(pos_x, pos_y, len(carnivores),
                                new_dna[0] + new_dna[1] + new_dna[2] + new_dna[3]))
    carnivores_pos[pos_y][pos_x].append(1)

# Spawn a new carnivore
def spawn_carnivore():
    pos_y = random.randint(1, 41)
    pos_x = random.randint(1, 41)
    if len(carnivores_pos[pos_y][pos_x]) < 1:
        carnivores.append(Carnivore(pos_x, pos_y, len(carnivores),
                                      str(random.randint(0, 7))
                                    + str(random.randint(0, 7))
                                    + str(random.randint(0, 7))
                                    + str(random.randint(0, 7))))
        carnivores_pos[pos_y][pos_x].append(1)

# Spawn herbivore that was born
def born_herbivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0, 99) >= mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0, 7)))
            print("MUTATION OCCURED!", i, new_dna[i])
    print("HERBIVORE:", dna1, dna2, new_dna)
    herbivores.append(Herbivore(pos_x, pos_y, len(herbivores),
                                new_dna[0] + new_dna[1] + new_dna[2] + new_dna[3]))
    herbivores_pos[pos_y][pos_x].append(1)

# Spawn a new herbivore
def spawn_herbivore():
    pos_y = random.randint(1, 41)
    pos_x = random.randint(1, 41)
    if len(herbivores_pos[pos_y][pos_x]) < 1:
        herbivores.append(Herbivore(pos_x, pos_y, len(herbivores),
                                      str(random.randint(0, 7))
                                    + str(random.randint(0, 7))
                                    + str(random.randint(0, 7))
                                    + str(random.randint(0, 7))))
        herbivores_pos[pos_y][pos_x].append(1)

#################################################################################################################################

# Add starting herbs, herbivores and carnivores.
for i in range(0, herbs_starting_amount):
    create_herb(herbs_energy)
for i in range(0, herbivores_starting_amount):
    spawn_herbivore()
for i in range(0, carnivores_starting_amount):
    spawn_carnivore()

# Set the main loop to not done and initialize a clock.
done = False
clock = pygame.time.Clock()


#=====================================================================================#
#######################################################################################
# -------------------------------- Main Program Loop -------------------------------- #
#######################################################################################
#=====================================================================================#


# Debug timer's variables.
underseconds_counter = 0
seconds_counter = 0

while not done:
    # Not real seconds.
    underseconds_counter += 1
    if underseconds_counter == 60:
        seconds_counter += 1
        print("Seconds since start:", seconds_counter)
        underseconds_counter = 0


    #####################################
    # -------- Main Event loop -------- #
    #####################################

    # Catching events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # If keyboard button clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Change /key_up/ flag to 1 - spawns 1 carnivore.
                key_up = 1
            if event.key == pygame.K_LEFT:
                # Add 10 herbivores.
                for i in range(0, 100):
                    spawn_herbivore()
            if event.key == pygame.K_RIGHT:
                # Add 10 carnivores.
                for i in range(0, 25):
                    spawn_carnivore()
            if event.key == pygame.K_ESCAPE:
                # Delete all objects.
                del_all = 1

        # If mouse button clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Start button clicked
            if pygame.mouse.get_pos()[0] >= 23 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 62 and pygame.mouse.get_pos()[1] <= 100:
                        button_start_clicked = 1

            # Pause button clicked
            if pygame.mouse.get_pos()[0] >= 68 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 107 and pygame.mouse.get_pos()[1] <= 100:
                        button_pause_clicked = 1

            # reset button clicked
            if pygame.mouse.get_pos()[0] >= 113 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 152 and pygame.mouse.get_pos()[1] <= 100:
                        button_reset_clicked = 1

            # Tempo plus button clicked
            if pygame.mouse.get_pos()[0] >= 742 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 755 and pygame.mouse.get_pos()[1] <= 243:
                        button_tempo_plus_clicked = 1

            # Tempo minus button clicked
            if pygame.mouse.get_pos()[0] >= 726 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 739 and pygame.mouse.get_pos()[1] <= 243:
                        button_tempo_minus_clicked = 1


        # If mouse button unclicked
        if event.type == pygame.MOUSEBUTTONUP:
            # reset button off on button
            if pygame.mouse.get_pos()[0] >= 113 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 152 and pygame.mouse.get_pos()[1] <= 100:
                        del_all = 1
                        button_reset_clicked = 0

            # reset button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 113 and pygame.mouse.get_pos()[1] >= 80
                        and pygame.mouse.get_pos()[0] <= 152 and pygame.mouse.get_pos()[1] <= 100):
                    button_reset_clicked = 0

            # Pause button off on button
            if pygame.mouse.get_pos()[0] >= 68 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 107 and pygame.mouse.get_pos()[1] <= 100:
                        start = tempo
                        pause = 1
                        button_pause_clicked = 0

            # Pause button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 68 and pygame.mouse.get_pos()[1] >= 80
                        and pygame.mouse.get_pos()[0] <= 107 and pygame.mouse.get_pos()[1] <= 100):
                    button_pause_clicked = 0

            # Start button off on button
            if pygame.mouse.get_pos()[0] >= 23 and pygame.mouse.get_pos()[1] >= 80:
                if pygame.mouse.get_pos()[0] <= 62 and pygame.mouse.get_pos()[1] <= 100:
                        pause = 0
                        button_start_clicked = 0

            # Start button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 23 and pygame.mouse.get_pos()[1] >= 80
                        and pygame.mouse.get_pos()[0] <= 62 and pygame.mouse.get_pos()[1] <= 100):
                    button_start_clicked = 0

            # Tempo plus button off on button
            if pygame.mouse.get_pos()[0] >= 742 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 755 and pygame.mouse.get_pos()[1] <= 243:
                        tempo += 0.07
                        button_tempo_plus_clicked = 0

            # Tempo plus unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 742 and pygame.mouse.get_pos()[1] >= 230
                        and pygame.mouse.get_pos()[0] <= 755 and pygame.mouse.get_pos()[1] <= 243):
                    button_tempo_plus_clicked = 0

            # Tempo minus button off on button
            if pygame.mouse.get_pos()[0] >= 726 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 739 and pygame.mouse.get_pos()[1] <= 243:
                        tempo -= 0.07
                        button_tempo_minus_clicked = 0

            # Tempo minus unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 726 and pygame.mouse.get_pos()[1] >= 230
                        and pygame.mouse.get_pos()[0] <= 739 and pygame.mouse.get_pos()[1] <= 243):
                    button_tempo_minus_clicked = 0


    # If /tempo/ is bigger than 59, set it to 59. Puts '59' limit on the variable.
    if tempo > 0.99: tempo = 0.99
    # If /tempo/ is smaller than 1, set it to 1. Puts '1' limit on the variable.
    if tempo < 0.01: tempo = 0.01
    # If /pause/ is true, sets /tempo/ to 0.
    #if pause: tempo = 0

    # Increase /counter/ with a step of a size of /tempo/ every frame, if simulation isn't paused. If /counter/ is equal to 120, reset it, and increase /big_counter/ by 1.
    counter_prev = counter
    big_counter_prev = big_counter
    clock.tick(fps)
    if not pause:
        counter += tempo
    if counter > 120:
        big_counter += 1
        counter = 0


    #####################################
    # --- Game Logic / Drawing Code --- #
    #####################################

    # If flag /key_up/ is equal to 1, add one carnivore and set the flag back to 0.
    if key_up == 1:
        spawn_herbivore()
        key_up = 0
    screen.fill(LIGHTGRAY)
    # Draw interface.
    draw_window()
    # Spawn herbs every /speed_dict[herbs_spawn_rate]/ frames.
    spawn_herbs(herbs_spawn_rate)
    # Draw herbs.
    for i in herbs:
        i.draw()

        # Check if any herbivore died out of starvation, try to either breed or eat, then move.
    for i in herbivores:
        if i.get_state() == 0:
            i.herbi_starved()
    if not pause:
        for i in herbivores:
            i.action()   # breed or eat
    for i in herbivores:
        i.draw()
        i.move()

        # Check if any carnivore died out of starvation, try to either breed or eat, then move.
    for i in carnivores:
        if i.get_state() == 0:
            i.carni_starved()
    if not pause:
        for i in carnivores:
            i.action()   # breed or eat
    for i in carnivores:
        i.draw()
        i.move()

    # If flag /del_all/ equals 1, remove all objects.
    if del_all == 1:
        if reset_counter > 0:
            for i in herbs:
                i.got_eaten()
            for i in herbivores:
                i.set_energy(0)
            for i in carnivores:
                i.set_energy(0)
        reset_counter -= 1
        print(reset_counter)
        if reset_counter == 0:
            for i in range(0, herbs_starting_amount):
                create_herb(herbs_energy)
            for i in range(0, herbivores_starting_amount):
                spawn_herbivore()
            for i in range(0, carnivores_starting_amount):
                spawn_carnivore()
            del_all = 0
            reset_counter = 12

    # Print the actual amount of objects every 120 counter ticks (1 big counter tick).
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % 15 == 0:
            print("...")
            print("..::: Current amount of HERBS:", len(herbs), ":::..")
            print("..::: Current amount of HERBIVORES:", len(herbivores), ":::..")
            print("..::: Current amount of CARNIVORES:", len(carnivores), ":::..")
            print(tempo)


    #####################################
    # ------- Update The Screen ------- #
    #####################################

    pygame.display.flip()
