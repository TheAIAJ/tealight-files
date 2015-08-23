from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    for i in range(0, 2):
      move(scale)
      turn(45)
      segment(scale / 2, detail - 1)
      turn(180)
      move(scale)
      #turn(90)
      #move(scale)

segment(100,1)
