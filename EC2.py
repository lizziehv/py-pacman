# Author: Lizzie Hernandez Videa
# Purpose: To create a Pac-Man game

from cs1lib import *
from dot import Dot
from random import randint

UP_KEY = "i"
DOWN_KEY = "m"
RIGHT_KEY = "l"
LEFT_KEY = "j"
PACMAN_SPEED = 1
GHOST_SPEED = 1

red = load_image("images/red.png")
blue = load_image("images/blue1.png")
orange = load_image("images/orange1.png")


def background():
    set_clear_color(0, 0, 0)
    clear()
    dots()
    obstacles()


def black_square(x,y):  # obstacles
    disable_stroke()
    draw_rectangle(x, y, 18, 18)
    enable_stroke()


def black_rectangle(x, y, w, h):  # obstacles
    disable_stroke()
    draw_rectangle(x, y, w, h)
    enable_stroke()


def obstacles():  # blue boxes
    enable_stroke()
    set_stroke_width(2)
    set_stroke_color(0, 0, 1)
    set_fill_color(0, 0, 0)
    # green boxes
    draw_rectangle(155, 155, 110, 70)  # ghost box
    draw_rectangle(160, 160, 100, 60)
    black_rectangle(150, 250, 120, 40)  # 2nd obstacle
    black_rectangle(190, 270, 40, 80)
    draw_rectangle(160, 260, 100, 20)
    draw_rectangle(200, 280, 20, 60)
    black_square(201,  271)
    black_rectangle(150, 30, 120, 40)  # 3rd obstacle
    black_rectangle(190, 50, 40, 80)
    draw_rectangle(160, 40, 100, 20)
    draw_rectangle(200, 60, 20, 60)
    black_square(201, 51)
    black_rectangle(90, 30, 40, 160)  # 4th obstacle
    black_rectangle(110, 90, 60, 40)
    draw_rectangle(100, 40, 20, 140)
    draw_rectangle(120, 100, 40, 20)
    black_square(119, 101)
    black_rectangle(290, 30, 40, 160)  # 5th obstacle
    black_rectangle(250, 90, 60, 40)
    draw_rectangle(300, 40, 20, 140)
    draw_rectangle(260, 100, 40, 20)
    black_square(299, 101)
    black_rectangle(90, 210, 40, 80)  # 6th obstacle
    draw_rectangle(100, 220, 20, 60)
    black_rectangle(290, 210, 40, 80)  # 7th obstacle
    draw_rectangle(300, 220, 20, 60)
    black_rectangle(90, 310, 80, 60)  # 8th obstacle
    draw_rectangle(100, 320, 60, 40)
    black_rectangle(250, 310, 80, 60)  # 9th obstacle
    draw_rectangle(260, 320, 60, 40)
    black_rectangle(0, 30, 70, 220)  # 10th
    draw_rectangle(0, 40, 60, 80)
    draw_rectangle(5, 45, 50, 70)
    draw_rectangle(0, 160, 60, 80)  # 11th
    draw_rectangle(5, 165, 50, 70)
    black_rectangle(0, 310, 70, 60)
    black_rectangle(30, 270, 40, 100)  # 12th
    draw_rectangle(0, 320, 60, 40)
    draw_rectangle(40, 280, 20, 80)
    black_rectangle(39, 321, 18, 38)
    black_rectangle(350, 30, 70, 220)  # 13th
    draw_rectangle(360, 40, 60, 80)
    black_rectangle(350, 270, 40, 100)  # 14th
    black_rectangle(350, 310, 70, 60)
    draw_rectangle(365, 45, 50, 70)
    draw_rectangle(360, 160, 60, 80)
    draw_rectangle(365, 165, 50, 70)
    draw_rectangle(360, 280, 20, 80)
    draw_rectangle(360, 320, 60, 40)
    black_square(361, 319)
    draw_rectangle(0, 395, 420, 20)  # text box


def dots():  # white dots
    global new_game, score
    x = 0
    disable_stroke()
    for dot in glist:
        dot.draw()
    if game_in_progress:
        for dot in glist:
            if ball_x - ball_r <= dot.x <= ball_x + ball_r and ball_y - ball_r <= dot.y <= ball_y + ball_r and not dot.eaten:
                dot.change_color()
                score += 10


