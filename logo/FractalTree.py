from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    for i in range(0, 2):
      turn(-45)
      segment(scale / 2, detail - 1)
      turn(45)
      segment(scale / 2, detail - 1)

segment(100,1)
