###################################################################
############################--- SERG ---###########################
###################- ARROW_UP: ADD ONE CARNIVORE -#################
#########- ARROW_LEFT: ADD 10 HERBIVORES AND 1 CARNIVORE -#########
#################- ESCAPE: REMOVE ALL THE ANIMALS -################
###################################################################

# Imports
import pygame
import random
from grid import grid
# Initialize the game engine
pygame.init()
# Set fonts
font = pygame.font.SysFont("liberationmono", 13)
font2= pygame.font.SysFont("liberationmono", 15)
font3= pygame.font.SysFont("liberationmono", 11)
font4= pygame.font.SysFont("humorsans", 70)
# Define colors
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GRAY        = ( 200, 200, 200)
LIGHTGRAY   = ( 239, 239, 239)
DARKGRAY    = ( 130, 130, 130)
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
RED_0       = ( 255, 179, 179)
RED_1       = ( 255, 128, 128)
RED_2       = ( 255,  77,  77)
RED_3       = ( 255,  26,  26)
RED_4       = ( 230,   0,   0)
RED_5       = ( 179,   0,   0)
RED_6       = ( 128,   0,   0)
RED_7       = (  77,   0,   0)
GREEN_0     = ( 194, 239, 194)
GREEN_1     = ( 154, 228, 154)
GREEN_2     = ( 114, 218, 114)
GREEN_3     = (  74, 207,  74)
GREEN_4     = (  48, 181,  48)
GREEN_5     = (  37, 141,  37)
GREEN_6     = (  27, 101,  27)
GREEN_7     = (  16,  60,  16)
'''
PURPLE_0    =
PURPLE_1    =
PURPLE_2    =
PURPLE_3    =
PURPLE_4    =
PURPLE_5    =
PURPLE_6    =
PURPLE_7    =
BLUE_0      =
BLUE_1      =
BLUE_2      =
BLUE_3      =
BLUE_4      =
BLUE_5      =
BLUE_6      =
BLUE_7      =
YELLOW_0    =
YELLOW_1    =
YELLOW_2    =
YELLOW_3    =
YELLOW_4    =
YELLOW_5    =
YELLOW_6    =
YELLOW_7    =
ORANGE_0    =
ORANGE_1    =
ORANGE_2    =
ORANGE_3    =
ORANGE_4    =
ORANGE_5    =
ORANGE_6    =
ORANGE_7    =
PINK_0      =
PINK_1      =
PINK_2      =
PINK_3      =
PINK_4      =
PINK_5      =
PINK_6      =
PINK_7      =
'''

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
game_speed = 30
herbs_spawn_rate = 7 # between 7 and -4
# DNA coding
color_dict = {
0: ORANGE,
1: YELLOW,
2: GREEN,
3: CYAN,
4: BLUE,
5: PURPLE,
6: PINK,
7: RED
}
color_dict_red = {
0: RED_0,
1: RED_1,
2: RED_2,
3: RED_3,
4: RED_4,
5: RED_5,
6: RED_6,
7: RED_7
}
color_dict_green = {
0: GREEN_0,
1: GREEN_1,
2: GREEN_2,
3: GREEN_3,
4: GREEN_4,
5: GREEN_5,
6: GREEN_6,
7: GREEN_7
}
'''
color_dict_purple = {
0: PURPLE_0,
1: PURPLE_1,
2: PURPLE_2,
3: PURPLE_3,
4: PURPLE_4,
5: PURPLE_5,
6: PURPLE_6,
7: PURPLE_7
}
color_dict_blue = {
0: BLUE_0,
1: BLUE_1,
2: BLUE_2,
3: BLUE_3,
4: BLUE_4,
5: BLUE_5,
6: BLUE_6,
7: BLUE_7
}
color_dict_yellow = {
0: YELLOW_0,
1: YELLOW_1,
2: YELLOW_2,
3: YELLOW_3,
4: YELLOW_4,
5: YELLOW_5,
6: YELLOW_6,
7: YELLOW_7
}
color_dict_orange = {
0: ORANGE_0,
1: ORANGE_1,
2: ORANGE_2,
3: ORANGE_3,
4: ORANGE_4,
5: ORANGE_5,
6: ORANGE_6,
7: ORANGE_7
}
color_dict_pink = {
0: PINK_0,
1: PINK_1,
2: PINK_2,
3: PINK_3,
4: PINK_4,
5: PINK_5,
6: PINK_6,
7: PINK_7
}
'''
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
7: 2
}
# Set size of the screen and create it
size = (614, 449)
pygame.display.set_caption("SERG")
screen = pygame.display.set_mode(size)
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
    def __init__(self,coord_x,coord_y,index,energy,speed):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.energy = 25

    def draw(self):
        pygame.draw.circle(screen, FORESTGREEN, [(grid[self.coord_y][self.coord_x][0])+4, (grid[self.coord_y][self.coord_x][1])+4], 3)

    def get_energy(self):
        return self.energy

    def get_coords(self):
        return self.coord_x, self.coord_y

    def got_eaten(self):
        del herbs[self.index]
        for i in range(self.index,len(herbs)):
            herbs[i].index -= 1
        #my_event = pygame.event.Event(DIED)
        #pygame.event.post(my_event)

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

    def get_intention(self): # 1 - breeding, 0 - food
        if self.energy > 35: return 1
        else: return 0

    def get_state(self):
        if self.energy > 0: return 1 #alive
        if self.energy < 1: return 0 #dead

    def get_energy(self):
        return self.energy

    def change_energy(self, new_energy):
        self.energy = new_energy

    def get_coords(self):
        return (self.coord_x, self.coord_y)

    def action(self, food_type):
        if self.get_intention() == 1:
            self.breeding()
        else:
            self.eat(food_type)

    def eat(self, food_type):
        for i in food_type:
            if self.coord_x == i.get_coords()[0] and self.coord_y == i.get_coords()[1]:
                self.energy += i.get_energy()
                i.got_eaten()
                break

    def starved(self, type_list):
        del type_list[self.index]
        for i in range(self.index,len(type_list)):
            type_list[i].index -= 1
        # and turn into a herb

    def move(self):
        pygame.draw.rect(screen, self.color, [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        if int(counter_prev) == int(counter):
            #print("ugh")
            pass
        else:
            if int(counter) % self.speed == 0:
                if self.get_type() == "carnivore":
                    self.energy -= 1
                else:
                    self.energy -= 1
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
                    if self.coord_x == 0:
                        self.coord_x += 1
                        #print("x wynosi 0, zwiekszam o 1")
                    elif self.coord_x == 42:
                        self.coord_x -= 1
                        #print("x wynosi 12, zmniejszam o 1")
                    elif self.coord_y == 0:
                        self.coord_y += 1
                        #print("y wynosi 0, zwiekszam o 1")
                    elif self.coord_y == 42:
                        self.coord_y -= 1
                        #print("y wynosi 12, zmniejszam o 1")

# Class creating carnivores
class carnivore(animal):
    def __init__(self,coord_x,coord_y,index,dna):
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.index = index
            self.dna = dna
            self.color = color_dict_red[int(dna[0])]
            self.speed = speed_dict[int(dna[1])]
            self.energy = 70
            self.type = carnivore
            self.type_list = carnivores
            self.food_type = herbivores
            self.last_bred_on = 0

    def breeding(self):
        for i in carnivores:
            if i.get_intention() == 1:
                if (self.coord_x, self.coord_y) == i.get_coords():
                    if i != carnivores[self.get_index()]:
                        if not self.last_bred_on == i.get_coords():
                            self.energy = int(self.energy / 2)
                            i.change_energy(int(i.get_energy()/2))
                            carnivores.append(carnivore(i.get_coords()[0],i.get_coords()[1],len(carnivores),str(random.randint(0,7))+str(random.randint(0,7))))
                            self.last_bred_on = (self.coord_x, self.coord_y)
                        break


# Class creating herbivores
class herbivore(animal):
    def __init__(self,coord_x,coord_y,index,dna):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.index = index
        self.dna = dna
        self.color = color_dict_green[int(dna[0])]
        self.speed = speed_dict[int(dna[1])]
        self.energy = 70
        self.type = herbivore
        self.type_list = herbivores
        self.food_type = herbs
        self.last_bred_on = 0

    def got_eaten(self):
        del herbivores[self.index]
        for i in range(self.index,len(herbivores)):
            herbivores[i].index -= 1

    def breeding(self):
        for i in herbivores:
            if i.get_intention() == 1:
                if (self.coord_x, self.coord_y) == i.get_coords():
                    if i != herbivores[self.get_index()]:
                        if not self.last_bred_on == i.get_coords():
                            self.energy = int(self.energy / 2)
                            i.change_energy(int(i.get_energy()/2))
                            herbivores.append(herbivore(i.get_coords()[0],i.get_coords()[1],len(herbivores),str(random.randint(0,7))+str(random.randint(0,7))))
                            self.last_bred_on = (self.coord_x, self.coord_y)
                        break

def spawn_herbs(speed):
    if int(counter_prev) == int(counter):
        pass
    else:
        if int(counter) % speed_dict[speed] == 0:
            for i in range(0,3): # adding new herbs each frame
                herbs.append(herb(random.randint(1,41),random.randint(1,41),len(herbs),25,3))


# Add starting herbs, herbivores and carnivores
for i in range(0,100):
    herbs.append(herb(random.randint(1,41),random.randint(1,41),len(herbs),25,3))
for i in range(0,25):
    herbivores.append(herbivore(random.randint(1,41),random.randint(1,41),len(herbivores),str(random.randint(0,7))+str(random.randint(0,7))))
for i in range(0,7):
    carnivores.append(carnivore(random.randint(1,41),random.randint(1,41),len(carnivores),str(random.randint(0,7))+str(random.randint(0,7))))

done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -------- #
while not done:
    counter_prev = counter
    big_counter_prev = big_counter
    delta_t = clock.tick(60)
    counter += game_speed * (delta_t/1000)
    if counter > 120:   # 16 possibile speeds:  1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.
        big_counter += 1
        print(big_counter)
        counter = 0

    # --- Main event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up=1
            #if event.key == pygame.K_DOWN:
            #if event.key == pygame.K_RIGHT:

            if event.key == pygame.K_LEFT:
                for i in range(0,10):
                    herbivores.append(herbivore(random.randint(1,41),random.randint(1,41),len(herbivores),str(random.randint(0,7))+str(random.randint(0,7))))
                for i in range(0,1):
                    carnivores.append(carnivore(random.randint(1,41),random.randint(1,41),len(carnivores),str(random.randint(0,7))+str(random.randint(0,7))))
        #    if event.key == pygame.K_SPACE: # <<<doesn't work yet>>>

            if event.key == pygame.K_ESCAPE:
                herbs = []
                omnivores = []
                carnivores = []

    # --- Game logic --- #
    spawn_herbs(herbs_spawn_rate)

    if key_up == 1:
        carnivores.append(carnivore(random.randint(1,41),random.randint(1,41),len(carnivores),str(random.randint(0,7))+str(random.randint(0,7))))
        key_up = 0


    # --- Drawing code --- #
    screen.fill(LIGHTGRAY)
    draw_window()
    for i in herbs:
        i.draw()
    for i in herbivores:
        if i.get_state()==0:
            i.starved(i.get_type_list())
        i.action(i.get_food_type())
        i.move()
    for i in carnivores:
        if i.get_state()==0:
            i.starved(i.get_type_list())
        i.action(i.get_food_type())
        i.move()

    if int(big_counter_prev) == int(big_counter):
        pass
    else:
        if int(big_counter) % 1 == 0:
            print("...")
            print("..::: Current amount of HERBS:",len(herbs),":::..")
            print("..::: Current amount of HERBIVORES:",len(herbivores),":::..")
            print("..::: Current amount of CARNIVORES:",len(carnivores),":::..")
    # --- Update the screen --- #
    pygame.display.flip()
