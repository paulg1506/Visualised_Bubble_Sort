import pygame
import random
'''
TODO Add timers, pass count, and swaps for each sort type.

TODO Add if statement to sort to check if passes equals 0 after going
through entire list. If true list is sorted and should not be iterated
through again.

TODO Add values for timers, passes, swaps to display after sort complete.
'''
WIDTH = 900
HEIGHT = 600
RECT_WIDTH = 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

index = 0
delay = 100
hue_bars = []
len_bars = []
dark_bars = []
static_hue = []
static_len = []
static_dark = []

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 14)


class bar:
	'''
	Creates a bar to be sorted.

		Parameters:
				x (int): Starting x coordinate.
				y (int): Starting y coordinate.
				length (int): Length of bar.
	'''


	def __init__(self, x, y, length):
		'''Initialises each bar with default values.'''
		self.x = x
		self.y = y
		self.length = length
		self.colour = BLACK
		self.hue = 0
		self.dark = 0


	def colour_gen(self):
		'''Generates a random RGB value for bar.'''
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.colour = (r, g, b)


	def calculate_dark(self):
		'''
		Calculates a value for how dark/light the bar colour is.
		This is calculated by summing the RGB values of colour.
		Higher numbers are light, lower numbers are dark.
		''' 
		r, g, b = self.colour
		self.dark = r + g + b


	def calculate_hue(self):
		'''
		Calculates a hue value for the bar based on the colour
		wheel system.
		Calculated hue is a value between 0 and 360 this represents 
		its location on the colour wheel.
		'''
		hue = 0
		r, g, b = self.colour
		r /= 255
		g /= 255
		b /= 255
		greatest = max(r, g, b)
		lowest = min(r, g, b)
		if (greatest - lowest) == 0:
			self.hue = 0
			return
		elif greatest == r:
			hue = (g - b)  / (greatest - lowest)
		elif greatest == g:
			hue = 2 + (b - r) / (greatest - lowest)
		elif greatest == b:
			hue = 4 + (r - g) / (greatest - lowest)
		hue = hue * 60
		hue %= 360
		if hue < 0:
			hue += 360
		self.hue = int(hue)


