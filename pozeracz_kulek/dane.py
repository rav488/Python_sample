import random
import pygame
pygame.font.init()


HEIGHT = 700
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


myfont = pygame.font.SysFont('Arial', 20)            #ustalenie czciąki i rozmiaru wyświetlanego textu
myfont_lvl = pygame.font.SysFont('Arial', 25)
myfont_looser = pygame.font.SysFont('Arial', 35)
#colors

BLACK = 0 ,0 ,0
YELLOW = 255,255,0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0,255,0
LOOSER = 43, 210, 230

#autoplay data
cos2 = []
wzor = ['a','u','t','o']
global auto
auto = False


start_oponent_x = 450
start_oponent_y = 450
start_player_x = 40
start_player_y = 40

opon_green_x = start_oponent_x
opon_green_y = start_oponent_y
wsp_gracz_X = start_player_x
wsp_gracz_Y =start_player_y

player_speed = 5
oponent_speed = 1
basic_size = 10
size_gamer = basic_size
size_oponent = basic_size
size_enemy = 10
LVL_number = 1
looser_time = 0
looser = False



#joystick_place
points_left = [(520, 300), (570, 300), (570, 350), (520,350)]
points_down = [(580,300),(630,300),(630,350),(580,350)]
points_right = [(640,300),(690,300),(690,350),(640,350)]
points_up = [(580,240),(630,240),(630,290),(580,290)]