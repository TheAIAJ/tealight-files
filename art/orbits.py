from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  
  if vx > 0:
    vx -= 0.05
  
  if vx < 0:
    vx += 0.05
    
  if vy > 0:
    vy -= 0.05
  
  if vy < 0:
    vy += 0.05
  
  vy += 0.1
  
  print 'x is ' + str(x)
  print 'y is ' + str(y)
  print 'screen width is ' + str(screen_width)
  
  if x >= screen_width or x <= 0:
    vx = -vx
    print '-vx'
  
  if y >= screen_height or y <= 0:
    vy = -vy
  
