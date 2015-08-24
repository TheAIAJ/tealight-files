from tealight.logo import move, turn

# Draws the triangle fractal

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    for i in range(0, 3):
      move(scale)
      turn(120)
      segment(scale / 2, detail - 1)


turn(90)
move(-150)
segment(300,15)
