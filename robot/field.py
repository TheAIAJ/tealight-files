from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
i = 400
for i in range(400):
  if look() == "flower":
    move()
  