from pygame import *


W_W = 700
W_H = 500
FPS = 60

window = display.set_mode((W_W , W_H))
display.set_caption('Пинг-Понг')
window.fill((0, 255, 239))


clock = time.Clock()


game_over = False
is_gameplay = True
while not game_over:
    clock.tick(FPS)


    for e in event.get():
        if e.type == QUIT:
            game_over = True


    display.update()