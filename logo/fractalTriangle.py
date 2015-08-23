from tealight.logo import move, turn

# Draws the triangle fractal

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 2, detail - 1)
   

turn(90)
segment(600,1)
