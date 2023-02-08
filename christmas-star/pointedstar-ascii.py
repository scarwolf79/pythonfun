#!/usr/bin/python

import math
import os

NUMOFPOINTS=18
STARSIZERATIO=0.25
BACKGROUNDGLYPH=" "
FOREGROUNDGLYPH="*"

SCREENSIZE=os.get_terminal_size()
SCREENLINES=SCREENSIZE.lines
SCREENWIDTH=SCREENSIZE.columns
TOTALLINES=int(SCREENLINES) - 1
TOTALWIDTH=int(SCREENWIDTH) - 1

if TOTALLINES < TOTALWIDTH:
  STARSIZE=TOTALLINES*STARSIZERATIO
else: 
  STARSIZE=TOTALWIDTH*STARSIZERATIO



os.system('clear')

for j in range(TOTALLINES+1):
  for i in range(TOTALWIDTH+1):
    x = (i-(TOTALWIDTH*0.5))/2
    y = j-(TOTALLINES*0.5)
    c = BACKGROUNDGLYPH
    for k in range(NUMOFPOINTS+1):
      ang=2*math.pi/NUMOFPOINTS*k
      u = x*math.cos(ang) + y*math.sin(ang)
      v = -x*math.sin(ang) + y*math.cos(ang)
      if v<0 and abs(u)<=2*(v+STARSIZE):
        c = FOREGROUNDGLYPH
    print(c, end='')
  print()






