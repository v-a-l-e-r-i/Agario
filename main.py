from pygame import *
from random import randint

# pip install pygame-ce

init()
window_size = 500, 400
win = display.set_mode(window_size)
clock = time.Clock()

class Ball:
    def __init__(self, x, y, radius,  color=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def reset(self, radius):
        draw.circle(win, self.color, (self.x, self.y), radius)

class Food(Ball):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, (randint(50, 255), randint(50, 255), randint(50, 255)))


b1 = Ball(0, 0, 25, (255, 0, 0)) #(0, 0, 25 (255, 0, 0))
foods = []
for _ in range(randint(5, 15)):
    f1 = Food(randint(0, 400), randint(0, 500), randint(3, 15))
    foods.append(f1)

while True:
    win.fill((0,0,0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            quit()

    scale = max(0.3, min(50 / b1.radius, 1.5))

    for food in foods:
        food.reset(food.radius*scale)
    b1.reset(b1.radius)

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