def my_key_press(key):  # sets pressed keys to true
    global i_pressed, m_pressed, l_pressed, j_pressed, game_in_progress
    if key == UP_KEY:
        i_pressed = True
    if key == DOWN_KEY:
        m_pressed = True
    if key == RIGHT_KEY:
        l_pressed = True
    if key == LEFT_KEY:
        j_pressed = True
    if key == "q":
        cs1_quit()
    if key == " ":
        game_in_progress = True


def my_key_release(key):  # sets pressed keys to false
    global i_pressed, m_pressed, l_pressed, j_pressed
    if key == UP_KEY:
        i_pressed = False
    if key == DOWN_KEY:
        m_pressed = False
    if key == RIGHT_KEY:
        l_pressed = False
    if key == LEFT_KEY:
        j_pressed = False


def text():
    enable_stroke()
    set_stroke_width(2)
    set_stroke_color(1, 1, 1)
    set_font("Ayuthaya")
    set_font_size(15)
    if game_in_progress:
        draw_text("HIGH SCORE: " + str(score), 55, 412)
    else:
        draw_text("Press space bar to start", 65, 412)


def top_wall():  # top boundaries
    if (160 - e <= ball_x <= 260+ e) and (ball_y == 240):
        return True
    elif ball_y == 360 + ball_r and (0 <= ball_x <= 60 + e or 100 -e <= ball_x <= 160 + e or 260 - e <= ball_x <= 320 + e or 360 - e <= ball_x <= 420):
        return True
    elif ball_y==280+ball_r and (100-e <= ball_x <=120 + e or 160 - e<= ball_x <=260+e or 300 - e<= ball_x <=320+e):
        return True
    elif ball_y== 120 + ball_r and (120<= ball_x <=160 + ball_r or 200-ball_r<= ball_x <=220 + ball_r or 260 - ball_r<= ball_x <=300+ball_r):
        return True
    elif ball_y==60 + ball_r and (160- e<= ball_x <=260 + e):
        return True
    elif ball_y== 240 + ball_r and (0<= ball_x <=60 + e or 360 - e<= ball_x <=420):
        return True
    elif ball_y==180+ball_r and (110-e<=ball_x<=120+e or 300-e<=ball_x<=320 +e ):
        return True
    elif ball_y==340+ball_r and 200-e<=ball_x<=220+e:
        return True
    elif ball_y==ball_r:
        return True


def bottom_wall():  # bottom boundaries
    if ball_y == 390 - ball_r:
        return True
    elif ball_y == 320 - ball_r and (0<= ball_x <=60 + e or 100- e <= ball_x <=160 + e or 260 - e<= ball_x <=320 + e or 360 - e<= ball_x <=420):
        return True
    elif ball_y == 280- ball_r and (40 - e<= ball_x <=60 + e or 360-e<= ball_x <=380 + e):
        return True
    elif ball_y ==260- ball_r and 160 - e <= ball_x <= 260 + e:
        return True
    elif ball_y ==100- ball_r and (120<= ball_x <= 160+ e or 260-e<= ball_x <=300):
        return True
    elif ball_y ==40- ball_r and (0<= ball_x <= 60 + e or 100- e<= ball_x <= 120+ e or 160 - e <= ball_x <= 260 + e or 300-e<= ball_x <=320 + e or ball_x>=360-e):
        return True
    elif ball_y ==220- ball_r and (100-e<= ball_x <=120 + e or 300-e <= ball_x <=320+e):
        return True
    elif ball_y == 160-ball_r and 160 - e <= ball_x <= 260 + e:
        return True


def right_wall():  # right boundaries
    if ball_x>= 420-ball_r:
        return True
    elif ball_x== 360 - ball_r and (40-e<= ball_y<=240+e or 280-e<= ball_y<=360 + e):
        return True
    elif ball_x== 300 -ball_r and (40-e<= ball_y<=180 + e or 220-e<= ball_y<=280 + e):
        return True
    elif ball_x== 260 -ball_r and (100-e<= ball_y <=120 + e or 320-e<= ball_y <=360+e):
        return True
    elif ball_x== 200 -ball_r and (60 + e<= ball_y <=120+e or 280<= ball_y <= 340+e):
        return True
    elif ball_x== 160 -ball_r and (40-e<= ball_y <=60+e or 160-e<= ball_y <=220+e or 260-e<= ball_y <=280+e):
         return True
    elif ball_x== 100 -ball_r and (40-e<= ball_y <=180 + e or 220-e<= ball_y <=280+e or 330-e<= ball_y <=360+ e):
        return True
    elif ball_x== 40 -ball_r and (280-e<= ball_y <=320):
        return True


