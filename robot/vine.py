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
  
  elif right_side() == 'fruit':
    turn(1)
  
  elif touch() != 'fruit':
    for i in range(0, 4):
      turn(1)
      if touch() == 'fruit':
        break
  
  i += 1