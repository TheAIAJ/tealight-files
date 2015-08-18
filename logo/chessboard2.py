from tealight.logo import (move, turn)


def square(side):
  for i in range(0,3):
    move(side)
    turn(120)