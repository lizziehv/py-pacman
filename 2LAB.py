# Author:Lizzie Hernandez Videa
# Date:Friday, April 19
# Purpose: To create a Pong game

from cs1lib import *


# Constants
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
LEFT_UP_KEY = "a"
LEFT_DOWN_KEY = "z"
RIGHT_UP_KEY = "k"
RIGHT_DOWN_KEY = "m"
PADDLE_SPEED = 8  # moves 8 pixels when keys are pressed


def background():
    set_clear_color(0, 0, 102/255)
    clear()


def my_key_press(key):  # sets pressed keys to true
    global a_pressed, z_pressed, k_pressed, m_pressed, y1, y2, game_in_progress  # Sets pressed keys to true
    if key == LEFT_UP_KEY:
        a_pressed = True
    if key == LEFT_DOWN_KEY:
        z_pressed = True
    if key == RIGHT_UP_KEY:
        k_pressed = True
    if key == RIGHT_DOWN_KEY:
        m_pressed = True
    if key == " ":  # starts new game
        game_in_progress = True
    if key == "q":  # quits the game
        cs1_quit()


def my_key_release(key):  # sets released keys to false
    global a_pressed, z_pressed, k_pressed, m_pressed
    if key == LEFT_UP_KEY:
        a_pressed = False
    if key == LEFT_DOWN_KEY:
        z_pressed = False
    if key == RIGHT_UP_KEY:
        k_pressed = False
    if key == RIGHT_DOWN_KEY:
        m_pressed = False


def left_paddle():
    global y1
    set_fill_color(204 / 255, 153 / 255, 1)
    if a_pressed and y1 > 0:  # move left paddle upward
        y1 = y1 - PADDLE_SPEED
    elif z_pressed and y1 < 400-PADDLE_HEIGHT:  # move left paddle downward
        y1 = y1 + PADDLE_SPEED
    draw_rectangle(0, y1, PADDLE_WIDTH, PADDLE_HEIGHT)  # left paddle


def right_paddle():
    global y2
    set_fill_color(204 / 255, 153 / 255, 1)
    if k_pressed and y2 > 0:  # move right paddle upward
        y2 = y2 - PADDLE_SPEED
    elif m_pressed and y2 < 400 - PADDLE_HEIGHT:  # move right paddle downward
        y2 = y2 + PADDLE_SPEED
    draw_rectangle(WINDOW_HEIGHT-PADDLE_WIDTH, y2, PADDLE_WIDTH, PADDLE_HEIGHT)  # right paddle


def text():  # text disappears when the game starts
    if not game_in_progress:
        set_stroke_color(1, 1, 1)
        set_font_size(20)
        set_font("Ayuthaya")
        draw_text("Press space bar to start", 55, 380)


def change_ball_direction():
    global vx, vy
    if x <= PADDLE_WIDTH + r and y1 - r <= y <= y1 + PADDLE_HEIGHT + r and vx < 0:  # bouncing off left paddle
        vx = -vx
    elif x >= WINDOW_WIDTH - PADDLE_WIDTH-r and y2-r <= y <= y2 + PADDLE_HEIGHT + r and vx > 0:  # bouncing off the right paddle
        vx = -vx
    if y <= r:  # bouncing off top wall
        vy = -vy
    elif y >= WINDOW_HEIGHT-r:  # bouncing off bottom wall
        vy = -vy


def ball():
    global x, y, game_in_progress
    set_fill_color(1, 1, 1)
    change_ball_direction()
    if game_in_progress:  # changes position of the ball depending on previous conditions
        x = x + vx
        y = y + vy
    if x <= -5 or x >= WINDOW_WIDTH + 5:  # leaving the window
        x = 200
        y = 200
        game_in_progress = False
    draw_circle(x, y, r)


def pong_game():
    background()
    left_paddle()
    right_paddle()
    ball()
    text()


# Initial conditions
y1 = 0  # left paddle position
y2 = WINDOW_HEIGHT-PADDLE_HEIGHT  # right paddle position
a_pressed = False
z_pressed = False
k_pressed = False
m_pressed = False
x = 200  # x coordinate of ball
y = 200  # y coordinate of ball
r = 10  # ball radius
vx = -5  # x velocity
vy = -3  # y velocity
game_in_progress = False


start_graphics(pong_game, key_press=my_key_press, key_release=my_key_release, framerate=50)
