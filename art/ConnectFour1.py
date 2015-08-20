from tealight.art import (color, line, spot, circle, box, image, text, background)

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

def handle_mouseup(x, y):
  global turn, columnCounter
  if (x > 50) and (x <=150):
    if turn == 1:
      color("red")
    else:
      color("yellow")
    DrawSpot(0, columnCounter[0])
    turn = (turn + 1) % 2
    print turn
    
  
def DrawSpot(x, y):
  global columnCounter
  spot(xArray[x], yArray[y], 40)
  columnCounter[x] += 1