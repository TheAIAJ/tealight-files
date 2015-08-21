#By: Huseyin Ergisi, Ryan Gregory, Andrew Jeffery
#GitHub: huseyinergisi, Rhino5651, TheAIAJ
from tealight.art import *
from tealight.net import connect, send

connect("Connect4Multi")

####Variables####
font("80px Arial")
text(275,1030,"Connect 4")
color("blue")
box(50,950,800,-800)

xArray = [100, 200, 300, 400, 500, 600, 700, 800]
yArray = [900, 800, 700, 600, 500, 400, 300, 200]

posArray = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

columnCounter = [0, 0, 0, 0, 0, 0, 0, 0]

counter = 0

x1 = 100
y1 = 900
x2 = 150
y2 = 950
x3 = 50
y3 = 850

turn = 0

def handle_message(message):
  global counter
  columnCounter = message[0]
  posArray = message[1]
  turn = message[2]
    
  for y in range(0, 8):
    for x in range(0, 8):
      if posArray[y][x] == 1:
        color("yellow")
        spot(xArray[x], yArray[y], 40)
      elif posArray[y][x] == 2:
        color("red")
        spot(xArray[x], yArray[y], 40)
  
  print posArray
  print turn
  
  win(turn, posArray)
  
  print posArray
  print turn
  
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
  i = -1
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
  elif x < 50:
    i = 0
    
  if turn == 1:
    color("red")
  elif turn ==0:
    color("yellow")
    
  if i <= 7 and columnCounter[i] < 8:
    DrawSpot(i, columnCounter[i], turn)
    win(turn, posArray)
    turn = (turn + 1) % 2
 
def clear():
  color("white")
  spot(100, 100, 40)
  spot(200, 100, 40)
  spot(300, 100, 40)
  spot(400, 100, 40)
  spot(500, 100, 40)
  spot(600, 100, 40)
  spot(700, 100, 40)
  spot(800, 100, 40)

def change():
  global xmove
  if turn == 0:
    color("yellow")
    spot(xmove, 100, 40)
  elif turn == 1:
    color("red")
    spot(xmove, 100, 40)

def handle_mousemove(x,y):
  global xmove
  #column1
  if 50 < x < 150:
    clear()
    xmove = 100
    change()
  #column2   
  if 150 < x < 250:
    clear()
    xmove = 200
    change()
  #column3   
  if 250 < x < 350:
    clear()
    xmove = 300
    change()
  #column4   
  if 350 < x < 450:
    clear()
    xmove = 400
    change()
  #column5   
  if 450 < x < 550:
    clear()
    xmove = 500
    change()
  #column6   
  if 550 < x < 650:
    clear()
    xmove = 600
    change()
  #column7  
  if 650 < x < 750:
    clear()
    xmove = 700
    change()
  #column8   
  if 750 < x < 850:
    clear()
    xmove = 800
    change()

def DrawSpot(x, y, turn):
  global columnCounter
  spot(xArray[x], yArray[y], 40)
  if columnCounter[x] < 8:
    columnCounter[x] += 1
    posArray[y][x] = turn + 1
   
        
def win(turn, posArray):
  global counter
  color("Black")
  font("80px Verdana")
  #check horizontal
  turn += 1
  for p in range(0, len(posArray)):
    for j in range(0, len(posArray[p]) - 3):
      if posArray[p][j] == turn and posArray[p][j + 1] == turn and posArray[p][j + 2] == turn and posArray[p][j + 3] == turn:
        if turn == 1 and counter == 0:
          text(225, 45, "Yellow Wins")
          counter += 1
        elif turn == 2 and counter == 0:
          text(225, 45, "Red Wins")
          counter += 1

  #check vertical
  for p in range(0, len(posArray) - 3):
    for j in range(0, len(posArray[p])):
      if posArray[p][j] == turn and posArray[p + 1][j] == turn and posArray[p + 2][j] == turn and posArray[p + 3][j] == turn:
        if turn == 1 and counter == 0:
          text(225, 45, "Yellow Wins")
          counter += 1
        elif turn == 2 and counter == 0:
          text(225, 45, "Red Wins")
          counter += 1
  
  #check diagonal up
  for p in range(0, len(posArray) - 3):
    for j in range(0, len(posArray[p]) - 3):
      if posArray[p][j] == turn and posArray[p + 1][j + 1] == turn and posArray[p + 2][j + 2] == turn and posArray[p + 3][j + 3] == turn:
        if turn == 1 and counter == 0:
          text(225, 45, "Yellow Wins")
          counter += 1
        elif turn == 2 and counter == 0:
          text(225, 45, "Red Wins")
          counter += 1
  
  #check diagonal down      
  for p in range(0, len(posArray)):
    for j in range(0, len(posArray[p]) - 3):
      if posArray[p][j] == turn and posArray[p - 1][j + 1] == turn and posArray[p - 2][j + 2] == turn and posArray[p - 3][j + 3] == turn:
        if turn == 1 and counter == 0:
          text(225, 45, "Yellow Wins")
          counter += 1
        elif turn == 2 and counter == 0:
          text(225, 45, "Red Wins")
          counter += 1