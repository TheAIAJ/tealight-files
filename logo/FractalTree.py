from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    move(scale)
    turn(45)
    move(scale)
    
      
segment(100,1)
