from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 0
while i < 1250:
  if touch() == 'fruit':
    turn(1)
    
  else:
    move()