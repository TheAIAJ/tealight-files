from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

i = 0
while i < 100:
  if look() == 'fruit':
    move()
  
  if touch() == 'fruit':
    move()

  i+= 1