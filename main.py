import pyttsx3
e = pyttsx3.init()
e_1 = e.getProperty("rate")
e.setProperty("rate", 150)
import pygame
icon = pygame.image.load("icon game.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("SELF DRIVING CAR")
e = pyttsx3.init()
e_1 = e.getProperty("rate")
e.setProperty("rate", 150)

r = input('we have yellow and red  color tell me your choice: ')
if "red" in r:
    e.say("That's right")
    car = pygame.image.load("tesla.png")
elif "yellow" in r:
    e.say("That's right")
    car = pygame.image.load("yellow (1).png")

import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')




car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(90)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
# import pygame
# pygame.init()
# display = pygame.display.set_mode((320,568))
# bg = pygame.image.load("bg.png")
# bird = pygame.image.load("bird.png")
# bird_y = 300
# clock = pygame.time.Clock()
# while True:
#     display.blit(bg, (0,0))
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         bird_y = bird_y - 6
#     elif keys[pygame.K_DOWN]:
#         bird_y = bird_y + 6
#     elif keys[pygame.K_UNKNOWN]:
#         print("press down and up key to move upward and downward ")
#
#
#     display.blit(bird, (0,300))
#     pygame.display.update()
#     clock.tick(60)

