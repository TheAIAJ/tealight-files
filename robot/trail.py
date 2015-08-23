from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 0
t = 1
while i < 400:
  if touch() == 'fruit':
    move()
  
  elif right_side() == 'fruit':
    turn(1)
    t += 1
  elif left_side() == 'fruit':
    turn(-1)
    t -= 1
  elif touch() != 'fruit' and left_side() != 'fruit' and right_side() != 'fruit':
    move()
    for i in range(0, 4):
      turn(1)
      t += 1
      if t == 3:
        move()
      if touch() == 'fruit':
        break
  
  i += 1


    