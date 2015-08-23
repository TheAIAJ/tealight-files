from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 0
while i < 400:
  if touch() == 'fruit':
    move()
  
  elif right_side() == 'fruit':
    turn(1)
  
  i += 1


    