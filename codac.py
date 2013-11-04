#! /usr/bin/python
def median(x):
  
  lst = sorted(x)
  length = len(lst)
  m = 0
  print lst
  if length % 2 == 0:
    n = length // 2
    m = (lst[n] + lst[n - 1]) / 2.0
    return m
  else:
    m_index = length // 2
    return lst[m_index]
    
