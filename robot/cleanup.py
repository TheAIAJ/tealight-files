from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

i = 0
while i < 500:
  if look() == 'fruit':
    move()
  
  if touch() == 'fruit':
    move()
  
  if right_side() == 'fruit':
    move()
  
  if left_side() == 'fruit':
    move()
  
  i+= 1