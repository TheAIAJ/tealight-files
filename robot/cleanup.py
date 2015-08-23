from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

i = 0
while i < 500:
  
  twoSide = right_side() == 'fruit' and left_side() == 'fruit'
  
  oneSide = right_side() == 'fruit' or left_side() == 'fruit'
  
  noSide = right_side() != 'fruit' and left_side() != 'fruit'
  
  if touch() != 'fruit' and noSide:
    if look() == 'fruit':
      move()
    elif look() != 'fruit':
      turn(-1)
  
  if touch() == 'fruit' and noSide:
    move()
    
  if touch() == 'fruit' and twoSide:
    turn(1)
    
  if touch() == 'fruit' and oneSide:
    move()
  
  if touch() != 'fruit' and left_side() == 'fruit':
    turn(-1)
  
  if touch() != 'fruit' and right_side() == 'fruit':
    turn(1)
 
  i+= 1
