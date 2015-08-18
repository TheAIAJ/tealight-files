from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

while touch() == 'fruit':
  move()

if right_side() == 'fruit':
  turn(1)

while right_side() == 'fruit':
  move()