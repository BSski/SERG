#########################################################
#######################--- SERG ---######################
##############- ARROW_UP: ADD ONE CARNIVORE -############
############- ARROW_LEFT: ADD 10 HERBIVORES -############
###########- ARROW_RIGHT: ADD 10 CARNIVORES -############
###########- ESCAPE: REMOVE ALL THE OBJECTS -############
#########################################################

# Info:
# DNA = [COLOR, SPEED, BOWEL_LENGTH, FAT_LIMIT, ]
# 16 possibile speeds with counter max 120:  1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.
# chews too much CPU? change /delta_t = clock.tick_busy_loop(60)/ to /delta_t = clock.tick(60)/

# to add: więcej cech, statystyki,   the faster the costier


# algorytm zarządzający tym wszystkim
# dość dokładnie opisać to w overleafie
# może SI, które sterowałoby każdym z tych obiektów?
# podziel na osobne pliki
# chunks

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
[(255, 173, 153),(255, 153, 128),(255, 133, 102),(255, 112, 77),(255, 92, 51),(255, 71, 26),(255, 51, 0),(230, 46, 0)],            # RED 1
[(255, 194, 153),(255, 179, 128),(255, 163, 102),(255, 148, 77),(255, 133, 51),(255, 117, 26),(255, 102, 0),(230, 92, 0)],         # RED 2
[(255, 153, 153),(255, 128, 128),(255, 102, 102),(255, 77, 77),(255, 51, 51),(255, 26, 26),(255, 0, 0),(230, 0, 0)],               # RED 3
[(255, 153, 187),(255, 128, 170),(255, 102, 153),(255, 77, 136),(255, 51, 119),(255, 26, 102),(255, 0, 85),(230, 0, 76)],          # RED 4
[(255, 173, 153),(255, 153, 128),(255, 133, 102),(255, 112, 77),(255, 92, 51),(255, 71, 26),(255, 51, 0),(230, 46, 0)],            # RED 1
[(255, 194, 153),(255, 179, 128),(255, 163, 102),(255, 148, 77),(255, 133, 51),(255, 117, 26),(255, 102, 0),(230, 92, 0)],         # RED 2
[(255, 153, 153),(255, 128, 128),(255, 102, 102),(255, 77, 77),(255, 51, 51),(255, 26, 26),(255, 0, 0),(230, 0, 0)],               # RED 3
[(255, 153, 187),(255, 128, 170),(255, 102, 153),(255, 77, 136),(255, 51, 119),(255, 26, 102),(255, 0, 85),(230, 0, 76)]           # RED 4
]
colors_list_green = [
[(77, 255, 136),(51, 255, 119),(26, 255, 102),(0, 255, 85),(0, 230, 77),(0, 204, 68),(0, 179, 60),(0, 153, 51),(0, 128, 43)],      # GREEN 1
[(77, 255, 77),(51, 255, 51),(26, 255, 26),(0, 255, 0),(0, 230, 0),(0, 204, 0),(0, 179, 0),(0, 153, 0),(0, 128, 0)],               # GREEN 2
[(51, 255, 153),(26, 255, 140),(0, 255, 128),(0, 230, 115),(0, 204, 102),(0, 179, 89),(0, 153, 77),(0, 128, 64)],                  # GREEN 3
[(51, 255, 204),(26, 255, 198),(0, 255, 191),(0, 230, 172),(0, 204, 153),(0, 179, 134),(0, 153, 115),(0, 128, 96)],                # GREEN 4
[(77, 255, 136),(51, 255, 119),(26, 255, 102),(0, 255, 85),(0, 230, 77),(0, 204, 68),(0, 179, 60),(0, 153, 51),(0, 128, 43)],      # GREEN 1
[(77, 255, 77),(51, 255, 51),(26, 255, 26),(0, 255, 0),(0, 230, 0),(0, 204, 0),(0, 179, 0),(0, 153, 0),(0, 128, 0)],               # GREEN 2
[(51, 255, 153),(26, 255, 140),(0, 255, 128),(0, 230, 115),(0, 204, 102),(0, 179, 89),(0, 153, 77),(0, 128, 64)],                  # GREEN 3
[(51, 255, 204),(26, 255, 198),(0, 255, 191),(0, 230, 172),(0, 204, 153),(0, 179, 134),(0, 153, 115),(0, 128, 96)]                # GREEN 4
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
clean_up=pygame.image.load("sprites/clean_up.png")
clean_down=pygame.image.load("sprites/clean_down.png")
start_up=pygame.image.load("sprites/start_up.png")
start_down=pygame.image.load("sprites/start_down.png")
pause_up=pygame.image.load("sprites/pause_up.png")
pause_down=pygame.image.load("sprites/pause_down.png")
#################################################################################################################################

# Define variables and lists
DNA = ["COLOR","SPEED", "BOWEL_LENGTH", "FAT_LIMIT"]

counter = 0
counter_prev = counter
big_counter = 0
big_counter_prev = big_counter
key_up = 0
del_all = 0
button_start_clicked = 0
button_pause_clicked = 0
button_clean_clicked = 0
button_tempo_plus_clicked = 0
button_tempo_minus_clicked = 0
clean_counter = 12
pause = 0
herbs = []
herbivores = []
carnivores = []

#################################################################################################################################

# Settings
fps = 180                               # between 20-60, suggested 30.   60 might lag when under load.  [it's possible to go over 60, but it will lag a lot]
program_speed = 0.3                    # between 0.01 and 0.99  [ 60 fps + 800/150/50 + program_speed 0.8 and it lags. program_speed 0.5 seems fine ]

herbs_spawn_rate = 7                   # between 7 and -5. higher is faster.
herbs_amount_per_spawn = 5            # suggested 5-20
herb_energy = 1000                      # suggested 30-200

herbs_starting_amount = 400            # suggested 200-1000
herbivores_starting_amount = 150       # suggested 50-200
carnivores_starting_amount = 30        # suggested 15-75

herbivores_spawn_energy = 2900          # suggested 100-300
carnivores_spawn_energy = 2000          # suggested 100-350

herbivore_breed_level = 3000            # suggested 250-450
carnivore_breed_level = 3000            # suggested 200-450

carnivore_movement_cost = 80            # suggested 1-6 (has big impact)
herbivore_movement_cost = 10            # suggested 2-8 (has big impact)

mutation_chance = 0                    # between 0 and 100, percent
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
    screen.blit(logo,(621,18))

    # grid
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

    # buttons part
        # lines
    pygame.draw.line(screen, GRAY, (13, 12), (13, 436), 1)
    pygame.draw.line(screen, GRAY, (159, 12), (159, 436), 1)
    pygame.draw.line(screen, GRAY, (615, 12), (615, 436), 1)
    pygame.draw.line(screen, GRAY, (761, 12), (761, 436), 1)
        # top buttons
    #pygame.draw.rect(screen, FORESTGREEN, [650, 76, 30, 30])
    #pygame.draw.rect(screen, DARKBLUE, [697, 76, 30, 30])
        # buttons 1

#    pygame.draw.rect(screen, DARKGRAY, [630, 128, 20, 20])
#    pygame.draw.rect(screen, DARKGRAY, [652, 128, 20, 20])
#    pygame.draw.rect(screen, DARKGRAY, [704, 128, 20, 20])


    # Fake buttons 1
    screen.blit(plus_up,[742,128])
    #screen.blit(plus_down,[744,128])
    screen.blit(minus_up,[726,128])
    #screen.blit(minus_down,[728,128])

    # Fake buttons 2
    screen.blit(plus_up,[742,162])
    #screen.blit(plus_down,[744,128])
    screen.blit(minus_up,[726,162])
    #screen.blit(minus_down,[728,128])

    # Fake buttons 3
    screen.blit(plus_up,[742,196])
    #screen.blit(plus_down,[744,128])
    screen.blit(minus_up,[726,196])
    #screen.blit(minus_down,[728,128])

    # Tempo plus button
    if button_tempo_plus_clicked == 1:
        screen.blit(plus_down,[742,230])
    else:
        screen.blit(plus_up,[742,230])

    # Tempo minus button
    if button_tempo_minus_clicked == 1:
        screen.blit(minus_down,[726,230])
    else:
        screen.blit(minus_up,[726,230])

    # Start button
    if button_start_clicked == 1:
        screen.blit(start_down,[625,282])
    else:
        screen.blit(start_up,[625,282])

    # Pause button
    if button_pause_clicked == 1:
        screen.blit(pause_down,[670,282])
    else:
        screen.blit(pause_up,[670,282])

    # Clean button
    if button_clean_clicked == 1:
        screen.blit(clean_down,[715,282])
    else:
        screen.blit(clean_up,[715,282])


    par_4 = font2.render("Empty first", True, (50, 50, 50))
    screen.blit(par_4,(630,128))
    par_4 = font2.render("Empty second", True, (50, 50, 50))
    screen.blit(par_4,(630,162))
    par_4 = font2.render("Empty third", True, (50, 50, 50))
    screen.blit(par_4,(630,196))
    par_4 = font2.render("Tempo", True, (50, 50, 50))
    screen.blit(par_4,(630,230))
    #pygame.draw.rect(screen, DARKGRAY, [631, 249, 20, 20])
    #pygame.draw.rect(screen, DARKGRAY, [653, 249, 20, 20])
    #pygame.draw.rect(screen, DARKGRAY, [704, 249, 20, 20])
    #pygame.draw.rect(screen, DARKGRAY, [726, 249, 20, 20])


    # bottom right part
    cornertext_1 = font.render("Use buttons on", True, (50, 50, 50))
    screen.blit(cornertext_1,(632,320))
    cornertext_2 = font.render("the right side", True, (50, 50, 50))
    screen.blit(cornertext_2,(632,340))
    cornertext_3 = font.render("of the window", True, (50, 50, 50))
    screen.blit(cornertext_3,(636,360))
    cornertext_4 = font.render("to modify", True, (50, 50, 50))
    screen.blit(cornertext_4,(652,380))
    cornertext_5 = font.render("the habitat.", True, (50, 50, 50))
    screen.blit(cornertext_5,(645,400))

    signature = font3.render("bsski 2020", True, (200, 200, 200))
    screen.blit(signature,(654,425))

#################################################################################################################################

# Class creating herbs
class herb:
    def __init__(self,coord_x,coord_y,index,energy):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.energy = energy

    def draw(self):
        pygame.draw.circle(screen, FORESTGREEN, [(grid[self.coord_y][self.coord_x][0])+4, (grid[self.coord_y][self.coord_x][1])+4],3,0)
        # You can unhash this line for fancier look of the herbs. It is also possible to experiment a bit with /2,0/ and /2/ parts to get interesting effects.
        #pygame.draw.circle(screen, GRAY, [(grid[self.coord_y][self.coord_x][0])+4, (grid[self.coord_y][self.coord_x][1])+4],2)

    def get_energy(self):
        return self.energy

    def get_coords(self):
        return self.coord_x, self.coord_y

    def got_eaten(self):
        herbs_pos[self.coord_y][self.coord_x] = []
        del herbs[self.index]
        for i in range(self.index,len(herbs)):
            herbs[i].index -= 1

# Class creating animals
class animal:
    def __init__(self,coord_x,coord_y,index,dna):
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
class carnivore(animal):
    def __init__(self,coord_x,coord_y,index,dna):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.dna = dna
            self.color = int(dna[0])
            self.speed = speed_dict[int(dna[1])]
            self.energy = carnivores_spawn_energy
            self.last_bred_on = 0
            self.bowel_length = bowel_length_dict[int(dna[2])]
            self.fat_limit = fat_limit_dict[int(dna[3])]

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > carnivore_breed_level: return 1
        else: return 0

    def breeding(self):
        if len(carnivores_pos[self.coord_y][self.coord_x]) > 1:
            for i in carnivores:
                    if (self.coord_x, self.coord_y) == i.get_coords():
                        if i.get_intention() == 1:
                            if i != carnivores[self.get_index()]:
                                if not self.last_bred_on == i.get_coords():
                                    self.energy = int(self.energy / 2)
                                    i.set_energy(int(i.get_energy()/2))
                                    born_carnivore(i.get_coords()[0],i.get_coords()[1], self.get_dna(), i.get_dna())
                                    self.last_bred_on = (self.coord_x, self.coord_y)
                                break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == 1:
            self.breeding()
        else:
            self.eat()

    def carni_starved(self):
        #print("it is this long:",len(carnivores_pos[self.coord_y][self.coord_x]))
        carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]
        del carnivores[self.index]
        for i in range(self.index,len(carnivores)):
            carnivores[i].index -= 1
        # and turn into a herb


    def move(self):
        carnivores_pos[self.coord_y][self.coord_x] = carnivores_pos[self.coord_y][self.coord_x][1:]
        # If energy is higher than 80, still display color as if it had 80 energy
        if int(self.get_energy()/1000)*2 > 7:
            pygame.draw.rect(screen, colors_list_red[self.color][7], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        # Change the animal's color depending on its energy
        else:
            pygame.draw.rect(screen, colors_list_red[self.color][int(self.get_energy()/1000)*2], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border
        pygame.draw.rect(screen, DARKERGRAY, [grid[self.coord_y][self.coord_x][0]-1, grid[self.coord_y][self.coord_x][1]-1, 11,11],1)

        if not int(counter_prev) == int(counter):
            if int(counter) % self.speed == 0:
                self.energy -= carnivore_movement_cost
                if not (self.coord_x == 0 or self.coord_x == 42 or self.coord_y == 0 or self.coord_y == 42):
                    if random.randint(0,1) == 0:
                        if random.randint(0,1) == 0:
                            self.coord_x -= 1
                        else:
                            self.coord_x += 1
                    else:
                        if random.randint(0,1) == 0:
                            self.coord_y -= 1
                        else:
                            self.coord_y += 1
                else:
                    if self.coord_x == 0: self.coord_x += 1
                    elif self.coord_x == 42: self.coord_x -= 1
                    elif self.coord_y == 0: self.coord_y += 1
                    elif self.coord_y == 42: self.coord_y -= 1
        carnivores_pos[self.coord_y][self.coord_x].append(1)

    def eat(self):
        if len(herbivores_pos[self.coord_y][self.coord_x]) > 0:
            for i in herbivores:
                if self.coord_x == i.get_coords()[0] and self.coord_y == i.get_coords()[1]:
                    self.energy += i.get_energy() * self.bowel_length
                    i.got_eaten()
                    break



# Class creating herbivores
class herbivore(animal):
    def __init__(self,coord_x,coord_y,index,dna):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.index = index
        self.dna = dna
        self.color = int(dna[0])
        self.speed = speed_dict[int(dna[1])]
        self.energy = herbivores_spawn_energy
        self.last_bred_on = 0
        self.bowel_length = bowel_length_dict[int(dna[2])]
        self.fat_limit = fat_limit_dict[int(dna[3])]

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > herbivore_breed_level: return 1
        else: return 0

    def breeding(self):
        if len(herbivores_pos[self.coord_y][self.coord_x]) > 1:
            for i in herbivores:
                if (self.coord_x, self.coord_y) == i.get_coords():
                    if i.get_intention() == 1:
                        if i != herbivores[self.get_index()]:
                            if not self.last_bred_on == i.get_coords():
                                self.energy = int(self.energy / 2)
                                i.set_energy(int(i.get_energy()/2))
                                born_herbivore(i.get_coords()[0],i.get_coords()[1], self.get_dna(), i.get_dna())
                                self.last_bred_on = (self.coord_x, self.coord_y)
                            break

    def action(self):
        if self.get_energy() > self.fat_limit:
            self.set_energy(self.fat_limit)
        if self.get_intention() == 1:
            self.breeding()
        else:
            self.eat()

    def herbi_starved(self):
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        del herbivores[self.index]
        for i in range(self.index,len(herbivores)):
            herbivores[i].index -= 1
        # and turn into a herb

    def move(self):
        herbivores_pos[self.coord_y][self.coord_x] = herbivores_pos[self.coord_y][self.coord_x][1:]
        # If energy is higher than 80, still display color as if it had 80 energy
        if int(self.get_energy()/1000)*2 > 7:
            pygame.draw.rect(screen, colors_list_green[self.color][7], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        # Change the animal's color depending on its energy
        else:
            pygame.draw.rect(screen, colors_list_green[self.color][int(self.get_energy()/1000)*2], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        # Draw its border
        pygame.draw.rect(screen, DARKERGRAY, [grid[self.coord_y][self.coord_x][0]-1, grid[self.coord_y][self.coord_x][1]-1, 11,11],1)

        if not int(counter_prev) == int(counter):
            if int(counter) % self.speed == 0:
                self.energy -= herbivore_movement_cost
                if not (self.coord_x == 0 or self.coord_x == 42 or self.coord_y == 0 or self.coord_y == 42):
                    if random.randint(0,1) == 0:
                        if random.randint(0,1) == 0:
                            self.coord_x -= 1
                        else:
                            self.coord_x += 1
                    else:
                        if random.randint(0,1) == 0:
                            self.coord_y -= 1
                        else:
                            self.coord_y += 1
                else:
                    if self.coord_x == 0: self.coord_x += 1
                    elif self.coord_x == 42: self.coord_x -= 1
                    elif self.coord_y == 0: self.coord_y += 1
                    elif self.coord_y == 42: self.coord_y -= 1
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
        for i in range(self.index,len(herbivores)):
            herbivores[i].index -= 1



#################################################################################################################################

# Creating a new herb - chooses random xy, checks on the herbs grid whether that xy is free. If it is - creates a new herb (adds 1 to the grid, symbolising that a herb exists there, and creates an object on herbs list).
def create_herb(herb_energy):
    pos_y = random.randint(1,41)
    pos_x = random.randint(1,41)
    if len(herbs_pos[pos_y][pos_x]) == 0:
        herbs.append(herb(pos_x,pos_y,len(herbs),herb_energy))
        herbs_pos[pos_y][pos_x].append(1)

# Spawning herbs every /speed_dict[speed]/ frames in the amount of /herbs_amount_per_spawn/.
def spawn_herbs(speed):
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % speed_dict[speed] == 0:
            for i in range(0,herbs_amount_per_spawn):
                create_herb(herb_energy)

#################################################################################################################################

# Spawn carnivore that was born
def born_carnivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0,99) >= mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0,7)))
            print("MUTATION OCCURED!", i, new_dna[i])
    print("CARNIVORE:", dna1, dna2, new_dna)

    carnivores.append(carnivore(pos_x, pos_y, len(carnivores), new_dna[0] + new_dna[1] + new_dna[2] + new_dna[3]))
    carnivores_pos[pos_y][pos_x].append(1)

