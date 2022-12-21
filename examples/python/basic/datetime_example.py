#!/usr/bin/env python

import datetime

def comparison_example():
  date1 = datetime.date(2022, 3, 8)
  date2 = datetime.date(2022, 6, 1)

  if date1 < date2:
    print('%s < %s' % (date1, date2))

  time1 = datetime.datetime(2022, 3, 8, 0, 0, 0)
  time2 = datetime.datetime(2022, 3, 8, 0, 5, 0)

  if time1 < time2:
    print('%s < %s' % (time1, time2))

  time3 = time1 + datetime.timedelta(hours=0, minutes=4, seconds=59)
  if time3 < time2:
    print('%s < %s' % (time3, time2))

  time4 = time1 + datetime.timedelta(hours=0, minutes=5, seconds=1)
  if time4 > time2:
    print('%s > %s' % (time4, time2))

  now = datetime.datetime.now()
  if time4 < now:
    print('%s < %s' % (time4, now))

print('==== comparison ====')
comparison_example()

def format_example():
  now = datetime.datetime.now()
  print(now.strftime('%Y-%m-%d %H:%M:%S'))

print('\n==== format ====')
format_example()
