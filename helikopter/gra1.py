import pygame
import random


size = WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

start_walls = 5
left_walls = 5  

pygame.init()
pygame.font.init()

plane = pygame.image.load('helikopter.png')
plane_height = 28
plane_width = 45

rect_x = WIDTH
rect_y = 0
rect_height = random.randint(50,100)
wall_gap = 150  
BG_Col = 50,80,200
BLACK = 0,0,0
YELLOW = 255,255,0
RED = 255,0,0
loop = 1
time_to_end_game = 0
wall_point = 0
lvl_value = 1
myfont = pygame.font.SysFont('Arial', 50,True)
myfont2 = pygame.font.SysFont('Arial', 20,True)
looser_value = False
lvl_text_x = WIDTH

def wall_generator(counter):
    global walls
    walls = [[rect_x + i*200, rect_y, 20, random.randint(50,150), True, random.randint(90, wall_gap)] for i in range(counter)]

wspx = 20
wspy = HEIGHT/2
run = True
while run:
    screen.fill(BG_Col)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wspy -=20
        if event.type == pygame.MOUSEBUTTONUP:
            wspy -=20

    #definicja helikoptra
    screen.blit(plane, [wspx,wspy])
    wspy+=1

    if loop == 1:
        wall_generator(start_walls)

    for wall in walls:
        if wspx + plane_width > wall[0] and wspx < wall[0]+20:
            if wspy <wall[3] or wspy + plane_height > wall[3]+wall[5]:
                textsurface_loos = myfont.render('Twój wynik to :' + str(wall_point), True, YELLOW)
                looser_value = True
    if looser_value:
        time_to_end_game +=1
        looser_text = myfont.render('Przegrales', True, YELLOW)
        screen.blit(looser_text, (30, HEIGHT/2))
        print(time_to_end_game)

    if (time_to_end_game == 60):
        run = False

    if left_walls >0:
        for wall in walls:
            if wall[4] == True:
                pygame.draw.rect(screen, BLACK, [wall[0], wall[1], 20, wall[3]])
                pygame.draw.rect(screen, BLACK, [wall[0], wall[3] + wall[5], 20, HEIGHT])
                wall[0] -=1
                if wall[0] < -20:
                    wall[4] = False
                    left_walls -=1
    
    if left_walls == 0:
        start_walls +=1
        left_walls = start_walls
        rect_x = HEIGHT
        lvl_value +=1

        lvl_text_x -= 2
        wall_generator(start_walls)

    lvl_text = myfont2.render('level nr '+str(lvl_value), True, RED)
    screen.blit(lvl_text, (WIDTH/2,5))

    pygame.display.update()
    rect_x -= 0.5
    clock.tick(30)
    loop +=1
    
pygame.quit()