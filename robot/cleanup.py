from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

i = 0
while i < 500:
  
  oneSide = right_side() == 'fruit' or left_side() == 'fruit'
  
  noSide = right_side() != 'fruit' and left_side() != 'fruit'
  
  if touch() == 'fruit' and oneSide:
    move()
    
  if touch() == 'fruit' and noSide:
    move()
  
  #elif right_side() == 'fruit':
   # turn(1)
  
  #elif left_side() == 'fruit':
   # turn(-1)
  
  elif noSide and look() != 'fruit':
    turn(-1)
    move()
  
  elif touch() != 'fruit' and look() == 'fruit':
    move()
  i+= 1
