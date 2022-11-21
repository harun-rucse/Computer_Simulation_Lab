import pygame

pygame.init()
pygame.display.set_caption('Bezier Curve')

width, height = 1000, 600
screenSize = (width, height)
screen = pygame.display.set_mode(screenSize)
screen.fill((0,0,0))

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render('P0', True, (0,0,0), (255,255,255))
position_text2 = font.render('P1', True, (0,0,0), (255,255,255))
position_text3 = font.render('P2', True, (0,0,0), (255,255,255))
position_text4 = font.render('P3', True, (0,0,0), (255,255,255))

textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()

control_points = [(100.0, 500.0),(200.0, 100.0),(600.0, 80.0),(650.0, 410.0)]

P0 = control_points[0]
P1 = control_points[1]
P2 = control_points[2]
P3 = control_points[3]

textRect1.center = P0
textRect2.center = P1
textRect3.center = P2
textRect4.center = P3

screen.blit(position_text1, textRect1)
screen.blit(position_text2, textRect2)
screen.blit(position_text3, textRect3)
screen.blit(position_text4, textRect4)

pygame.draw.line(screen, (255,255,255), P0, P1, 1)
pygame.draw.line(screen, (255,255,255), P2, P3)

u = 0
speed = 0.004

while u <= 1:
    P0_x = pow((1-u), 3) * P0[0]
    P0_y = pow((1-u), 3) * P0[1]

    P1_x = 3 * u * pow((1-u), 2) * P1[0]
    P1_y = 3 * u * pow((1-u), 2) * P1[1]

    P2_x = 3 * pow(u, 2) * (1-u) * P2[0]
    P2_y = 3 * pow(u, 2) * (1-u) * P2[1]

    P3_x = pow(u, 3) * P3[0]
    P3_y = pow(u,3) * P3[1]

    x, y = [(P0_x+P1_x+P2_x+P3_x), (P0_y+P1_y+P2_y+P3_y)]

    pygame.draw.circle(screen, (255,255,255),( round(x), round(y)), 1)
    pygame.display.flip()
    pygame.time.delay(10)

    u += speed


pygame.time.delay(1000)
pygame.quit()
