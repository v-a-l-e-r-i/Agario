from pygame import *

init()
window_size = 500, 400
window = display.set_mode(window_size)
clock = time.Clock()

rect = Rect(0, 0, 50, 50)

little_leaf = image.load('assets_level/little_leaf.png')
little_leaf = transform.scale(little_leaf, (50, 50))

while True:
    window.fill((0,0,0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            quit()

    draw.rect(window, (255, 0, 0), rect)

    window.blit(little_leaf, (100, 200))

    
    if keys[K_w]:
        rect.y -= 5
    if keys[K_s]:
        rect.y += 5
    if keys[K_d]:
        rect.x += 5
    if keys[K_a]:
        rect.x -= 5

    display.update()
    clock.tick(60)