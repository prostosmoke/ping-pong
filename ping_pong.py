from pygame import *


W_W = 700
W_H = 500
FPS = 60

window = display.set_mode((W_W , W_H))
display.set_caption('Пинг-Понг')


ball = image.load('ball.png')
ball = transform.scale(ball, (30, 30))
ball_x = 50
ball_y = 50
ball_speed_x = 3
ball_speed_y = 3

clock = time.Clock()


game_over = False
is_gameplay = True
while not game_over:
    clock.tick(FPS)


    for e in event.get():
        if e.type == QUIT:
            game_over = True

    
    #правила
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_y+30 >= W_H:
        ball_speed_y *= -1
    if ball_x+30 >= W_W:
        ball_speed_x *= -1
    if ball_y < 0:
        ball_speed_y *= -1
    if ball_x < 0:
        ball_speed_x *= -1

        
    #отрисовка
    window.fill((0, 255, 239))
    window.blit(ball, (ball_x, ball_y))
    display.update()