from tealight.logo import move, turn

# Draws the tree fractal

def branchesRight(scale):
  turn(45)
  move(scale)
  
def branchesLeft(scale):
  turn(-45)
  move(scale)
  

def segment(scale, detail):
  
  if detail == 0:
    None
  else:
    move(scale)
    
    
    
    segment(scale / 2, detail - 1)
    
    
      
segment(100,1)
