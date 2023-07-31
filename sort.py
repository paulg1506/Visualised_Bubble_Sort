import pygame
from sort_lib import *

#Initialize Pygame set Icon and Caption
pygame.init()
icon = pygame.image.load('generic-sorting-64.ico')
pygame.display.set_caption('Bubble Sort')
pygame.display.set_icon(icon)

#Setup
gen_bars()
running = True

#Main loop
while running:
	draw()
	sort_bars()
	key_press_check()
	sort_delay()

pygame.quit()