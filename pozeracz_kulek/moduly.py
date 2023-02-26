#cheat - autoplay

def automation(wsp_gracz_X, wsp_gracz_Y, enemy_x, enemy_y):
    if wsp_gracz_X == enemy_x and wsp_gracz_Y == enemy_y:
        pass
    else:
        if wsp_gracz_X > enemy_x:
            wsp_gracz_X -= 1
        else:
            wsp_gracz_X += 1
        if wsp_gracz_Y > enemy_y:
            wsp_gracz_Y -= 1
        else:
            wsp_gracz_Y += 1          
    return wsp_gracz_X, wsp_gracz_Y

