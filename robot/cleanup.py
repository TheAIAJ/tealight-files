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
  
  elif right_side() == 'fruit':
    turn(1)
  
  elif left_side() == 'fruit':
    turn(-1)
  
  i+= 1