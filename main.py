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
# Define variables and lists
key_up = 0
counter = 0
counter_prev = counter
animals=[]
herbs=[]
# DNA coding
color_dict={
0: ORANGE,
1: YELLOW,
2: GREEN,
3: CYAN,
4: BLUE,
5: PURPLE,
6: PINK,
7: RED
}
speed_dict={
0: 12,
1: 10,
2: 8,
3: 6,
4: 5,
5: 4,
6: 3,
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
            for i in range(self.index,len(herbs)):
                print(i)
                herbs[i].index-=1

    def draw(self):
        pygame.draw.circle(screen, FORESTGREEN, [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1]], 3)

    def got_eaten(self):
        del herbs[self.index]
        for i in range(self.index,len(herbs)):
            try:
                herbs[i].index-=1
            except IndexError:
                pass
        for i in herbs:
            print(i.index)

# Class creating animals
class animal:
    def __init__(self,coord_x,coord_y,index,dna):
            self.dna=dna
            self.index=index
            self.color=color_dict[int(dna[0])]
            self.speed=speed_dict[int(dna[1])]
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.energy = 25

    def get_index(self):
        return self.index

    def get_dna(self):
        return self.dna

    def get_state(self):
        if self.energy>0: return 1 #alive
        if self.energy<1: return 0 #dead

    def get_energy(self):
        return self.energy

    def get_coord(self):
        return self.coord_x, self.coord_y

    def move(self):
        global counter
        pygame.draw.rect(screen, self.color, [grid[self.coord_y][self.coord_x][0], grid[self.coord_y][self.coord_x][1], 9, 9])
        if int(counter_prev) == int(counter):
            #print("ugh")
            pass
        else:
            if int(counter)%self.speed == 0:
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
    pass

# Class creating herbivores
class herbivore(animal):
    pass


# Add 10 herbs to 'herbs' list
for i in range(0,10):
    herbs.append(herb(random.randint(0,43),random.randint(0,43),len(herbs),25,3))
# Add 10 animals to 'animals' list
for i in range(0,10):
    animals.append(animal(random.randint(1,42),random.randint(1,42),len(animals),str(random.randint(0,7))+str(random.randint(0,7))))

done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -------- #
while not done:
    counter_prev = counter
    delta_t = clock.tick(60)
    counter += 30 * (delta_t/1000)
    if counter > 120:   # 16 possibile speeds:  1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120.
        counter = 0

    # --- Main event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up=1
            if event.key == pygame.K_DOWN:
                print(len(animals))
            if event.key == pygame.K_RIGHT:
                herbs[2].got_eaten()
            if event.key == pygame.K_LEFT:
                for i in range(0,5):
                    animals.append(animal(random.randint(1,42),random.randint(1,42),len(animals),str(random.randint(0,7))+str(random.randint(0,7))))
            if event.key == pygame.K_SPACE: # <<<doesn't work yet>>>
                for i in herbs:
                    i.draw()

    # --- Game logic --- #
    if key_up == 1:
        animals.append(animal(random.randint(1,42),random.randint(1,42),len(animals),str(random.randint(0,7))+str(random.randint(0,7))))
        key_up = 0

    # --- Drawing code --- #
    screen.fill(LIGHTGRAY)
    draw_window()
    for i in range(0,len(animals)):
        animals[i].move()



    # --- Update the screen --- #
    pygame.display.flip()
