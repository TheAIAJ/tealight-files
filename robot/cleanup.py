from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
"""
i = 0
while i < 500:
  
  twoSide = right_side() == 'fruit' and left_side() == 'fruit'
  
  oneSide = right_side() == 'fruit' or left_side() == 'fruit'
  
  noSide = right_side() != 'fruit' and left_side() != 'fruit'
  
  if touch() != 'fruit' and noSide:
    if look() == 'fruit':
      move()
    elif look() != 'fruit':
      turn(-1)
  
  if touch() == 'fruit' and noSide:
    move()
    
  if touch() == 'fruit' and twoSide:
    turn(1)
    
  if touch() == 'fruit' and right_side() != 'fruit':
    move()
    
  elif touch() == 'fruit' and right_side() == 'fruit':
    turn(1)
  
  if touch() != 'fruit' and left_side() == 'fruit':
    turn(-1)
  
  if touch() != 'fruit' and right_side() == 'fruit':
    turn(1)
 
  i+= 1
"""
def m(num):
  for i in range(0, num):
    move()

    
def r():
  turn(1)
  
def l():
  turn(-1)
  
m(4)
l()
m(1)
l()
m(6)
r()
m(1)
r()
m(9)
l()
m(1)
l()
m(11)
r()
m(1)
r()
m(20)
