#TheAIAJ
#Andrew Jeffery

#box(x, y, width, height)

from tealight.art import (line, spot, circle, box, rectangle, image, text, background, color, screen_width, screen_height)

counterRadius = 10

numCounter = 8

width = screen_width

height = screen_height

box(200, 150, counterRadius * numCounter, counterRadius * numCounter) 

boardList = [[], [], [], [], [], [], [], []]

for i in range(0, 8):
  None