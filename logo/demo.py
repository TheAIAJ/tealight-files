from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["yellow", "magenta", "cyan"]

for i in range(0,100):
  move(i)
  turn(91)
  color(colors[i%3])