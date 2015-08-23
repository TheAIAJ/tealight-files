from tealight.logo import move, turn

# Draws the tree fractal


def segment(scale, detail):
  
  if detail == 0:
    None
  
  else:
    move(scale)
    
    turn(45)
    segment(scale / 1, detail - 1)
    turn(-90)
    segment(scale / 1, detail - 1)
    turn(45)
    move(-scale)
move(-200)    
segment(200,10)
