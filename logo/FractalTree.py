from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    move(scale)
    turn(45)
    move(scale/2)
    turn(180)
    move(scale)
    turn(90)
    move(scale)
    turn(180)
    move(scale)
    turn(-90)
    
    
    segment(scale / 2, detail - 1)
    
    
      
segment(100,2)
