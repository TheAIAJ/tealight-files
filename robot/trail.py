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
  
  i += 1


    