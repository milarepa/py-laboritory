#! /usr/bin/python
from random import randint
# generate random lists...
# little tools to help work exercises

# generate a random list - more or less between 1 and 10
def gen_list():
  lst = []
  for i in range(1, randint(1,10)):
    lst.append(randint(1, i))
  return lst

# unneeded sort function :)
def sort_list(x):
  return sorted(x)

# median of a list
def median(x):
  lst = sorted(x)
  length = len(lst)
    
  if length % 2 == 0:
    a = lst[length / 2 - 1]
    b = lst[length / 2]
    return (a + b) / 2.0
  else:
    a = lst[int(length / 2.0 - 0.5)]
    return a