# Spawn a new carnivore
def spawn_carnivore():
    pos_y = random.randint(1,41)
    pos_x = random.randint(1,41)
    if len(carnivores_pos[pos_y][pos_x]) < 1:
        carnivores.append(carnivore(pos_x,pos_y,len(carnivores),str(random.randint(4,7))+str(random.randint(0,7))+str(random.randint(0,7))+str(random.randint(0,7))))
        carnivores_pos[pos_y][pos_x].append(1)

# Spawn herbivore that was born
def born_herbivore(pos_x, pos_y, dna1, dna2):
    new_dna = []
    for i in range(0, int(len(DNA))):
        if random.randint(0,100) > mutation_chance:
            new_dna.append(random.choice(dna1[i] + dna2[i]))
        else:
            new_dna.append(str(random.randint(0,7)))
            print("MUTATION OCCURED!", i, new_dna[i])
    print("HERBIVORE:", dna1, dna2, new_dna)

    herbivores.append(herbivore(pos_x, pos_y, len(herbivores), new_dna[0] + new_dna[1] + new_dna[2] + new_dna[3]))
    herbivores_pos[pos_y][pos_x].append(1)

# Spawn a new herbivore
def spawn_herbivore():
    pos_y = random.randint(1,41)
    pos_x = random.randint(1,41)
    if len(herbivores_pos[pos_y][pos_x]) < 1:
        herbivores.append(herbivore(pos_x,pos_y,len(herbivores),str(random.randint(0,3))+str(random.randint(0,7))+str(random.randint(0,7))+str(random.randint(0,7))))
        herbivores_pos[pos_y][pos_x].append(1)

