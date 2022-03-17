#!/usr/bin/env python

try:
  from matplotlib import pyplot as plt
  import numpy as np
  import math
except Exception as e:
  print("Press any key to exit")
  input()
  raise e

ro = 1133
taoy = 0.8661
k = 0.0583
n = 0.7299
f = 0.007619
R = 0.025
D = 2 * R

def tao0(v):
  return f * ro * math.pow(v, 2) / 2

def rplug(v):
  return taoy * R / tao0(v)

def Aplug(v):
  return math.pi * math.pow(rplug(v), 2)

def uplug(v):
  return (D / (2 * math.pow(k, 1/n) * tao0(v))) * (n / (n + 1)) * math.pow(tao0(v) - taoy, (n + 1) / n)

def Q(v):
  return math.pi * math.pow(R, 2) * v

def Qplug(v):
  return uplug(v) * Aplug(v)

def vann(v):
  return (Q(v) - Qplug(v)) / (math.pi * (math.pow(R, 2) - math.pow(rplug(v), 2)))

def Dshear(v):
  return D - 2 * rplug(v)

def fv(v):
  value = 8 * ro * math.pow(vann(v), 2) / (taoy + k * math.pow(8 * vann(v) / Dshear(v), n))
  if value < 2100 and 2100 - value < 30:
    print("v = %s, 2100 - value = %s" % (v, 2100 - value))
  return value

def main():
  wrapped_fv = np.frompyfunc(fv, 1, 1)

  x = np.arange(0.8, 1, 0.0001)
  y = wrapped_fv(x)

  plt.plot(x,y)
  plt.xlabel("v")
  plt.ylabel("f(v)")
  plt.title('when v = ?, f(v) -> 2100')
  plt.show()

if __name__ == '__main__':
  main()
