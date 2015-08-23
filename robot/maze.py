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
  if touch() == 'wall':
    turn(1)
    
  elif right_side() != 'wall':
    turn(1)
    move()
  elif right_side() == 'wall':
    move()