#################################################################################################################################

# Add starting herbs, herbivores and carnivores.
for i in range(0,herbs_starting_amount):
    create_herb(herb_energy)
for i in range(0,herbivores_starting_amount):
    spawn_herbivore()
for i in range(0,carnivores_starting_amount):
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
        print("Seconds since start:",seconds_counter)
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
                for i in range(0,100):
                    spawn_herbivore()
            if event.key == pygame.K_RIGHT:
                # Add 10 carnivores.
                for i in range(0,25):
                    spawn_carnivore()
            if event.key == pygame.K_ESCAPE:
                # Delete all objects.
                del_all = 1


        # If mouse button clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Start button clicked
            if pygame.mouse.get_pos()[0] >= 625 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 664 and pygame.mouse.get_pos()[1] <= 302:
                        button_start_clicked = 1

            # Pause button clicked
            if pygame.mouse.get_pos()[0] >= 670 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 709 and pygame.mouse.get_pos()[1] <= 302:
                        button_pause_clicked = 1

            # Clean button clicked
            if pygame.mouse.get_pos()[0] >= 715 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 754 and pygame.mouse.get_pos()[1] <= 322:
                        button_clean_clicked = 1

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
            # Clean button off on button
            if pygame.mouse.get_pos()[0] >= 715 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 754 and pygame.mouse.get_pos()[1] <= 322:
                        del_all = 1
                        button_clean_clicked = 0
            # Clean button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 715 and pygame.mouse.get_pos()[1] >= 282 and pygame.mouse.get_pos()[0] <= 754 and pygame.mouse.get_pos()[1] <= 322):
                    button_clean_clicked = 0

            # Pause button off on button
            if pygame.mouse.get_pos()[0] >= 670 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 709 and pygame.mouse.get_pos()[1] <= 302:
                        start = program_speed
                        pause = 1
                        button_pause_clicked = 0
            # Pause button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 670 and pygame.mouse.get_pos()[1] >= 282 and pygame.mouse.get_pos()[0] <= 709 and pygame.mouse.get_pos()[1] <= 302):
                    button_pause_clicked = 0

            # Start button off on button
            if pygame.mouse.get_pos()[0] >= 625 and pygame.mouse.get_pos()[1] >= 282:
                if pygame.mouse.get_pos()[0] <= 664 and pygame.mouse.get_pos()[1] <= 302:
                        pause = 0
                        button_start_clicked = 0
            # Start button unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 625 and pygame.mouse.get_pos()[1] >= 282 and pygame.mouse.get_pos()[0] <= 664 and pygame.mouse.get_pos()[1] <= 302):
                    button_start_clicked = 0

            # Tempo plus button off on button
            if pygame.mouse.get_pos()[0] >= 742 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 755 and pygame.mouse.get_pos()[1] <= 243:
                        program_speed += 0.1
                        button_tempo_plus_clicked = 0
            # Tempo plus unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 742 and pygame.mouse.get_pos()[1] >= 230 and pygame.mouse.get_pos()[0] <= 755 and pygame.mouse.get_pos()[1] <= 243):
                    button_tempo_plus_clicked = 0

            # Tempo minus button off on button
            if pygame.mouse.get_pos()[0] >= 726 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 739 and pygame.mouse.get_pos()[1] <= 243:
                        program_speed -= 0.1
                        button_tempo_minus_clicked = 0
            # Tempo minus unclicked not on button
            if not (pygame.mouse.get_pos()[0] >= 726 and pygame.mouse.get_pos()[1] >= 230 and pygame.mouse.get_pos()[0] <= 739 and pygame.mouse.get_pos()[1] <= 243):
                    button_tempo_minus_clicked = 0


    # If /program_speed/ is bigger than 59, set it to 59. Puts '59' limit on the variable.
    if program_speed > 0.99: program_speed = 0.99
    # If /program_speed/ is smaller than 1, set it to 1. Puts '1' limit on the variable.
    if program_speed < 0.01: program_speed = 0.01
    # If /pause/ is true, sets /program_speed/ to 0.
    #if pause: program_speed = 0

    # Increase /counter/ with a step of a size of /program_speed/ every frame, if simulation isn't paused. If /counter/ is equal to 120, reset it, and increase /big_counter/ by 1.
    counter_prev = counter
    big_counter_prev = big_counter
    clock.tick(fps)
    if not pause:
        counter += program_speed
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
        i.move()


        # Check if any carnivore died out of starvation, try to either breed or eat, then move.
    for i in carnivores:
        if i.get_state() == 0:
            i.carni_starved()
    if not pause:
        for i in carnivores:
            i.action()   # breed or eat
    for i in carnivores:
        i.move()



    # If flag /del_all/ equals 1, remove all objects.
    if del_all == 1:
        if clean_counter > 0:
            for i in herbs:
                i.got_eaten()
            for i in herbivores:
                i.set_energy(0)
            for i in carnivores:
                i.set_energy(0)
        clean_counter -= 1
        print(clean_counter)
        if clean_counter == 0:
            del_all = 0
            clean_counter = 12

    # Print the actual amount of objects every 120 counter ticks (1 big counter tick).
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % 15 == 0:
            print("...")
            print("..::: Current amount of HERBS:",len(herbs),":::..")
            print("..::: Current amount of HERBIVORES:",len(herbivores),":::..")
            print("..::: Current amount of CARNIVORES:",len(carnivores),":::..")
            print(program_speed)


    #####################################
    # ------- Update The Screen ------- #
    #####################################

    pygame.display.flip()
