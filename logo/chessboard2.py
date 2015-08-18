from tealight.logo import (move, turn)


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
#square(10)

def row(side):
  for i in range(0,8):
    turn(90)
    move(side)
    turn(-90)
    square(side)

row(10)