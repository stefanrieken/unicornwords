#!/usr/bin/env python

import sys, matrix, colors

line=sys.stdin.readline().strip().lower()

while line:
  matrix.matrix("   "+ line + "  ", colors.pastel())
  line=sys.stdin.readline().strip().lower()
