#!/usr/bin/env python

import threading
import time
import datetime

# def run():
#   print('Run')
#
# timer_thread = threading.Timer(5, run)
# timer_thread.start()
#
# timer_thread.join()

lock = threading.Lock()

while True:
  print('loop')
  with lock:
    print('with lock')
    break
  time.sleep(5)

cond = threading.Condition()
flag = False

def wait_for_cond():
  with cond:
    while not flag:
      print('Time before waiting: %s' % datetime.datetime.now())
      cond.wait(timeout=5)
      print('Time after waiting: %s' % datetime.datetime.now())
    print('Flag is true')

thread = threading.Thread(target=wait_for_cond)
thread.start()

time.sleep(30)
with cond:
  flag = True
  cond.notify()

thread.join()
