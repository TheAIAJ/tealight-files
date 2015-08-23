from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 0
while i < 1111:
  if touch() == 'fruit':
    move()
  
  elif left_side() == 'fruit':
    turn(-1)
  
  
  i += 1