def left_wall():  # left boundaries
     if ball_x == ball_r:
         return True
     elif ball_x == 60 + ball_r and (40-e<= ball_y<=240+e or 280-e<= ball_y<=360 + e):
         return True
     elif ball_x == 160 + ball_r and (100-e<= ball_y<=120 + e or 320-e<= ball_y<=360 + e):
         return True
     elif ball_x == 120 + ball_r and (40-e<= ball_y<=180 + e or 220-e<= ball_y<=280 + e):
         return True
     elif ball_x == 220 + ball_r and (60 + e<= ball_y <=120+e or 280<= ball_y <= 340+e):
         return True
     elif ball_x == 260 + ball_r and (40-e<= ball_y <=60+e or 160-e<= ball_y <=220+e or 260-e<= ball_y <=280+e):
         return True
     elif ball_x== 320 + ball_r and (40-e<= ball_y <=180 + e or 220-e<= ball_y <=280+e or 330-e<= ball_y <=360+ e):
         return True
     elif ball_x== 380 + ball_r and (280-e<= ball_y <=320):
         return True


def change_pacman_direction():
    global ball_y, ball_x, mouth_x1, mouth_y1, mouth_y2, mouth_x2, m_pressed, i_pressed, j_pressed, l_pressed
    if top_wall():
        i_pressed = False
    if bottom_wall():
        m_pressed = False
    if right_wall():
        l_pressed = False
    if left_wall():
        j_pressed = False
    if not game_in_progress:
        ball_x = 210
        ball_y = 243
        mouth_x1 = ball_x + 13
        mouth_x2 = ball_x + 13
        mouth_y1 = ball_y + 6
        mouth_y2 = ball_y - 6
    if i_pressed:
        ball_y = ball_y - PACMAN_SPEED
        mouth_x1 = ball_x - 6
        mouth_y1 = ball_y - 13
        mouth_x2 = ball_x + 6
        mouth_y2 = ball_y - 13
    elif m_pressed:
        ball_y = ball_y + PACMAN_SPEED
        mouth_x1 = ball_x - 6
        mouth_y1 = ball_y + 13
        mouth_x2 = ball_x + 6
        mouth_y2 = ball_y + 13
    elif j_pressed:
        ball_x = ball_x - PACMAN_SPEED
        mouth_x1 = ball_x - 13
        mouth_x2 = ball_x - 13
        mouth_y1 = ball_y + 6
        mouth_y2 = ball_y - 6
    elif l_pressed:
        ball_x = ball_x + PACMAN_SPEED
        mouth_x1 = ball_x + 13
        mouth_x2 = ball_x + 13
        mouth_y1 = ball_y + 6
        mouth_y2 = ball_y - 6


def pacman():
    set_fill_color(1, 1, 0)
    disable_stroke()
    change_pacman_direction()
    draw_circle(ball_x, ball_y, ball_r)
    set_fill_color(0, 0, 0)
    draw_triangle(ball_x, ball_y, mouth_x1, mouth_y1, mouth_x2, mouth_y2)


def red_ghost_simulator():
    global y_r, x_r, new_game, game_in_progress
    if ball_x - ball_r <= x_r + 20 <= ball_x + ball_r and ball_y - ball_r <= y_r + 20 <= ball_y + ball_r:
        new_game = True
        game_in_progress = False
    if y_r == 180 and 61<= x_r<= 162:
        x_r = x_r-GHOST_SPEED
    elif x_r==60 and 1<=y_r<=361:
        y_r = y_r - GHOST_SPEED
    elif y_r ==0 and 60<=x_r<=320:
        x_r = x_r + GHOST_SPEED
    elif x_r==321 and 0<=y_r<=360:
        y_r = y_r +GHOST_SPEED
    elif y_r == 361 and 61<=x_r<=321:
        x_r = x_r -GHOST_SPEED

def red_ghost():
    global x_r, y_r
    if game_in_progress:
        red_ghost_simulator()
    else:
        x_r = 162
        y_r = 180
    draw_image(red, x_r, y_r)


