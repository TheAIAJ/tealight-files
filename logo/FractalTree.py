from tealight.logo import move, turn

# Draws the tree fractal


def segment(scale, detail, angle):
  
  if detail == 0:
    None
  
  else:
    move(scale)
    turn(45)
    segment(scale / angle, detail - 1)
    turn(-90)
    segment(scale / angle, detail - 1)
    turn(45)
    move(-scale)
move(-200)    
segment(200,10, 90)
