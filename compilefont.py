#!/usr/bin/env python

import sys

i=0
s=""
s2=""
file = open (sys.argv[1], "r")

sys.stdout.write("(")
	
for line in file:
  if i % 6 == 0:
    sys.stdout.write(s2)
    sys.stdout.write("(")
  val = 0
  for x in range(4):
    bit = 1 if line[x] == '#' else 0
    val += bit * pow(2,x)
  i+= 1
  if i % 6 == 0:
    sys.stdout.write(")")
    s = ""
  else:
    sys.stdout.write(s)
    sys.stdout.write(str(val))
    s=","
  s2 = ","
sys.stdout.write(")")

file.close()

sys.stdout.write("\n")

