from pygame import *

# pip install pygame-ce

init()
window_size = 500, 400
window = display.set_mode(window_size)
clock = time.Clock()

class Ball:
    def __init__(self, x, y, radius, color=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def reset(self):
        draw.circle(window, self.color, (self.x, self.y), self.radius)

b1 = Ball(0, 0, 25, (255, 0, 0)) #(0, 0, 25, (255, 0, 0))

while True:
    window.fill((0,0,0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            quit()

    b1.reset()

    if keys[K_w]:
        b1.y -= 5
    if keys[K_s]:
        b1.y += 5
    if keys[K_d]:
        b1.x += 5
    if keys[K_a]:
        b1.x -= 5

    display.update()
    clock.tick(60)