from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    move(scale)
    turn(45)
    for i in range(0, 2):
      move(scale)
    segment(scale / 2, detail - 1)
    
    
      
segment(100,1)
