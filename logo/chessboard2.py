from tealight.logo import (move, turn)


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
#square(10)

def row(side):
  for i in range(0,8):
    square(side)
    turn(90)
    move(side)
    turn(-90)

#row(10)

def board(side):
  for i in range(0,8):
    row(side)
    move(side)
    turn(-90)
    move(side*8)
    turn(90)
    
board(20)