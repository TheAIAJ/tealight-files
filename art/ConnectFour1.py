from tealight.art import (color, line, spot, circle, box, image, text, background)
from github.huseyinergisi.art.movecounter import *
####Variables####
color("blue")
box(50,950,800,-800)

xArray = [100, 200, 300, 400, 500, 600, 700, 800]
yArray = [900, 800, 700, 600, 500, 400, 300, 200]

columnCounter = [0, 0, 0, 0, 0, 0, 0, 0]

x1 = 100
y1 = 900
x2 = 150
y2 = 950
x3 = 50
y3 = 850

turn = 0
####Board######
for j in range (0,8):
  for i in range (0,8):
   color("white")
   spot(x1, y1, 40)
   x1 += 100
  x1 = 100
  y1 -= 100

for b in range (0,7):
 color("black")
 line(x2, y2, x2,y2-800)
 x2 += 100
  
for a in range (0,7):
 color("black")
 line(x3, y3, x3+800,y3)
 y3 += -100
####Gameplay####
def handle_mouseup(x, y):
  global turn, columnCounter
  
  if 50 < x <= 150:
    i = 0
  elif 150 < x <= 250:
    i = 1
  elif 250 < x <= 350:
    i = 2
  elif 350 < x <= 450:
    i = 3
  elif 450 < x <= 550:
    i = 4
  elif 550 < x <= 650:
    i = 5
  elif 650 < x <= 750:
    i = 6
  elif 750 < x <= 850:
    i = 7
  
  if turn == 1:
    color("red")
  else:
    color("yellow")
  if i <= 7 and columnCounter[i] < 8:
    DrawSpot(i, columnCounter[i])
    turn = (turn + 1) % 2
  print turn
  print columnCounter
 
import handle_mousemove()

def DrawSpot(x, y):
  global columnCounter
  spot(xArray[x], yArray[y], 40)
  if columnCounter[x] < 8:
    columnCounter[x] += 1