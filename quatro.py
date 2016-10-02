#!/usr/bin/env python

# the most advanced functions of this module
# show four font characters on screen,
# but you can also place single characters with it

import unicornhat, time, random
from datetime import datetime

import fonts, colors

def one(fontletter, plusx, plusy, color):
  y = 0
  for line in fontletter:
    for x in range(5):
      if line & pow(2, x): unicornhat.set_pixel(x+plusx,y+plusy, *color)
    y += 1
  unicornhat.show()
  time.sleep(0.125)

unicornhat.rotation(180)

def twonums(num1, num2, color):
  one(fonts.number(num1 / 10), 0,0, colors.dim(color, 2))
  one(fonts.number(num1 % 10), 4,0, colors.dim(color, 2))
  one(fonts.number(num2 / 10), 0,3, color)
  one(fonts.number(num2 % 10),4,3, color)
  unicornhat.clear()
  time.sleep(3.5)

def num(number, color):
  twonums(number / 100, number % 100, color)

def word(string, color):
  for i in range(0, len(string), 4):
    one(fonts.find(string[i]), 0,0, colors.dim(color,2))
    if i+1 < len(string): one(fonts.find(string[i+1]), 4,0, colors.dim(color,2))
    if i+2 < len(string): one(fonts.find(string[i+2]), 0,3, color)
    if i+3 < len(string): one(fonts.find(string[i+3]), 4,3, color)
    unicornhat.clear()
    time.sleep(0.25)
  time.sleep(1.25)

if __name__ == "__main__":
  word("quatro  isa fourletter  word", colors.pastel())
