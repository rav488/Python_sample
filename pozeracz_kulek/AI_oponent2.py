import math
def go_to_enemy(player_x, player_y, target_x, target_y, oponent_speed):
    if player_x == target_x and player_y == target_y:
        pass
    else:
        if player_x > target_x:
            player_x -= oponent_speed
        else:
            player_x += oponent_speed
        if player_y > target_y:
            player_y -= oponent_speed
        else:
            player_y += oponent_speed  
    return player_x, player_y      

def run_away(player_x, player_y, target_x, target_y, oponent_speed):
    if player_x == target_x and player_y == target_y:
        pass
    else:
        if player_x > target_x:
            player_x += oponent_speed
        else:
            player_x -= oponent_speed
        if player_y > target_y:
            player_y += oponent_speed
        else:
            player_y -= oponent_speed              
    return player_x, player_y          


def oponent(opon_green_x, opon_green_y, enemy_x, enemy_y, wsp_gracz_X, wsp_gracz_Y, size_gamer,  size_oponent, oponent_speed):
    oponent_enemy_x = abs(enemy_x - opon_green_x)
    oponent_gamer_x = abs(opon_green_x - wsp_gracz_X)
    oponent_enemy_y = abs(enemy_y - opon_green_y)
    oponent_gamer_y = abs(opon_green_y - wsp_gracz_Y)
    
    lenght_oponent_gamer = round(math.sqrt(oponent_gamer_x**2+oponent_gamer_y**2))
    lenght_oponent_enemy = round(math.sqrt(oponent_enemy_x**2+oponent_enemy_y**2))
    if size_gamer < size_oponent:
        if lenght_oponent_gamer < lenght_oponent_enemy: #tybizej
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = go_to_enemy(opon_green_x, opon_green_y, wsp_gracz_X, wsp_gracz_Y, oponent_speed)
        elif lenght_oponent_gamer > lenght_oponent_enemy: #kropablizej
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = go_to_enemy(opon_green_x, opon_green_y, enemy_x, enemy_y, oponent_speed)

    elif size_gamer > size_oponent:#ty
        if lenght_oponent_gamer < lenght_oponent_enemy: #tybizej
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = run_away(opon_green_x, opon_green_y, wsp_gracz_X, wsp_gracz_Y, oponent_speed)
        elif lenght_oponent_gamer > lenght_oponent_enemy: #kropablizej
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = go_to_enemy(opon_green_x, opon_green_y, enemy_x, enemy_y, oponent_speed)

    else:
        if lenght_oponent_gamer <= lenght_oponent_enemy:
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = go_to_enemy(opon_green_x, opon_green_y, enemy_x, enemy_y, oponent_speed)
        elif lenght_oponent_gamer > lenght_oponent_enemy:
            if opon_green_x == enemy_x and opon_green_y == enemy_y:
                pass
            else:
                opon_green_x, opon_green_y = go_to_enemy(opon_green_x, opon_green_y, enemy_x, enemy_y, oponent_speed)
    
    return opon_green_x, opon_green_y


'''
założenia programu
1. jeżeli wiekszy od przeciwnika
a) bliżej przeciwnik - atakuj
b) blizej kula - zjedz - jest
2. jezeli mniejszy
a) bliżej przeciwnik uciekaj
b) bliżej kulka zjedz
'''
