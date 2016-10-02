#!/usr/bin/env python

numbers = ((6,9,9,9,6),(4,6,4,4,4),(6,9,4,2,15),(7,8,6,8,7),(4,6,5,15,4),(15,1,7,8,7),(6,1,7,9,6),(15,8,4,2,2),(6,9,6,9,6),(6,9,14,8,6))
upper = ((6,9,15,9,9),(7,9,7,9,7),(6,9,1,9,6),(7,9,9,9,7),(15,1,7,1,15),(15,1,7,1,1),(6,1,13,9,6),(9,9,15,9,9),(7,2,2,2,7),(8,8,8,9,6),(9,5,3,5,9),(1,1,1,1,15),(9,15,9,9,9),(9,11,13,9,9),(6,9,9,9,6),(7,9,7,1,1),(6,9,9,13,14),(7,9,7,5,9),(14,1,6,8,7),(15,2,2,2,2),(9,9,9,9,6),(9,9,9,5,3),(9,9,9,15,9),(9,6,6,9,9),(9,9,14,8,6),(15,4,2,1,15))
special1 = ((0,0,0,0,0),(2,2,2,0,2),(5,5,0,0,0),(5,15,5,15,5),(6,5,6,10,7),(0,9,4,2,9),(6,1,10,5,10),(4,4,0,0,0),(4,2,2,2,4),(2,4,4,4,2),(0,9,6,9,0),(0,4,14,4,0),(0,0,0,4,2),(0,0,14,0,0),(0,0,0,0,2),(0,8,4,2,1))
space = (0,0,0,0,0)

def find_in(char, collection, first):
  ordinal = ord(char) - ord(first) 
  if 0 <= ordinal < len(collection):
    return collection[ordinal]
  else:
    return space 

def number(index):
  return(numbers[index])

def find(char):
  # maybe 'first' should be a capital 'a'
  # since the font is named upper, but
  # pending a lower, let's avoid shouting
  result = find_in(char, upper, 'a')

  if result == space:
    result = find_in(char, numbers, '0')

  if result == space:
    result = find_in(char, special1, ' ')
  return result


