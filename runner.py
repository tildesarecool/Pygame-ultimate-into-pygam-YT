'''
"""
video: of about 3h 45m
https://www.youtube.com/watch?v=AY9MnQ4x3zk

Link to the project folder: https://github.com/clear-code-projects/UltimatePygameIntro

Link to the background music: https://opengameart.org/content/5-chiptunes-action
Link to the artwork: https://opengameart.org/content/platformer-art-pixel-edition

got to showing the ground/sky surfaces at the 37m 15s mark or so

left off on "working with text" at 37:44 in

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
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# test_surface = pygame.Surface((100, 200)) # uses width/height - i guess double parens is necessary

# test_surface.fill('Red')

sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black') # text, anti-alias true/false, color

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 350

# setup infinite game loop
while True:
    for event in pygame.event.get(): # loop through all the events
        if event.type == pygame.QUIT:
            pygame.quit() # polar opposite of pygame.init()
            exit() # this prevents error "pygame.error: video system not initialized"
    # draw all elements
    # the order these are in is the layeers - the top one drawn here is "under" the  second one (like sky being under "ground" if the orders sky then ground surface)
    screen.blit(sky_surface,(0,0)) # takes surface and position
    screen.blit(ground_surface,(0,300)) # takes surface and position
    screen.blit(text_surface, (300, 50))
    snail_x_pos += 1
    screen.blit(snail_surface, (snail_x_pos, 265))


    # update everything
    pygame.display.update() # connected back to that screen variable
    clock.tick(60) # 60 fps

