from tealight.logo import move, turn

# Draws the tree fractal

def branchesRight(scale):
  turn(45)
  move(scale/2)
  turn(180)
  move(scale/2)
  turn(135)
  
def branchesLeft(scale):
  turn(-45)
  move(scale/2)
  turn(180)
  move(scale/2)
  turn(-90)
  move(scale/2)
  

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    
    branchesRight(scale)
    branchesLeft(scale)
    
    segment(scale / 2, detail - 1)
    
    
      
segment(100,4)
