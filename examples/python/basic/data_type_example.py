#!/usr/bin/env python

s = None
if s:
  print('None is truthy.')
else:
  print('None is falsy.')

s = ''
if s:
  print("'' is truthy.")
else:
  print("'' is falsy.")

s = ' '
if s:
  print("' ' is truthy.")
else:
  print("' ' is falsy.")

animals = ['cat', 'dog', 'pig', 'fish']

for animal in animals:
  if animal == 'dog':
    animals.remove(animal)

print('Updated animals list: ', animals)

tuples = [('foo', 1), ('bar', 2)]
print(len(tuples))
for e in tuples:
  print(e[0])
  print(e[1])

print('Reverse order:')
for e in tuples[::-1]:
  print(e[0])
  print(e[1])

tuples.pop(0)

tuples.append(('baz', 3))
for e in tuples:
  print(e[0])
  print(e[1])

d = { 'foo': 1, 'bar': 2 }
for k in d:
    print(k)
