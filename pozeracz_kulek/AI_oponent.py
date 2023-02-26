def oponent(opon_green_x, opon_green_y, enemy_x, enemy_y, wsp_gracz_X, wsp_gracz_Y):
    my_way_x = abs(enemy_x - opon_green_x)
    oponent_way_x = abs(enemy_x - wsp_gracz_X)
    my_way_y = abs(enemy_y - opon_green_y)
    oponent_way_y = abs(enemy_y - wsp_gracz_Y)

    if my_way_x < oponent_way_x or my_way_y < oponent_way_y:
        speed = 1
    else:
        speed = 4

    if opon_green_x == enemy_x and opon_green_y == enemy_y:
        pass
    else:
        if opon_green_x > enemy_x:
            opon_green_x -= speed
        else:
            opon_green_x += speed
        if opon_green_y > enemy_y:
            opon_green_y -= speed
        else:
            opon_green_y += speed   
    return opon_green_x, opon_green_y