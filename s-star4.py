#!/usr/bin/python
import math
import os

NUMOFPOINTS=6
STARSIZERATIO=0.25
TOTALLINES=40
TOTALWIDTH=200
STARSIZE=TOTALLINES*STARSIZERATIO

os.system('clear')

for j in range(TOTALLINES+1):
  for i in range(TOTALWIDTH+1):
    x = (i-(TOTALWIDTH*0.5))/2
    y = j-(TOTALLINES*0.5)
    c = "*"
    for k in range(NUMOFPOINTS+1):
      ang=2*math.pi/NUMOFPOINTS*k
      u = x*math.cos(ang) + y*math.sin(ang)
      v = -x*math.sin(ang) + y*math.cos(ang)
      if v<0 and abs(u)<=2*(v+STARSIZE):
        c = " "
    print(c, end='')
  print()






