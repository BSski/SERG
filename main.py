#########################################################
#######################--- SERG ---######################
##############- ARROW_UP: ADD ONE CARNIVORE -############
############- ARROW_LEFT: ADD 10 HERBIVORES -############
###########- ARROW_RIGHT: ADD 10 CARNIVORES -############
############- ESCAPE: REMOVE ALL THE ANIMALS -###########
#########################################################

# Info:
# DNA = [COLOR, SPEED, ]
# 16 possibile speeds with counter max 120:  1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.
# chews too much CPU? change /delta_t = clock.tick_busy_loop(60)/ to /delta_t = clock.tick(60)/

# working on line 314-316, 334. investigate why always [1] and not [1,1].
# problem is in born_carnivore(pos_y,pos_x), or spawn_carnivore(), or update_pos(). most likely in the last one and the order of calling them

# Imports
import pygame
import random
from grid import grid
from positions import *
# Initialize the game engine
pygame.init()
# Set fonts
font = pygame.font.SysFont("liberationmono", 13)
font2= pygame.font.SysFont("liberationmono", 15)
font3= pygame.font.SysFont("liberationmono", 11)
font4= pygame.font.SysFont("humorsans", 70)
# Define colors
colors_list=[
[(77, 255, 136),(51, 255, 119),(26, 255, 102),(0, 255, 85),(0, 230, 77),(0, 204, 68),(0, 179, 60),(0, 153, 51),(0, 128, 43)],      # DARK 1
[(77, 255, 77),(51, 255, 51),(26, 255, 26),(0, 255, 0),(0, 230, 0),(0, 204, 0),(0, 179, 0),(0, 153, 0),(0, 128, 0)],               # DARK 2
[(51, 255, 153),(26, 255, 140),(0, 255, 128),(0, 230, 115),(0, 204, 102),(0, 179, 89),(0, 153, 77),(0, 128, 64)],                  # DARK 3
[(51, 255, 204),(26, 255, 198),(0, 255, 191),(0, 230, 172),(0, 204, 153),(0, 179, 134),(0, 153, 115),(0, 128, 96)],                # DARK 4
[(255, 173, 153),(255, 153, 128),(255, 133, 102),(255, 112, 77),(255, 92, 51),(255, 71, 26),(255, 51, 0),(230, 46, 0)],            # FAIR 1
[(255, 194, 153),(255, 179, 128),(255, 163, 102),(255, 148, 77),(255, 133, 51),(255, 117, 26),(255, 102, 0),(230, 92, 0)],         # FAIR 2
[(255, 153, 153),(255, 128, 128),(255, 102, 102),(255, 77, 77),(255, 51, 51),(255, 26, 26),(255, 0, 0),(230, 0, 0)],               # FAIR 3
[(255, 153, 187),(255, 128, 170),(255, 102, 153),(255, 77, 136),(255, 51, 119),(255, 26, 102),(255, 0, 85),(230, 0, 76)]           # FAIR 4
]

BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GRAY        = ( 210, 210, 210)
LIGHTGRAY   = ( 239, 239, 239)
MIDDLEGRAY  = ( 180, 180, 180)
DARKGRAY    = ( 130, 130, 130)
DARKERGRAY  = ( 100, 100, 100)
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


# Define variables and lists
key_up = 0
counter = 0
counter_prev = counter
big_counter = 0
big_counter_prev = big_counter
herbs = []
herbivores = []
carnivores = []

# Settings
game_speed = 30  # min 1 max 60 // 800/150/50 + game_speed 50 and it lags. game_speed 30 seems fine

herbs_spawn_rate = 7 # between 7 and -4
herbs_amount_per_spawn = 4
herb_energy = 125

herbs_starting_amount = 800
herbivores_starting_amount = 150
carnivores_starting_amount = 50

herbivores_spawn_energy = 250
carnivores_spawn_energy = 260

herbivore_breed_level = 300
carnivore_breed_level = 300

carnivore_movement_cost = 2
herbivore_movement_cost = 4

