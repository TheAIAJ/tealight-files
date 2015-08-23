from tealight.logo import move, turn

# Draws the tree fractal


def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    
    move(scale)
    move(-scale)
    
    turn(-45)
    segment(scale / 2, detail - 1)
    
    
    turn(90)
    segment(scale / 2, detail - 1)
    
    
    
#move(100)
segment(100,2)