def blue_ghost_simulator():
    global y_b, x_b, new_game, game_in_progress
    if ball_x - ball_r <= x_b + 20 <= ball_x + ball_r and ball_y - ball_r <= y_b + 20 <= ball_y + ball_r:
        new_game = True
        game_in_progress = False
    if 120 <= y_b <= 170 and x_b == 192:
        y_b = y_b - GHOST_SPEED
    elif y_b == 120-GHOST_SPEED and 192 <= x_b <= 265:
        x_b = x_b + GHOST_SPEED
    elif x_b == 265 + GHOST_SPEED and 119 <= y_b <= 280:
        y_b = y_b + GHOST_SPEED
    elif 222 <=x_b<= 267 and y_b == 280 + GHOST_SPEED:
        x_b = x_b - GHOST_SPEED
    elif x_b==222-GHOST_SPEED and 281 <=y_b <= 360:
        y_b = y_b + GHOST_SPEED
    elif 165<=x_b<=224 and y_b == 360 + GHOST_SPEED:
        x_b = x_b -GHOST_SPEED
    elif 280<=y_b<=361 and x_b== 165 - GHOST_SPEED:
        y_b = y_b - GHOST_SPEED
    elif 120<=x_b<=164 and y_b == 280-GHOST_SPEED:
        x_b = x_b - GHOST_SPEED
    elif x_b==120- GHOST_SPEED and 120<=y_b<=279:
        y_b = y_b -1
    elif 119<=x_b<=160 and y_b==120-GHOST_SPEED:
        x_b = x_b + 1
    elif x_b == 160+ GHOST_SPEED and 60<=y_b<=119:
        y_b = y_b - 1
    elif 120<=x_b<=161 and y_b == 60-GHOST_SPEED:
        x_b = x_b - GHOST_SPEED
    elif x_b==120 - GHOST_SPEED and 1<=y_b <= 59:
        y_b = y_b-1
    elif y_b == 0 and 119<=x_b<= 260:
        x_b = x_b + 1
    elif x_b ==261 and 0<=y_b<= 60:
        y_b = y_b + 1
    elif y_b ==61 and 221<=x_b<=261:
        x_b = x_b - 1
    elif x_b == 220 and 61<=y_b<= 119:
        y_b = y_b + 1


def blue_ghost():
    global x_b, y_b
    if game_in_progress:
        blue_ghost_simulator()
    else:
        x_b = 192
        y_b = 170
    draw_image(blue, x_b, y_b)


def orange_ghost_simulator():
     global y_o, x_o, new_game, game_in_progress
     if ball_x - ball_r <= x_o + 20 <= ball_x + ball_r and ball_y - ball_r <= y_o + 20 <= ball_y + ball_r:
         new_game = True
         game_in_progress = False
     if y_o == 180 and 222 <= x_o <= 260:
         x_o = x_o + GHOST_SPEED
     elif x_o==261 and 119<=y_o<=280:
         y_o = y_o + GHOST_SPEED
     elif y_o==281 and 261<=x_o<=320:
         x_o = x_o + GHOST_SPEED
     elif x_o== 321 and 281 <=y_o <=360:
         y_o = y_o + GHOST_SPEED
     elif y_o==361 and 61<=x_o<=321:
         x_o = x_o -GHOST_SPEED
     elif x_o== 60 and 180<=y_o<=361:
         y_o = y_o - GHOST_SPEED
     elif y_o==179 and 60<=x_o<= 120:
         x_o = x_o + GHOST_SPEED
     elif x_o==121 and 120<=y_o<= 179:
         y_o = y_o - GHOST_SPEED
     elif y_o== 119 and 121<=x_o<= 260:
         x_o = x_o + GHOST_SPEED


def orange_ghost():
    global x_o, y_o
    if game_in_progress:
        orange_ghost_simulator()
    else:
        x_o = 222
        y_o = 180
    draw_image(orange, x_o, y_o)


def window():
    background()
    pacman()
    red_ghost()
    blue_ghost()
    orange_ghost()
    text()


ball_x = 220  # pacman center
ball_y = 240
ball_r = 13  # pacman radius
mouth_x1 = ball_x + 13  # pacman mouth coordinates
mouth_x2 = ball_x + 13
mouth_y1 = ball_y + 6
mouth_y2 = ball_y - 6
x_r = 162   # coordinates for red ghost
y_r = 180
x_b = 192  # coordinates for blue ghost
y_b = 170
x_o = 222  # coordinates for orange ghost
y_o = 180
i_pressed = False  # initial conditions
m_pressed = False
l_pressed = False
j_pressed = False
new_game = True
game_in_progress = False
score = 0
e = ball_r  # error
glist = []  # dot list
for y in range(0, 19):
    for x in range(0, 20):
        d = Dot(20*x + 20, 20*y + 20)
        glist.append(d)

start_graphics(window, framerate=70, height=420, width=420, key_press=my_key_press, key_release=my_key_release)