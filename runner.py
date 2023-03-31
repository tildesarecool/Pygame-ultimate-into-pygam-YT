'''
"""
video: of about 3h 45m
https://www.youtube.com/watch?v=AY9MnQ4x3zk

Link to the project folder: https://github.com/clear-code-projects/UltimatePygameIntro

Link to the background music: https://opengameart.org/content/5-chiptunes-action
Link to the artwork: https://opengameart.org/content/platformer-art-pixel-edition
"""
'''
# pygame 2.3.0
import pygame
from sys import exit

pygame.init() # always run first

#create display surface and stored in var

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# test_surface = pygame.Surface((100, 200)) # uses width/height - i guess double parens is necessary

# test_surface.fill('Red')

test_surface = pygame.image.load('graphics/sky.png')

# setup infinite game loop
while True:
    for event in pygame.event.get(): # loop through all the events
        if event.type == pygame.QUIT:
            pygame.quit() # polar opposite of pygame.init()
            exit() # this prevents error "pygame.error: video system not initialized"
    # draw all elements
    screen.blit(test_surface,(200,100)) # takes surface and position


    # update everything
    pygame.display.update() # connected back to that screen variable
    clock.tick(60) # 60 fps

