from tealight.logo import move, turn

# Draws the tree fractal

def segment(scale, detail, angle):
  
  if detail == 0:
    None
  else:
    move(scale)
    turn(angle)  
    segment(scale / 2, detail - 1, 45)
    turn(180)
    move(scale)
    turn(-90)
    segment(scale / 2, detail - 1, -45)
    
      
segment(100,1,45)
