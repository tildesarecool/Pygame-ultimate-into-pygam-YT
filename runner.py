'''
"""
video: of about 3h 45m
https://www.youtube.com/watch?v=AY9MnQ4x3zk

Link to the project folder: https://github.com/clear-code-projects/UltimatePygameIntro

Link to the background music: https://opengameart.org/content/5-chiptunes-action
Link to the artwork: https://opengameart.org/content/platformer-art-pixel-edition

got to showing the ground/sky surfaces at the 37m 15s mark or so

left off on "working with text" at 37:44 in
ractangles: 51:30


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


# convert make the PNG intosome kind of native python/pygame format...or something -- 50:30 in
# surface origin point always upper left corner
# rectangle (for collission box) can be set to midleft/midbottom etc which adjusts the coords
# this combination of surface/rectwill be repplaced by sprite class/something else later
# for now "move rect instead of surface" is proper way to move element/character
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black') # text, anti-alias true/false, color

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # alpha to acknowledge transparancy of PNG image
snail_rect = snail_surf.get_rect(midbottom = (600,300))

#snail_x_pos = 600  # no longer needed

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300)) # effectively sets the surface and rectanble into one thing


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

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800 # 800 is right side of screen
    screen.blit(snail_surf, snail_rect)
    #snail_x_pos -= 3

    player_rect.left += 1 # as defined aboe, the rectangle around the player surface with "origin point" midbottom - this moves it via cordinates
#    print(player_rect.left) # useful for output of cords
    screen.blit(player_surf, player_rect) # now display both via biltter

    # update everything
    pygame.display.update() # connected back to that screen variable
    clock.tick(60) # 60 fps