def gen_bars():
	'''
	Generates the lists of bars which will be sorted by the algorithm.
	A static and dynamic list is created for Hue, Length, and Darkness.
	'''
	x = 0
	while x <= 300 - RECT_WIDTH:
		hue_bars.append(bar(x, 0, HEIGHT // 2))
		x += RECT_WIDTH
	for each in hue_bars:
		each.colour_gen()
		each.calculate_hue()
	for each in hue_bars:
		static_hue.append((each.x, each.colour))
	
	while x <= 600 - RECT_WIDTH:
		rect_height = random.randint(1, (HEIGHT // 2 - 20))
		y_pos = HEIGHT // 2 - rect_height
		static_len.append(bar(x, y_pos, rect_height))
		len_bars.append(bar(x, (y_pos + HEIGHT // 2), rect_height))
		x += RECT_WIDTH
	
	while x <= WIDTH - RECT_WIDTH:
		dark_bars.append(bar(x, 0, HEIGHT // 2))
		x += RECT_WIDTH
	for each in dark_bars:
		each.colour_gen()
		each.calculate_dark()
	for each in dark_bars:
		static_dark.append((each.x, each.colour))
			

def sort_bars():
	'''
	Performs bubble sort based on bar hue, length, and darkness.
	Each swap updates the x location value of bar and its list index.
	The x location value makes sure it is displayed correctly.
	The list index ensures list is in correct order for next iteration.
	'''
	global index
	if (len(len_bars)) == (len(hue_bars)) and (
		(len(hue_bars)) == (len(dark_bars))):
		if index < len(len_bars) - 1:
			bar1 = len_bars[index].length
			bar2 = len_bars[index + 1].length
			if bar1 > bar2:
				len_bars[index].x, len_bars[index+ 1].x = (
					len_bars[index + 1].x, len_bars[index].x
					)
				len_bars[index], len_bars[index + 1] = (
					len_bars[index + 1], len_bars[index]
					)
			bar1 = hue_bars[index].hue
			bar2 = hue_bars[index + 1].hue
			if bar1 > bar2:
				hue_bars[index].x, hue_bars[index + 1].x = (
					hue_bars[index + 1].x, hue_bars[index].x
					)
				hue_bars[index], hue_bars[index + 1] = (
					hue_bars[index + 1], hue_bars[index]
					)
			bar1 = dark_bars[index].dark
			bar2 = dark_bars[index + 1].dark
			if bar1 > bar2:
				dark_bars[index].x, dark_bars[index + 1].x = (
					dark_bars[index + 1].x, dark_bars[index].x
					)
				dark_bars[index], dark_bars[index + 1] = (
					dark_bars[index + 1], dark_bars[index]
					)
		else:
			index = 0
			return
	index += 1


def draw():
	'''
	Draws bars to display.
	Draws the frame to display.
	Draws the labels to display.
	'''
	screen.fill(WHITE)

	for bar in static_len:
		pygame.draw.rect(screen, bar.colour, 
			pygame.Rect(bar.x, bar.y, RECT_WIDTH, bar.length)
			)
	for bar in static_dark:
		bar_x, bar_colour = bar
		pygame.draw.rect(screen, bar_colour, 
			pygame.Rect(bar_x, 0, RECT_WIDTH, HEIGHT // 2)
			)
	for bar in static_hue:
		bar_x, bar_colour = bar
		pygame.draw.rect(screen, bar_colour,	
			pygame.Rect(bar_x, 0, RECT_WIDTH, HEIGHT // 2)
			)
	for bar in len_bars:
		pygame.draw.rect(screen, bar.colour,	
			pygame.Rect(bar.x, bar.y, RECT_WIDTH, bar.length)
			)
	for bar in dark_bars:
		pygame.draw.rect(screen, bar.colour,	
			pygame.Rect(bar.x, HEIGHT // 2, RECT_WIDTH, bar.length)
			)
	for bar in hue_bars:
		pygame.draw.rect(screen, bar.colour, 
			pygame.Rect(bar.x, HEIGHT // 2, RECT_WIDTH, bar.length)
			)
	
	pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, 4))
	pygame.draw.rect(screen, BLACK, pygame.Rect(0, 298, WIDTH, 4))
	pygame.draw.rect(screen, BLACK, pygame.Rect(0, 596, WIDTH, 4))
	pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 4, HEIGHT))
	pygame.draw.rect(screen, BLACK, pygame.Rect(298, 0, 4, HEIGHT))
	pygame.draw.rect(screen, BLACK, pygame.Rect(598, 0, 4, HEIGHT))
	pygame.draw.rect(screen, BLACK, pygame.Rect(896, 0, 4, HEIGHT))
	
	text = font.render('Hue Original', True, BLACK, WHITE)
	text_length, text_height = font.size('Hue Original')
	screen.blit(text, ((150 - (text_length // 2)), 5))
	text = font.render('Length Original', True, BLACK, WHITE)
	text_length, text_height = font.size('Length Original')
	screen.blit(text, ((450 - (text_length // 2)), 5))
	text = font.render('Dark/Light Original', True, BLACK, WHITE)
	text_length, text_height = font.size('Dark/Light Original')
	screen.blit(text, ((750 - (text_length // 2)), 5))
	text = font.render('Hue Sorted', True, BLACK, WHITE)
	text_length, text_height = font.size('Hue Sorted')
	screen.blit(text, ((150 - (text_length // 2)), 305))
	text = font.render('Length Sorted', True, BLACK, WHITE)
	text_length, text_height = font.size('Length Sorted')
	screen.blit(text, ((450 - (text_length // 2)), 305))
	text = font.render('Dark/Light Sorted', True, BLACK, WHITE)
	text_length, text_height = font.size('Dark/Light Sorted')
	screen.blit(text, ((750 - (text_length // 2)), 305))
	pygame.display.update()


def sort_delay():
	'''
	Speeds up or slows down sort by adding a small delay after
	each iteration.
	''' 
	pygame.time.wait(delay)


def key_press_check():
	'''Checks for key press. Allows changing sort speed and exiting'''
	global delay
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				delay += 10
				if delay > 1000:
					delay = 1000
			elif event.key == pygame.K_UP:
				delay -= 10
				if delay < 0:
					delay = 0
			elif event.key == pygame.K_ESCAPE:
				pygame.quit()
				quit()