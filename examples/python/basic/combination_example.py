#!/usr/bin/env python

# A Python program to print all
# combinations of given length
from itertools import combinations

s = 'abcdefg'
l = []
start = 1
for i in range(len(s) - 1):
# for i in range(15):
  l.append(start)
  start += 2

def insert(source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

# print(l)

count = 0
for i in range(len(l)):
  comb = combinations(l, i + 1)
  for e in list(comb):
      count += 1
      source_str = s
      delta = 0
      for j in l:
        if j in e:
          source_str = insert(source_str, '.', j - delta)
        else:
          delta += 1
      print("str: %s" % source_str)
