from tealight.logo import (move, turn)

def chessboard(size):
  for i in range(0,8):
    vertical(size)
  
def vertical(size):
  move(size * 8)
  turn(90)
  move(size)
  turn(90)

size = 10
chessboard(size)