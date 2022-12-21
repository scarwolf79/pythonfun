#!/usr/bin/python

import math
import os
from PIL import Image

NUMOFPOINTS=20
STARSIZERATIO=0.125
BACKGROUNDCOLOR="white"
FOREGROUNDCOLOR="red"

TOTALWIDTH=900
TOTALLINES=430

SCREENRATIO=TOTALWIDTH / TOTALLINES
TWICESR = SCREENRATIO * 2
SQUAREDSR = SCREENRATIO ** 2


STARSIZE=TOTALLINES*STARSIZERATIO

# Initialize Image
img = Image.new("RGB", (TOTALWIDTH,TOTALLINES), BACKGROUNDCOLOR)
pixels = img.load()


for j in range(TOTALLINES):
  for i in range(TOTALWIDTH):
    x = (i-(TOTALWIDTH*0.5))/2
    y = j-(TOTALLINES*0.5)
    for k in range(NUMOFPOINTS+1):
      ang=2*math.pi/NUMOFPOINTS*k
      u = x*math.cos(ang) + y*math.sin(ang)
      v = -x*math.sin(ang) + y*math.cos(ang)
      if v<0 and abs(u)<=2*(v+(0.25*TOTALLINES)):
        img.putpixel((i, j),(0,0,0))
  print("Line " + str(j) + " of " + str(TOTALLINES))

img.show()







