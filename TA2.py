import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
#Add gravity and assign 1000.               # for SA make this 0, for AA2 make it 1000
#Add wind and assign 0.                     # for SA change this to value between 100-1000, for AA2 keep the value of SA
space = pymunk.Space()
#Declare space.gravity and assign wind, gravity to it.
draw_options = pymunk.pygame_util.DrawOptions(screen)

#Add body and assign pymunk.Body(1,100).
#Add shape and assign pymunk.Circle(body, 25).
#Add body.position and assign 200, 100
#Add body and shape to space using space.add(body, shape).

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Add space.debug_draw(draw_options) to draw the created body.
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)
