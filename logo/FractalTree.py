from tealight.logo import move, turn

# Draws the tree fractal


def segment(scale, detail):
  
  if detail == 0:
    None
  
  else:
    move(scale)
    if scale > 5:
      turn(45)
      segment(scale / 2, detail - 1)
      turn(-90)
      segment(scale / 2, detail - 1)
      turn(45)
    move(-scale)
    
segment(100,4)
