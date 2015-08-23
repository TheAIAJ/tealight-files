from tealight.logo import move, turn

# Draws the tree fractal

def branchesRight(scale):
  turn(45)
  move(scale)
  turn(180)
  move(scale)
  turn(135)
  
def branchesLeft(scale):
  turn(-45)
  move(scale)
  turn(180)
  move(scale)
  turn(-90)
  move(scale)
  

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    move(scale)
    
    branchesRight(scale)
    branchesLeft(scale)
    
    segment(scale / 2, detail - 1)
    
    
      
segment(100,2)
