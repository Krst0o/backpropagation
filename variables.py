import pygame
from Examples import *
from Neural_Network import *

# pygame variables
running = True
(width, height) = (450, 450)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption('Backpropagation')
screen = pygame.display.set_mode((width, height))
learn_button_text = "LEARN"

# img and arm variables
robot_img = pygame.image.load('robot.png')
img_width = robot_img.get_width()
img_height = robot_img.get_height()
arm_length = 80.0
