from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 0
turn = 1
while i < 400:
  if touch() == 'fruit':
    move()
  
  elif right_side() == 'fruit':
    turn(1)
    turn += 1
  elif left_side() == 'fruit':
    turn(-1)
    turn -= 1
  elif touch() != 'fruit' and left_side() != 'fruit' and right_side() != 'fruit':
    move()
    for i in range(0, 4):
      turn(1)
      turn += 1
      if turn == 3:
        moev()
      if touch() == 'fruit':
        break
  
  i += 1


    