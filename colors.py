#!/usr/bin/env python

import random

def pastel():
  return random.randint(100,200), random.randint(100,200), random.randint(100,200)

def dim(c,factor):
  return int(c[0] / factor), int(c[1] / factor), int(c[2] / factor)

