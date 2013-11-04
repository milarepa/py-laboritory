#! /usr/bin/python
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
    