# DNA coding
speed_dict = {
-4: 120,
-3: 60,
-2: 40,
-1: 30,
0: 24,
1: 20,
2: 12,
3: 10,
4: 8,
5: 6,
6: 4,
7: 2,
8: 1  # available only through turbo mode
}
# Set size of the screen and create it
size = (614, 449)
pygame.display.set_caption("SERG")
screen = pygame.display.set_mode(size)
serg_icon = pygame.image.load('serg.png')
pygame.display.set_icon(serg_icon)
# Function to draw the main parts
def draw_window():
    # logo
    logo = font4.render("SERG", True, (80, 80, 80))
    screen.blit(logo,(460,18))

    # grid
    #square=32
    square=10
    square_width=square
    square_height=square
    y=-square_height+10
    for i in range(0,43):
        y+=square_height
        x=-square_width+13
        for j in range(0,43):
            x+=square_width
            pygame.draw.rect(screen, GRAY, [x, y, square_width-1, square_height-1])
    # buttons part
        # lines
    pygame.draw.line(screen, GRAY, (454, 12), (454, 436), 1)
    pygame.draw.line(screen, GRAY, (600, 12), (600, 436), 1)
        # top buttons
    pygame.draw.rect(screen, FORESTGREEN, [489, 76, 30, 30])
    pygame.draw.rect(screen, DARKBLUE, [536, 76, 30, 30])
        # buttons 1
    par_1 = font2.render("5", True, (50, 50, 50))
    screen.blit(par_1,(523,130))
    pygame.draw.rect(screen, DARKGRAY, [470, 128, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [492, 128, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [543, 128, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [565, 128, 20, 20])
        # buttons 2
    par_2 = font2.render("2", True, (50, 50, 50))
    screen.blit(par_2,(523,171))
    pygame.draw.rect(screen, DARKGRAY, [470, 169, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [492, 169, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [543, 169, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [565, 169, 20, 20])
        # buttons 3
    par_3 = font2.render("8", True, (50, 50, 50))
    screen.blit(par_3,(523,211))
    pygame.draw.rect(screen, DARKGRAY, [470, 209, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [492, 209, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [543, 209, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [565, 209, 20, 20])
        # buttons 4
    par_4 = font2.render("1", True, (50, 50, 50))
    screen.blit(par_4,(523,251))
    pygame.draw.rect(screen, DARKGRAY, [470, 249, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [492, 249, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [543, 249, 20, 20])
    pygame.draw.rect(screen, DARKGRAY, [565, 249, 20, 20])
        # button reset
    pygame.draw.rect(screen, DARKRED, [503, 282, 50, 20])



    # bottom right part
    cornertext_1 = font.render("Use buttons on", True, (50, 50, 50))
    screen.blit(cornertext_1,(471,320))
    cornertext_2 = font.render("the right side", True, (50, 50, 50))
    screen.blit(cornertext_2,(471,340))
    cornertext_3 = font.render("of the window", True, (50, 50, 50))
    screen.blit(cornertext_3,(475,360))
    cornertext_4 = font.render("to modify", True, (50, 50, 50))
    screen.blit(cornertext_4,(491,380))
    cornertext_5 = font.render("the habitat.", True, (50, 50, 50))
    screen.blit(cornertext_5,(484,400))

    signature = font3.render("bsski 2020", True, (200, 200, 200))
    screen.blit(signature,(493,425))


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
        herbs_pos[self.coord_y][self.coord_x]=[]
        del herbs[self.index]
        for i in range(self.index,len(herbs)):
            herbs[i].index -= 1

# Class creating animals
class animal:
    def __init__(self,coord_x,coord_y,index,dna):
        pass

    def get_type(self):
        return self.type

    def get_type_list(self):
        return self.type_list

    def get_food_type(self):
        return self.food_type

    def get_index(self):
        return self.index

    def get_dna(self):
        return self.dna

    def get_state(self):
        if self.energy > 0: return 1 #alive
        if self.energy < 1: return 0 #dead

    def get_energy(self):
        return self.energy

    def change_energy(self, new_energy):
        self.energy = new_energy

    def get_coords(self):
        return (self.coord_x, self.coord_y)

    def eat(self, food_type):
        for i in food_type:
            if self.coord_x == i.get_coords()[0] and self.coord_y == i.get_coords()[1]:
                self.energy += i.get_energy()
                i.got_eaten()
                break


    def move(self):
        if int(self.get_energy()/100)*2>7:
            pygame.draw.rect(screen, colors_list[self.color][7], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        else:
            pygame.draw.rect(screen, colors_list[self.color][int(self.get_energy()/100)*2], [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        pygame.draw.rect(screen, DARKERGRAY, [grid[self.coord_y][self.coord_x][0]-1, grid[self.coord_y][self.coord_x][1]-1, 11,11],1)

        if int(counter_prev) == int(counter):
            #print("ugh")
            pass
        else:
            if int(counter) % self.speed == 0:
                if self.get_type() == "carnivore":
                    self.energy -= carnivore_movement_cost
                else:
                    self.energy -= herbivore_movement_cost
                #print("ani x ani y nie są skrajne")
                if not (self.coord_x == 0 or self.coord_x == 42 or self.coord_y == 0 or self.coord_y == 42):
                    #print("ruszam")
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
            self.type = carnivore
            self.type_list = carnivores
            self.food_type = herbivores
            self.last_bred_on = 0
            self.type_pos_list = carnivores_pos

    def update_pos(self):
        carnivores_pos[self.coord_y][self.coord_x]=carnivores_pos[self.coord_y][self.coord_x][1:]
        carnivores_pos[self.coord_y][self.coord_x].append(1)

    def get_type_pos_list(self):
        return self.type_pos_list

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > carnivore_breed_level: return 1
        else: return 0

    def breeding(self):
    #    print("i denied sex cus:",len(carnivores_pos[self.coord_y][self.coord_x]))
        #if len(carnivores_pos[self.coord_y][self.coord_x])>1:
    #        print("WOOOOOOOOHO:",carnivores_pos[self.coord_y][self.coord_x])
            for i in carnivores:
                    if (self.coord_x, self.coord_y) == i.get_coords():
                        if i.get_intention() == 1:
                            if i != carnivores[self.get_index()]:
                                if not self.last_bred_on == i.get_coords():
                                    self.energy = int(self.energy / 2)
                                    i.change_energy(int(i.get_energy()/2))
                                    born_carnivore(i.get_coords()[1],i.get_coords()[0])
                                    self.last_bred_on = (self.coord_x, self.coord_y)
                                break

    def action(self):
        if self.get_intention() == 1:
            self.breeding()
        else:
            self.eat(herbivores)

    def carni_starved(self):
        #print("it is this long:",len(carnivores_pos[self.coord_y][self.coord_x]))
        carnivores_pos[self.coord_y][self.coord_x]=carnivores_pos[self.coord_y][self.coord_x][1:]
        del carnivores[self.index]
        for i in range(self.index,len(carnivores)):
            carnivores[i].index -= 1
        # and turn into a herb


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
        self.type = herbivore
        self.type_list = herbivores
        self.food_type = herbs
        self.last_bred_on = 0
        self.type_pos_list = herbivores_pos

    def herbi_starved(self):
        herbivores_pos[self.coord_y][self.coord_x]=herbivores_pos[self.coord_y][self.coord_x][1:]
        del herbivores[self.index]
        for i in range(self.index,len(herbivores)):
            herbivores[i].index -= 1
        # and turn into a herb


    def get_type_pos_list(self):
        return self.type_pos_list

    def got_eaten(self):
        del herbivores[self.index]
        for i in range(self.index,len(herbivores)):
            herbivores[i].index -= 1

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > herbivore_breed_level: return 1
        else: return 0

    def breeding(self):
        for i in herbivores:
            if (self.coord_x, self.coord_y) == i.get_coords():
                if i.get_intention() == 1:
                    if i != herbivores[self.get_index()]:
                        if not self.last_bred_on == i.get_coords():
                            self.energy = int(self.energy / 2)
                            i.change_energy(int(i.get_energy()/2))
                            herbivores.append(herbivore(i.get_coords()[0],i.get_coords()[1],len(herbivores),str(random.randint(0,3))+str(random.randint(0,7))))
                            self.last_bred_on = (self.coord_x, self.coord_y)
                        break

    def action(self):
        if self.get_intention() == 1:
            self.breeding()
        else:
            self.eat(herbs)
#######################################################################################################################
# Creating a new herb - chooses random xy, checks on the herbs grid whether that xy is free. If it is - creates a new herb (adds 1 to the grid, symbolising that a herb exists there, and creates an object on herbs list).
def create_herb(herb_energy):
    pos_y = random.randint(1,41)
    pos_x = random.randint(1,41)
    if len(herbs_pos[pos_y][pos_x])<1:
        herbs.append(herb(pos_y,pos_x,len(herbs),herb_energy))
        herbs_pos[pos_y][pos_x].append(1)

# Spawning herbs every /speed_dict[speed]/ frames in the amount of /herbs_amount_per_spawn/.
def spawn_herbs(speed):
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % speed_dict[speed] == 0:
            for i in range(0,herbs_amount_per_spawn):
                create_herb(herb_energy)


#######################################################################################################################

def born_carnivore(pos_y,pos_x):
    carnivores.append(carnivore(pos_y,pos_x,len(carnivores),str(random.randint(4,7))+str(random.randint(0,7))))
    carnivores_pos[pos_y][pos_x].append(1)

def spawn_carnivore():
    pos_y = random.randint(1,41)
    pos_x = random.randint(1,41)
    if len(carnivores_pos[pos_y][pos_x])<1:
        carnivores.append(carnivore(pos_y,pos_x,len(carnivores),str(random.randint(4,7))+str(random.randint(0,7))))
        carnivores_pos[pos_y][pos_x].append(1)


# Add starting herbs, herbivores and carnivores.
for i in range(0,herbs_starting_amount+1):
    herbs.append(herb(random.randint(1,41),random.randint(1,41),len(herbs),herb_energy))
for i in range(0,herbivores_starting_amount+1):
    herbivores.append(herbivore(random.randint(1,41),random.randint(1,41),len(herbivores),str(random.randint(0,3))+str(random.randint(0,7))))
for i in range(0,carnivores_starting_amount+1):
    spawn_carnivore()

#
done = False
clock = pygame.time.Clock()

#=====================================#
#######################################
# -------- Main Program Loop -------- #
#######################################
#=====================================#
underseconds_counter=0
seconds_counter=0
while not done:
    underseconds_counter+=1
    if underseconds_counter==60:
        seconds_counter+=1
        print("Seconds since start:",seconds_counter)
        underseconds_counter=0
    # Increase /counter/ with a step of a size of /game_speed * (delta_t/1000)/. If /counter/ is equal to 120, reset it, and increase /big_counter/ by 1.
    counter_prev = counter
    big_counter_prev = big_counter
    delta_t = clock.tick_busy_loop(60)  # high CPU usage? change it to delta_t = clock.tick(60)
    counter += game_speed * (delta_t/1000)
    if counter > 120:
        big_counter += 1
        #print(big_counter)
        counter = 0
    ###########################
    # --- Main Event loop --- #
    ###########################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Change /key_up/ flag to 1.
                key_up = 1
            if event.key == pygame.K_LEFT:
                # Add 10 herbivores.
                for i in range(0,100):
                    herbivores.append(herbivore(random.randint(1,41),random.randint(1,41),len(herbivores),str(random.randint(0,3))+str(random.randint(0,7))))
            if event.key == pygame.K_RIGHT:
                # Add 10 carnivores.
                for i in range(0,100):
                    spawn_carnivore()
            if event.key == pygame.K_ESCAPE:
                # Reset all to 0.
                herbs = []
                herbivores = []
                carnivores = []

    ######################
    # --- Game logic --- #
    ######################
    # Spawn herbs every /speed_dict[herbs_spawn_rate]/ frames.
    spawn_herbs(herbs_spawn_rate)

    # If flag /key_up/ is equal to 1, add one carnivore and set the flag back to 0.
    if key_up == 1:
        spawn_carnivore()
        key_up = 0

    ########################
    # --- Game Logic / Drawing Code --- #
    ########################
    screen.fill(LIGHTGRAY)
    # Draw every part of the interface.
    draw_window()

    # Draw every herb.
    for i in herbs:
        i.draw()
    # Check if any herbivore died out of starvation, try to either breed or eat [optimalisation opportunity over there - they don't have to scan entire list of food/partners every fps], then move.
    for i in herbivores:
        if i.get_state()==0:
            i.herbi_starved()
        else:
            i.action()
            i.move()

    # Check if any carnivore died out of starvation, try to either breed or eat [optimalisation opportunity over there - they don't have to scan entire list of food/partners every fps], then move.
    for i in carnivores:
        if i.get_state()==0:
            i.carni_starved()
        else:
            i.update_pos()
            i.action()
            i.move()

    # Print the actual state of the grid every 120 counter ticks (1 big counter tick).
    if int(big_counter_prev) == int(big_counter):
        pass
    else:
        if int(big_counter) % 1 == 0:
            print("...")
            print("..::: Current amount of HERBS:",len(herbs),":::..")
            print("..::: Current amount of HERBIVORES:",len(herbivores),":::..")
            print("..::: Current amount of CARNIVORES:",len(carnivores),":::..")

    #############################
    # --- Update The Screen --- #
    #############################
    pygame.display.flip()
