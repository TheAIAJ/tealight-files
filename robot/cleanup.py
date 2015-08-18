from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while True:
  if look() == 'fruit':
    move()
  
  if touch() == 'fruit':
    move()
    
  #else:
 #   print 'hello'