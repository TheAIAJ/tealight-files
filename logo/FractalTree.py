from tealight.logo import move, turn

# Draws the tree fractal


def segment(scale, detail, ratio):
  
  if detail == 0:
    None
  
  else:
    move(scale)
    turn(45)
    segment(scale * ratio, detail - 1, ratio)
    turn(-90)
    segment(scale * ratio, detail - 1, ratio)
    turn(45)
    move(-scale)
#move(-200)    
segment(200,10,0.75)
