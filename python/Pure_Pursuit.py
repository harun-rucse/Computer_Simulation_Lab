import pygame
import numpy as np

pygame.init()
pygame.display.set_caption('Pure Pursuit')

width, height = 1000, 700
screenSize = (width, height)
screen = pygame.display.set_mode(screenSize)

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render('F', True, (0,255,0), (0,0,0))
position_text2 = font.render('B', True, (255,0,0), (0,0,0))
position_text3 = font.render('Caught', True, (0,255,0), (0,0,0))
position_text4 = font.render('Escape', True, (255,0,0), (0,0,0))

textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()

def coord(pos):
    return (3 * (pos[0]+50), 6 * (pos[1]+50))

inputs = []
with open('./pp_input.txt') as file:
    for line in file.readlines():
        inputs.append(line.rstrip().rsplit(','))

vf = int(inputs[0][0])
xb = [int(x) for x in inputs[1]]
yb = [int(x) for x in inputs[2]]

xf = [0]
yf = [50]

t = 0
running = True

screen.fill((0,0,0))

while t <= len(xb) and running:
    ''' Display time '''
    pygame.time.delay(900)
    position_text5 = font.render('Time: {}'.format(t+1), True, (0,0,0), (255,255,255))
    textRect5 = position_text5.get_rect()

    textRect5.center = (90, height-50)
    screen.blit(position_text5, textRect5)    

    if t > 10:
        textRect4.center = (width/2, height/2)
        screen.blit(position_text4, textRect4)

        print('Bomber escaped!')
        running = False

    if t > 0:
        pygame.draw.line(screen, (0,255,0), coord([xf[t-1], yf[t-1]]), coord([xf[t], yf[t]]), 1)
        pygame.draw.line(screen, (255,0,0), coord([xb[t-1], yb[t-1]]), coord([xb[t], yb[t]]), 1)

        pygame.draw.circle(screen, (255,255,255), coord([xf[t], yf[t]]), 2)
        pygame.draw.circle(screen, (255,255,255), coord([xb[t], yb[t]]), 2)

    else:
        textRect1.center = coord([xf[t], yf[t]])
        screen.blit(position_text1, textRect1)

        textRect2.center = coord([xb[t], yb[t]])
        screen.blit(position_text2, textRect2)

    dist = np.sqrt( (xb[t]-xf[t])**2 + (yb[t]-yf[t])**2 )
    if dist <= 10:
        textRect3.center = (width/2, height/2)
        screen.blit(position_text3, textRect3)

        print('Target caught at Time: {} Bomber position: {} and Fighter position: {}'.format(t+1, (xb[t], yb[t]), (xf[t], yf[t])))
        running = False
        
    sin_theta = (yb[t] - yf[t]) / dist
    cos_theta = (xb[t] - xf[t]) / dist

    xf.append(round(xf[t] + vf * cos_theta))
    yf.append(round(yf[t] + vf * sin_theta))

    t += 1
    pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()