#!/usr/bin/env python

import unicornhat, time, random
from datetime import datetime

import colors, quatro

unicornhat.rotation(180)

def clock(times):
  while times > 0 or times == -1:
    dt = datetime.now()
    quatro.word("year", colors.pastel())
    quatro.num(dt.year, colors.pastel())
    quatro.word("date", colors.pastel())
    quatro.twonums(dt.month, dt.day, colors.pastel())
    quatro.word("time", colors.pastel())
    quatro.twonums(dt.hour, dt.minute, colors.pastel())
    if times != -1: times -= 1

if __name__ == "__main__":
  clock(-1)

