#!/usr/bin/env python

import datetime

class CustomException(Exception):
    def __init__(self):
        super().__init__('Bar')

def test():
    raise CustomException()
    # raise Exception("foo")

try:
    test()
except CustomException as e:
    print('CustomException: %s' % e)
except Exception as e:
    print('Exception: %s' % e)
