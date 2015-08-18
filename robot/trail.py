from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

while True:
  forward()

if right_side() == 'fruit':
  turn(1)

def forward():
  while touch() == 'fruit':
    move()