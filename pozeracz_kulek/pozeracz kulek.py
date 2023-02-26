import random
import pygame
from dane import *
from AI_oponent2 import *
from moduly import *
import string



pygame.init()
pygame.font.init()

           
enemy=[[random.randint(0,WIDTH), random.randint(0, HEIGHT), True]]
enemy_green=[[random.randint(0,WIDTH), random.randint(0, HEIGHT), True]]
             

def ruch_od_myszki(m_x, m_y):
    pos_x, pos_y = m_x, m_y 
    global wsp_gracz_X, wsp_gracz_Y

    if pos_x in range(points_up[0][0], points_up[1][0]) and pos_y in range(points_up[1][1], points_up[2][1]):
        wsp_gracz_Y -= player_speed
    if pos_x in range(points_down[0][0], points_down[1][0]) and pos_y in range(points_down[1][1], points_down[2][1]):
        wsp_gracz_Y += player_speed
    if pos_x in range(points_left[0][0], points_left[1][0]) and pos_y in range(points_left[1][1], points_left[2][1]):
        wsp_gracz_X -= player_speed
    if pos_x in range(points_right[0][0], points_right[1][0]) and pos_y in range(points_right[1][1], points_right[2][1]):
        wsp_gracz_X += player_speed
       


running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            global cos
            cos = str(pygame.key.name(event.key))
            if cos =="a" or cos == 'u' or cos == 't' or cos == 'o':
                cos2.append(cos)
                print(cos2)
            else:
                cos2.clear()
    if cos2 == wzor and auto == False:
        print('ale jaja')
        auto = True
        cos2.clear()
    if cos2 == wzor and auto == True:
        print('ale jaja2')
        auto = False
        cos2.clear()
        
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_LEFT]:
        wsp_gracz_X -= player_speed
    if keys[pygame.K_RIGHT]:
        wsp_gracz_X += player_speed
    if keys[pygame.K_UP]:
        wsp_gracz_Y -= player_speed
    if keys[pygame.K_DOWN] :
        wsp_gracz_Y += player_speed
    if pygame.mouse.get_pressed()[0]:
        ruch_od_myszki(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])            
            
    for ene_red in enemy:
            if ene_red[-1] == True:
                pygame.draw.circle(screen, RED, (ene_red[0], ene_red[1]), size_enemy)

    for ene_green in enemy_green:
            if ene_green[-1] == True:
                pygame.draw.circle(screen, GREEN, (ene_green[0], ene_green[1]), size_enemy)

    if auto == True:
        wsp_gracz_X, wsp_gracz_Y = automation(wsp_gracz_X, wsp_gracz_Y, enemy[-1][0], enemy[-1][1])
     
#gracz
    pygame.draw.circle(screen, RED, (wsp_gracz_X, wsp_gracz_Y), size_gamer)
    pygame.draw.circle(screen, GREEN, (opon_green_x, opon_green_y), size_oponent)
    opon_green_x, opon_green_y = oponent(opon_green_x, opon_green_y, enemy_green[-1][0], enemy_green[-1][1], wsp_gracz_X, wsp_gracz_Y, size_gamer,  size_oponent, oponent_speed)


    if (wsp_gracz_X in range((ene_red[0]-size_gamer), (ene_red[0]+size_gamer))) and (wsp_gracz_Y in range((ene_red[1]-size_gamer),(ene_red[1]+size_gamer))):
        ene_red[-1] = False
        size_gamer +=1
        draw_enemy = [random.randint(0,500), random.randint(0, 500), True]
        enemy.append(draw_enemy)


    #if (opon_green_x in range((ene_green[0]-size_oponent), (ene_green[0]+size_oponent))) and (opon_green_y in range((ene_green[1]-size_oponent),(ene_green[1]+size_oponent))):
    if (ene_green[0] - size_oponent - oponent_speed) < opon_green_x < (ene_green[0] + size_oponent + oponent_speed) and (ene_green[1]-size_oponent - oponent_speed) < opon_green_y < (ene_green[1] + size_oponent + oponent_speed):
        ene_green[-1] = False
        size_oponent +=1       
        draw_enemy_green = [random.randint(0,500), random.randint(0, 500), True]
        enemy_green.append(draw_enemy_green)
    
    pygame.draw.polygon
    pygame.draw.polygon(screen, (0,0,255), points_left)
    pygame.draw.polygon(screen, (0,0,255), points_down)
    pygame.draw.polygon(screen, (0,0,255), points_right)
    pygame.draw.polygon(screen, (0,0,255), points_up)    


    gamer_size_info = myfont.render('YOU :' + str(size_gamer-basic_size), True, RED)
    screen.blit(gamer_size_info, (0,0))
    oponent_size_info = myfont.render('OPONENT :' + str(size_oponent-basic_size), True, GREEN)
    screen.blit(oponent_size_info, (WIDTH - 200,0))
    oponent_size_info = myfont_lvl.render('LEVEL :' + str(LVL_number), True, YELLOW)
    screen.blit(oponent_size_info, (WIDTH /2 -100,0))    
 
    
    if wsp_gracz_X > WIDTH:
        wsp_gracz_X = 0
    if wsp_gracz_X < -10:
        wsp_gracz_X = WIDTH - size_gamer
    if wsp_gracz_Y > HEIGHT:
        wsp_gracz_Y = 0
    if wsp_gracz_Y < -10:
        wsp_gracz_Y = HEIGHT -size_gamer
    if opon_green_x > WIDTH:
        opon_green_x = 0
    if opon_green_x < -10:
        opon_green_x = WIDTH - size_oponent    
    if opon_green_y > HEIGHT:
        opon_green_y = 0    
    if opon_green_y < -10:
        opon_green_y = HEIGHT - size_oponent
    
    if opon_green_x -size_oponent < wsp_gracz_X < opon_green_x +size_oponent and opon_green_y -size_oponent < wsp_gracz_Y < opon_green_y +size_oponent and size_gamer > size_oponent:
        print('trafiles')
        LVL_number +=1
        oponent_speed += 0.2
        opon_green_x, opon_green_y = start_oponent_x, start_oponent_y
        wsp_gracz_X, wsp_gracz_Y = start_player_x, start_player_y
    elif opon_green_x -size_oponent < wsp_gracz_X < opon_green_x +size_oponent and opon_green_y -size_oponent < wsp_gracz_Y < opon_green_y +size_oponent and size_gamer < size_oponent:
        looser = True

    if looser:
        screen.fill(BLACK)
        looser_txt = myfont_looser.render('Przegrałeś', True, LOOSER)
        screen.blit(looser_txt, (150, WIDTH/2-30))
        score_txt = myfont_looser.render('Twój wynik :' +str(LVL_number), True, LOOSER)
        screen.blit(score_txt, (130, WIDTH/2))
        looser_time +=1

    if looser_time == 120:
        running = False        

    pygame.display.update()
    clock.tick(60)     


pygame.quit()        
