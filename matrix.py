#!/usr/bin/env python

import numpy, time, unicornhat

import fonts, colors

unicornhat.rotation(180)

def setletter (banner, letter, plusx, plusy):
  y = 0
  for line in fonts.find(letter):
    for x in range(5):
      if line & pow(2, x): banner[x+plusx][y+plusy] = True
    y += 1

# ox,oy offset fom top left
def showbanner(banner, ox, oy, speed, color):
  width = len(banner)-7
  height = len(banner[0])-7
  max = width if width > height else height
  for plus in range(max):
      plusx= plus * width / max if width > 0 else 0
      plusy= plus * height / max if height > 0 else 0
#      unicornhat.clear()
      for y in range(8):
        for x in range(8):
          if len(banner) > x+plusx and len(banner[0]) > y+plusy and banner[x+plusx][y+plusy]:
            unicornhat.set_pixel(x+ox,y+oy, *color)
      unicornhat.show()
      unicornhat.clear()
      time.sleep(speed)

# sx,sy font spacing
def makebanner(message, width, height, sx, sy, color):
  banner = numpy.zeros((width, height), dtype=bool)
  for i in range(len(message)):
    posx = (i*(4+sx)) % width
    posy = (i/(width / (4+sx))) * (5+sy)
    setletter(banner, message[i], posx, posy)
  return banner

def rocket(message, color):
  banner = makebanner(message, 5, 6*len(message), 1,1, color)
  showbanner(banner, 2,0, 0.0625, color)

def matrix(message, color):
  banner = makebanner(message, 5*len(message), 6, 1, 1, color)
  showbanner(banner, 0,1, 0.0625, color)

def panner(message, width, sx, sy, color):
  ln = len(message) + (len(message) % width)
  banner = makebanner(message, (4+sx)*width, (5+sy)*ln/width, sx, sy, color)
  showbanner(banner, 0,0, 0.25, color)
  time.sleep(0.25)

if __name__ == "__main__":
  matrix(" !\"#$%&'()*+,-./0123456789", colors.pastel())
#  rocket("the quick brown fox jumps over the lazy dog", colors.pastel())
  rocket("the buzzing rocket fluxed away in quivered jumps", colors.pastel())
  panner("road house", 5, 1,1, colors.pastel())
#  matrix("'dolfijn, extra quizvragen!' sprak de boekenwurm cynisch.", colors.pastel())
#  matrix("the daft box jumping craze was quickly over", colors.pastel())
#  matrix("the crazy box jumping fad wore off quickly", colors.pastel()) 
#  matrix("extra kampquiz bevordert cynisch getwijfel", colors.pastel())
