#! /usr/bin/python
from random import randint
# generate random lists...
# little tools to help work exercises

def gen_list():
  lst = []
  for i in range(1, randint(1,10)):
    lst.append(randint(1, i))
  return lst

def sort_list(x):
  return sorted(x)
